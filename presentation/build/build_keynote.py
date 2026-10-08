"""Build presentation/herding-agents.key from slides.json, natively in Keynote.

Uses Keynote's stock "Basic White" theme and its own master slides (Title,
Statement, Big Fact, Title & Bullets, Title Only), so Document > Change Theme
restyles the whole deck. Speaker notes come straight from slides.json.

Generates an AppleScript and runs it with osascript (JXA can't set a slide's
master in current Keynote). Standard library only:

    python3 presentation/build/build_keynote.py

Keynote is sandboxed: the first run may ask for permission to control it.
"""
import json
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = json.loads((Path(__file__).parent / "slides.json").read_text())
IMAGES = ROOT / "images"
OUT = ROOT / "presentation" / "herding-agents.key"

W, H, M = 1920, 1080, 60
MASTER = {
    "title": "Title",
    "statement": "Statement",
    "bigfact": "Big Fact",
    "bullets": "Title & Bullets",
    "image": "Title Only",
    "image-side": "Title Only",
}


def q(text):
    """AppleScript string literal."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def fit(path, box):
    iw, ih = png_size(path)
    bx, by, bw, bh = box
    r = min(bw / iw, bh / ih)
    w, h = round(iw * r), round(ih * r)
    return bx + (bw - w) // 2, by + (bh - h) // 2, w, h


lines = [
    'tell application "Keynote"',
    f'set d to make new document with properties {{document theme:theme "Basic White", width:{W}, height:{H}}}',
]
for s in SPEC["slides"]:
    t = s["type"]
    lines.append(
        f'set s to make new slide at end of slides of d with properties {{base slide:master slide {q(MASTER[t])} of d}}'
    )
    if t == "title":
        lines.append(f"set object text of default title item of s to {q(s['title'])}")
        lines.append(f"set object text of default body item of s to {q(s.get('subtitle', ''))}")
        # the Title master's "Author and Date" placeholder: the empty text item at the bottom
        lines += [
            "repeat with t in text items of s",
            f"if object text of t is \"\" and (item 2 of (get position of t)) > {H // 2} then "
            f"set object text of t to {q(SPEC['meta']['author_date'])}",
            "end repeat",
        ]
    elif t == "bigfact":
        # Big Fact: the body is the big number, the title is its caption
        lines.append(f"set object text of default body item of s to {q(s['title'])}")
        lines.append(f"set object text of default title item of s to {q(s.get('subtitle', ''))}")
        lines.append("set title showing of s to true")
    elif t == "statement":
        lines.append(f"set object text of default body item of s to {q(s['title'])}")
    elif t == "bullets":
        lines.append(f"set object text of default title item of s to {q(s['title'])}")
        lines.append(f"set object text of default body item of s to {q(chr(10).join(s['bullets']))}")
    else:
        lines.append(f"set object text of default title item of s to {q(s['title'])}")
        img = IMAGES / s["image"]
        if t == "image-side":
            # tall, narrow screenshot: title on the left, image on the right
            lines.append(f"set position of default title item of s to {{{M * 2}, {H // 2 - 120}}}")
            lines.append("set width of default title item of s to 1000")
            x, y, w, h = fit(img, (1300, M, W - 1300 - M, H - 2 * M))
        else:
            # Basic White's Title Only title sits in the top ~200pt
            top = 220
            x, y, w, h = fit(img, (M, top, W - 2 * M, H - top - M))
        lines.append(f"tell s to set i to make new image with properties {{file:(POSIX file {q(str(img))})}}")
        lines.append(f"set width of i to {w}")
        lines.append(f"set height of i to {h}")
        lines.append(f"set position of i to {{{x}, {y}}}")
    lines.append(f"set presenter notes of s to {q(s['notes'])}")

lines += [
    "delete slide 1 of d -- the blank slide every new document starts with",
    f"save d in (POSIX file {q(str(OUT))})",
    "close d saving no",
    "end tell",
]

script = "with timeout of 600 seconds\n" + "\n".join(lines) + "\nend timeout\n"
subprocess.run(["osascript", "-"], input=script, text=True, check=True)
print(f"wrote {OUT.relative_to(ROOT)} ({len(SPEC['slides'])} slides)")
