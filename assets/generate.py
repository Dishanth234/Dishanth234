#!/usr/bin/env python3
"""Generate retro Windows-95-style SVG assets for Dishanth's GitHub profile README."""
import os, random

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------- palette (Win95 SOC) ----------
TEAL   = "#0B7B7B"   # desktop
FACE   = "#C0C0C0"   # window face
HILITE = "#FFFFFF"   # bevel light
SHDW   = "#808080"   # bevel dark
BLACK  = "#000000"
NAVY   = "#000080"   # title bars + selection highlight
WHITE  = "#FFFFFF"
AMBER  = "#FFB000"   # shutdown-screen amber
ORANGE = "#FF8C00"
RED    = "#D84040"
GREEN  = "#3F9E3F"
YELLOW = "#F6D56A"   # folder yellow
BLUE   = "#2F6FD0"
PURPLE = "#9C56B8"
DIM    = "#9A9A9A"

MONO = "ui-monospace,'Courier New',monospace"
UIF  = "Tahoma,'Segoe UI',Verdana,Geneva,sans-serif"

def mono_w(n, fs):
    return round(n * 0.6 * fs)

def esc(s):
    return s.replace("&", "&amp;")

def mtext(x, y, s, fs=22, fill=BLACK, bold=False, anchor=None):
    b = ' font-weight="bold"' if bold else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{fs}"{b}{a} fill="{fill}">{esc(s)}</text>'

def utext(x, y, s, fs=16, fill=BLACK, bold=True, anchor=None):
    b = ' font-weight="bold"' if bold else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-family="{UIF}" font-size="{fs}"{b}{a} fill="{fill}">{esc(s)}</text>'

def headline(x, y, s, fs=80):
    """big Tahoma-bold headline, white with hard black drop shadow (for teal bg)."""
    return (f'<text x="{x+4}" y="{y+4}" text-anchor="middle" font-family="{UIF}" font-weight="bold" '
            f'font-size="{fs}" fill="{BLACK}">{esc(s)}</text>'
            f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{UIF}" font-weight="bold" '
            f'font-size="{fs}" fill="{WHITE}">{esc(s)}</text>')

def selection(x, y_baseline, s, fs=25, bold=False):
    """Win95 text-selection highlight: navy bar, white text. x is text x."""
    w = mono_w(len(s), fs) + 22
    rect_y = y_baseline - fs - 1
    h = fs + 9
    out = f'<rect x="{x-6}" y="{rect_y}" width="{w}" height="{h}" fill="{NAVY}"/>'
    out += mtext(x, y_baseline, s, fs, WHITE, bold)
    return out

def bevel_out(x, y, w, h):
    """raised 3D bevel edges around a FACE rect."""
    return (f'<path d="M{x} {y+h-1} L{x} {y} L{x+w-1} {y}" stroke="{HILITE}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+w-1} {y} L{x+w-1} {y+h-1} L{x} {y+h-1}" stroke="{BLACK}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+w-3} {y+2} L{x+w-3} {y+h-3} L{x+2} {y+h-3}" stroke="{SHDW}" stroke-width="2" fill="none"/>')

def sunken(x, y, w, h, fill=WHITE):
    """sunken 3D panel (inverted bevel)."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'
            f'<path d="M{x} {y+h-1} L{x} {y} L{x+w-1} {y}" stroke="{SHDW}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+1} {y+h-2} L{x+1} {y+1} L{x+w-2} {y+1}" stroke="{BLACK}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+w-1} {y} L{x+w-1} {y+h-1} L{x} {y+h-1}" stroke="{HILITE}" stroke-width="2" fill="none"/>')

def titlebar_buttons(w, bar_y=6, small=False):
    sz = 18 if small else 24
    g = []
    for i, glyph in enumerate(["_", "o", "x"]):
        bx = w - 8 - (3 - i) * (sz + 4)
        g.append(f'<rect x="{bx}" y="{bar_y+3}" width="{sz}" height="{sz}" fill="{FACE}"/>')
        g.append(bevel_out(bx, bar_y + 3, sz, sz))
        g.append(f'<text x="{bx+sz/2}" y="{bar_y+sz-3}" text-anchor="middle" font-family="{UIF}" '
                 f'font-weight="bold" font-size="{13 if small else 16}" fill="{BLACK}">{glyph}</text>')
    return "".join(g)

def window(w, h, title, small_bar=False):
    """Win95 window at local (0,0)."""
    bar_h = 24 if small_bar else 32
    fs = 14 if small_bar else 17
    return (
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="{FACE}"/>'
        + bevel_out(0, 0, w, h)
        + f'<rect x="6" y="6" width="{w-12}" height="{bar_h}" fill="{NAVY}"/>'
        + f'<text x="14" y="{6+bar_h-8}" font-family="{UIF}" font-weight="bold" font-size="{fs}" '
          f'fill="{WHITE}">{esc(title)}</text>'
        + titlebar_buttons(w - 6, bar_y=6 + (bar_h - 24) // 2, small=small_bar)
    )

def button(x, y, w, h, label, fs=22):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{FACE}"/>'
            + bevel_out(x, y, w, h)
            + f'<text x="{x+w//2}" y="{y+h//2+fs//2-2}" text-anchor="middle" font-family="{MONO}" '
              f'font-weight="bold" font-size="{fs}" fill="{BLACK}">{esc(label)}</text>')

def progress(x, y, w, h, frac, color=NAVY):
    """Win95 segmented progress bar in a sunken track."""
    out = [sunken(x, y, w, h)]
    seg_w, gap = 14, 4
    px = x + 4
    limit = x + 4 + int((w - 8) * frac)
    while px + seg_w <= limit:
        out.append(f'<rect x="{px}" y="{y+4}" width="{seg_w}" height="{h-8}" fill="{color}"/>')
        px += seg_w + gap
    return "".join(out)

# ---------- pixel font ----------
FONT = {
    "D": ["XXXX.","X...X","X...X","X...X","X...X","X...X","XXXX."],
    "I": ["XXXXX","..X..","..X..","..X..","..X..","..X..","XXXXX"],
    "S": [".XXXX","X....","X....",".XXX.","....X","....X","XXXX."],
    "H": ["X...X","X...X","X...X","XXXXX","X...X","X...X","X...X"],
    "A": [".XXX.","X...X","X...X","XXXXX","X...X","X...X","X...X"],
    "N": ["X...X","XX..X","X.X.X","X..XX","X...X","X...X","X...X"],
    "T": ["XXXXX","..X..","..X..","..X..","..X..","..X..","..X.."],
}

def pixel_text(s, cell=13, fill=NAVY):
    out, cx = [], 0
    for ch in s:
        if ch == " ":
            cx += 3
            continue
        for ry, row in enumerate(FONT[ch]):
            for rx, c in enumerate(row):
                if c == "X":
                    out.append(f'<rect x="{(cx+rx)*cell}" y="{ry*cell}" width="{cell}" height="{cell}" fill="{fill}"/>')
        cx += 6
    return "".join(out), (cx - 1) * cell

def svg(w, h, body, bg=TEAL):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">\n'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>\n{body}\n</svg>')

def save(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print(f"wrote {name} ({len(content)} bytes)")

# ---------- desktop icons ----------
def desk_icon(x, y, label, art, selected=False):
    lw = round(len(label) * 8.2) + 14
    lbl = (f'<rect x="{30-lw//2}" y="72" width="{lw}" height="22" fill="{NAVY}"/>'
           f'<text x="30" y="88" text-anchor="middle" font-family="{UIF}" font-size="14" fill="{WHITE}">{esc(label)}</text>'
           ) if selected else (
           f'<text x="30" y="88" text-anchor="middle" font-family="{UIF}" font-size="14" fill="{WHITE}">{esc(label)}</text>')
    return f'<g transform="translate({x},{y})">{art}{lbl}</g>'

ART = {
    "shield": (f'<path d="M30 2 L56 12 L56 32 C56 48 44 58 30 64 C16 58 4 48 4 32 L4 12 Z" '
               f'fill="{WHITE}" stroke="{BLACK}" stroke-width="3"/>'
               f'<path d="M18 30 L27 40 L44 20" fill="none" stroke="{NAVY}" stroke-width="5"/>'),
    "lock": (f'<rect x="12" y="28" width="36" height="30" fill="{YELLOW}" stroke="{BLACK}" stroke-width="3"/>'
             f'<path d="M20 28 V18 C20 10 40 10 40 18 V28" fill="none" stroke="{BLACK}" stroke-width="4"/>'
             f'<rect x="27" y="38" width="6" height="12" fill="{BLACK}"/>'),
    "bomb": (f'<circle cx="30" cy="40" r="19" fill="{BLACK}"/>'
             f'<rect x="26" y="14" width="8" height="10" fill="{BLACK}"/>'
             f'<path d="M34 12 l8 -6 M40 14 l6 -2 M38 6 l2 -4" stroke="{ORANGE}" stroke-width="3" fill="none"/>'),
    "floppy": (f'<path d="M8 10 L46 10 L56 20 L56 58 L8 58 Z" fill="{NAVY}" stroke="{BLACK}" stroke-width="3"/>'
               f'<rect x="18" y="10" width="20" height="14" fill="{WHITE}"/>'
               f'<rect x="16" y="34" width="32" height="20" fill="{WHITE}" stroke="{BLACK}" stroke-width="2.5"/>'),
    "monitor": (f'<rect x="6" y="8" width="48" height="38" fill="{FACE}" stroke="{BLACK}" stroke-width="3"/>'
                f'<rect x="12" y="14" width="36" height="26" fill="{NAVY}"/>'
                f'<text x="30" y="33" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{GREEN}" font-weight="bold">OK</text>'
                f'<rect x="22" y="46" width="16" height="6" fill="{FACE}" stroke="{BLACK}" stroke-width="2"/>'
                f'<rect x="14" y="52" width="32" height="6" fill="{FACE}" stroke="{BLACK}" stroke-width="2"/>'),
    "flag": (f'<rect x="14" y="4" width="5" height="56" fill="{BLACK}"/>'
             f'<path d="M19 6 L52 14 L19 26 Z" fill="{RED}" stroke="{BLACK}" stroke-width="3"/>'),
    "mag": (f'<circle cx="26" cy="26" r="16" fill="{WHITE}" stroke="{BLACK}" stroke-width="4"/>'
            f'<line x1="38" y1="38" x2="54" y2="54" stroke="{BLACK}" stroke-width="6"/>'),
    "bin": (f'<path d="M12 22 L48 22 L44 62 L16 62 Z" fill="{FACE}" stroke="{BLACK}" stroke-width="3"/>'
            f'<rect x="8" y="16" width="44" height="6" fill="{FACE}" stroke="{BLACK}" stroke-width="2.5"/>'
            f'<line x1="22" y1="28" x2="23" y2="56" stroke="{SHDW}" stroke-width="3"/>'
            f'<line x1="30" y1="28" x2="30" y2="56" stroke="{SHDW}" stroke-width="3"/>'
            f'<line x1="38" y1="28" x2="37" y2="56" stroke="{SHDW}" stroke-width="3"/>'
            f'<path d="M24 40 l5 -8 l5 8 M34 46 l-5 8 l-5 -8" fill="none" stroke="{GREEN}" stroke-width="3"/>'),
}

# ---------- win95 arrow cursor ----------
def cursor(x, y):
    return (f'<g transform="translate({x},{y})">'
            f'<path d="M0 0 L0 34 L8 27 L14 40 L20 37 L14 25 L24 24 Z" '
            f'fill="{WHITE}" stroke="{BLACK}" stroke-width="2.5"/></g>')

# =====================================================================
# 1. BANNER — the desktop
# =====================================================================
def banner():
    b = []
    # left + right desktop icon columns
    b.append(desk_icon(56, 60, "defense", ART["shield"], selected=True))
    b.append(desk_icon(56, 180, "hunt", ART["mag"]))
    b.append(desk_icon(56, 300, "evidence.zip", ART["floppy"]))
    b.append(desk_icon(56, 420, "defused", ART["bomb"]))
    b.append(desk_icon(1524, 60, "encrypted", ART["lock"]))
    b.append(desk_icon(1524, 180, "host: ok", ART["monitor"]))
    b.append(desk_icon(1524, 300, "flagged", ART["flag"]))
    b.append(desk_icon(1520, 420, "recycle bin", ART["bin"]))

    # welcome window with pixel name
    w = [window(1040, 330, "welcome.exe")]
    w.append(sunken(12, 44, 1016, 274))
    name, nw = pixel_text("DISHANTH")
    w.append(f'<g transform="translate({(1040-nw)//2},78)">{name}</g>')
    w.append(utext(520, 244, "SECURITY COMPLIANCE OFFICER · GRC ENGINEER · AI BLUE TEAM", 22, NAVY, True, "middle"))
    w.append(mtext(520, 284, "MS cybersecurity, yeshiva '26  ·  jersey city", 18, BLACK, False, "middle"))
    b.append(f'<g transform="translate(300,70)">{"".join(w)}</g>')

    # notepad quote window
    n = [window(620, 130, "readme.txt - Notepad", small_bar=True)]
    n.append(sunken(8, 34, 604, 88))
    n.append(mtext(24, 62, "HOW TO KEEP A SOC CALM BY GIVING", 20, BLACK, True))
    n.append(mtext(24, 88, "EVERY ALERT A GRAPH AND A STORY", 20, BLACK, True))
    n.append(mtext(24, 114, "// and reading", 17))
    sel_x = 24 + mono_w(15, 17)
    n.append(f'<rect x="{sel_x-4}" y="{114-17}" width="{mono_w(12,17)+14}" height="23" fill="{NAVY}"/>')
    n.append(mtext(sel_x, 114, "all the logs", 17, WHITE))
    b.append(f'<g transform="translate(300,430)">{"".join(n)}</g>')

    # alert feed mini window
    a = [window(330, 130, "alert_feed", small_bar=True)]
    a.append(sunken(8, 34, 314, 88))
    bars = [(40, RED), (70, ORANGE), (110, YELLOW), (160, GREEN), (210, BLUE), (250, PURPLE)]
    y = 42
    for bw, color in bars:
        a.append(f'<rect x="18" y="{y}" width="{bw}" height="10" fill="{color}"/>')
        y += 13
    a.append(f'<rect x="284" y="48" width="10" height="36" fill="{BLACK}"/>')
    b.append(f'<g transform="translate(960,430)">{"".join(a)}</g>')

    # taskbar
    t = [f'<rect x="0" y="574" width="1640" height="46" fill="{FACE}"/>'
         f'<line x1="0" y1="575" x2="1640" y2="575" stroke="{HILITE}" stroke-width="2"/>']
    t.append(f'<rect x="6" y="580" width="116" height="34" fill="{FACE}"/>' + bevel_out(6, 580, 116, 34))
    t.append(f'<rect x="16" y="588" width="8" height="8" fill="{RED}"/><rect x="26" y="588" width="8" height="8" fill="{GREEN}"/>'
             f'<rect x="16" y="598" width="8" height="8" fill="{BLUE}"/><rect x="26" y="598" width="8" height="8" fill="{YELLOW}"/>')
    t.append(utext(44, 604, "Start", 19, BLACK, True))
    t.append(sunken(140, 580, 230, 34, FACE))
    t.append(mtext(152, 603, "triage_pipeline.exe", 17))
    t.append(sunken(382, 580, 160, 34, FACE))
    t.append(mtext(394, 603, "soc_2.exe", 17))
    t.append(sunken(554, 580, 180, 34, FACE))
    t.append(mtext(566, 603, "grc_audit.exe", 17))
    t.append(sunken(1504, 580, 128, 34, FACE))
    t.append(mtext(1568, 603, "3:00 AM", 17, BLACK, False, "middle"))
    b.append("".join(t))
    save("banner.svg", svg(1640, 620, "".join(b)))

# =====================================================================
# 2. DIVIDER — beveled toolbar strip
# =====================================================================
def divider():
    body = (f'<rect x="0" y="6" width="1640" height="16" fill="{FACE}"/>'
            f'<line x1="0" y1="7" x2="1640" y2="7" stroke="{HILITE}" stroke-width="2"/>'
            f'<line x1="0" y1="20" x2="1640" y2="20" stroke="{SHDW}" stroke-width="2"/>'
            f'<line x1="0" y1="22" x2="1640" y2="22" stroke="{BLACK}" stroke-width="1"/>')
    save("divider.svg", svg(1640, 28, body))

# =====================================================================
# 3. ABOUT — resume-current
# =====================================================================
def about():
    b = [headline(820, 120, "THREATS, TRIAGED.", 84)]
    b.append(mtext(240, 196, "hi, i'm dishanth. security compliance officer, GRC engineer & blue teamer.", 25, WHITE, True))
    b.append(mtext(300, 242, "i wire AI triage pipelines, ATT&CK-mapped SIEM feeds,", 25, WHITE))
    b.append(selection(300, 288, "and agentic LLM systems across AWS.", 25, True))
    b.append(mtext(300, 330, "the receipts: alert accuracy +50%, investigations", 25, WHITE))
    b.append(mtext(300, 366, "40% faster, and a SOC that stays calm at", 25, WHITE))
    b.append(selection(910, 366, "3 a.m.", 25))

    # dishanth.exe Properties — memory bars
    bars = [
        ("threat hunting", "9.2 MB", 0.92, NAVY),
        ("grc audits",     "8.4 MB", 0.84, NAVY),
        ("coffee",         "7.6 MB", 0.76, NAVY),
        ("sleep",          "2.0 MB", 0.20, NAVY),
        ("false positives","0.4 MB", 0.05, RED),
    ]
    w = [window(1040, 286, "dishanth.exe Properties")]
    y = 62
    for label, mb, frac, color in bars:
        w.append(mtext(40, y + 20, label, 21))
        w.append(mtext(370, y + 20, mb, 21, BLACK, False, "end"))
        w.append(progress(392, y, 560, 28, frac, color))
        y += 42
    b.append(f'<g transform="translate(300,420)">{"".join(w)}</g>')

    b.append(mtext(300, 742, "off hours: CTFs, packet captures, one more kali VM.", 23, WHITE, True))

    # orange pixel padlock
    b.append(f'<g transform="translate(1390,190)">'
             f'<g fill="{ORANGE}">'
             f'<rect x="48" y="0" width="104" height="24"/>'
             f'<rect x="48" y="24" width="24" height="60"/>'
             f'<rect x="128" y="24" width="24" height="60"/>'
             f'<rect x="16" y="84" width="168" height="132"/></g>'
             f'<rect x="84" y="116" width="32" height="32" fill="{TEAL}"/>'
             f'<rect x="92" y="148" width="16" height="40" fill="{TEAL}"/></g>')
    save("about-terminal.svg", svg(1640, 760, "".join(b)))

# =====================================================================
# 4. TECH STACK — explorer window
# =====================================================================
def folder95(x, y, label, selected=False):
    lw = round(len(label) * 8.4) + 14
    if selected:
        lbl = (f'<rect x="{57-lw//2}" y="92" width="{lw}" height="24" fill="{NAVY}"/>'
               f'<rect x="{57-lw//2}" y="92" width="{lw}" height="24" fill="none" stroke="{FACE}" stroke-width="1.5" stroke-dasharray="3 3"/>'
               f'<text x="57" y="109" text-anchor="middle" font-family="{UIF}" font-size="15" fill="{WHITE}">{esc(label)}</text>')
    else:
        lbl = f'<text x="57" y="109" text-anchor="middle" font-family="{UIF}" font-size="15" fill="{BLACK}">{esc(label)}</text>'
    return (f'<g transform="translate({x},{y})">'
            f'<path d="M14 16 L14 8 L44 8 L52 16 L100 16 L100 78 L14 78 Z" fill="{YELLOW}" stroke="{BLACK}" stroke-width="2.5"/>'
            f'<line x1="14" y1="24" x2="100" y2="24" stroke="{BLACK}" stroke-width="2"/>'
            f'{lbl}</g>')

def tech_stack():
    b = [headline(820, 96, "THE ARSENAL", 80)]
    w = [window(1400, 540, "C:\\defense")]
    w.append(sunken(14, 46, 1372, 424))

    row1 = [("python", True), ("splunk", False), ("elk stack", False),
            ("qradar", False), ("neo4j", False), ("weaviate", False)]
    row2 = [("claude+llms", True), ("graphrag", True), ("sigma rules", False),
            ("suricata", False), ("aws", False), ("kali linux", False)]
    for i, (label, sel) in enumerate(row1):
        w.append(folder95(70 + i * 225, 78, label, sel))
    for i, (label, sel) in enumerate(row2):
        w.append(folder95(70 + i * 225, 240, label, sel))

    # recycle bin with alert fatigue
    w.append(f'<g transform="translate(1250,352)">{ART["bin"]}'
             f'<g transform="translate(30,-14) rotate(12)">'
             f'<rect x="0" y="0" width="104" height="24" fill="{WHITE}" stroke="{BLACK}" stroke-width="2"/>'
             f'<text x="52" y="17" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{BLACK}">alert fatigue</text></g>'
             f'<text x="30" y="88" text-anchor="middle" font-family="{UIF}" font-size="15" fill="{BLACK}">recycle bin</text></g>')

    # status bar cells
    w.append(sunken(14, 484, 330, 32, FACE))
    w.append(mtext(26, 506, "12 object(s), 3 selected", 17))
    w.append(sunken(352, 484, 1034, 32, FACE))
    w.append(f'<text x="364" y="506" font-family="{MONO}" font-size="17" fill="{BLACK}">'
             f'also on the shelf: burp suite, nmap, metasploit, wireshark, nestjs+next.js, vanta</text>')
    b.append(f'<g transform="translate(120,140)">{"".join(w)}</g>')
    b.append(cursor(506, 434))
    save("tech-stack.svg", svg(1640, 760, "".join(b)))

# =====================================================================
# 5. NOW BUILDING — blueberries
# =====================================================================
def now_building():
    w = [window(1500, 560, "now_building.exe")]

    w.append(f'<text x="90" y="164" font-family="{UIF}" font-weight="bold" font-size="82" '
             f'fill="{NAVY}">"15% TO 95%,</text>')
    w.append(f'<text x="250" y="252" font-family="{UIF}" font-weight="bold" font-size="82" '
             f'fill="{NAVY}">IN A MONTH"</text>')

    w.append(mtext(560, 306, "at BLUEBERRIES: security compliance", 25))
    w.append(mtext(560, 342, "officer & lead dev. SOC 2 type 2 across", 25))
    w.append(selection(560, 382, "71 vanta controls, 9 policies fixed.", 25))
    w.append(mtext(560, 418, "plus an agentic LLM FP&A platform.", 25))

    w.append(mtext(560, 456, "STATUS: SOC 2 control completion", 25, bold=True))
    w.append(progress(560, 466, 560, 28, 0.95))
    w.append(mtext(1136, 488, "15% → 95%", 21))

    w.append(mtext(560, 524, "also built: NLP property attribution &", 25))
    w.append(mtext(560, 550, "a plain-english treasury stress-tester.", 25))

    w.append(mtext(80, 534, "→ ask me about SOC 2 in a month", 24, bold=True))

    # remediated-controls checklist
    g = [sunken(0, 0, 300, 180)]
    rows = ["cloudtrail", "guardduty", "vpc flow logs", "iam policies"]
    y = 22
    for label in rows:
        g.append(sunken(22, y, 22, 22))
        g.append(f'<path d="M27 {y+11} L33 {y+17} L41 {y+4}" fill="none" stroke="{NAVY}" stroke-width="3.5"/>')
        g.append(f'<text x="60" y="{y+18}" font-family="{MONO}" font-size="17" fill="{BLACK}">{esc(label)}</text>')
        y += 31
    g.append(f'<text x="150" y="166" text-anchor="middle" font-family="{MONO}" font-weight="bold" '
             f'font-size="17" fill="{BLACK}">aws gaps: closed</text>')
    w.append(f'<g transform="translate(120,296)">{"".join(g)}</g>')

    b = f'<g transform="translate(70,50)">{"".join(w)}</g>'
    save("currently-building.svg", svg(1640, 660, b))

# =====================================================================
# 6. PROJECT CARDS
# =====================================================================
def card(name, title_notch, big, lines, arrow):
    w = [window(748, 410, title_notch)]
    w.append(sunken(12, 46, 724, 352))
    w.append(f'<text x="36" y="122" font-family="{UIF}" font-weight="bold" font-size="46" '
             f'fill="{NAVY}">{esc(big)}</text>')
    y = 190
    for ln in lines:
        w.append(f'<text x="36" y="{y}" font-family="{MONO}" font-size="22" fill="{BLACK}">{esc(ln)}</text>')
        y += 34
    w.append(f'<text x="36" y="360" font-family="{MONO}" font-weight="bold" font-size="23" '
             f'fill="{BLACK}">{esc(arrow)}</text>')
    body = f'<g transform="translate(20,24)">{"".join(w)}</g>'
    save(name, svg(800, 470, body))

def cards():
    card("card-deception.svg", "project_01.exe", "CLOUD DECEPTION",
         ["AI honeypots bait attackers and log",
          "their TTPs. CSPM scans catch IAM, S3,",
          "EC2 misconfigs. MITRE ATT&CK mapped."],
         "→ the capstone repo, on github")
    card("card-cygeniq.svg", "internship.log", "GRAPHRAG SOC",
         ["at cygeniq: taught LLMs to triage",
          "10K+ alerts. weaviate vectors, neo4j",
          "graph. +50% accuracy, 40% faster digs."],
         "→ blue team intern, jan-apr 2026")
    card("card-serverless.svg", "project_02.exe", "SECURE SERVERLESS",
         ["HIPAA-aligned serverless on AWS.",
          "cognito MFA, AES-256 + TLS, WAF,",
          "cloudtrail + cloudwatch eyes on."],
         "→ aws · appsec · hipaa")
    card("card-portfolio.svg", "front_door.url", "THE SITE",
         ["case studies, projects, and",
          "the occasional incident",
          "write-up."],
         "→ dishanthca.com")

# =====================================================================
# 7. PAPER TRAIL — certs
# =====================================================================
def paper_trail():
    b = [headline(820, 96, "PAPER TRAIL", 80)]
    w = [window(1400, 380, "certmgr.exe")]
    w.append(sunken(14, 46, 1372, 318))

    certs = [("CySA+", "comptia"), ("Security+", "comptia"), ("CSAP", "comptia"),
             ("BTL-1", "security blue team"), ("RH124", "red hat")]
    for i, (cert, issuer) in enumerate(certs):
        x = 50 + i * 216
        w.append(
            f'<g transform="translate({x},80)">'
            f'<rect x="0" y="0" width="188" height="150" fill="{WHITE}" stroke="{BLACK}" stroke-width="3"/>'
            f'<rect x="10" y="10" width="168" height="130" fill="none" stroke="{NAVY}" stroke-width="2" stroke-dasharray="6 5"/>'
            f'<text x="94" y="62" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="26" fill="{BLACK}">{esc(cert)}</text>'
            f'<text x="94" y="92" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{SHDW}">{esc(issuer)}</text>'
            f'<circle cx="94" cy="116" r="11" fill="{YELLOW}" stroke="{BLACK}" stroke-width="3"/>'
            f'<path d="M88 124 L84 140 M100 124 L104 140" stroke="{BLACK}" stroke-width="3"/>'
            f'</g>')

    # CTF trophy card
    w.append(
        f'<g transform="translate(1160,80)">'
        f'<rect x="0" y="0" width="188" height="150" fill="{YELLOW}" stroke="{BLACK}" stroke-width="3"/>'
        f'<path d="M74 26 L114 26 L110 62 C108 76 96 84 94 84 C92 84 80 76 78 62 Z" fill="{ORANGE}" stroke="{BLACK}" stroke-width="3"/>'
        f'<path d="M74 32 C60 32 58 52 76 56 M114 32 C128 32 130 52 112 56" fill="none" stroke="{BLACK}" stroke-width="3"/>'
        f'<rect x="86" y="84" width="16" height="10" fill="{BLACK}"/>'
        f'<rect x="76" y="94" width="36" height="8" fill="{BLACK}"/>'
        f'<text x="94" y="126" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="19" fill="{BLACK}">2nd place CTF</text>'
        f'<text x="94" y="144" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{BLACK}">yeshiva u · dec 2025</text>'
        f'</g>')

    w.append(mtext(40, 336, "pen tested the competition. they were not patched.", 18))
    w.append(mtext(1346, 336, "5 certs · 1 trophy · 0 expired", 18, BLACK, False, "end"))
    b.append(f'<g transform="translate(120,140)">{"".join(w)}</g>')
    save("credentials.svg", svg(1640, 580, "".join(b)))

# =====================================================================
# 8. FOOTER — shutdown screen
# =====================================================================
def footer():
    b = []
    b.append(f'<text x="820" y="104" text-anchor="middle" font-family="{MONO}" font-weight="bold" '
             f'font-size="36" fill="{AMBER}">It\'s now safe to connect with dishanth.</text>')
    b.append(f'<rect x="1258" y="76" width="18" height="34" fill="{AMBER}"/>')
    chips = [("dishanthk02@gmail.com", 380), ("in/dishanth-ca", 250), ("dishanthca.com", 250)]
    total = sum(c[1] for c in chips) + 30 * (len(chips) - 1)
    x = (1640 - total) // 2
    for label, cw in chips:
        b.append(button(x, 156, cw, 54, label, 22))
        x += cw + 30
    b.append(f'<text x="820" y="284" text-anchor="middle" font-family="{MONO}" font-size="19" fill="{DIM}">'
             f'© 2026 dishanth ca · jersey city · all packets inspected</text>')
    save("footer.svg", svg(1640, 340, "".join(b), bg=BLACK))

# =====================================================================
banner()
divider()
about()
tech_stack()
now_building()
cards()
paper_trail()
footer()
print("done.")
