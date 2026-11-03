#!/usr/bin/env python3
"""The Decision Room / LATE BRIEF story renderer.

Usage: python3 build_story.py spec.json out.png
Spec kinds: "prices" (morning board) and "news" (evening slide).
Fonts are read from ./fonts next to this script.
"""
import json, sys, html, pathlib, asyncio

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE / "fonts"

FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def fa(s):
    """Persian digits, ٬ thousands, ٫ decimal. Input like '3,965.2' or '-8.6'."""
    s = str(s).replace(",", "٬").replace(".", "٫")
    s = s.replace("-", "−")
    return s.translate(FA)


def esc(s):
    return html.escape(str(s))


def chg(v, unit=True):
    """Change pill: v is a number (percent)."""
    if v is None:
        return ""
    up = v >= 0
    arrow = "▲" if up else "▼"
    cls = "up" if up else "dn"
    num = fa(f"{abs(v):.1f}" if abs(v) < 10 else f"{abs(v):.0f}")
    tail = " درصد" if unit else ""
    return f'<span class="chg {cls}">{arrow} {num}{tail}</span>'


ICONS = {
    "oil": '<path d="M24 6c6 9 12 15 12 22a12 12 0 0 1-24 0c0-7 6-13 12-22z"/>',
    "gold": '<path d="M8 34h32l-5-12H13zM14 22h20l-4-9H18z"/>',
    "coin": '<circle cx="24" cy="24" r="15"/><circle cx="24" cy="24" r="9"/><path d="M24 12v-4M24 40v-4"/>',
    "cash": '<rect x="6" y="14" width="36" height="20" rx="3"/><circle cx="24" cy="24" r="5"/><path d="M11 19v10M37 19v10"/>',
    "shield": '<path d="M24 6l15 6v10c0 10-7 17-15 20C16 39 9 32 9 22V12z"/><path d="M20 18l8 12M28 18l-8 12"/>',
    "out": '<path d="M24 34V10M15 19l9-9 9 9"/><path d="M8 38h32"/>',
    "pie": '<circle cx="24" cy="24" r="15"/><path d="M24 24V9M24 24l12 9"/>',
    "ship": '<path d="M8 30h32l-5 9H13z"/><path d="M14 30V20h20v10M24 20v-9"/>',
    "chart": '<path d="M8 38h32M12 32l8-9 7 5 11-14"/><circle cx="38" cy="14" r="2"/>',
    "globe": '<circle cx="24" cy="24" r="15"/><path d="M9 24h30M24 9c5 5 5 25 0 30M24 9c-5 5-5 25 0 30"/>',
    "check": '<circle cx="24" cy="24" r="15"/><path d="M17 24l5 5 9-10"/>',
}


def icon(name):
    p = ICONS.get(name, ICONS["chart"])
    return f'<svg class="ic" viewBox="0 0 48 48">{p}</svg>'


def font_css():
    f = FONTS.as_uri()
    return f"""
@font-face{{font-family:'Vazirmatn';font-weight:400;src:url('{f}/vazirmatn-arabic-400-normal.woff2') format('woff2');unicode-range:U+0600-06FF,U+200C-200E,U+2010-2011,U+204F,U+2E41,U+FB50-FDFF,U+FE70-FEFF;}}
@font-face{{font-family:'Vazirmatn';font-weight:500;src:url('{f}/vazirmatn-arabic-500-normal.woff2') format('woff2');unicode-range:U+0600-06FF,U+200C-200E,U+FB50-FDFF,U+FE70-FEFF;}}
@font-face{{font-family:'Vazirmatn';font-weight:700;src:url('{f}/vazirmatn-arabic-700-normal.woff2') format('woff2');unicode-range:U+0600-06FF,U+200C-200E,U+FB50-FDFF,U+FE70-FEFF;}}
@font-face{{font-family:'Vazirmatn';font-weight:900;src:url('{f}/vazirmatn-arabic-900-normal.woff2') format('woff2');unicode-range:U+0600-06FF,U+200C-200E,U+FB50-FDFF,U+FE70-FEFF;}}
@font-face{{font-family:'Vazirmatn';font-weight:400;src:url('{f}/vazirmatn-latin-400-normal.woff2') format('woff2');unicode-range:U+0000-00FF,U+2000-206F,U+25A0-25FF;}}
@font-face{{font-family:'Vazirmatn';font-weight:700;src:url('{f}/vazirmatn-latin-700-normal.woff2') format('woff2');unicode-range:U+0000-00FF,U+2000-206F,U+25A0-25FF;}}
@font-face{{font-family:'Naskh';font-weight:700;src:url('{f}/noto-naskh-arabic-arabic-700-normal.woff2') format('woff2');}}
@font-face{{font-family:'Inter';font-weight:400;src:url('{f}/inter-latin-400-normal.woff2') format('woff2');}}
@font-face{{font-family:'Inter';font-weight:600;src:url('{f}/inter-latin-600-normal.woff2') format('woff2');}}
@font-face{{font-family:'Inter';font-weight:700;src:url('{f}/inter-latin-700-normal.woff2') format('woff2');}}
"""


BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--navy:#1C2433;--amber:#F59E0B;--amber2:#B45309;--steel:#7E9DC0;--ink2:#3A4A63;--up:#2E7D5B;--dn:#B23B3B}
html,body{width:1080px;height:1920px;overflow:hidden}
body{background:linear-gradient(180deg,#C9D6E4 0%,#DCE5EF 38%,#E8EEF5 70%,#F2F5F9 100%);color:var(--navy);font-family:'Vazirmatn',sans-serif;position:relative}
.deco{position:absolute;inset:0;z-index:0}
.wrap{position:absolute;inset:0;z-index:1;padding:0 64px}
.lat{font-family:'Inter',sans-serif;direction:ltr;unicode-bidi:isolate}
header{position:absolute;top:200px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:flex-start}
.logo .l1{font-family:'Inter';font-weight:700;font-size:30px;letter-spacing:7px;color:var(--navy)}
.logo .l2{font-family:'Inter';font-weight:600;font-size:21px;letter-spacing:9px;color:var(--amber2);margin-top:8px;display:flex;align-items:center;gap:14px}
.logo .l2:before{content:'';width:36px;height:2px;background:var(--amber)}
.logo .l2 svg{margin-left:-4px}
.pulse{display:block;margin:16px 0 16px auto}
.tags{display:flex;gap:12px}
.tag{font-family:'Inter';font-weight:600;font-size:19px;letter-spacing:3px;border:1.5px solid var(--steel);color:var(--ink2);padding:9px 16px;border-radius:30px;background:rgba(255,255,255,.35)}
.hl{position:absolute;right:64px;left:64px;text-align:right;direction:rtl}
.hl h1{font-family:'Naskh';font-weight:700;color:var(--navy);line-height:1.38}
.rule{width:170px;height:4px;background:linear-gradient(90deg,rgba(245,158,11,0),var(--amber) 40%,var(--amber2));margin:18px 0 18px auto;border-radius:2px;box-shadow:0 0 14px rgba(245,158,11,.55)}
.sub{font-weight:500;font-size:37px;color:var(--ink2);line-height:1.55}
.glass{background:rgba(255,255,255,.52);border:1.5px solid rgba(126,157,192,.55);border-radius:34px;box-shadow:0 18px 50px rgba(28,36,51,.10),inset 0 1px 0 rgba(255,255,255,.9)}
.feat{position:absolute;left:64px;right:64px;display:grid;gap:16px;direction:rtl}
.tile{padding:26px 18px 22px;text-align:center}
.tile .ic{width:54px;height:54px;fill:none;stroke:var(--navy);stroke-width:2.3;stroke-linecap:round;stroke-linejoin:round}
.tile .ic{filter:drop-shadow(0 0 6px rgba(245,158,11,.25))}
.tile .lb{font-size:27px;font-weight:500;color:var(--ink2);margin-top:8px}
.tile .v{font-size:46px;font-weight:900;color:var(--navy);margin-top:6px;line-height:1.2}
.tile .u{font-size:22px;color:var(--ink2);font-weight:500}
.chg{font-size:24px;font-weight:700;display:inline-block;margin-top:6px}
.chg.up{color:var(--up)} .chg.dn{color:var(--dn)}
.board{position:absolute;left:64px;right:64px;padding:26px 34px;direction:rtl;display:grid;grid-template-columns:1fr 1fr;column-gap:46px}
.col h3{font-size:27px;font-weight:700;color:var(--amber2);margin:2px 0 10px;display:flex;align-items:center;gap:12px}
.col h3:after{content:'';flex:1;height:1.5px;background:linear-gradient(270deg,rgba(126,157,192,.7),rgba(126,157,192,0))}
.row{display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1px dashed rgba(126,157,192,.5)}
.row:last-child{border-bottom:none}
.row .n{font-size:26px;font-weight:500;color:var(--navy);white-space:nowrap}
.row .n .lat{font-size:18px;color:#56657C;font-weight:600;letter-spacing:1px;margin-right:8px}
.row .p{text-align:left;white-space:nowrap}
.row .p b{font-size:30px;font-weight:900}
.row .p .chg{font-size:20px;margin:0 10px 0 0}
.cap{grid-column:1/-1;font-size:20px;color:#56657C;margin-top:12px;text-align:right}
.tagline{position:absolute;left:64px;right:64px;border:1.8px solid var(--navy);border-radius:16px;padding:20px 26px;text-align:center;font-family:'Inter';font-weight:700;font-size:25px;letter-spacing:5px;color:var(--navy);background:rgba(255,255,255,.25)}
.q{position:absolute;left:64px;right:64px;direction:rtl;text-align:right;font-size:36px;font-weight:700;color:var(--navy);line-height:1.6}
.q:before{content:'';display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--amber);box-shadow:0 0 12px var(--amber);margin-left:16px;vertical-align:middle}
.foot{position:absolute;left:64px;right:64px;bottom:200px}
.closer{direction:rtl;text-align:right;font-size:27px;font-weight:900;color:var(--navy);margin-bottom:6px}
.disc{direction:rtl;text-align:right;font-size:22px;font-weight:500;color:var(--ink2)}
.src{display:flex;gap:18px;align-items:flex-start;margin-top:12px;padding-top:12px;border-top:1px solid rgba(126,157,192,.55);direction:ltr}
.src .r{flex:1;min-width:0;font-family:'Inter';font-size:17px;color:#56657C;line-height:1.5;text-align:left}
.src .r b{color:var(--navy);font-weight:700;letter-spacing:1px}
.src .sig{font-family:'Inter';font-weight:700;font-size:15px;letter-spacing:3px;color:var(--amber2);white-space:nowrap;padding-top:2px}
"""


def deco_svg(theme):
    """Light premium 3D decor: dotted rings, glass sphere, glowing amber line."""
    dots = []
    # dotted globe (top-left area for prices, centre for news)
    import math
    if theme == "prices":
        cx, cy, R = 130, 560, 300
    elif theme == "crypto":
        cx, cy, R = 540, 870, 250
    else:
        cx, cy, R = 540, 870, 250
    for lat in range(-80, 81, 10):
        r = R * math.cos(math.radians(lat))
        y = cy - R * math.sin(math.radians(lat))
        n = max(4, int(r / 14))
        for i in range(n):
            a = 2 * math.pi * i / n
            x = cx + r * math.cos(a)
            depth = (math.sin(a) + 1) / 2
            op = 0.10 + 0.35 * depth
            dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{2.2 + 1.6*depth:.1f}" fill="#7E9DC0" opacity="{op:.2f}"/>')
    rings = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{R + 40 + k*46}" fill="none" stroke="#7E9DC0" stroke-width="2" stroke-dasharray="2 12" opacity="{0.45 - k*0.08:.2f}"/>'
        for k in range(4)
    )
    if theme == "prices":
        line = "M -40 1520 C 220 1470, 380 1560, 580 1500 S 900 1470, 1140 1500"
        sph = (120, 1512, 38)
    elif theme == "crypto":
        line = "M -40 1000 C 200 930, 330 1050, 540 980 S 880 890, 1140 950"
        sph = (860, 880, 58)
    else:
        line = "M 140 990 C 300 800, 520 1010, 700 850 S 900 760, 980 800"
        sph = (870, 790, 58)
    glow = f"""
<path d="{line}" fill="none" stroke="#F59E0B" stroke-width="16" opacity=".35" filter="url(#blur)"/>
<path d="{line}" fill="none" stroke="#F59E0B" stroke-width="5" opacity=".9"/>
<path d="{line}" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
"""
    sx, sy, sr = sph
    sphere = f"""
<circle cx="{sx}" cy="{sy}" r="{sr}" fill="url(#glass)"/>
<circle cx="{sx}" cy="{sy}" r="{sr}" fill="none" stroke="#FFFFFF" stroke-opacity=".8" stroke-width="2"/>
<ellipse cx="{sx - sr*0.32}" cy="{sy - sr*0.38}" rx="{sr*0.32}" ry="{sr*0.18}" fill="#fff" opacity=".75" transform="rotate(-30 {sx - sr*0.32} {sy - sr*0.38})"/>
<circle cx="{sx}" cy="{sy}" r="{sr*0.25}" fill="url(#amberorb)" opacity=".9"/>
"""
    return f"""<svg class="deco" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
<defs>
<filter id="blur"><feGaussianBlur stdDeviation="9"/></filter>
<radialGradient id="glass" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".55" stop-color="#DCE6F1" stop-opacity=".55"/><stop offset="1" stop-color="#7E9DC0" stop-opacity=".45"/></radialGradient>
<radialGradient id="amberorb" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#FFF4D6"/><stop offset=".5" stop-color="#F59E0B"/><stop offset="1" stop-color="#B45309"/></radialGradient>
</defs>
{rings}{''.join(dots)}{glow}{sphere}
</svg>"""


def header(spec):
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in spec.get("tags", []))
    glyph = ('<svg width="44" height="18" viewBox="0 0 44 18"><path d="M0 9 H14 L18 3 L23 15 L27 1 L31 17 L34 9 H44" fill="none" '
             'stroke="#F59E0B" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/></svg>')
    return f"""<header><div class="logo"><div class="l1">THE DECISION ROOM</div><div class="l2">FINANCE PULSE {glyph}</div></div><div class="tags">{tags}</div></header>"""


PULSE = ('<svg class="pulse" width="230" height="30" viewBox="0 0 230 30"><defs><filter id="pg" x="-20%" y="-80%" width="140%" height="260%">'
         '<feGaussianBlur stdDeviation="3.5"/></filter></defs>'
         '<path d="M2 15 H150 L160 5 L171 26 L182 2 L193 28 L202 15 H228" fill="none" stroke="#F59E0B" stroke-width="7" opacity=".45" filter="url(#pg)"/>'
         '<path d="M2 15 H150 L160 5 L171 26 L182 2 L193 28 L202 15 H228" fill="none" stroke="#F59E0B" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"/>'
         '<path d="M2 15 H150 L160 5 L171 26 L182 2 L193 28 L202 15 H228" fill="none" stroke="#fff" stroke-width="1.1" stroke-linejoin="round" stroke-linecap="round"/></svg>')


def headline(spec, top, size):
    return f"""<div class="hl" style="top:{top}px"><h1 style="font-size:{size}px">{spec['headline']}</h1>{PULSE}<div class="sub">{spec['subline']}</div></div>"""


def tiles(items, top, cols):
    out = []
    for t in items:
        unit = f'<div class="u">{t["unit"]}</div>' if t.get("unit") else ""
        out.append(
            f'<div class="tile glass">{icon(t.get("icon","chart"))}<div class="lb">{t["label"]}</div>'
            f'<div class="v">{fa(t["value"])}</div>{unit}{chg(t.get("change"))}</div>'
        )
    return f'<div class="feat" style="top:{top}px;grid-template-columns:repeat({cols},1fr)">{"".join(out)}</div>'


def board(cols, top):
    html_cols = []
    for c in cols:
        rows = []
        for r in c["rows"]:
            tick = f'<span class="lat">{esc(r["ticker"])}</span>' if r.get("ticker") else ""
            rows.append(
                f'<div class="row"><span class="n">{r["name"]}{tick}</span>'
                f'<span class="p"><b>{fa(r["value"])}</b>{chg(r.get("change"), False)}</span></div>'
            )
        html_cols.append(f'<div class="col"><h3>{c["title"]}</h3>{"".join(rows)}</div>')
    cap = '<div class="cap">عدد کوچک کنار هر قیمت: تغییر روزانه به درصد</div>'
    return f'<div class="board glass" style="top:{top}px">{"".join(html_cols)}{cap}</div>'


def foot(spec):
    closer = spec.get("closer", "عدد از ما، تصمیم از شما.")
    serial = spec.get("serial", "")
    lead = f"<b>{esc(serial)}</b> · " if serial else ""
    return (f'<div class="foot"><div class="closer">{closer}</div>'
            f'<div class="disc">{spec.get("disclaimer","اطلاع‌رسانیه، نه توصیه‌ی مالی.")}</div>'
            f'<div class="src"><div class="r">{lead}{esc(spec["sources"])}</div><div class="sig">ANIYA × CLAUDE</div></div></div>')


def build_html(spec):
    kind = spec["kind"]
    body = [header(spec)]
    if kind == "prices":
        body.append(deco_svg("prices"))
        body.append(headline(spec, 330, 72))
        body.append(tiles(spec["tiles"], 600, len(spec["tiles"])))
        body.append(board(spec["board"], 905))
        body.append(f'<div class="tagline" style="top:1395px">{esc(spec["tagline"])}</div>')
    else:
        body.append(deco_svg(spec.get("theme", "news")))
        body.append(headline(spec, 330, 76))
        body.append(tiles(spec["tiles"], 1020, len(spec["tiles"])))
        if spec.get("question"):
            body.append(f'<div class="q" style="top:1345px">{spec["question"]}</div>')
        body.append(f'<div class="tagline" style="top:1475px">{esc(spec["tagline"])}</div>')
    body.append(foot(spec))
    return f"""<!doctype html><html lang="fa"><head><meta charset="utf-8"><style>{font_css()}{BASE_CSS}</style></head>
<body>{body[1] if kind else ''}<div class="wrap">{body[0]}{''.join(body[2:])}</div></body></html>"""


async def render(html_str, out_png):
    from playwright.async_api import async_playwright
    tmp = pathlib.Path(out_png).resolve().with_suffix(".html")
    tmp.write_text(html_str, encoding="utf-8")
    async with async_playwright() as p:
        try:
            b = await p.chromium.launch()
        except Exception:
            b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        await pg.goto(tmp.as_uri())
        await pg.evaluate("document.fonts.ready")
        # keep headline and subline on one line each for the prices layout (shrink to fit)
        await pg.evaluate("""() => {
          if (!document.querySelector('.board')) return;
          for (const sel of ['.hl h1', '.hl .sub']) {
            const el = document.querySelector(sel); if (!el) continue;
            let fs = parseFloat(getComputedStyle(el).fontSize);
            const lh = () => parseFloat(getComputedStyle(el).lineHeight) || fs * 1.4;
            while (el.getBoundingClientRect().height > lh() * 1.3 && fs > 44) { fs -= 2; el.style.fontSize = fs + 'px'; }
          }
        }""")
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=out_png, type="png")
        await b.close()


if __name__ == "__main__":
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    asyncio.run(render(build_html(spec), sys.argv[2]))
    print("ok", sys.argv[2])
