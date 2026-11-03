# Finance Pulse runbook (for the wake-ups in Aniya's main chat)

Stories for @aniyameysa (The Decision Room). Talk to her in Persian or Finglish, as she writes.
Load the decision-room-brand and finance-pulse skills first if they are listed.

## 0. Setup
- Repo clone: /home/claude/late-brief-stories (git pull --rebase origin main). If it is missing, clone
  https://github.com/aniyameysa-code/late-brief-stories. If a push is refused, call add_repo
  (owner aniyameysa-code, repo late-brief-stories, access push) and retry.
- Renderer: kit/build_story.py with kit/fonts and kit/specs (examples only; their content is old).
  `cd kit && python3 build_story.py specs/<file>.json out/<serial>.png` (Playwright + Chromium are preinstalled).
- Next serial = serial.txt + 1, written FP-0000.

## 1. Morning (weekdays, publish 10:00 Dubai): kind "prices", one slide
- Global figures only: forex (EUR/USD, GBP/USD, USD/JPY, DXY ...), gold, Brent, WTI, crypto (BTC, ETH, ...).
- No Iranian markets or Iran news.
- Every figure confirmed by two sources; if they disagree beyond intraday drift, mark «حدودی» with no % change, or leave it out.
- Shape: kit/specs/morning.json (4 tiles, board with «فارکس» and «کریپتو» columns).

## 2. Evening (daily, publish 18:00 and 18:01 Dubai): kind "news", two slides
- She wants IMPORTANT economic news with a positive or constructive angle (3 Nov feedback: a crypto
  story about users withdrawing money from Binance was "not important"; the UAE trade record and the
  ADNOC Gas LNG deal were the right kind).
- Slide 1: the most important global economy, energy or markets story of the last 24 hours with a
  constructive angle. Crypto only when it is a major market-moving development, told by its business meaning.
- Slide 2: UAE / GCC trade, energy or economy, positive or neutral.
- Every fact and number confirmed by two outlets or one outlet plus an official statement. Never estimate.
- Shape: kit/specs/evening1.json and evening2.json. 3 or 4 tiles; keep tile labels short (one line).

## 3. Content rules (both)
- No buy/sell suggestion, no predictions, no signals. Separate fact from opinion.
- Nothing that could harm the UAE economy, the dirham or UAE foreign relations. No Iran.
- Geopolitics only as a short neutral phrase reported by a named outlet.
- Persian digits, «٫» decimals, «٬» thousands, «درصد» not «٪», no «·» beside Persian digits. No emoji or hype.
- Disclaimer «اطلاع‌رسانیه، نه توصیه‌ی مالی.»; crypto adds no suggestion to buy or sell any coin;
  hedging, contracts or instruments add: consult a licensed bank or SCA-licensed adviser.
- English sources line naming each outlet and date.

## 4. Render and check
- Open each PNG with Read: no overlap or clipping, one-line labels, FINANCE PULSE lockup, serial,
  sources strip and ANIYA × CLAUDE signature visible. Fix and re-render.

## 5. Archive, host, publish
- Copy to stories/<YYYY-MM-DD>/<morning|evening1|evening2>.png and archive/<serial>.png, write serial.txt,
  commit (with the attribution lines the session asks for), push to main.
- Check https://raw.githubusercontent.com/aniyameysa-code/late-brief-stories/<SHA>/archive/<serial>.png
  returns 200 image/png.
- Metricool createScheduledPost: blogId "7580488", date and publicationDate at the target time Asia/Dubai
  (if under 5 minutes away or past, 5 minutes from now), providers [{"network":"instagram"}],
  instagramData {"type":"STORY"}, media [the SHA raw URL], text "", autoPublish true, draft false,
  descendants [], firstCommentText "", mediaAltText [], shortener false, smartLinkData {"ids":[]},
  hasNotReadNotes false.

## 6. Archive page and report
- Page https://claude.ai/artifact/4dzC4A5SAocU3WMmReFtrH (local copy /home/claude/story/late-brief.html):
  read it first, upload the PNG(s) as assets, set the JSON in <script id="brief"> (morning: today only;
  evening: add to today's), publish. On a conflict, merge and publish again.
- Send the PNG(s) with SendUserFile and a short message with serial(s) and scheduled time(s).

## 7. Keep the wake-ups going
- list_triggers: if fewer than 4 future Finance Pulse wake-ups are pending, add the next ones with
  send_later (morning 09:27 Dubai Mon to Fri, evening 17:29 Dubai every day), message:
  "Finance Pulse <morning|evening> run: follow kit/RUNBOOK.md in the late-brief-stories repo."
