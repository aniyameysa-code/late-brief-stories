# FP-0032 · Gold carousel · 16 Nov 2026 · «پناهگاه امن ترک برداشته؟»
# "|" in Persian text = ZWNJ (replaced at build time).
SERIAL = "FP-0032"
TAG = "GOLD DESK"

EXTRA_CSS = """
.hud{font-family:Unb;font-weight:500;font-size:13px;letter-spacing:.18em;fill:#9FB4D0}
.row{display:flex;align-items:center;gap:22px}
.badge{flex:0 0 64px;height:64px;border-radius:50%;background:linear-gradient(145deg,#FBBF24,#D97706);color:#fff;font-weight:900;font-size:32px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 7px rgba(245,158,11,.16),0 8px 20px rgba(217,119,6,.35)}
.node{position:absolute;right:0;left:0;height:104px;padding:0 26px 0 22px}
.node .t{font-weight:700;font-size:31px;line-height:1.35;flex:1}
.mrow{position:absolute;right:0;left:0;height:112px;display:flex;align-items:center;gap:20px}
.mrow .lab{flex:0 0 372px;text-align:right}
.mrow .lab .a{font-weight:900;font-size:29px;line-height:1.3}
.mrow .lab .b{font-weight:500;font-size:20.5px;line-height:1.45;color:#5B6B85;margin-top:2px}
.card3{position:absolute;right:0;left:0;height:256px;padding:26px 30px}
.card3 .hd{display:flex;align-items:center;gap:16px}
.card3 .ic{flex:0 0 66px;height:66px;border-radius:20px;background:linear-gradient(145deg,#fff,#E3EAF3);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 #fff,0 6px 16px rgba(28,36,51,.1)}
.card3 .tt{font-weight:900;font-size:36px}
.card3 .d{font-weight:500;font-size:26px;line-height:1.55;color:#3A4A63;margin-top:12px}
.card3 .q{position:absolute;left:30px;bottom:22px;font-weight:700;font-size:24px;color:#B45309;background:rgba(245,158,11,.14);padding:6px 18px;border-radius:22px}
.dec{position:absolute;right:0;left:0;height:132px;padding:0 28px;display:flex;align-items:center;gap:22px}
.dec .t{font-weight:500;font-size:28.5px;line-height:1.5;color:#E6ECF4}
.dec .t b{color:#fff;font-weight:900}
"""

S = []

# ---------------------------------------------------------------- 01 cover (dark)
S.append(dict(theme="dark", src="Kitco, JM Bullion (spot, Nov 16, 2026, 09:50 GST) · CBS News, StoneX (record, Jan 28, 2026) · World Gold Council (Q3 2026) · Kitco, U.S. Global Investors (Oct CPI)", body="""
<div class="abs" style="top:104px;right:0;left:0;text-align:right"><span class="kick">پرونده|ی طلا</span><span class="note" style="margin-right:18px">دوشنبه ۱۶ نوامبر ۲۰۲۶</span></div>
<div class="abs h1" style="top:168px;right:0;left:0;font-size:112px">پناهگاهِ امن<br>ترک برداشته؟</div>
<svg class="abs" style="top:418px;left:-72px" width="1080" height="450" viewBox="0 0 1080 450">
<defs>
 <linearGradient id="gF" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FCD34D"/><stop offset=".55" stop-color="#E5980E"/><stop offset="1" stop-color="#9A5208"/></linearGradient>
 <linearGradient id="gT" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF4C7"/><stop offset=".5" stop-color="#FBD15B"/><stop offset="1" stop-color="#E9A21A"/></linearGradient>
 <linearGradient id="gR" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B9650A"/><stop offset="1" stop-color="#6E3606"/></linearGradient>
 <radialGradient id="flo" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F59E0B" stop-opacity=".55"/><stop offset="1" stop-color="#F59E0B" stop-opacity="0"/></radialGradient>
 <radialGradient id="core" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".4" stop-color="#FDE68A" stop-opacity=".8"/><stop offset="1" stop-color="#F59E0B" stop-opacity="0"/></radialGradient>
 <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F59E0B" stop-opacity="0"/><stop offset="1" stop-color="#F59E0B" stop-opacity=".9"/></linearGradient>
 <filter id="b6"><feGaussianBlur stdDeviation="6"/></filter><filter id="b14"><feGaussianBlur stdDeviation="14"/></filter>
 <clipPath id="cL"><polygon points="300,120 566,120 566,165 582,190 556,214 588,244 560,276 592,304 574,345 300,345"/></clipPath>
 <clipPath id="cR"><polygon points="566,120 566,165 582,190 556,214 588,244 560,276 592,304 574,345 840,345 840,120"/></clipPath>
 <g id="bar">
  <polygon points="350,320 730,320 700,232 380,232" fill="url(#gF)"/>
  <polygon points="380,232 700,232 752,190 432,190" fill="url(#gT)"/>
  <polygon points="730,320 700,232 752,190 790,272" fill="url(#gR)"/>
  <polygon points="414,224 666,224 704,198 452,198" fill="none" stroke="#FFF3C4" stroke-opacity=".6" stroke-width="2"/>
  <polyline points="380,232 700,232" stroke="#FFF7DA" stroke-width="2" opacity=".8"/>
 </g>
</defs>
<!-- HUD rings and scan -->
<g fill="none" stroke="#7E9DC0" stroke-linecap="round">
 <circle cx="566" cy="250" r="168" stroke-width="2" stroke-dasharray="2 10" opacity=".7"/>
 <circle cx="566" cy="250" r="212" stroke-width="1.5" stroke-dasharray="1 7" opacity=".45"/>
 <circle cx="566" cy="250" r="128" stroke-width="1" opacity=".25"/>
</g>
<path d="M566 38 A212 212 0 0 1 760 165" fill="none" stroke="url(#scan)" stroke-width="4" stroke-linecap="round"/>
<g stroke="#9FB4D0" stroke-width="2" opacity=".75">
 <line x1="566" y1="74" x2="566" y2="90"/><line x1="566" y1="410" x2="566" y2="426"/><line x1="390" y1="250" x2="406" y2="250"/><line x1="726" y1="250" x2="742" y2="250"/>
</g>
<!-- falling price line behind the bar -->
<g fill="none" stroke-linejoin="round" stroke-linecap="round">
 <polyline points="96,86 190,96 238,84 330,150 392,132 470,214 540,196 640,268 700,252 806,330 870,316 984,398" stroke="#F59E0B" stroke-width="10" opacity=".35" filter="url(#b6)"/>
 <polyline points="96,86 190,96 238,84 330,150 392,132 470,214 540,196 640,268 700,252 806,330 870,316 984,398" stroke="#F59E0B" stroke-width="3.4"/>
 <polyline points="96,86 190,96 238,84 330,150 392,132 470,214 540,196 640,268 700,252 806,330 870,316 984,398" stroke="#FFF7E6" stroke-width="1.2"/>
</g>
<circle cx="96" cy="86" r="7" fill="#FDE68A"/><circle cx="984" cy="398" r="9" fill="#F59E0B"/><circle cx="984" cy="398" r="20" fill="#F59E0B" opacity=".25"/>
<!-- floor glow -->
<ellipse cx="560" cy="350" rx="290" ry="34" fill="url(#flo)"/>
<!-- the broken bar: two halves drifting apart -->
<g clip-path="url(#cL)" transform="translate(-16 12) rotate(-4 470 300)"><use href="#bar"/></g>
<g clip-path="url(#cR)" transform="translate(12 -6) rotate(2.5 660 260)"><use href="#bar"/></g>
<!-- glowing fracture -->
<polyline points="572,150 584,188 558,214 590,244 562,276 592,304 578,342" fill="none" stroke="#F59E0B" stroke-width="16" opacity=".55" filter="url(#b6)"/>
<polyline points="572,150 584,188 558,214 590,244 562,276 592,304 578,342" fill="none" stroke="#FFF7E6" stroke-width="3"/>
<circle cx="576" cy="245" r="70" fill="url(#core)" opacity=".55" filter="url(#b14)"/>
<!-- shards -->
<g fill="#F7B733" stroke="#FFF1C2" stroke-width="1">
 <polygon points="586,356 600,362 592,374"/><polygon points="560,372 572,370 566,386" opacity=".85"/>
 <polygon points="600,392 612,396 604,408" opacity=".7"/><polygon points="574,404 582,406 578,416" opacity=".55"/>
 <polygon points="618,370 626,376 616,382" opacity=".8"/>
</g>
<!-- focus corners -->
<g fill="none" stroke="#DCE5F0" stroke-width="3" stroke-linecap="round" opacity=".85">
 <path d="M318 150 v-26 h26"/><path d="M816 150 v-26 h-26"/><path d="M318 372 v26 h26"/><path d="M816 372 v26 h-26"/>
</g>
<!-- HUD labels -->
<text class="hud" x="92" y="36" direction="ltr">ATH · JAN 28, 2026</text>
<text class="hud" x="92" y="60" direction="ltr" style="fill:#FDE68A;font-weight:700;font-size:16px">5,589</text>
<text class="hud" x="988" y="36" direction="ltr" text-anchor="end">AI SCAN · SAFE-HAVEN STATUS</text>
<text class="hud" x="988" y="60" direction="ltr" text-anchor="end" style="fill:#FBBF24;font-weight:700;font-size:16px">?</text>
<text class="hud" x="92" y="436" direction="ltr" style="fill:#FBBF24">≈ −30% FROM RECORD</text>
<text class="hud" x="988" y="436" direction="ltr" text-anchor="end">XAU/USD 3,845 · NOV 16 · 09:50 GST</text>
</svg>
<div class="abs sub" style="top:868px;right:0;left:0">تنش در منطقه هست. تورم آمریکا بیشتر از انتظار اومد. بانک|های مرکزی ۴۲ درصد بیشتر طلا خریدن.</div>
<div class="abs h3" style="top:980px;right:0;left:0;text-align:right;color:#FBBF24">ولی طلا حدود ۳۰ درصد زیر رکوردشه.</div>
<div class="cta" style="top:1052px"><span><span class="dot"></span>یه دلیل، همه|ی این|ها رو خنثی کرد. ورق بزن</span><span class="ar">←</span></div>
"""))

# ---------------------------------------------------------------- 02 the number (chart)
def xs(d): return 70 + (d - 15) / 315 * 846
def ys(v): return 390 - (v - 3500) / 2300 * 360
pts = [(28, 5589), (79, 4494), (303, 3876), (320, 3845)]
P = [(round(xs(d), 1), round(ys(v), 1)) for d, v in pts]
grid = "".join(f'<line x1="70" x2="916" y1="{ys(v):.1f}" y2="{ys(v):.1f}" stroke="#7E9DC0" stroke-opacity=".28" stroke-width="1"/><text x="58" y="{ys(v)+7:.1f}" direction="rtl" text-anchor="start" font-size="19" fill="#5B6B85" font-family="Vaz">{lab}</text>'
               for v, lab in [(4000, "۴٬۰۰۰"), (4500, "۴٬۵۰۰"), (5000, "۵٬۰۰۰"), (5500, "۵٬۵۰۰")])
months = "".join(f'<text x="{xs(d):.1f}" y="424" direction="rtl" text-anchor="middle" font-size="19" fill="#5B6B85" font-family="Vaz">{m}</text>'
                 for d, m in [(15, "ژانویه"), (75, "مارس"), (136, "مه"), (197, "ژوئیه"), (258, "سپتامبر"), (319, "نوامبر")])
line = " ".join(f"{x},{y}" for x, y in P)
dots = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#F59E0B" stroke="#fff" stroke-width="2.5"/>' for x, y in P[:-1])
CHART = f"""<svg width="936" height="440" viewBox="0 0 936 440" style="direction:ltr">
<defs><filter id="cg"><feGaussianBlur stdDeviation="5"/></filter></defs>
{grid}
<line x1="70" x2="916" y1="390" y2="390" stroke="#7E9DC0" stroke-opacity=".6" stroke-width="1.5"/>
{months}
<line x1="{P[0][0]}" x2="900" y1="{P[0][1]}" y2="{P[0][1]}" stroke="#B45309" stroke-width="1.6" stroke-dasharray="5 6" opacity=".7"/>
<polyline points="{line}" fill="none" stroke="#7E9DC0" stroke-width="2.4" stroke-dasharray="7 7"/>
<line x1="900" x2="900" y1="{P[0][1]+10}" y2="{P[3][1]-14}" stroke="#B45309" stroke-width="2.4"/>
<path d="M892 {P[3][1]-26} L900 {P[3][1]-12} L908 {P[3][1]-26}" fill="none" stroke="#B45309" stroke-width="2.4"/>
<text x="886" y="178" direction="rtl" text-anchor="start" font-family="Vaz" font-weight="900" font-size="30" fill="#B45309">حدود ۳۰ درصد</text>
<text x="886" y="206" direction="rtl" text-anchor="start" font-family="Vaz" font-weight="500" font-size="19" fill="#5B6B85">زیر رکورد</text>
{dots}
<circle cx="{P[3][0]}" cy="{P[3][1]}" r="22" fill="#F59E0B" opacity=".35" filter="url(#cg)"/>
<circle cx="{P[3][0]}" cy="{P[3][1]}" r="11" fill="#B45309" stroke="#fff" stroke-width="3"/>
<text x="{P[0][0]+20}" y="{P[0][1]+30}" direction="rtl" text-anchor="end" font-family="Vaz" font-weight="900" font-size="23" fill="#1C2433">۲۸ ژانویه: رکورد ۵٬۵۸۹ دلار</text>
<text x="{P[1][0]+18}" y="{P[1][1]-46}" direction="rtl" text-anchor="end" font-family="Vaz" font-weight="700" font-size="21" fill="#1C2433">۲۰ مارس: بدترین هفته از دهه|ی ۸۰ میلادی</text>
<text x="{P[1][0]+18}" y="{P[1][1]-18}" direction="rtl" text-anchor="end" font-family="Vaz" font-weight="500" font-size="19" fill="#5B6B85">بیش از ۱۰ درصد ریزش در یک هفته</text>
<text x="{P[2][0]-16}" y="{P[2][1]+38}" direction="rtl" text-anchor="start" font-family="Vaz" font-weight="700" font-size="21" fill="#1C2433">۳۰ اکتبر: بدترین اکتبر از ۲۰۰۸</text>
<text x="{P[3][0]-6}" y="{P[3][1]-92}" direction="rtl" text-anchor="start" font-family="Vaz" font-weight="900" font-size="23" fill="#1C2433">۱۶ نوامبر: حدود ۳٬۸۴۵ دلار</text>
<text x="{P[3][0]-6}" y="{P[3][1]-64}" direction="rtl" text-anchor="start" font-family="Vaz" font-weight="500" font-size="19" fill="#5B6B85">پایین|ترین سطح در بیش از یک سال</text>
</svg>"""
S.append(dict(theme="light", src="CBS News, StoneX, Nasdaq (record, Jan 28) · Investing.com, Global Times (week to Mar 20) · Investing.com via Averin, U.S. Global Investors (October) · Kitco, Trading Economics (Nov 16, 2026)", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick n">یک عدد</span></div>
<div class="abs h2" style="top:168px;right:0;left:0">از ۵٬۵۸۹ دلار به ۳٬۸۴۵ دلار<br><span class="am">در کمتر از ۱۰ ماه</span></div>
<div class="abs glass" style="top:352px;right:0;left:0;height:560px;padding:34px 0 0 0">
<div style="padding:0 34px;font-weight:700;font-size:25px;color:#3A4A63">قیمت هر اونس طلا، دلار؛ چهار ایستگاه کلیدی</div>
<div style="margin-top:22px">{CHART}</div></div>
<div class="abs note" style="top:930px;right:0;left:0;text-align:right">نقطه|چین: فقط ایستگاه|های کلیدی، نه همه|ی مسیر. قیمت ۱۶ نوامبر: ۹:۵۰ صبح به وقت دبی.</div>
<div class="abs glass" style="top:1000px;right:0;left:0;height:118px;display:flex;align-items:center;justify-content:space-between;padding:0 34px">
<div style="font-weight:700;font-size:30px">سؤال اینه: این همه دلیل برای بالا رفتن داشت؛ <span class="am">پس چرا ریخت؟</span></div>
<div style="font-family:VazL;font-size:34px;color:#B45309">←</div></div>
"""))

# ---------------------------------------------------------------- 03 the paradox (scale)
SCALE = """<svg width="936" height="330" viewBox="0 0 936 330" style="direction:ltr">
<defs><radialGradient id="orbA" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#FFF4C7"/><stop offset=".45" stop-color="#F7B733"/><stop offset="1" stop-color="#B45309"/></radialGradient>
<radialGradient id="orbG" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#DCE6F2"/><stop offset="1" stop-color="#9DB3CE"/></radialGradient>
<filter id="sg"><feGaussianBlur stdDeviation="10"/></filter></defs>
<polygon points="468,118 420,292 516,292" fill="#1C2433" opacity=".9"/>
<rect x="360" y="292" width="216" height="14" rx="7" fill="#1C2433"/>
<line x1="178" y1="178" x2="758" y2="58" stroke="#1C2433" stroke-width="12" stroke-linecap="round"/>
<circle cx="468" cy="118" r="13" fill="#F59E0B" stroke="#fff" stroke-width="3"/>
<line x1="178" y1="178" x2="128" y2="236" stroke="#5B6B85" stroke-width="2.5"/><line x1="178" y1="178" x2="228" y2="236" stroke="#5B6B85" stroke-width="2.5"/>
<line x1="758" y1="58" x2="708" y2="116" stroke="#5B6B85" stroke-width="2.5"/><line x1="758" y1="58" x2="808" y2="116" stroke="#5B6B85" stroke-width="2.5"/>
<path d="M96 236 H260 Q240 268 178 268 Q116 268 96 236Z" fill="#1C2433"/>
<path d="M676 116 H840 Q820 148 758 148 Q696 148 676 116Z" fill="#1C2433"/>
<circle cx="178" cy="166" r="80" fill="#F59E0B" opacity=".35" filter="url(#sg)"/>
<circle cx="178" cy="172" r="66" fill="url(#orbA)"/>
<text x="178" y="166" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="25" fill="#1C2433">نرخ</text>
<text x="178" y="196" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="25" fill="#1C2433">بهره</text>
<circle cx="722" cy="86" r="28" fill="url(#orbG)" stroke="#fff" stroke-width="2"/><text x="722" y="96" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="26" fill="#1C2433">۱</text>
<circle cx="776" cy="86" r="28" fill="url(#orbG)" stroke="#fff" stroke-width="2"/><text x="776" y="96" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="26" fill="#1C2433">۲</text>
<circle cx="749" cy="40" r="28" fill="url(#orbG)" stroke="#fff" stroke-width="2"/><text x="749" y="50" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="26" fill="#1C2433">۳</text>
</svg>"""
S.append(dict(theme="light", src="Kitco (Nov 13) · U.S. Global Investors, Kitco (Oct CPI) · World Gold Council, Kitco (Q3 2026) · Trading Economics, Kitco (CME FedWatch, Nov 11–13) · Mitrade, Admiral Markets (10Y, Nov 13–16)", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick n">یک خبر</span></div>
<div class="abs h2" style="top:168px;right:0;left:0">همه|چیز به نفع طلا بود…<br><span class="am">جز یه چیز</span></div>
<div class="abs" style="top:356px;right:0;left:0">{SCALE}</div>
<div class="abs glass" style="top:694px;right:0;width:452px;height:294px;padding:22px 26px">
<div style="font-weight:900;font-size:27px;color:#3A4A63">سه دلیل برای بالا رفتن</div>
<div style="font-size:23px;line-height:1.5;margin-top:12px"><b>۱. تنش در منطقه</b></div>
<div style="font-size:23px;line-height:1.5;margin-top:8px"><b>۲. تورم بیشتر از انتظار</b><div style="font-weight:500;font-size:20px;color:#5B6B85">اکتبر آمریکا: ۰٫۴ درصد؛ پیش|بینی ۰٫۳</div></div>
<div style="font-size:23px;line-height:1.5;margin-top:8px"><b>۳. خرید بیشتر بانک|های مرکزی</b><div style="font-weight:500;font-size:20px;color:#5B6B85">فصل سوم: ۳۲۱ تن؛ ۴۲ درصد بیشتر از پارسال</div></div></div>
<div class="abs glass" style="top:694px;left:0;width:464px;height:294px;padding:22px 26px;border:2px solid rgba(245,158,11,.75)">
<div style="font-weight:900;font-size:27px;color:#B45309">یه وزنه|ی سنگین: پول گرون شد</div>
<div style="font-weight:500;font-size:22px;color:#5B6B85;margin-top:14px">احتمال افزایش نرخ فد در دسامبر</div>
<div style="font-weight:900;font-size:38px;line-height:1.3">حدود ۹۰ درصد</div>
<div style="font-weight:500;font-size:22px;color:#5B6B85;margin-top:8px">سود اوراق ۱۰ ساله|ی آمریکا</div>
<div style="font-weight:900;font-size:38px;line-height:1.3">حدود ۵٫۱۵ درصد</div></div>
<div class="abs" style="top:1004px;right:0;left:0;border-radius:22px;background:#1C2433;color:#fff;padding:20px 28px;font-weight:700;font-size:24.5px;line-height:1.5">طلا سود نمی|ده. وقتی پولِ بی|خطر بیش از ۵ درصد سود می|ده، <span style="color:#FBBF24">نگه داشتن طلا هزینه داره.</span></div>
"""))

# ---------------------------------------------------------------- 04 why: the chain
nodes = [("تورم آمریکا بیشتر از انتظار اومد", "۰٫۴ درصد در اکتبر"),
         ("بازار مطمئن|تر شد فد در دسامبر نرخ رو بالا می|بره", "حدود ۹۰ درصد"),
         ("سود اوراق ۱۰ ساله|ی آمریکا بالا رفت", "حدود ۵٫۱۵ درصد"),
         ("دلار قوی|تر شد", "طلا برای بقیه گرون|تر"),
         ("طلای بی|سود، کم|جاذبه|تر شد", "پایین|ترین در بیش از یک سال")]
NODES = "".join(f"""<div class="node glass row" style="top:{268 + k*120}px"><div class="badge">{'۱۲۳۴۵'[k]}</div><div class="t">{t}</div><span class="chip">{c}</span></div>""" for k, (t, c) in enumerate(nodes))
S.append(dict(theme="light", src="U.S. Global Investors, Kitco (CPI) · Trading Economics, Kitco (CME FedWatch) · Mitrade, Admiral Markets (10Y) · Kitco, Gulf News (dollar) · Khaleej Times, Gulf Business, Trading Economics (CBUAE, Sep–Oct 2026)", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick n">چرا؟</span></div>
<div class="abs h2" style="top:168px;right:0;left:0;font-size:56px">زنجیره|ای که طلا رو پایین کشید</div>
<svg class="abs" style="top:300px;right:40px" width="80" height="560"><defs><filter id="lg"><feGaussianBlur stdDeviation="4"/></filter></defs>
<line x1="40" y1="0" x2="40" y2="500" stroke="#F59E0B" stroke-width="10" opacity=".35" filter="url(#lg)"/><line x1="40" y1="0" x2="40" y2="500" stroke="#F59E0B" stroke-width="3"/><line x1="40" y1="0" x2="40" y2="500" stroke="#FFF7E6" stroke-width="1"/></svg>
{NODES}
<div class="abs glass" style="top:886px;right:0;left:0;height:232px;padding:26px 30px;border:2px solid rgba(245,158,11,.7)">
<div style="font-weight:900;font-size:30px;color:#B45309">نسخه|ی امارات</div>
<div style="font-weight:500;font-size:26px;line-height:1.6;margin-top:8px">درهم به دلار گره خورده. نرخ پایه|ی بانک مرکزی امارات (الان ۳٫۹ درصد) به نرخ فد وصله و معمولاً هم|جهتش تغییر می|کنه؛ یعنی این زنجیره به وام|های <span class="ltr">EIBOR</span> هم می|رسه.</div></div>
"""))

# ---------------------------------------------------------------- 05 impact map (view, diverging dumbbells)
WARM, COOL, MID = "#B45309", "#2F6DB5", "#8A96A8"
def track(lo, hi):
    X = lambda v: 290 + v * 120
    col = lambda v: WARM if v < 0 else (COOL if v > 0 else MID)
    ticks = "".join(f'<line x1="{X(v)}" x2="{X(v)}" y1="44" y2="68" stroke="#9AA6B6" stroke-width="{2 if v==0 else 1}" opacity="{.9 if v==0 else .5}"/>' for v in (-2, -1, 0, 1, 2))
    return f"""<svg width="540" height="112" viewBox="0 0 540 112" style="direction:ltr;flex:1">
<line x1="50" x2="530" y1="56" y2="56" stroke="#C3CEDC" stroke-width="2"/>{ticks}
<line x1="{X(lo)}" x2="{X(hi)}" y1="56" y2="56" stroke="#9AA6B6" stroke-width="7" stroke-linecap="round"/>
<circle cx="{X(lo)}" cy="56" r="13" fill="{col(lo)}" stroke="#fff" stroke-width="3"/>
<circle cx="{X(hi)}" cy="56" r="13" fill="{col(hi)}" stroke="#fff" stroke-width="3"/></svg>"""
rows = [("طلافروش و جواهرفروش", "ارزش موجودی پایین اومد؛ ولی قیمت پایین|تر مشتری رو برمی|گردونه", -2, 1),
        ("تولیدکننده با وام نرخ متغیر", "اگه نرخ امارات بالا بره، تأمین مالی گرون|تر", -2, -1),
        ("واردکننده از اروپا و آسیا", "درهمِ قوی|تر یعنی خرید ارزون|تر؛ ولی وام گرون|تر", -1, 1),
        ("صادرکننده به بازار غیردلاری", "جنس شما برای خریدار خارجی گرون|تر می|شه", -1, 0),
        ("تاجر نفت و مواد غذایی", "هزینه|ی نگه داشتن موجودی با وام بالاتر", -1, 0),
        ("صاحب نقدینگی درهمی", "سود سپرده معمولاً همراه نرخ پایه بالا می|ره", 1, 2)]
MROWS = "".join(f"""<div class="mrow" style="top:{352 + k*112}px;{'border-top:1px solid rgba(126,157,192,.35);' if k else ''}"><div class="lab"><div class="a">{a}</div><div class="b">{b}</div></div>{track(lo, hi)}</div>""" for k, (a, b, lo, hi) in enumerate(rows))
S.append(dict(theme="light", src="Our mechanism view, not a forecast · Khaleej Times, Gulf Business (CBUAE base rate, savers and borrowers, Sep–Nov 2026) · Gulf News (dirham peg) · Kitco, Gulf News (stronger dollar)", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick n">از دید هر صنف</span></div>
<div class="abs h2" style="top:168px;right:0;left:0">یه خبر، <span class="am">شش سرنوشت</span></div>
<div class="abs" style="top:282px;left:0;width:540px;height:56px;direction:ltr;font-weight:700;font-size:23px">
<span class="abs" style="left:24px;top:10px;color:{WARM}">● فشار</span><span class="abs" style="left:262px;top:10px;color:#5B6B85">خنثی</span><span class="abs" style="right:0;top:10px;color:{COOL}">فرصت ●</span></div>
<div class="abs" style="top:282px;right:0;width:372px;text-align:right;font-weight:700;font-size:23px;color:#5B6B85;padding-top:10px">اثر کوتاه|مدت، از دید ما</div>
{MROWS}
<div class="abs note" style="top:1036px;right:0;left:0;text-align:right;line-height:1.55">هر خط، بازه|ی اثر رو نشون می|ده. برداشت ما از سازوکاره، نه پیش|بینی؛ اثر واقعی به قرارداد و ساختار هر کسب|وکار بستگی داره.</div>
"""))

# ---------------------------------------------------------------- 06 zoom: three sectors, three questions
ic_gold = '<svg width="40" height="40" viewBox="0 0 48 48" fill="none" stroke="#1C2433" stroke-width="2.8" stroke-linejoin="round"><path d="M6 36h36l-5-12H11zM14 24h20l-4-9H18z"/></svg>'
ic_bank = '<svg width="40" height="40" viewBox="0 0 48 48" fill="none" stroke="#1C2433" stroke-width="2.8" stroke-linejoin="round"><path d="M6 18L24 8l18 10zM10 20v16M19 20v16M29 20v16M38 20v16M6 40h36"/></svg>'
ic_ship = '<svg width="40" height="40" viewBox="0 0 48 48" fill="none" stroke="#1C2433" stroke-width="2.8" stroke-linejoin="round"><path d="M6 30h36l-5 9H11zM12 30V20h24v10M18 20v-7h12v7"/></svg>'
cards = [(ic_gold, "طلافروش|ها", "تقاضای جواهر در امارات در فصل سوم ۲۹ درصد کمتر از پارسال بود (۴٫۵ تن). ولی هر بار قیمت پایین اومده، رفت|وآمد مغازه|ها و خرید شمش بیشتر شده.", "ریسک ارزش ویترین|تون پوشش داره؟"),
         (ic_bank, "وام|گیرنده|های EIBOR", "نرخ پایه|ی امارات ۳٫۹ درصده و به نرخ فد وصله. جلسه|ی بعدی فد ۸ و ۹ دسامبره و بازار حدود ۹۰ درصد احتمال افزایش می|ده.", "نرخ وام شما کی تمدید می|شه؟"),
         (ic_ship, "واردکننده و صادرکننده", "درهم به دلار گره خورده. دلار قوی|تر یعنی خرید از اروپا و آسیا ارزون|تر، و فروش به همون بازارها سخت|تر.", "قراردادهاتون به چه ارزیه؟")]
CARDS = "".join(f"""<div class="card3 glass" style="top:{282 + k*278}px"><div class="hd"><div class="ic">{ic}</div><div class="tt">{t.replace('EIBOR','<span class="ltr">EIBOR</span>')}</div></div><div class="d">{d}</div><div class="q">{q}</div></div>""" for k, (ic, t, d, q) in enumerate(cards))
S.append(dict(theme="light", src="Khaleej Times citing WGC Gold Demand Trends Q3 2026 (Nov 3) · Khaleej Times, Emirates 24|7 (Dubai buying on dips) · Khaleej Times, Gulf Business (CBUAE) · Kitco, Trading Economics (Fed, Dec 8–9 odds)", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick n">زوم</span></div>
<div class="abs h2" style="top:168px;right:0;left:0">سه صنف، <span class="am">سه سؤال</span></div>
{CARDS}
"""))

# ---------------------------------------------------------------- 07 the other side (central banks bar chart)
def by(v): return 300 - v / 360 * 250
BARS = f"""<svg width="420" height="340" viewBox="0 0 420 340" style="direction:ltr">
<line x1="30" x2="400" y1="300" y2="300" stroke="#7E9DC0" stroke-opacity=".7" stroke-width="1.5"/>
<path d="M90 300 V{by(226)+4:.1f} Q90 {by(226):.1f} 94 {by(226):.1f} H182 Q186 {by(226):.1f} 186 {by(226)+4:.1f} V300Z" fill="#9DB3CE"/>
<path d="M244 300 V{by(321)+4:.1f} Q244 {by(321):.1f} 248 {by(321):.1f} H336 Q340 {by(321):.1f} 340 {by(321)+4:.1f} V300Z" fill="#F59E0B"/>
<text x="138" y="{by(226)-14:.1f}" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="34" fill="#1C2433">۲۲۶</text>
<text x="292" y="{by(321)-14:.1f}" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="900" font-size="34" fill="#1C2433">۳۲۱</text>
<text x="138" y="332" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="500" font-size="21" fill="#5B6B85">فصل سوم ۲۰۲۵</text>
<text x="292" y="332" direction="rtl" text-anchor="middle" font-family="Vaz" font-weight="700" font-size="21" fill="#1C2433">فصل سوم ۲۰۲۶</text>
</svg>"""
S.append(dict(theme="light", src="World Gold Council, Gold Demand Trends Q3 2026 (Nov 3) · Kitco, EWN, Engineering News (Nov 3) · Admiral Markets, Kitco (Fed calendar)", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick n">سمت دیگر ماجرا</span></div>
<div class="abs h2" style="top:168px;right:0;left:0">بزرگ|ترها نفروختن؛<br><span class="am">بیشتر خریدن</span></div>
<div class="abs glass" style="top:352px;right:0;left:0;height:400px;padding:26px 30px">
<div style="font-weight:700;font-size:25px;color:#3A4A63">خرید خالص بانک|های مرکزی، تن</div>
<div class="abs" style="left:26px;top:44px">{BARS}</div>
<div class="abs" style="right:30px;top:120px;width:420px;text-align:right">
<div class="chip" style="font-size:30px">۴۲ درصد بیشتر</div>
<div style="font-weight:500;font-size:25px;line-height:1.6;margin-top:18px;color:#3A4A63">۹ ماه اول ۲۰۲۶: ۶۷۵ تن، ۶ درصد بیشتر از همین دوره|ی پارسال.</div></div></div>
<div class="abs glass" style="top:774px;right:0;width:452px;height:226px;padding:22px 26px">
<div style="font-weight:900;font-size:26px;color:#2F6DB5">داده</div>
<div style="font-weight:500;font-size:23.5px;line-height:1.6;margin-top:6px">شورای جهانی طلا انتظار داره خرید بانک|های مرکزی در ۲۰۲۶ دست|کم هم|اندازه|ی ۲۰۲۵ باشه.</div></div>
<div class="abs glass" style="top:774px;left:0;width:464px;height:226px;padding:22px 26px">
<div style="font-weight:900;font-size:26px;color:#B45309">برداشت ما</div>
<div style="font-weight:500;font-size:23.5px;line-height:1.6;margin-top:6px">فشار فعلی بیشتر از نرخ بهره|ست تا فرار خریدارهای بزرگ. یعنی کف قیمت معلومه؟ <b>نه.</b></div></div>
<div class="abs" style="top:1022px;right:0;left:0;height:96px;border-radius:22px;background:#1C2433;color:#fff;display:flex;align-items:center;justify-content:space-around;padding:0 20px;font-weight:700;font-size:25px">
<span><span style="color:#FBBF24">۱۸ نوامبر، ساعت ۲۳ دبی:</span> صورت|جلسه|ی فد</span><span style="width:2px;height:40px;background:rgba(255,255,255,.35);display:inline-block"></span><span><span style="color:#FBBF24">۸ و ۹ دسامبر:</span> جلسه|ی فد</span></div>
"""))

# ---------------------------------------------------------------- 08 decision + record (dark)
decs = [("موجودی طلا دارید؟", "سؤال درست اینه که ریسک ویترین پوشش داره یا نه؛ نه این|که قیمت فردا کجاست."),
        ("وام با نرخ متغیر دارید؟", "قبل از ۹ دسامبر، تاریخ تمدید نرخ رو چک کنید."),
        ("با ارز دیگه می|خرید یا می|فروشید؟", "ببینید قراردادها به چه ارزیه و کی تسویه می|شه.")]
DECS = "".join(f"""<div class="dec glass" style="top:{262 + k*146}px"><div class="badge">{'۱۲۳'[k]}</div><div class="t"><b>{a}</b> {b}</div></div>""" for k, (a, b) in enumerate(decs))
S.append(dict(theme="dark", src="Kitco, JM Bullion (spot, Nov 16, 2026) · Kitco, Trading Economics (CME FedWatch) · Khaleej Times (CBUAE) · Educational analysis, not financial advice", body=f"""
<div class="abs" style="top:110px;right:0"><span class="kick">یک تصمیم</span></div>
<div class="abs h2" style="top:168px;right:0;left:0;font-size:58px">برای کسب|وکار شما یعنی چی؟</div>
{DECS}
<div class="abs" style="top:712px;right:0;left:0;height:184px;border:2px dashed rgba(245,158,11,.85);border-radius:26px;padding:22px 30px;background:rgba(245,158,11,.06)">
<div style="font-family:Unb;font-weight:700;font-size:15px;letter-spacing:.22em;color:#FBBF24;direction:ltr;text-align:right">ON RECORD · {SERIAL}</div>
<div style="font-weight:500;font-size:27.5px;line-height:1.6;margin-top:8px;color:#F3F6FA">امروز، ۱۶ نوامبر ۲۰۲۶، این رو ثبت می|کنیم: طلا حدود ۳٬۸۴۵ دلار، احتمال افزایش نرخ فد در دسامبر حدود ۹۰ درصد. <span style="color:#FBBF24">سه ماه دیگه با هم برمی|گردیم سراغش.</span></div></div>
<div class="abs" style="top:926px;right:0;left:0;text-align:right;font-weight:900;font-size:31px;line-height:1.45">تو کامنت بنویسید: این ریزش برای کسب|وکار شما <span style="color:#FBBF24">«فشار»</span>ه یا <span style="color:#7FB0EA">«فرصت»</span>؟</div>
<div class="abs" style="top:1040px;right:0;left:0;text-align:right">
<div style="font-weight:900;font-size:29px;color:#FBBF24">عدد از ما، تصمیم از شما.</div>
<div class="note" style="margin-top:6px;line-height:1.5;font-size:20.5px">تحلیل آموزشی، نه توصیه|ی مالی. برای پوشش ریسک و ابزارهای مالی با بانک یا مشاور دارای مجوز <span class="ltr">SCA</span> مشورت کنید.</div></div>
"""))

SLIDES = [dict(theme=s["theme"], src=s["src"], body=s["body"].replace("|", "‌")) for s in S]
