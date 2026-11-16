"""Finance Pulse carousel renderer (1080x1350 slides).

    python3 build_carousel.py <slides_module.py> <out_dir>

The slides module defines SERIAL, TAG, SLIDES (list of dicts: theme 'light'|'dark', body html,
src = English sources line). Header, footer, fonts and background are shared here so every
carousel carries the same signature: lockup, serial + page, sources strip, ANIYA x CLAUDE.
"""
import importlib.util, pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
FONTS = (HERE.parent / "v2" / "fonts").as_uri()

CSS = """
@font-face{font-family:Lalezar;src:url(F/lalezar-arabic-400-normal.woff2) format('woff2')}
@font-face{font-family:Vaz;font-weight:400;src:url(F/vazirmatn-arabic-400-normal.woff2) format('woff2')}
@font-face{font-family:Vaz;font-weight:500;src:url(F/vazirmatn-arabic-500-normal.woff2) format('woff2')}
@font-face{font-family:Vaz;font-weight:700;src:url(F/vazirmatn-arabic-700-normal.woff2) format('woff2')}
@font-face{font-family:Vaz;font-weight:900;src:url(F/vazirmatn-arabic-900-normal.woff2) format('woff2')}
@font-face{font-family:VazL;font-weight:400;src:url(F/vazirmatn-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:VazL;font-weight:700;src:url(F/vazirmatn-latin-700-normal.woff2) format('woff2')}
@font-face{font-family:Unb;font-weight:500;src:url(F/unbounded-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:Unb;font-weight:700;src:url(F/unbounded-latin-700-normal.woff2) format('woff2')}
@font-face{font-family:Unb;font-weight:800;src:url(F/unbounded-latin-800-normal.woff2) format('woff2')}
@font-face{font-family:Rdx;font-weight:400;src:url(F/readex-pro-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:Rdx;font-weight:600;src:url(F/readex-pro-latin-600-normal.woff2) format('woff2')}
:root{--navy:#1C2433;--ink:#3A4A63;--mut:#5B6B85;--amber:#F59E0B;--amber2:#B45309;--steel:#7E9DC0;--blue:#2F6DB5}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#888;font-family:Vaz,VazL,sans-serif}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;direction:rtl;margin-bottom:20px}
.light{background:linear-gradient(165deg,#C3D2E3 0%,#DDE6F0 40%,#F3F6FA 100%);color:var(--navy)}
.dark{background:radial-gradient(1200px 900px at 30% 45%,#24365A 0%,#152139 55%,#0D1527 100%);color:#F3F6FA}
.bgfx{position:absolute;inset:0;pointer-events:none}
.safe{position:absolute;left:72px;right:72px;top:72px;bottom:72px}
header{position:absolute;top:0;left:0;right:0;height:80px;direction:ltr;display:flex;justify-content:space-between;align-items:flex-start}
.l1{font-family:Unb;font-weight:800;font-size:22px;letter-spacing:.2em}
.l2{font-family:Unb;font-weight:500;font-size:15px;letter-spacing:.42em;color:var(--amber2);margin-top:10px;display:flex;align-items:center;gap:10px}
.dark .l2{color:var(--amber)}
.tags{display:flex;gap:10px}
.tag{font-family:Unb;font-weight:700;font-size:15px;letter-spacing:.14em;padding:10px 18px;border-radius:30px}
.tag.k{background:var(--navy);color:#fff}
.dark .tag.k{background:var(--amber);color:var(--navy)}
.tag.p{border:1.5px solid rgba(126,157,192,.8);color:var(--ink);background:rgba(255,255,255,.4)}
.dark .tag.p{color:#DCE5F0;background:rgba(255,255,255,.06);border-color:rgba(126,157,192,.6)}
footer{position:absolute;left:0;right:0;bottom:0;direction:ltr;display:flex;justify-content:space-between;align-items:flex-end;gap:28px;padding-top:12px;border-top:1px solid rgba(126,157,192,.55)}
footer .r{font-family:Rdx;font-weight:400;font-size:15.5px;line-height:1.45;color:#4B5B75}
.dark footer .r{color:#AEBBD0}
footer .r b{font-family:Unb;font-weight:700;letter-spacing:.06em;color:var(--navy)}
.dark footer .r b{color:#fff}
footer .sig{font-family:Unb;font-weight:700;font-size:14px;letter-spacing:.24em;color:var(--amber2);white-space:nowrap}
.dark footer .sig{color:var(--amber)}
.abs{position:absolute}
.kick{display:inline-block;font-weight:700;font-size:26px;color:#fff;background:linear-gradient(90deg,#F59E0B,#D97706);padding:8px 24px;border-radius:40px;box-shadow:0 8px 22px rgba(217,119,6,.32)}
.kick.n{background:var(--navy);box-shadow:none}
.h1{font-family:Lalezar;font-size:118px;line-height:1.12;text-align:right}
.h2{font-weight:900;font-size:62px;line-height:1.3;text-align:right}
.h3{font-weight:900;font-size:40px;line-height:1.35}
.sub{font-weight:500;font-size:33px;line-height:1.6;text-align:right;color:var(--ink)}
.dark .sub{color:#D5DEEA}
.am{color:var(--amber2)} .dark .am{color:var(--amber)}
.glass{background:rgba(255,255,255,.62);border:1.5px solid rgba(255,255,255,.95);box-shadow:0 16px 44px rgba(28,36,51,.11),inset 0 1px 0 #fff;border-radius:30px}
.dark .glass{background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14);box-shadow:0 16px 44px rgba(0,0,0,.25)}
.cta{position:absolute;left:0;right:0;height:78px;border-radius:22px;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 32px;font-weight:700;font-size:29px}
.dark .cta{background:linear-gradient(90deg,#F59E0B,#D97706);color:var(--navy)}
.cta .ar{font-family:VazL;font-size:34px;color:var(--amber)} .dark .cta .ar{color:var(--navy)}
.cta .dot{width:14px;height:14px;border-radius:50%;background:var(--amber);box-shadow:0 0 14px var(--amber);margin-left:16px;display:inline-block}
.dark .cta .dot{background:var(--navy);box-shadow:none}
.pulse{display:block}
.note{font-weight:500;font-size:22px;color:var(--mut)} .dark .note{color:#AEBBD0}
.chip{display:inline-block;font-weight:700;font-size:25px;padding:4px 16px;border-radius:24px;background:rgba(245,158,11,.16);color:var(--amber2)}
.dark .chip{background:rgba(245,158,11,.18);color:#FBBF24}
.ltr{direction:ltr;unicode-bidi:isolate;font-family:VazL}
"""

PULSE = """<svg class="pulse" width="210" height="26" viewBox="0 0 210 26"><defs><filter id="gl{i}"><feGaussianBlur stdDeviation="3"/></filter></defs>
<path d="M2 15H120l10-12 10 22 10-14 6 4H208" fill="none" stroke="#F59E0B" stroke-width="6" opacity=".45" filter="url(#gl{i})"/>
<path d="M2 15H120l10-12 10 22 10-14 6 4H208" fill="none" stroke="#F59E0B" stroke-width="3.2"/>
<path d="M2 15H120l10-12 10 22 10-14 6 4H208" fill="none" stroke="#FFF7E6" stroke-width="1.1"/></svg>"""

def bgfx(theme, i):
    # dotted globe + concentric dotted rings + a flowing light line (brand graphics, rendered not downloaded)
    dot = "#7E9DC0" if theme == "light" else "#5D7AA3"
    op = ".28" if theme == "light" else ".35"
    return f"""<svg class="bgfx" width="1080" height="1350" viewBox="0 0 1080 1350">
<defs><radialGradient id="glow{i}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F59E0B" stop-opacity=".22"/><stop offset="1" stop-color="#F59E0B" stop-opacity="0"/></radialGradient>
<filter id="bl{i}"><feGaussianBlur stdDeviation="5"/></filter></defs>
<g opacity="{op}" fill="none" stroke="{dot}" stroke-width="2" stroke-dasharray="2 11" stroke-linecap="round">
<circle cx="-40" cy="1080" r="260"/><circle cx="-40" cy="1080" r="340"/><circle cx="-40" cy="1080" r="420"/>
<circle cx="1120" cy="250" r="190"/><circle cx="1120" cy="250" r="260"/></g>
</svg>"""

def page(serial, tag, n, total, s, i):
    th = s["theme"]
    return f"""<section class="slide {th}" id="s{n:02d}">{bgfx(th, i)}
<div class="safe">
<header><div><div class="l1">THE DECISION ROOM</div><div class="l2"><span style="display:inline-block;width:34px;height:2px;background:currentColor"></span>FINANCE PULSE <svg width="26" height="14" viewBox="0 0 26 14"><path d="M0 8h8l3-6 4 10 3-6h8" fill="none" stroke="currentColor" stroke-width="2"/></svg></div></div>
<div class="tags"><span class="tag k">{tag}</span><span class="tag p">{n:02d}/{total:02d}</span></div></header>
{s['body'].replace('{PULSE}', PULSE.replace('{i}', str(i)))}
<footer><div class="r"><b>{serial} · {n:02d}/{total:02d}</b> · {s['src']}</div><div class="sig">ANIYA × CLAUDE</div></footer>
</div></section>"""

def main(mod_path, out_dir):
    spec = importlib.util.spec_from_file_location("deck", mod_path)
    deck = importlib.util.module_from_spec(spec); spec.loader.exec_module(deck)
    total = len(deck.SLIDES)
    html = "<!doctype html><html lang='fa'><head><meta charset='utf-8'><style>" + CSS.replace("url(F/", f"url({FONTS}/") + getattr(deck, "EXTRA_CSS", "") + "</style></head><body>"
    html += "".join(page(deck.SERIAL, deck.TAG, n + 1, total, s, n) for n, s in enumerate(deck.SLIDES))
    html += "</body></html>"
    out = pathlib.Path(out_dir).resolve(); out.mkdir(parents=True, exist_ok=True)
    hp = out / "deck.html"; hp.write_text(html, encoding="utf-8")
    only = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg.goto(hp.as_uri()); pg.wait_for_timeout(600)
        pg.evaluate("document.fonts.ready")
        for n in range(1, total + 1):
            if only and str(n) not in only: continue
            pg.locator(f"#s{n:02d}").screenshot(path=str(out / f"{deck.SERIAL}-{n:02d}.png"))
        b.close()
    print("ok", total)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
