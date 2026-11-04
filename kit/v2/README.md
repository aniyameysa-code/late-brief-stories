# Finance Pulse v2: motion stories with music

    cd kit/v2 && python3 render_v2.py specs/<spec>.json out/<serial>.mp4
    python3 render_v2.py specs/<spec>.json out/check --frames 3.9,8.9,13.5,19,24,29.5   # stills to check first

- 1080x1920, 30 fps, H.264 + AAC, about 30 s. Each scene is rendered to its own MP4 and joined;
  music.py composes an original music bed (royalty-free) with typing clicks and scene whooshes.
- Fonts: Lalezar (headlines), Readex Pro (body), Vazirmatn (all numbers, because Lalezar and Readex
  draw «٫» like a comma), Unbounded (Latin caps).
- Scene types, in order: hook, bars, timeline, angles, think, cta. See specs/example.json.
  - hook: kicker, headline (typed on with an underline cursor), counter from/to with unit and change, sub.
  - bars: up to 3 bars of % change, optional numbered ring, 2 callouts.
  - timeline: 3 or 4 dated steps.
  - angles: 3 cards "اگه واردکننده‌اید / صادرکننده‌اید / ..." explaining the mechanism, not predicting.
  - think: 3 questions to ask before a decision.
  - cta: personal line, a question with 2 options, DM line, bubble with the keyword «عضویت».
- The gold-bar illustration shows only in the hook; other topics get the globe and light line.
- Check stills before the full render (2 to 3 minutes).
