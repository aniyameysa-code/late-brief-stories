# Finance Pulse runbook (for the wake-ups in Aniya's main chat)

**13 Nov 2026: Metricool Free plan limit reached (20 published posts a month, resets on the 1st).**
FP-0025 failed at 10:00 with "You have reached your Metricool account limit". Until Aniya upgrades
or until 1 Dec 2026: render and archive as usual, but do NOT schedule on Metricool. Send the MP4 with
SendUserFile before the slot time so she can post it to her story herself, and say so in one line.

**Since 4 Nov 2026 every slot is ONE v2 video story with music (section 8 and kit/v2/README.md).**
Morning (Mon to Fri, 10:00): the day's biggest market move; bars = daily % moves of the main assets.
Evening (daily, 18:00): the most important economic story with a constructive angle.
Sections 1 and 2 below still define the content and sourcing; ignore their old slide layouts.

Stories for @aniyameysa (The Decision Room). Talk to her in Persian or Finglish, as she writes.
Load the decision-room-brand and finance-pulse skills first if they are listed.

## 0. Setup
- Repo clone: /home/claude/late-brief-stories (git pull --rebase origin main). If it is missing, clone
  https://github.com/aniyameysa-code/late-brief-stories. If a push is refused, call add_repo
  (owner aniyameysa-code, repo late-brief-stories, access push) and retry.
- Renderer: kit/build_story.py with kit/fonts and kit/specs (examples only; their content is old).
  `cd kit && python3 build_story.py specs/<file>.json out/<serial>.png` (Playwright + Chromium are preinstalled).
- Next serial = serial.txt + 1, written FP-0000. Read serial.txt right before rendering: other chats
  of hers may also publish Finance Pulse pieces (4 Nov: FP-0006 came from another chat).
- Before starting, check Metricool getScheduledPosts for today: if a story for this slot is already
  published or scheduled (morning 09:00 to 12:00, evening 17:00 to 20:00), do not make another one;
  tell her in one line instead.

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
- Since 13 Nov (a 17:29 wake-up never arrived): every slot also gets a BACKUP wake-up 15 minutes later
  (morning 09:42, evening 17:45) that runs the slot only if stories/<date>/<slot>.mp4 is missing from the repo.
- Duplicate guard: before starting any run, git pull and skip the slot if stories/<date>/<slot>.mp4 already exists.

## 8. Format v2 (from 4 Nov 2026): video stories with music
Aniya asked for more playful, engaging stories: always with music; charts, tables and timelines;
striking graphics; ways to think; one story seen from several angles with its effects; a personal
voice that talks to people so they write back; psychology (curiosity hook, "which side are you?",
a free thinking framework, an invitation to DM); new fonts and graphics.
- Use kit/v2 (README there). One video story per slot, about 30 s, six scenes.
- Hook: a curiosity line («برای کسب‌وکار شما یعنی چی؟ تا آخر ببینید.»). Angles: importer, exporter,
  and one more group, mechanism only («توضیحِ سازوکاره، نه پیش‌بینی»). Think: three questions.
  CTA: Aniya's first-person line, «شما کدوم طرفید؟» with two options, DM invitation, keyword «عضویت».
- Same rules as above: every number with two sources, no advice, sources and disclaimer on screen.
- Check stills at the busiest moment of each scene before the full render.
- Metricool takes the MP4 as an Instagram STORY the same way (media = SHA raw URL of archive/<serial>.mp4).
- Two looks (Aniya's choice, 14 Nov 2026):
  - Morning: light theme (default), tags ["MORNING MARKETS", "<DD MON YYYY>"], music 96 BPM Am-F-C-G.
  - Evening: add "theme": "evening" to the spec (deep navy and gold, calmer 84 BPM Dm-Bb-F-C music),
    tags ["EVENING BRIEF", "<DD MON YYYY>"].
