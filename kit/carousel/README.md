# Finance Pulse carousels (1080x1350)

    cd kit/carousel && python3 build_carousel.py fp0032.py out          # all slides
    python3 build_carousel.py fp0032.py out 1,3                          # only some slides

- A deck is a small Python file (see fp0032.py): SERIAL, TAG, SLIDES (theme light/dark, body HTML, English sources line).
  In Persian text, "|" stands for ZWNJ and is replaced at build time.
- Shared signature comes from build_carousel.py: lockup, tag + page counter, serial + sources strip, ANIYA x CLAUDE,
  72 px empty safe margin on every side (inside the 3:4 grid crop), dotted rings in the background.
- Fonts come from ../v2/fonts (Lalezar for the cover headline, Vazirmatn for everything with digits).
- Persian labels inside SVG need direction="rtl"; with rtl, text-anchor start = right edge, end = left edge.
- Pattern that worked for FP-0032: dark cover (one question, one image, one number), light inner slides
  (number, paradox, chain, sector map, zoom, other side), dark last slide (decision, record, comment question).
- Check every PNG with Read before archiving: no overlap, no orphan words, sources line at most 3 lines.
- Archive: archive/<serial>/<serial>-NN.png + caption.txt, then serial.txt.
