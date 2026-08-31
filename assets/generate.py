#!/usr/bin/env python3
"""Retro Windows-95 'SOC desktop' SVG assets for Dishanth's GitHub profile README — CRT edition."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
TEAL   = "#0F6E6A"
TEAL2  = "#0D6360"
TEALWM = "#12807A"   # watermark
DKTEAL = "#053E3B"
FACE   = "#C8C5BE"
HILITE = "#FFFFFF"
SHDW   = "#8A867E"
BLACK  = "#161616"
NAVY   = "#000080"
NAVY2  = "#2F6FB8"
WHITE  = "#FFFFFF"
AMBER  = "#E8A33D"
ORANGE = "#D98E4A"
ORANGE2= "#E5B06A"
RED    = "#C65A54"
GREEN  = "#5E9A5E"
TGREEN = "#4CBF74"   # terminal green
YELLOW = "#E9CF7E"
YELLOW2= "#F6EAB8"
BLUE   = "#5B7FB5"
PURPLE = "#9678A8"
DIM    = "#9A9A9A"
CASE   = "#DEDACE"   # CRT plastic
CASE2  = "#BBB6A8"
BEZEL  = "#37352F"

MONO = "ui-monospace,'Courier New',monospace"
UIF  = "Tahoma,'Segoe UI',Verdana,Geneva,sans-serif"

def esc(s): return s.replace("&", "&amp;")
def mono_w(n, fs): return round(n * 0.6 * fs)

def mtext(x, y, s, fs=22, fill=BLACK, bold=False, anchor=None):
    b = ' font-weight="bold"' if bold else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{fs}"{b}{a} fill="{fill}">{esc(s)}</text>'

def utext(x, y, s, fs=16, fill=BLACK, bold=True, anchor=None):
    b = ' font-weight="bold"' if bold else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-family="{UIF}" font-size="{fs}"{b}{a} fill="{fill}">{esc(s)}</text>'

def kicker(y, s):
    return (f'<text x="820" y="{y}" text-anchor="middle" font-family="{MONO}" font-size="17" '
            f'letter-spacing="6" fill="#BADAD5">{esc(s)}</text>')

def headline(x, y, s, fs=80):
    return (f'<text x="{x+4}" y="{y+4}" text-anchor="middle" font-family="{UIF}" font-weight="bold" '
            f'letter-spacing="-1" font-size="{fs}" fill="{DKTEAL}">{esc(s)}</text>'
            f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{UIF}" font-weight="bold" '
            f'letter-spacing="-1" font-size="{fs}" fill="{WHITE}">{esc(s)}</text>')

def selection(x, y_baseline, s, fs=25, bold=False):
    w = mono_w(len(s), fs) + 22
    return (f'<rect x="{x-6}" y="{y_baseline-fs-1}" width="{w}" height="{fs+9}" fill="{NAVY}"/>'
            + mtext(x, y_baseline, s, fs, WHITE, bold))

def bevel_out(x, y, w, h):
    return (f'<path d="M{x} {y+h-1} L{x} {y} L{x+w-1} {y}" stroke="{HILITE}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+w-1} {y} L{x+w-1} {y+h-1} L{x} {y+h-1}" stroke="{BLACK}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+w-3} {y+2} L{x+w-3} {y+h-3} L{x+2} {y+h-3}" stroke="{SHDW}" stroke-width="2" fill="none"/>')

def sunken(x, y, w, h, fill=WHITE):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'
            f'<path d="M{x} {y+h-1} L{x} {y} L{x+w-1} {y}" stroke="{SHDW}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+1} {y+h-2} L{x+1} {y+1} L{x+w-2} {y+1}" stroke="{BLACK}" stroke-width="2" fill="none"/>'
            f'<path d="M{x+w-1} {y} L{x+w-1} {y+h-1} L{x} {y+h-1}" stroke="{HILITE}" stroke-width="2" fill="none"/>')

DEFS = (f'<defs>'
        f'<pattern id="dz" width="4" height="4" patternUnits="userSpaceOnUse">'
        f'<rect width="4" height="4" fill="{TEAL}"/><rect width="2" height="2" fill="{TEAL2}"/>'
        f'<rect x="2" y="2" width="2" height="2" fill="{TEAL2}"/></pattern>'
        f'<pattern id="sb" width="4" height="4" patternUnits="userSpaceOnUse">'
        f'<rect width="4" height="4" fill="{WHITE}"/><rect width="2" height="2" fill="{FACE}"/>'
        f'<rect x="2" y="2" width="2" height="2" fill="{FACE}"/></pattern>'
        f'<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        f'<rect width="4" height="4" fill="{BLACK}"/><rect y="2" width="4" height="1" fill="#0C0C0C"/></pattern>'
        f'<pattern id="crt" width="6" height="3" patternUnits="userSpaceOnUse">'
        f'<rect width="6" height="3" fill="none"/><rect y="2" width="6" height="1" fill="{BLACK}" fill-opacity="0.14"/></pattern>'
        f'<linearGradient id="case" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9E5D9"/><stop offset="1" stop-color="#CFCBBD"/></linearGradient><linearGradient id="tb" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY2}"/></linearGradient>'
        f'<radialGradient id="vig" cx="0.5" cy="0.45" r="0.75">'
        f'<stop offset="0.75" stop-color="{BLACK}" stop-opacity="0"/>'
        f'<stop offset="1" stop-color="{BLACK}" stop-opacity="0.22"/></radialGradient>'
        f'</defs>')

TICON = {
    "shield": f'<path d="M9 1 L17 4 L17 9 C17 14 13 16 9 18 C5 16 1 14 1 9 L1 4 Z" fill="{YELLOW}" stroke="{BLACK}" stroke-width="1.5"/><path d="M5 9 L8 12 L13 6" fill="none" stroke="{NAVY}" stroke-width="2"/>',
    "note":   f'<rect x="2" y="1" width="14" height="17" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/><line x1="5" y1="6" x2="13" y2="6" stroke="{NAVY}" stroke-width="1.5"/><line x1="5" y1="9" x2="13" y2="9" stroke="{NAVY}" stroke-width="1.5"/><line x1="5" y1="12" x2="11" y2="12" stroke="{NAVY}" stroke-width="1.5"/>',
    "folder": f'<path d="M1 5 L1 3 L7 3 L9 5 L17 5 L17 15 L1 15 Z" fill="{YELLOW}" stroke="{BLACK}" stroke-width="1.5"/>',
    "chart":  f'<rect x="1" y="1" width="16" height="16" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/><rect x="4" y="9" width="3" height="6" fill="{NAVY}"/><rect x="8" y="5" width="3" height="10" fill="{RED}"/><rect x="12" y="7" width="3" height="8" fill="{GREEN}"/>',
    "cert":   f'<rect x="1" y="2" width="16" height="12" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/><circle cx="9" cy="8" r="3" fill="{YELLOW}" stroke="{BLACK}" stroke-width="1"/><path d="M7 14 L7 18 M11 14 L11 18" stroke="{BLACK}" stroke-width="1.5"/>',
    "pc":     f'<rect x="1" y="2" width="16" height="11" fill="{FACE}" stroke="{BLACK}" stroke-width="1.5"/><rect x="3" y="4" width="12" height="7" fill="{NAVY}"/><rect x="6" y="15" width="6" height="2" fill="{BLACK}"/>',
    "bomb":   f'<circle cx="9" cy="11" r="6" fill="{BLACK}"/><rect x="8" y="3" width="2" height="4" fill="{BLACK}"/><path d="M10 3 l3 -2" stroke="{ORANGE}" stroke-width="1.5"/>',
    "globe":  f'<circle cx="9" cy="9" r="8" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/><ellipse cx="9" cy="9" rx="3.5" ry="8" fill="none" stroke="{NAVY}" stroke-width="1.2"/><line x1="1" y1="9" x2="17" y2="9" stroke="{NAVY}" stroke-width="1.2"/>',
    "net":    f'<rect x="1" y="1" width="6" height="6" fill="{RED}" stroke="{BLACK}" stroke-width="1.2"/><rect x="11" y="3" width="6" height="6" fill="{GREEN}" stroke="{BLACK}" stroke-width="1.2"/><rect x="5" y="11" width="6" height="6" fill="{BLUE}" stroke="{BLACK}" stroke-width="1.2"/><line x1="6" y1="5" x2="12" y2="6" stroke="{BLACK}" stroke-width="1.2"/><line x1="5" y1="6" x2="8" y2="12" stroke="{BLACK}" stroke-width="1.2"/><line x1="13" y1="9" x2="10" y2="12" stroke="{BLACK}" stroke-width="1.2"/>',
    "lock":   f'<rect x="3" y="8" width="12" height="9" fill="{YELLOW}" stroke="{BLACK}" stroke-width="1.5"/><path d="M6 8 V5 C6 2 12 2 12 5 V8" fill="none" stroke="{BLACK}" stroke-width="1.8"/>',
}

def titlebar_buttons(right_x, bar_y, sz=22):
    g, gap = [], 4
    for i, kind in enumerate(["min", "max", "close"]):
        bx = right_x - (3 - i) * (sz + gap)
        g.append(f'<rect x="{bx}" y="{bar_y}" width="{sz}" height="{sz}" fill="{FACE}"/>')
        g.append(bevel_out(bx, bar_y, sz, sz))
        cx, cy = bx + sz / 2, bar_y + sz / 2
        if kind == "min":
            g.append(f'<rect x="{bx+5}" y="{bar_y+sz-8}" width="{sz-11}" height="3" fill="{BLACK}"/>')
        elif kind == "max":
            g.append(f'<rect x="{bx+4}" y="{bar_y+4}" width="{sz-9}" height="{sz-9}" fill="none" stroke="{BLACK}" stroke-width="2"/>'
                     f'<line x1="{bx+4}" y1="{bar_y+5}" x2="{bx+sz-5}" y2="{bar_y+5}" stroke="{BLACK}" stroke-width="3"/>')
        else:
            g.append(f'<path d="M{cx-5} {cy-5} L{cx+5} {cy+5} M{cx+5} {cy-5} L{cx-5} {cy+5}" stroke="{BLACK}" stroke-width="2.5"/>')
    return "".join(g)

def menubar(y, w, items=("File", "Edit", "View", "Help"), fs=15):
    g, x = [], 16
    for it in items:
        g.append(f'<text x="{x}" y="{y+18}" font-family="{UIF}" font-size="{fs}" fill="{BLACK}">{esc(it)}</text>')
        x += len(it) * round(fs * 0.62) + 26
    g.append(f'<line x1="6" y1="{y+26}" x2="{w-6}" y2="{y+26}" stroke="{SHDW}" stroke-width="1.5"/>')
    g.append(f'<line x1="6" y1="{y+28}" x2="{w-6}" y2="{y+28}" stroke="{HILITE}" stroke-width="1.5"/>')
    return "".join(g)

def back_window(w, h, dx=-20, dy=-20):
    """inactive cascade window peeking out behind the main one."""
    return (f'<g transform="translate({dx},{dy})">'
            f'<rect x="6" y="6" width="{w}" height="{h}" fill="{DKTEAL}"/>'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="{FACE}"/>'
            + bevel_out(0, 0, w, h)
            + f'<rect x="6" y="6" width="{w-12}" height="30" fill="{SHDW}"/>'
            f'</g>')

def window(w, h, title, icon=None, small_bar=False, shadow=True, menu=False):
    bar_h = 24 if small_bar else 32
    fs = 14 if small_bar else 17
    out = []
    if shadow:
        out.append(f'<rect x="8" y="8" width="{w}" height="{h}" fill="{DKTEAL}"/>')
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{FACE}"/>')
    out.append(bevel_out(0, 0, w, h))
    out.append(f'<rect x="6" y="6" width="{w-12}" height="{bar_h}" fill="url(#tb)"/>')
    tx = 14
    if icon:
        iy = 6 + (bar_h - 18) // 2
        out.append(f'<g transform="translate(12,{iy})">{TICON[icon]}</g>')
        tx = 38
    out.append(f'<text x="{tx}" y="{6+bar_h-9}" font-family="{UIF}" font-weight="bold" font-size="{fs}" '
               f'fill="{WHITE}">{esc(title)}</text>')
    out.append(titlebar_buttons(w - 10, 6 + (bar_h - (18 if small_bar else 22)) // 2, sz=18 if small_bar else 22))
    if menu:
        out.append(menubar(6 + bar_h + 2, w))
    return "".join(out)

def button(x, y, w, h, label, fs=22, font=MONO):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{FACE}"/>'
            + bevel_out(x, y, w, h)
            + f'<text x="{x+w//2}" y="{y+h//2+fs//2-2}" text-anchor="middle" font-family="{font}" '
              f'font-weight="bold" font-size="{fs}" fill="{BLACK}">{esc(label)}</text>')

def scrollbar_v(x, y, h):
    g = [f'<rect x="{x}" y="{y}" width="26" height="{h}" fill="url(#sb)"/>']
    for by, d in ((y, "up"), (y + h - 26, "down")):
        g.append(f'<rect x="{x}" y="{by}" width="26" height="26" fill="{FACE}"/>' + bevel_out(x, by, 26, 26))
        if d == "up":
            g.append(f'<path d="M{x+13} {by+8} L{x+19} {by+16} L{x+7} {by+16} Z" fill="{BLACK}"/>')
        else:
            g.append(f'<path d="M{x+7} {by+10} L{x+19} {by+10} L{x+13} {by+18} Z" fill="{BLACK}"/>')
    g.append(f'<rect x="{x}" y="{y+30}" width="26" height="72" fill="{FACE}"/>' + bevel_out(x, y + 30, 26, 72))
    return "".join(g)

def watermark(x, y, s=4.4):
    return (f'<g transform="translate({x},{y}) scale({s})" opacity="1">'
            f'<path d="M30 2 L56 12 L56 32 C56 48 44 58 30 64 C16 58 4 48 4 32 L4 12 Z" '
            f'fill="{TEALWM}" stroke="none"/>'
            f'<path d="M18 30 L27 40 L44 20" fill="none" stroke="{TEAL2}" stroke-width="5"/></g>')

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

def svg(w, h, body, bg="dz"):
    if bg == "dz":
        base = f'<rect width="{w}" height="{h}" fill="url(#dz)"/>'
    elif bg == "scan":
        base = f'<rect width="{w}" height="{h}" fill="url(#scan)"/>'
    else:
        base = f'<rect width="{w}" height="{h}" fill="{bg}"/>'
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">\n'
            f'{DEFS}\n{base}\n{body}\n</svg>')

def save(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print(f"wrote {name} ({len(content)} bytes)")

def desk_icon(x, y, label, art, selected=False):
    lw = round(len(label) * 8.2) + 14
    if selected:
        lbl = (f'<rect x="{30-lw//2}" y="72" width="{lw}" height="22" fill="{NAVY}"/>'
               f'<rect x="{30-lw//2}" y="72" width="{lw}" height="22" fill="none" stroke="{YELLOW}" stroke-width="1" stroke-dasharray="2 2"/>'
               f'<text x="30" y="88" text-anchor="middle" font-family="{UIF}" font-size="14" fill="{WHITE}">{esc(label)}</text>')
    else:
        lbl = (f'<text x="31" y="89" text-anchor="middle" font-family="{UIF}" font-size="14" fill="{BLACK}">{esc(label)}</text>'
               f'<text x="30" y="88" text-anchor="middle" font-family="{UIF}" font-size="14" fill="{WHITE}">{esc(label)}</text>')
    return f'<g transform="translate({x},{y})">{art}{lbl}</g>'

ART = {
    "shield": (f'<path d="M30 2 L56 12 L56 32 C56 48 44 58 30 64 C16 58 4 48 4 32 L4 12 Z" fill="{WHITE}" stroke="{BLACK}" stroke-width="3"/>'
               f'<path d="M30 2 L56 12 L56 32 C56 44 48 52 40 57 L40 8 Z" fill="{FACE}" stroke="none"/>'
               f'<path d="M30 2 L56 12 L56 32 C56 48 44 58 30 64 C16 58 4 48 4 32 L4 12 Z" fill="none" stroke="{BLACK}" stroke-width="3"/>'
               f'<path d="M18 30 L27 40 L44 20" fill="none" stroke="{NAVY}" stroke-width="5"/>'),
    "lock": (f'<rect x="12" y="28" width="36" height="30" fill="{YELLOW}" stroke="{BLACK}" stroke-width="3"/>'
             f'<rect x="12" y="28" width="10" height="30" fill="{YELLOW2}" stroke="none"/>'
             f'<rect x="12" y="28" width="36" height="30" fill="none" stroke="{BLACK}" stroke-width="3"/>'
             f'<path d="M20 28 V18 C20 10 40 10 40 18 V28" fill="none" stroke="{BLACK}" stroke-width="4"/>'
             f'<rect x="27" y="38" width="6" height="12" fill="{BLACK}"/>'),
    "bomb": (f'<circle cx="30" cy="40" r="19" fill="{BLACK}"/>'
             f'<circle cx="24" cy="34" r="5" fill="#3A3A3A"/>'
             f'<rect x="26" y="14" width="8" height="10" fill="{BLACK}"/>'
             f'<path d="M34 12 l8 -6 M40 14 l6 -2 M38 6 l2 -4" stroke="{ORANGE}" stroke-width="3" fill="none"/>'),
    "floppy": (f'<path d="M8 10 L46 10 L56 20 L56 58 L8 58 Z" fill="{NAVY}" stroke="{BLACK}" stroke-width="3"/>'
               f'<rect x="18" y="10" width="20" height="14" fill="{WHITE}"/>'
               f'<rect x="30" y="12" width="6" height="10" fill="{NAVY}"/>'
               f'<rect x="16" y="34" width="32" height="20" fill="{WHITE}" stroke="{BLACK}" stroke-width="2.5"/>'
               f'<line x1="20" y1="40" x2="44" y2="40" stroke="{SHDW}" stroke-width="2"/>'
               f'<line x1="20" y1="46" x2="44" y2="46" stroke="{SHDW}" stroke-width="2"/>'),
    "monitor": (f'<rect x="6" y="8" width="48" height="38" fill="{FACE}" stroke="{BLACK}" stroke-width="3"/>'
                f'<rect x="12" y="14" width="36" height="26" fill="{NAVY}"/>'
                f'<text x="30" y="33" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#40FF70" font-weight="bold">OK</text>'
                f'<rect x="22" y="46" width="16" height="6" fill="{FACE}" stroke="{BLACK}" stroke-width="2"/>'
                f'<rect x="14" y="52" width="32" height="6" fill="{FACE}" stroke="{BLACK}" stroke-width="2"/>'),
    "flag": (f'<rect x="14" y="4" width="5" height="56" fill="{BLACK}"/>'
             f'<path d="M19 6 L52 14 L19 26 Z" fill="{RED}" stroke="{BLACK}" stroke-width="3"/>'),
    "mag": (f'<circle cx="26" cy="26" r="16" fill="{WHITE}" stroke="{BLACK}" stroke-width="4"/>'
            f'<circle cx="21" cy="21" r="5" fill="{FACE}"/>'
            f'<line x1="38" y1="38" x2="54" y2="54" stroke="{BLACK}" stroke-width="6"/>'),
    "bin": (f'<path d="M12 22 L48 22 L44 62 L16 62 Z" fill="{FACE}" stroke="{BLACK}" stroke-width="3"/>'
            f'<rect x="8" y="16" width="44" height="6" fill="{FACE}" stroke="{BLACK}" stroke-width="2.5"/>'
            f'<line x1="22" y1="28" x2="23" y2="56" stroke="{SHDW}" stroke-width="3"/>'
            f'<line x1="30" y1="28" x2="30" y2="56" stroke="{SHDW}" stroke-width="3"/>'
            f'<line x1="38" y1="28" x2="37" y2="56" stroke="{SHDW}" stroke-width="3"/>'
            f'<path d="M24 40 l5 -8 l5 8 M34 46 l-5 8 l-5 -8" fill="none" stroke="{GREEN}" stroke-width="3"/>'),
}

def cursor(x, y):
    return (f'<g transform="translate({x},{y})">'
            f'<path d="M0 0 L0 34 L8 27 L14 40 L20 37 L14 25 L24 24 Z" '
            f'fill="{WHITE}" stroke="{BLACK}" stroke-width="2.5"/></g>')

# =====================================================================
# 1. BANNER — desktop inside a CRT monitor
# =====================================================================
def banner():
    d = [f'<rect width="1640" height="620" fill="url(#dz)"/>']
    d.append(watermark(1230, 130, 5.2))
    d.append(desk_icon(56, 56, "defense", ART["shield"], selected=True))
    d.append(desk_icon(56, 178, "hunt", ART["mag"]))
    d.append(desk_icon(56, 300, "evidence.zip", ART["floppy"]))
    d.append(desk_icon(56, 422, "defused", ART["bomb"]))
    d.append(desk_icon(1524, 56, "encrypted", ART["lock"]))
    d.append(desk_icon(1524, 178, "host: ok", ART["monitor"]))
    d.append(desk_icon(1524, 300, "flagged", ART["flag"]))
    d.append(desk_icon(1520, 422, "recycle bin", ART["bin"]))

    w = [back_window(1040, 344)]
    w.append(window(1040, 344, "welcome.exe", icon="shield", menu=True))
    w.append(sunken(12, 70, 1016, 200))
    name, nw = pixel_text("DISHANTH")
    w.append(f'<g transform="translate({(1040-nw)//2},92)">{name}</g>')
    w.append(utext(520, 232, "SECURITY COMPLIANCE OFFICER · GRC ENGINEER · AI BLUE TEAM", 22, NAVY, True, "middle"))
    w.append(sunken(12, 280, 506, 32, FACE))
    w.append(mtext(24, 302, "MS cybersecurity, yeshiva '26", 17))
    w.append(sunken(522, 280, 506, 32, FACE))
    w.append(mtext(1016, 302, "jersey city, nj", 17, BLACK, False, "end"))
    d.append(f'<g transform="translate(300,58)">{"".join(w)}</g>')

    n = [window(640, 134, "readme.txt - Notepad", icon="note", small_bar=True)]
    n.append(sunken(8, 34, 624, 92))
    n.append(mtext(24, 64, "HOW TO KEEP A SOC CALM BY GIVING", 20, BLACK, True))
    n.append(mtext(24, 90, "EVERY ALERT A GRAPH AND A STORY", 20, BLACK, True))
    n.append(mtext(24, 116, "// and reading", 17))
    sel_x = 24 + mono_w(15, 17)
    n.append(f'<rect x="{sel_x-4}" y="{116-17}" width="{mono_w(12,17)+14}" height="23" fill="{NAVY}"/>')
    n.append(mtext(sel_x, 116, "all the logs", 17, WHITE))
    d.append(f'<g transform="translate(300,428)">{"".join(n)}</g>')

    a = [window(368, 134, "alert_feed", icon="chart", small_bar=True)]
    a.append(sunken(8, 34, 326, 92))
    bars = [("crit", 40, RED), ("high", 74, ORANGE), ("med", 116, YELLOW),
            ("low", 168, GREEN), ("info", 218, BLUE), ("dbg", 262, PURPLE)]
    y = 44
    for label, bw, color in bars:
        a.append(f'<text x="16" y="{y+8}" font-family="{MONO}" font-size="11" fill="{SHDW}">{label}</text>')
        a.append(f'<rect x="52" y="{y}" width="{bw}" height="9" fill="{color}"/>')
        y += 13
    a.append(scrollbar_v(334, 34, 92))
    d.append(f'<g transform="translate(972,428)">{"".join(a)}</g>')

    t = [f'<rect x="0" y="574" width="1640" height="46" fill="{FACE}"/>'
         f'<line x1="0" y1="575" x2="1640" y2="575" stroke="{HILITE}" stroke-width="2"/>']
    t.append(f'<rect x="6" y="580" width="116" height="34" fill="{FACE}"/>' + bevel_out(6, 580, 116, 34))
    t.append(f'<rect x="16" y="588" width="8" height="8" fill="{RED}"/><rect x="26" y="588" width="8" height="8" fill="{GREEN}"/>'
             f'<rect x="16" y="598" width="8" height="8" fill="{BLUE}"/><rect x="26" y="598" width="8" height="8" fill="{YELLOW}"/>')
    t.append(utext(44, 605, "Start", 19, BLACK, True))
    t.append(sunken(140, 580, 230, 34, FACE))
    t.append(mtext(152, 603, "triage_pipeline.exe", 17))
    t.append(sunken(382, 580, 150, 34, FACE))
    t.append(mtext(394, 603, "soc_2.exe", 17))
    t.append(sunken(544, 580, 180, 34, FACE))
    t.append(mtext(556, 603, "grc_audit.exe", 17))
    t.append(sunken(1408, 580, 224, 34, FACE))
    t.append(f'<path d="M1422 597 L1430 591 L1430 603 Z M1430 594 L1436 594 L1436 600 L1430 600 Z" fill="{BLACK}"/>')
    t.append(f'<g transform="translate(1444,588)">{TICON["shield"]}</g>')
    t.append(mtext(1620, 603, "3:00 AM", 17, BLACK, False, "end"))
    d.append("".join(t))
    desktop = "".join(d)

    # ---- CRT shell ----
    b = []
    b.append(f'<rect x="14" y="8" width="1612" height="702" rx="30" fill="{CASE2}"/>')
    b.append(f'<rect x="10" y="4" width="1612" height="698" rx="30" fill="url(#case)"/>')
    b.append(f'<rect x="10" y="4" width="1612" height="698" rx="30" fill="none" stroke="#8F8A7B" stroke-width="2"/>')
    b.append(f'<rect x="24" y="16" width="1584" height="60" rx="18" fill="#E4E1D6" opacity="0.55"/>')
    b.append(f'<rect x="52" y="34" width="1536" height="600" rx="18" fill="{BEZEL}"/>')
    b.append(f'<rect x="52" y="34" width="1536" height="600" rx="18" fill="none" stroke="#26251F" stroke-width="3"/>')
    # screen
    b.append(f'<clipPath id="scr"><rect x="70" y="50" width="1500" height="568" rx="10"/></clipPath>')
    b.append(f'<g clip-path="url(#scr)"><g transform="translate(70,50) scale(0.9146)">{desktop}</g>'
             f'<rect x="70" y="50" width="1500" height="568" fill="url(#crt)"/>'
             f'<rect x="70" y="50" width="1500" height="568" fill="url(#vig)"/>'
             f'<polygon points="120,50 430,50 210,618 70,618 70,240" fill="{WHITE}" opacity="0.05"/>'
             f'<polygon points="470,50 540,50 320,618 250,618" fill="{WHITE}" opacity="0.04"/></g>')
    b.append(f'<rect x="70" y="50" width="1500" height="568" rx="10" fill="none" stroke="{BLACK}" stroke-width="2" opacity="0.6"/>')
    # chin
    b.append(f'<rect x="96" y="652" width="150" height="30" rx="4" fill="#CBC7BA"/>'
             f'<rect x="96" y="652" width="150" height="30" rx="4" fill="none" stroke="#9B968A" stroke-width="2"/>')
    b.append(f'<text x="171" y="673" text-anchor="middle" font-family="{UIF}" font-weight="bold" font-size="17" '
             f'fill="#6E695C">DISHANTH·95</text>')
    for i in range(26):
        b.append(f'<rect x="{660+i*13}" y="658" width="6" height="20" rx="2" fill="#C2BEB0"/>')
    b.append(f'<circle cx="1502" cy="668" r="17" fill="{CASE2}"/>'
             f'<circle cx="1500" cy="666" r="15" fill="#E2DFD4" stroke="#8F8A7B" stroke-width="2"/>'
             f'<circle cx="1500" cy="666" r="5" fill="none" stroke="#6E695C" stroke-width="2"/>')
    b.append(f'<rect x="1440" y="660" width="12" height="12" rx="2" fill="{TGREEN}"/>'
             f'<rect x="1440" y="660" width="12" height="12" rx="2" fill="none" stroke="#5A5648" stroke-width="1.5"/>')
    b.append(f'<text x="1446" y="694" text-anchor="middle" font-family="{UIF}" font-size="11" fill="#6E695C" font-weight="bold">PWR</text>')
    save("banner.svg", svg(1640, 716, "".join(b), bg="none"))

# =====================================================================
# 1b. BOOT SCREEN
# =====================================================================
def boot():
    b = []
    lines = [
        ("DISHANTH BIOS v2.6 - (c) 1995-2026 blue team labs", DIM, False),
        ("CPU: caffeine @ 3:00AM ................ OK", WHITE, False),
        ("memory test: 10,000+ alerts ........... TRIAGED", WHITE, False),
        ("loading defense.sys ................... OK", WHITE, False),
        ("loading grc_audit.dll ................. OK", WHITE, False),
        ("mounting C:\\soc_2 ..................... 95% COMPLIANT", TGREEN, False),
        ("scanning for threats .................. 0 SURVIVING", TGREEN, False),
    ]
    y = 56
    for s, c, _ in lines:
        b.append(mtext(120, y, s, 20, c))
        y += 32
    b.append(mtext(120, y + 14, "press DEL to enter setup, ESC to skip the small talk", 18, AMBER))
    b.append(f'<rect x="{120+mono_w(53,18)+10}" y="{y}" width="12" height="20" fill="{AMBER}"/>')
    # "SOC energy" badge
    b.append(f'<g transform="translate(1380,52)">'
             f'<rect x="0" y="0" width="150" height="150" rx="8" fill="none" stroke="#2A2A2A" stroke-width="2"/>'
             f'<path d="M75 16 L118 32 L118 66 C118 96 96 112 75 122 C54 112 32 96 32 66 L32 32 Z" '
             f'fill="none" stroke="{TGREEN}" stroke-width="3"/>'
             f'<path d="M56 64 L70 80 L96 46" fill="none" stroke="{TGREEN}" stroke-width="4"/>'
             f'<text x="75" y="143" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#4A4A4A">soc energy ok</text>'
             f'</g>')
    save("boot.svg", svg(1640, 324, "".join(b), bg=BLACK))

# =====================================================================
# 2. DIVIDER
# =====================================================================
def divider():
    b = [f'<rect x="0" y="0" width="1640" height="36" fill="url(#sb)"/>']
    b.append(f'<rect x="0" y="0" width="34" height="36" fill="{FACE}"/>' + bevel_out(0, 0, 34, 36))
    b.append(f'<path d="M22 10 L22 26 L12 18 Z" fill="{BLACK}"/>')
    b.append(f'<rect x="1606" y="0" width="34" height="36" fill="{FACE}"/>' + bevel_out(1606, 0, 34, 36))
    b.append(f'<path d="M1618 10 L1618 26 L1628 18 Z" fill="{BLACK}"/>')
    b.append(f'<rect x="700" y="0" width="240" height="36" fill="{FACE}"/>' + bevel_out(700, 0, 240, 36))
    for gx in (790, 818, 846):
        b.append(f'<line x1="{gx}" y1="10" x2="{gx}" y2="26" stroke="{SHDW}" stroke-width="2"/>'
                 f'<line x1="{gx+2}" y1="10" x2="{gx+2}" y2="26" stroke="{HILITE}" stroke-width="2"/>')
    save("divider.svg", svg(1640, 36, "".join(b), bg=FACE))

# =====================================================================
# 3. ABOUT
# =====================================================================
def about():
    b = [watermark(96, 560, 3.6)]
    b.append(kicker(58, "— 01 · IDENTITY —"))
    b.append(headline(820, 138, "THREATS, TRIAGED.", 80))
    b.append(mtext(300, 214, "hi, i'm dishanth. security compliance officer, GRC engineer & blue teamer.", 25, WHITE, True))
    b.append(mtext(300, 258, "i wire AI triage pipelines, ATT&CK-mapped SIEM feeds,", 25, WHITE))
    b.append(selection(300, 302, "and agentic LLM systems across AWS.", 25, True))
    b.append(mtext(300, 344, "the receipts: alert accuracy +50%, investigations", 25, WHITE))
    b.append(mtext(300, 380, "40% faster, and a SOC that stays calm at", 25, WHITE))
    b.append(selection(908, 380, "3 a.m.", 25))

    bars = [
        ("threat hunting", "9.2 MB", 0.92, NAVY),
        ("grc audits",     "8.4 MB", 0.84, NAVY),
        ("coffee",         "7.6 MB", 0.76, NAVY),
        ("sleep",          "2.0 MB", 0.20, NAVY),
        ("false positives","0.4 MB", 0.05, RED),
    ]
    w = [back_window(1040, 348)]
    w.append(window(1040, 348, "dishanth.exe Properties", icon="pc"))
    for i, (tab, active) in enumerate([("Performance", True), ("Compliance", False), ("Jokes", False)]):
        tw = 130
        tx = 14 + i * (tw + 4)
        ty = 48 if active else 52
        th = 30 if active else 26
        w.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" fill="{FACE}"/>'
                 f'<path d="M{tx} {ty+th} L{tx} {ty} L{tx+tw-1} {ty}" stroke="{HILITE}" stroke-width="2" fill="none"/>'
                 f'<path d="M{tx+tw-1} {ty} L{tx+tw-1} {ty+th}" stroke="{BLACK}" stroke-width="2" fill="none"/>')
        w.append(utext(tx + tw // 2, ty + 20, tab, 14, BLACK, active, "middle"))
    w.append(f'<line x1="14" y1="78" x2="1026" y2="78" stroke="{HILITE}" stroke-width="2"/>')
    y = 96
    for label, mb, frac, color in bars:
        w.append(mtext(44, y + 20, label, 20))
        w.append(mtext(366, y + 20, mb, 20, BLACK, False, "end"))
        seg = [sunken(390, y, 560, 28)]
        seg_x = 394
        limit = 394 + int(552 * frac)
        while seg_x + 14 <= limit:
            seg.append(f'<rect x="{seg_x}" y="{y+4}" width="14" height="20" fill="{color}"/>')
            seg_x += 18
        w.append("".join(seg))
        y += 38
    w.append(button(678, 296, 108, 32, "OK", 15, UIF))
    w.append(button(798, 296, 108, 32, "Cancel", 15, UIF))
    w.append(button(918, 296, 108, 32, "Apply", 15, UIF))
    b.append(f'<g transform="translate(300,430)">{"".join(w)}</g>')

    # office-assistant bubble + pixel paperclip
    c = []
    c.append(f'<rect x="6" y="6" width="270" height="188" rx="12" fill="{DKTEAL}"/>')
    c.append(f'<rect x="0" y="0" width="270" height="188" rx="12" fill="#FFFDF2" stroke="{BLACK}" stroke-width="2.5"/>')
    c.append(f'<path d="M118 187 L104 224 L158 187 Z" fill="#FFFDF2" stroke="{BLACK}" stroke-width="2.5"/>')
    c.append(f'<rect x="118" y="184" width="42" height="6" fill="#FFFDF2"/>')
    c.append(mtext(24, 38, "It looks like you're", 16))
    c.append(mtext(24, 62, "trying to breach a", 16))
    c.append(mtext(24, 86, "network.", 16))
    c.append(mtext(24, 116, "Would you like help?", 16, BLACK, True))
    c.append(button(24, 134, 100, 36, "No", 15, UIF))
    c.append(button(136, 134, 110, 36, "Never", 15, UIF))
    b.append(f'<g transform="translate(1250,430)">{"".join(c)}</g>')
    b.append(f'<g transform="translate(1352,660)">'
             f'<path d="M14 82 L14 22 A13 13 0 0 1 40 22 L40 66 A9 9 0 0 1 22 66 L22 32" '
             f'fill="none" stroke="#66788F" stroke-width="7" stroke-linecap="round"/>'
             f'<path d="M14 82 L14 22 A13 13 0 0 1 40 22 L40 66 A9 9 0 0 1 22 66 L22 32" '
             f'fill="none" stroke="#93A5BC" stroke-width="3" stroke-linecap="round"/></g>')
    b.append(mtext(300, 800, "off hours: CTFs, packet captures, one more kali VM.", 23, WHITE, True))
    save("about-terminal.svg", svg(1640, 836, "".join(b)))

# =====================================================================
# 4. TECH STACK — explorer
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
            f'<path d="M14 24 L100 24 L100 78 L14 78 Z" fill="{YELLOW2}"/>'
            f'<path d="M14 16 L14 8 L44 8 L52 16 L100 16 L100 78 L14 78 Z" fill="none" stroke="{BLACK}" stroke-width="2.5"/>'
            f'<line x1="14" y1="24" x2="100" y2="24" stroke="{BLACK}" stroke-width="2"/>'
            f'{lbl}</g>')

def toolbar_btn(x, y, glyph):
    return (f'<rect x="{x}" y="{y}" width="34" height="30" fill="{FACE}"/>' + bevel_out(x, y, 34, 30)
            + f'<g transform="translate({x+8},{y+6})">{glyph}</g>')

def tech_stack():
    b = [watermark(1404, 600, 3.6)]
    b.append(kicker(58, "— 02 · TOOLBOX —"))
    b.append(headline(820, 136, "THE ARSENAL", 80))
    w = [back_window(1400, 640), back_window(1400, 640, -38, -34)]
    w[0], w[1] = w[1], w[0]
    w.append(window(1400, 640, "Exploring - C:\\defense", icon="folder", menu=True))
    # toolbar
    tb_glyphs = [
        f'<path d="M14 9 L4 9 M8 4 L3 9 L8 14" stroke="{BLACK}" stroke-width="2.5" fill="none"/>',
        f'<path d="M4 9 L14 9 M10 4 L15 9 L10 14" stroke="{SHDW}" stroke-width="2.5" fill="none"/>',
        f'<path d="M2 14 L2 6 L7 6 L9 8 L16 8 L16 14 Z" fill="{YELLOW}" stroke="{BLACK}" stroke-width="1.5"/><path d="M9 4 L9 0 M9 0 L6 3 M9 0 L12 3" stroke="{BLACK}" stroke-width="2" fill="none"/>',
        f'<rect x="3" y="3" width="8" height="11" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/><rect x="7" y="6" width="8" height="11" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/>',
        f'<rect x="4" y="2" width="10" height="13" fill="{WHITE}" stroke="{BLACK}" stroke-width="1.5"/><rect x="6" y="0" width="6" height="4" fill="{FACE}" stroke="{BLACK}" stroke-width="1.5"/>',
    ]
    tx = 16
    for gph in tb_glyphs:
        w.append(toolbar_btn(tx, 68, gph))
        tx += 40
    w.append(f'<line x1="{tx+6}" y1="70" x2="{tx+6}" y2="96" stroke="{SHDW}" stroke-width="2"/>')
    # address bar
    w.append(utext(tx + 24, 90, "Address", 15, BLACK, False))
    w.append(sunken(tx + 92, 68, 1400 - tx - 92 - 130, 30))
    w.append(mtext(tx + 104, 89, "C:\\defense", 18))
    ax = 1400 - 122
    w.append(f'<rect x="{ax}" y="70" width="26" height="26" fill="{FACE}"/>' + bevel_out(ax, 70, 26, 26))
    w.append(f'<path d="M{ax+6} {80} L{ax+20} {80} L{ax+13} {90} Z" fill="{BLACK}"/>')
    w.append(f'<rect x="{ax+32}" y="68" width="76" height="30" fill="{FACE}"/>' + bevel_out(ax + 32, 68, 76, 30))
    w.append(utext(ax + 70, 89, "Go", 15, BLACK, True, "middle"))

    w.append(sunken(14, 110, 1340, 442))
    w.append(scrollbar_v(1356, 110, 442))

    row1 = [("python", True), ("splunk", False), ("elk stack", False),
            ("qradar", False), ("neo4j", False), ("weaviate", False)]
    row2 = [("claude+llms", True), ("graphrag", True), ("sigma rules", False),
            ("suricata", False), ("vanta grc", False), ("kali linux", False)]
    for i, (label, sel) in enumerate(row1):
        w.append(folder95(56 + i * 208, 146, label, sel))
    for i, (label, sel) in enumerate(row2):
        w.append(folder95(56 + i * 208, 320, label, sel))

    w.append(f'<g transform="translate(1220,428)">{ART["bin"]}'
             f'<g transform="translate(28,-14) rotate(12)">'
             f'<rect x="0" y="0" width="104" height="24" fill="{WHITE}" stroke="{BLACK}" stroke-width="2"/>'
             f'<text x="52" y="17" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{BLACK}">alert fatigue</text></g>'
             f'<text x="30" y="88" text-anchor="middle" font-family="{UIF}" font-size="15" fill="{BLACK}">recycle bin</text></g>')

    w.append(sunken(14, 566, 340, 32, FACE))
    w.append(mtext(26, 588, "12 object(s), 3 selected", 17))
    w.append(sunken(362, 566, 862, 32, FACE))
    w.append(f'<text x="374" y="588" font-family="{MONO}" font-size="17" fill="{BLACK}">'
             f'shelf: burp suite, nmap, metasploit, wireshark, nestjs+next.js, aws</text>')
    w.append(sunken(1232, 566, 154, 32, FACE))
    w.append(mtext(1244, 588, "1 in trash", 17))
    b.append(f'<g transform="translate(120,176)">{"".join(w)}</g>')
    b.append(cursor(520, 546))
    save("tech-stack.svg", svg(1640, 880, "".join(b)))

# =====================================================================
# 5. NOW BUILDING — defrag
# =====================================================================
def now_building():
    b = [watermark(40, 430, 3.2)]
    w = [back_window(1400, 596)]
    w.append(window(1400, 596, "defrag.exe - now_building", icon="chart", menu=True))

    w.append(f'<text x="70" y="184" font-family="{UIF}" font-weight="bold" font-size="80" letter-spacing="-1" '
             f'fill="{NAVY}">"15% TO 95%,</text>')
    w.append(f'<text x="230" y="270" font-family="{UIF}" font-weight="bold" font-size="80" letter-spacing="-1" '
             f'fill="{NAVY}">IN A MONTH"</text>')

    w.append(mtext(520, 326, "at BLUEBERRIES: security compliance", 25))
    w.append(mtext(520, 362, "officer & lead dev. SOC 2 type 2 across", 25))
    w.append(selection(520, 402, "71 vanta controls, 9 policies fixed.", 25))
    w.append(mtext(520, 438, "plus an agentic LLM FP&A platform.", 25))

    w.append(mtext(520, 478, "Defragmenting drive C: (soc_2)", 25, bold=True))
    w.append(mtext(1080, 478, "15% → 95%", 21, NAVY, True, "end"))
    g = [sunken(520, 488, 560, 68)]
    cols, size, gap = 38, 12, 2
    total = cols * 3
    filled = int(total * 0.95)
    idx = 0
    for r in range(3):
        for c in range(cols):
            x = 526 + c * (size + gap)
            y = 494 + r * (size + gap + 4)
            if idx < filled:
                color = NAVY if idx % 9 else RED
            else:
                color = WHITE
            g.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" stroke="{SHDW}" stroke-width="0.5"/>')
            idx += 1
    w.append("".join(g))
    w.append(mtext(520, 584, "■ compliant · ■ hot fix · □ to do — plus: NLP attribution, treasury sim.", 17))

    w.append(mtext(70, 548, "→ ask me about SOC 2 in a month", 24, bold=True))

    g = [sunken(0, 0, 300, 190)]
    g.append(utext(150, 26, "remediation.dlg", 14, SHDW, True, "middle"))
    rows = ["cloudtrail", "guardduty", "vpc flow logs", "iam policies"]
    y = 40
    for label in rows:
        g.append(sunken(22, y, 22, 22))
        g.append(f'<path d="M27 {y+11} L33 {y+17} L41 {y+4}" fill="none" stroke="{NAVY}" stroke-width="3.5"/>')
        g.append(f'<text x="60" y="{y+18}" font-family="{MONO}" font-size="17" fill="{BLACK}">{esc(label)}</text>')
        y += 30
    g.append(f'<text x="150" y="176" text-anchor="middle" font-family="{MONO}" font-weight="bold" '
             f'font-size="17" fill="{GREEN}">aws gaps: closed ✓</text>')
    w.append(f'<g transform="translate(110,320)">{"".join(g)}</g>')

    b.append(f'<g transform="translate(120,44)">{"".join(w)}</g>')
    save("currently-building.svg", svg(1640, 700, "".join(b)))

# =====================================================================
# 6. PROJECT CARDS
# =====================================================================
def card(name, title_notch, ticon, big, glyph, lines, arrow, status_left):
    w = [back_window(748, 434, -14, -14)]
    w.append(window(748, 434, title_notch, icon=ticon, menu=True))
    w.append(sunken(12, 74, 724, 306))
    w.append(f'<g transform="translate(560,196) scale(9)" opacity="0.07">{TICON[ticon]}</g>')
    w.append(f'<text x="36" y="146" font-family="{UIF}" font-weight="bold" font-size="46" '
             f'fill="{NAVY}">{esc(big)}</text>')
    w.append(f'<g transform="translate(640,96)">{glyph}</g>')
    y = 210
    for ln in lines:
        w.append(f'<text x="36" y="{y}" font-family="{MONO}" font-size="22" fill="{BLACK}">{esc(ln)}</text>')
        y += 34
    w.append(f'<text x="36" y="352" font-family="{MONO}" font-weight="bold" font-size="23" '
             f'fill="{BLACK}">{esc(arrow)}</text>')
    w.append(sunken(12, 388, 420, 30, FACE))
    w.append(mtext(24, 409, status_left, 15))
    w.append(sunken(440, 388, 296, 30, FACE))
    w.append(mtext(452, 409, "double-click to open", 15))
    body = f'<g transform="translate(24,20)">{"".join(w)}</g>'
    save(name, svg(800, 478, body))

def big_glyph(kind):
    return f'<g transform="scale(3.2)">{TICON[kind]}</g>'

def cards():
    card("card-deception.svg", "project_01.exe", "bomb", "CLOUD DECEPTION", big_glyph("bomb"),
         ["AI honeypots bait attackers and log",
          "their TTPs. CSPM scans catch IAM, S3,",
          "EC2 misconfigs. MITRE ATT&CK mapped."],
         "→ the capstone repo, on github",
         "python · aws · att&ck")
    card("card-cygeniq.svg", "internship.log", "net", "GRAPHRAG SOC", big_glyph("net"),
         ["at cygeniq: taught LLMs to triage",
          "10K+ alerts. weaviate vectors, neo4j",
          "graph. +50% accuracy, 40% faster digs."],
         "→ blue team intern, jan-apr 2026",
         "weaviate · neo4j · llms")
    card("card-serverless.svg", "project_02.exe", "lock", "SECURE SERVERLESS", big_glyph("lock"),
         ["HIPAA-aligned serverless on AWS.",
          "cognito MFA, AES-256 + TLS, WAF,",
          "cloudtrail + cloudwatch eyes on."],
         "→ aws · appsec · hipaa",
         "lambda · cognito · waf")
    card("card-portfolio.svg", "front_door.url", "globe", "THE SITE", big_glyph("globe"),
         ["case studies, projects, and",
          "the occasional incident",
          "write-up."],
         "→ dishanthca.com",
         "always open")

# =====================================================================
# 7. PAPER TRAIL
# =====================================================================
def paper_trail():
    b = [watermark(96, 330, 3.4)]
    b.append(kicker(58, "— 03 · RECEIPTS —"))
    b.append(headline(820, 136, "PAPER TRAIL", 80))
    w = [back_window(1400, 420)]
    w.append(window(1400, 420, "certmgr.exe - credentials", icon="cert", menu=True))
    w.append(sunken(14, 74, 1340, 296))
    w.append(scrollbar_v(1356, 74, 296))

    certs = [("CySA+", "comptia"), ("Security+", "comptia"), ("CSAP", "comptia"),
             ("BTL-1", "security blue team"), ("RH124", "red hat")]
    for i, (cert, issuer) in enumerate(certs):
        x = 46 + i * 212
        w.append(
            f'<g transform="translate({x},104)">'
            f'<rect x="6" y="6" width="188" height="150" fill="{SHDW}"/>'
            f'<rect x="0" y="0" width="188" height="150" fill="{WHITE}" stroke="{BLACK}" stroke-width="3"/>'
            f'<rect x="10" y="10" width="168" height="130" fill="none" stroke="{NAVY}" stroke-width="2" stroke-dasharray="6 5"/>'
            f'<text x="94" y="62" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="26" fill="{BLACK}">{esc(cert)}</text>'
            f'<text x="94" y="92" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{SHDW}">{esc(issuer)}</text>'
            f'<circle cx="94" cy="116" r="11" fill="{YELLOW}" stroke="{BLACK}" stroke-width="3"/>'
            f'<circle cx="94" cy="116" r="5" fill="{ORANGE}"/>'
            f'<path d="M88 124 L84 140 M100 124 L104 140" stroke="{BLACK}" stroke-width="3"/>'
            f'</g>')

    w.append(
        f'<g transform="translate(1116,104)">'
        f'<rect x="6" y="6" width="188" height="150" fill="{SHDW}"/>'
        f'<rect x="0" y="0" width="188" height="150" fill="{YELLOW}" stroke="{BLACK}" stroke-width="3"/>'
        f'<path d="M74 26 L114 26 L110 62 C108 76 96 84 94 84 C92 84 80 76 78 62 Z" fill="{ORANGE}" stroke="{BLACK}" stroke-width="3"/>'
        f'<path d="M74 32 C60 32 58 52 76 56 M114 32 C128 32 130 52 112 56" fill="none" stroke="{BLACK}" stroke-width="3"/>'
        f'<rect x="86" y="84" width="16" height="10" fill="{BLACK}"/>'
        f'<rect x="76" y="94" width="36" height="8" fill="{BLACK}"/>'
        f'<text x="94" y="126" text-anchor="middle" font-family="{MONO}" font-weight="bold" font-size="19" fill="{BLACK}">2nd place CTF</text>'
        f'<text x="94" y="144" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{BLACK}">yeshiva u · dec 2025</text>'
        f'</g>')

    w.append(sunken(14, 378, 700, 30, FACE))
    w.append(mtext(26, 399, "pen tested the competition. they were not patched.", 16))
    w.append(sunken(722, 378, 632, 30, FACE))
    w.append(mtext(1342, 399, "5 certs · 1 trophy · 0 expired", 16, BLACK, False, "end"))
    b.append(f'<g transform="translate(120,176)">{"".join(w)}</g>')
    save("credentials.svg", svg(1640, 656, "".join(b)))

# =====================================================================
# 7b. BSOD
# =====================================================================
def bsod():
    b = []
    b.append(f'<rect x="770" y="44" width="100" height="34" fill="{FACE}"/>')
    b.append(mtext(820, 69, "SOC", 24, NAVY, True, "middle"))
    lines = [
        "A fatal exception 0xC0FFEE has occurred at 0028:C0DE0000 in VXD ATTACKER(01).",
        "The intruder has been terminated. All lateral movement has been rolled back.",
        "",
        "*  Press any key to review the evidence in evidence.zip",
        "*  Press CTRL+ALT+DEL to hire the analyst responsible for this screen",
        "",
    ]
    y = 122
    for ln in lines:
        if ln:
            b.append(mtext(820, y, ln, 21, WHITE, False, "middle"))
        y += 33
    b.append(mtext(820, y, "Press any key to continue", 21, WHITE, False, "middle"))
    b.append(f'<rect x="{820+mono_w(13,21)+10}" y="{y-18}" width="12" height="22" fill="{WHITE}"/>')
    save("bsod.svg", svg(1640, 360, "".join(b), bg=NAVY))

# =====================================================================
# 8. FOOTER — shutdown screen
# =====================================================================
def footer():
    b = []
    import random as _r
    rng = _r.Random(42)
    for _ in range(30):
        x, y = rng.randint(10, 1630), rng.randint(10, 330)
        s = rng.choice([2, 2, 3])
        c = rng.choice([AMBER, DIM, "#5A5A5A", AMBER])
        b.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{c}" opacity="0.7"/>')
    b.append(f'<circle cx="150" cy="86" r="24" fill="#E8C46A" opacity="0.55"/>'
             f'<circle cx="142" cy="80" r="6" fill="#D3AC4C" opacity="0.6"/>'
             f'<circle cx="160" cy="94" r="4" fill="#D3AC4C" opacity="0.6"/>'
             f'<circle cx="152" cy="72" r="3" fill="#D3AC4C" opacity="0.6"/>')
    b.append(f'<text x="820" y="64" text-anchor="middle" font-family="{MONO}" font-size="16" letter-spacing="6" fill="#6F6F6F">— SESSION ENDED —</text>')
    b.append(f'<text x="820" y="118" text-anchor="middle" font-family="{MONO}" font-weight="bold" '
             f'font-size="36" fill="{AMBER}">It\'s now safe to connect with dishanth.</text>')
    b.append(f'<rect x="1262" y="90" width="18" height="34" fill="{AMBER}"/>')
    b.append(f'<text x="820" y="150" text-anchor="middle" font-family="{MONO}" font-size="18" fill="{DIM}">'
             f'(or press any button below to keep the session alive)</text>')
    chips = [("dishanthk02@gmail.com", 380), ("in/dishanth-ca", 250), ("dishanthca.com", 250)]
    total = sum(c[1] for c in chips) + 30 * (len(chips) - 1)
    x = (1640 - total) // 2
    for label, cw in chips:
        b.append(button(x, 180, cw, 54, label, 22))
        x += cw + 30
    b.append(f'<text x="820" y="298" text-anchor="middle" font-family="{MONO}" font-size="19" fill="{SHDW}">'
             f'© 2026 dishanth ca · jersey city · all packets inspected</text>')
    b.append(f'<polygon points="0,0 260,0 120,340 0,340" fill="{WHITE}" opacity="0.025"/>')
    save("footer.svg", svg(1640, 340, "".join(b), bg="scan"))

# =====================================================================
# 9. CONTACT BUTTONS
# =====================================================================
def contact_buttons():
    for fname, label, w in (("btn-linkedin.svg", "LINKEDIN", 224),
                            ("btn-email.svg", "EMAIL", 190),
                            ("btn-portfolio.svg", "PORTFOLIO", 246),
                            ("btn-github.svg", "GITHUB", 202)):
        body = (f'<rect x="0" y="0" width="{w}" height="56" fill="{FACE}"/>'
                + bevel_out(0, 0, w, 56)
                + f'<rect x="14" y="23" width="10" height="10" fill="{NAVY}"/>'
                + f'<text x="{(w+24)//2}" y="36" text-anchor="middle" font-family="{MONO}" '
                  f'font-weight="bold" font-size="20" fill="{BLACK}">{esc(label)}</text>')
        save(fname, svg(w, 56, body, bg="none"))

# =====================================================================
banner()
boot()
divider()
about()
tech_stack()
now_building()
cards()
paper_trail()
bsod()
footer()
contact_buttons()
print("done.")
