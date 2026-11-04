"""Finance Pulse v2 motion story renderer.

    python3 render_v2.py specs/<spec>.json out/<name>.mp4 [--frames t1,t2,...]

--frames only saves full-size JPEG stills at those times (for checking) and exits.
Without it: renders each scene to its own MP4 (frames piped to ffmpeg, no PNGs on disk),
joins them, composes the original music bed (music.py) and muxes it.
"""
import asyncio, json, os, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
FPS = 30


async def open_page(p, spec):
    try:
        b = await p.chromium.launch()
    except Exception:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    await pg.add_init_script("window.SPEC = " + json.dumps(spec, ensure_ascii=False) + ";")
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.goto((HERE / "template.html").as_uri())
    await pg.evaluate("document.fonts.ready")
    await pg.wait_for_timeout(400)
    if errs:
        raise SystemExit("page error: " + "; ".join(errs))
    return b, pg


async def stills(spec, out_dir, times):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b, pg = await open_page(p, spec)
        for t in times:
            await pg.evaluate(f"renderAt({t})")
            await pg.screenshot(path=str(out_dir / f"frame_{t:05.2f}.jpg"), type="jpeg", quality=92)
        await b.close()


async def render_scene(spec, i, start, end, out_mp4):
    from playwright.async_api import async_playwright
    tmp = out_mp4.with_name(out_mp4.stem + ".part.mp4")
    n = int(round((end - start) * FPS))
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                           "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                           "-pix_fmt", "yuv420p", "-r", str(FPS), str(tmp)], stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b, pg = await open_page(p, spec)
        for k in range(n):
            await pg.evaluate(f"renderAt({start + k / FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
        await b.close()
    ff.stdin.close()
    if ff.wait() != 0:
        raise SystemExit(f"ffmpeg failed on scene {i}")
    tmp.rename(out_mp4)


def main():
    spec_path, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    times, t0 = [], 0.0
    for s in spec["scenes"]:
        times.append((t0, t0 + s["dur"]))
        t0 += s["dur"]
    if "--frames" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--frames") + 1].split(",")]
        out.mkdir(parents=True, exist_ok=True)
        asyncio.run(stills(spec, out, ts))
        print("stills in", out)
        return
    work = out.parent / (out.stem + "_work")
    work.mkdir(parents=True, exist_ok=True)

    async def all_scenes():
        await asyncio.gather(*[render_scene(spec, i, a, b, work / f"s{i}.mp4") for i, (a, b) in enumerate(times)])
    asyncio.run(all_scenes())
    lst = work / "list.txt"
    lst.write_text("".join(f"file 's{i}.mp4'\n" for i in range(len(times))))
    silent = work / "video.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(silent)], check=True)
    # music: typing clicks follow the hook headline; whooshes on scene changes
    hook = spec["scenes"][0]
    clicks = []
    if hook["type"] == "hook":
        nch = len(hook["headline"])
        clicks = [0.25 + hook.get("typeDur", 1.6) * (k + 1) / nch for k in range(nch) if hook["headline"][k] != " "]
    cues = {"total": t0, "clicks": clicks, "whoosh": [b for _, b in times[:-1]],
            "pops": [times[0][0] + 2.5]}
    wav = work / "music.wav"
    subprocess.run([sys.executable, str(HERE / "music.py"), json.dumps(cues), str(wav)], check=True)
    tmp = out.with_name(out.stem + ".part.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent), "-i", str(wav), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-15:TP=-1.5:LRA=7",
                    "-shortest", "-movflags", "+faststart", str(tmp)], check=True)
    tmp.rename(out)
    print("ok", out, f"{t0:.1f}s")


if __name__ == "__main__":
    main()
