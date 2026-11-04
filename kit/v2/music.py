"""Original music bed for Finance Pulse v2 stories (synthesized, royalty-free).

    python3 music.py '<cues json>' out.wav
cues: {"total": seconds, "clicks": [t...], "whoosh": [t...], "pops": [t...], "seed": n}
Calm-premium groove: Am-F-C-G pads, soft pluck arpeggio, light kick and hat,
keyboard clicks while the headline types, airy whooshes on scene changes.
"""
import json, sys, wave
import numpy as np

SR = 44100
cues = json.loads(sys.argv[1])
out = sys.argv[2]
T = cues["total"] + 0.4
n = int(T * SR)
rng = np.random.default_rng(cues.get("seed", 7))
L = np.zeros(n); Rch = np.zeros(n)
BPM = 96; BEAT = 60 / BPM

CH = [  # (bass, pad notes)
    (110.00, [220.00, 261.63, 329.63]),   # Am
    (87.31, [174.61, 220.00, 261.63]),    # F
    (130.81, [261.63, 329.63, 392.00]),   # C
    (98.00, [196.00, 246.94, 293.66]),    # G
]
CHORD_LEN = 8 * BEAT


def add(buf, start, sig):
    i = int(start * SR)
    if i >= n:
        return
    j = min(n, i + len(sig))
    buf[i:j] += sig[: j - i]


def lowpass(x, a):
    y = np.empty_like(x); acc = 0.0
    for k in range(len(x)):  # small signals only
        acc += a * (x[k] - acc); y[k] = acc
    return y


def env(length, att, rel):
    m = int(length * SR); e = np.ones(m)
    a = max(1, int(att * SR)); r = max(1, int(rel * SR))
    e[:a] = np.linspace(0, 1, a); e[-r:] *= np.linspace(1, 0, r)
    return e


# pads
t_chord = 0.0; ci = 0
while t_chord < T:
    bass, notes = CH[ci % 4]
    dur = CHORD_LEN + 0.6
    tt = np.arange(int(dur * SR)) / SR
    e = env(dur, 0.9, 1.0)
    pad = np.zeros_like(tt)
    for f in notes:
        for det in (-0.12, 0.0, 0.12):
            ff = f * (1 + det / 100)
            pad += sum(np.sin(2 * np.pi * ff * h * tt) / h ** 1.6 for h in (1, 2, 3, 4))
    pad *= e * 0.018
    add(L, t_chord, pad); add(Rch, t_chord + 0.012, pad)
    # sub bass on each bar
    for bar in range(2):
        bt = t_chord + bar * 4 * BEAT
        d = 4 * BEAT
        tb = np.arange(int(d * SR)) / SR
        s = np.sin(2 * np.pi * bass * tb) * np.exp(-tb * 0.9) * env(d, 0.02, 0.3) * 0.11
        add(L, bt, s); add(Rch, bt, s)
    t_chord += CHORD_LEN; ci += 1

# pluck arpeggio from 2.4s
step = BEAT / 2; k = 0; t = 2.4
while t < T - 1.2:
    ci = int(t // CHORD_LEN) % 4
    notes = CH[ci][1]
    f = notes[[0, 1, 2, 1, 2, 0, 1, 2][k % 8]] * 2
    d = 0.6; tt = np.arange(int(d * SR)) / SR
    s = (np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(4 * np.pi * f * tt)) * np.exp(-tt * 7) * 0.05
    pan = 0.5 + 0.25 * np.sin(k * 0.9)
    add(L, t, s * (1 - pan) * 1.6); add(Rch, t, s * pan * 1.6)
    t += step; k += 1

# kick (beats 1 and 3) and hat (offbeats) after the hook
start_beat = 5.0
t = start_beat
while t < T - 1.0:
    beat_idx = int(round((t - start_beat) / BEAT))
    if beat_idx % 2 == 0:
        d = 0.35; tt = np.arange(int(d * SR)) / SR
        f = 45 + 70 * np.exp(-tt * 30)
        s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9) * 0.32
        add(L, t, s); add(Rch, t, s)
    h = rng.standard_normal(int(0.05 * SR)); h = np.diff(h, prepend=0) * np.exp(-np.arange(len(h)) / SR * 90) * 0.035
    add(L, t + BEAT / 2, h * 0.8); add(Rch, t + BEAT / 2, h)
    t += BEAT

# keyboard clicks
for c in cues.get("clicks", []):
    m = int(0.012 * SR)
    s = np.diff(rng.standard_normal(m), prepend=0) * np.exp(-np.arange(m) / SR * 500) * 0.10
    add(L, c, s); add(Rch, c, s * 0.9)

# whooshes into each scene change
for w in cues.get("whoosh", []):
    d = 0.75; m = int(d * SR)
    x = rng.standard_normal(m)
    x = lowpass(x, 0.08) * 3
    e = np.concatenate([np.linspace(0, 1, int(m * 0.6)) ** 2, np.linspace(1, 0, m - int(m * 0.6))])
    s = x * e * 0.09
    add(L, w - 0.45, s); add(Rch, w - 0.43, s)

# pop when the change chip appears
for p in cues.get("pops", []):
    d = 0.12; tt = np.arange(int(d * SR)) / SR
    s = np.sin(2 * np.pi * (660 + 600 * tt / d) * tt) * np.exp(-tt * 30) * 0.12
    add(L, p, s); add(Rch, p, s)

mix = np.stack([L, Rch], axis=1)
fade_in = int(0.3 * SR); fade_out = int(1.6 * SR)
mix[:fade_in] *= np.linspace(0, 1, fade_in)[:, None]
mix[-fade_out:] *= np.linspace(1, 0, fade_out)[:, None]
mix = np.tanh(mix * 1.4) / np.tanh(1.4)
mix /= max(1e-9, np.abs(mix).max()) / 0.89
pcm = (mix * 32767).astype(np.int16)
with wave.open(out, "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes(pcm.tobytes())
print("music", out, f"{T:.1f}s")
