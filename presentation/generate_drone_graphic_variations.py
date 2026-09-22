#!/usr/bin/env python3
"""Drone graphic variations - asset pack for Technical / Feasibility / Impact slides."""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree
from PIL import Image, ImageDraw

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, 'assets')
os.makedirs(ASSETS_DIR, exist_ok=True)

OUT = os.path.join(SCRIPT_DIR, 'Phoenix_Drone_Graphic_Variations.pptx')
DRONE_NAVY = os.path.join(ASSETS_DIR, 'drone_navy.png')
DRONE_ORANGE = os.path.join(ASSETS_DIR, 'drone_orange.png')
DRONE_ASPECT = 480 / 238  # w/h of the source icon


def ensure_drone_icons():
    """Generates clean drone PNG glyphs if they don't already exist."""
    def make_icon(filename, color_tuple):
        if os.path.exists(filename):
            return
        w, h = 480, 238
        img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        cx, cy = w / 2, h / 2
        off_x, off_y = 160, 75
        motors = [
            (cx - off_x, cy - off_y),
            (cx + off_x, cy - off_y),
            (cx - off_x, cy + off_y),
            (cx + off_x, cy + off_y)
        ]
        for mx, my in motors:
            d.line([(cx, cy), (mx, my)], fill=color_tuple, width=12)
        disc_r = 46
        for mx, my in motors:
            d.ellipse([mx - 14, my - 14, mx + 14, my + 14], fill=color_tuple)
            d.ellipse([mx - disc_r, my - 6, mx + disc_r, my + 6], fill=color_tuple)
            d.ellipse([mx - 6, my - disc_r, mx + 6, my + disc_r], fill=color_tuple)
        bw, bh = 110, 68
        d.rounded_rectangle([cx - bw/2, cy - bh/2, cx + bw/2, cy + bh/2], radius=16, fill=color_tuple)
        d.rounded_rectangle([cx - bw/4, cy - bh/4, cx + bw/4, cy + bh/4], radius=8, fill=(255, 255, 255, 180))
        d.ellipse([cx - 16, cy - bh/2 - 14, cx + 16, cy - bh/2 + 8], fill=color_tuple)
        d.ellipse([cx - 8, cy - bh/2 - 10, cx + 8, cy - bh/2 + 2], fill=(240, 132, 24, 255))
        img.save(filename, 'PNG')

    make_icon(DRONE_NAVY, (31, 73, 125, 255))
    make_icon(DRONE_ORANGE, (240, 132, 24, 255))


NAVY, NAVY_D, STEEL = '1F497D', '14345C', '8494A8'
ORG, ORG_D, ORG_T, ORG_S = 'F08418', 'D9700F', 'B35A00', 'FDEEDD'
BLUE, BLUE_S = '0070C0', 'E1EEF9'
CARD, CARD_LN = 'F7FAFD', 'D6E1EE'
TXT, MUTED, WHITE = '1E2638', '566074', 'FFFFFF'
BG = 'FFFFFF'

ALIGN = {'l': PP_ALIGN.LEFT, 'c': PP_ALIGN.CENTER, 'r': PP_ALIGN.RIGHT}
ANCH = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}


def rgb(h):
    return RGBColor.from_string(h)


def box(sl, kind, x, y, w, h, fill=None, line=None, lw=0.75, r=None, shadow=False, rot=0):
    sp = sl.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    st = sp._element.find(qn('p:style'))
    if st is not None:
        sp._element.remove(st)
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = rgb(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line)
        sp.line.width = Pt(lw)
    else:
        sp.line.fill.background()
    if r is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        sp.adjustments[0] = min(0.5, r / min(w, h))
    if rot:
        sp.rotation = rot
    if shadow:
        eff = etree.SubElement(sp._element.spPr, qn('a:effectLst'))
        sh = etree.SubElement(eff, qn('a:outerShdw'), blurRad='101600', dist='25400', dir='5400000', algn='t', rotWithShape='0')
        c = etree.SubElement(sh, qn('a:srgbClr'), val='1B2A44')
        etree.SubElement(c, qn('a:alpha'), val='13000')
    return sp


def set_alpha(sp, pct):
    """pct 0-100 opacity"""
    sf = sp.fill.fore_color._xFill.find(qn('a:srgbClr'))
    if sf is None:
        return
    a = etree.SubElement(sf, qn('a:alpha'))
    a.set('val', str(int(pct * 1000)))


def seg(sl, x1, y1, x2, y2, color, w=1.0, dash=None):
    ln = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    st = ln._element.find(qn('p:style'))
    if st is not None:
        ln._element.remove(st)
    ln.line.color.rgb = rgb(color)
    ln.line.width = Pt(w)
    if dash:
        lnEl = ln.line._get_or_add_ln()
        etree.SubElement(lnEl, qn('a:prstDash'), val=dash)
    return ln


def pic(sl, path, x, y, w, h, alt):
    p = sl.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    p._element.nvPicPr.cNvPr.set('descr', alt)
    return p


def R(t, b=None, i=None, c=None, s=None, spc=None):
    return dict(t=t, b=b, i=i, c=c, s=s, spc=spc)


def P(runs, after=0, before=0, align=None, ls=None):
    if isinstance(runs, dict):
        runs = [runs]
    return dict(runs=runs, after=after, before=before, align=align, ls=ls)


def T(sl, x, y, w, h, content, size=11, color=TXT, bold=False, italic=False, align='l', anchor='t', font='Calibri', spc=None):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = ANCH[anchor]
    paras = [P([R(content, spc=spc)])] if isinstance(content, str) else content
    for n, pd in enumerate(paras):
        p = tf.paragraphs[0] if n == 0 else tf.add_paragraph()
        p.alignment = ALIGN[pd['align'] or align]
        if pd['ls']:
            p.line_spacing = pd['ls']
        p.space_before = Pt(pd['before'])
        p.space_after = Pt(pd['after'])
        pPr = p._p.get_or_add_pPr()
        etree.SubElement(pPr, qn('a:buNone'))
        for rd in pd['runs']:
            r = p.add_run()
            r.text = rd['t']
            fo = r.font
            fo.name = font
            fo.size = Pt(rd['s'] or size)
            fo.bold = bold if rd['b'] is None else rd['b']
            fo.italic = italic if rd['i'] is None else rd['i']
            fo.color.rgb = rgb(rd['c'] or color)
            rPr = r._r.get_or_add_rPr()
            rPr.set('lang', 'en-US')
            if rd['spc']:
                rPr.set('spc', str(int(rd['spc'] * 100)))
    return tb


def pill(sl, label, x, y, fill=ORG_S, txt=ORG_T, fs=10, h=0.28):
    w = len(label) * fs * 0.0092 + 0.4
    box(sl, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, fill=fill, r=h / 2)
    T(sl, x, y, w, h, label, size=fs, bold=True, color=txt, align='c', anchor='m', font='Calibri')
    return w


def num_badge(sl, n, x, y, d, fill=ORG_D, txt=WHITE, fs=11):
    box(sl, MSO_SHAPE.OVAL, x, y, d, d, fill=fill)
    T(sl, x, y, d, d, str(n), size=fs, bold=True, color=txt, align='c', anchor='m')


def page_chrome(sl, kicker, title, style_tag, style_fill, style_txt, pageno):
    box(sl, MSO_SHAPE.RECTANGLE, 0, 0, XW_FULL, 0.06, fill=ORG_D)
    T(sl, 0.6, 0.28, 6, 0.22, kicker, size=10.5, bold=True, color=ORG_T, spc=1.2)
    T(sl, 0.6, 0.5, 8.5, 0.5, title, size=22, bold=True, color=NAVY_D)
    pill(sl, style_tag, XW_FULL - 0.5 - (len(style_tag) * 10.5 * 0.0092 + 0.4), 0.34, fill=style_fill, txt=style_txt, fs=10.5, h=0.32)
    T(sl, 0.6, 7.15, 8.0, 0.24, 'Drone graphic asset — copy the elements you want into your deck.', size=9.5, italic=True, color=MUTED)
    T(sl, XW_FULL - 1.0, 7.15, 0.5, 0.24, str(pageno), size=9.5, color=MUTED, align='r')


XW_FULL = 13.333


# =====================================================================
# Schematic (Style A) drone builder -- native, fully editable shapes
# =====================================================================
def draw_schematic_drone(sl, cx, cy, scale=1.0, body_color=NAVY, prop_color=STEEL, arm_color=STEEL):
    bw, bh = 1.55 * scale, 1.05 * scale
    off = 1.35 * scale
    hub_d = 0.30 * scale
    prop_d = 0.62 * scale
    motors = {
        'FL': (cx - off, cy - off * 0.86),
        'FR': (cx + off, cy - off * 0.86),
        'RL': (cx - off, cy + off * 0.86),
        'RR': (cx + off, cy + off * 0.86),
    }
    # arms (behind everything)
    for mx, my in motors.values():
        seg(sl, cx, cy, mx, my, arm_color, w=7)
    # prop discs + hubs
    for mx, my in motors.values():
        d = box(sl, MSO_SHAPE.OVAL, mx - prop_d / 2, my - prop_d / 2, prop_d, prop_d, fill=arm_color)
        set_alpha(d, 22)
        d.line.fill.background()
        box(sl, MSO_SHAPE.OVAL, mx - hub_d / 2, my - hub_d / 2, hub_d, hub_d, fill=ORG_D)
    # body
    box(sl, MSO_SHAPE.ROUNDED_RECTANGLE, cx - bw / 2, cy - bh / 2, bw, bh, fill=body_color, r=0.16 * scale, shadow=True)
    canopy_w, canopy_h = bw * 0.42, bh * 0.5
    box(sl, MSO_SHAPE.ROUNDED_RECTANGLE, cx - canopy_w / 2, cy - canopy_h / 2, canopy_w, canopy_h, fill=NAVY_D, r=0.08 * scale)
    # camera (nose)
    cam_d = 0.26 * scale
    cam_y = cy - bh / 2 - cam_d * 0.55
    box(sl, MSO_SHAPE.OVAL, cx - cam_d / 2, cam_y - cam_d / 2, cam_d, cam_d, fill=NAVY_D, line=ORG_D, lw=1.75)
    box(sl, MSO_SHAPE.OVAL, cx - cam_d * 0.28, cam_y - cam_d * 0.28, cam_d * 0.56, cam_d * 0.56, fill=ORG_D)
    # antenna (rear)
    ax0, ay0 = cx + bw * 0.22, cy + bh * 0.1
    ax1, ay1 = ax0 + 0.42 * scale, ay0 - 0.5 * scale
    seg(sl, ax0, ay0, ax1, ay1, STEEL, w=2.25)
    box(sl, MSO_SHAPE.OVAL, ax1 - 0.05 * scale, ay1 - 0.05 * scale, 0.1 * scale, 0.1 * scale, fill=ORG_D)
    return {
        'nose': (cx, cam_y - cam_d / 2),
        'antenna': (ax1, ay1),
        'body_l': (cx - bw / 2, cy - bh * 0.05),
        'body_r': (cx + bw / 2, cy - bh * 0.05),
        'belly': (cx, cy + bh / 2),
        'motor': motors['FR'],
    }


# =====================================================================
# Icon (Style B) drone builder -- single recoloured glyph
# =====================================================================
def draw_icon_drone(sl, cx, cy, w, color_path=DRONE_NAVY):
    h = w / DRONE_ASPECT
    pic(sl, color_path, cx - w / 2, cy - h / 2, w, h, 'Phoenix drone icon')
    return {
        'nose': (cx, cy - h * 0.5),
        'antenna': (cx + w * 0.30, cy - h * 0.42),
        'body_l': (cx - w * 0.22, cy + h * 0.05),
        'body_r': (cx + w * 0.22, cy + h * 0.05),
        'belly': (cx, cy + h * 0.46),
        'motor': (cx + w * 0.46, cy - h * 0.40),
    }


# =====================================================================
# Callout layout: 6 zones -> 2 columns x 3 rows of cards, leader lines drawn
# UNDER the cards so any crossing segment is hidden.
# =====================================================================
CARD_W, CARD_H, CGAP_X, CGAP_Y = 3.05, 1.66, 0.22, 0.16
COL_X = [7.15, 7.15 + CARD_W + CGAP_X]
ROW_Y = [1.28, 1.28 + CARD_H + CGAP_Y, 1.28 + 2 * (CARD_H + CGAP_Y)]
ZONE_ORDER = ['nose', 'antenna', 'body_l', 'body_r', 'belly', 'motor']
ZONE_SLOT = {  # zone -> (row, col)
    'nose': (0, 0), 'antenna': (0, 1),
    'body_l': (1, 0), 'body_r': (1, 1),
    'belly': (2, 0), 'motor': (2, 1),
}


def draw_callouts(sl, anchors, items, style):
    """items: dict zone -> (title, desc). style: 'A' or 'B'"""
    slots = {}
    for zone, (r, c) in ZONE_SLOT.items():
        slots[zone] = (COL_X[c], ROW_Y[r], CARD_W, CARD_H)

    # 1) leader lines + anchor dots (drawn first -> sit behind cards)
    for i, zone in enumerate(ZONE_ORDER):
        ax, ay = anchors[zone]
        cx0, cy0, cw, ch = slots[zone]
        edge_x, edge_y = cx0, cy0 + ch / 2
        color = ORG_D if style == 'A' else NAVY
        dash = None if style == 'A' else 'dash'
        seg(sl, ax, ay, edge_x, edge_y, color, w=1.5, dash=dash)
        box(sl, MSO_SHAPE.OVAL, ax - 0.06, ay - 0.06, 0.12, 0.12, fill=color)

    # 2) cards on top
    for i, zone in enumerate(ZONE_ORDER):
        title, desc = items[zone]
        x, y, w, h = slots[zone]
        if style == 'A':
            box(sl, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, fill=WHITE, line=CARD_LN, r=0.12, shadow=True)
            num_badge(sl, i + 1, x + 0.16, y + 0.16, 0.34, fill=ORG_D, txt=WHITE, fs=12)
            T(sl, x + 0.62, y + 0.14, w - 0.8, 0.4, title, size=12.5, bold=True, color=NAVY_D)
            T(sl, x + 0.2, y + 0.62, w - 0.4, h - 0.76, desc, size=11, color=TXT)
        else:
            fillc = BLUE_S if i % 2 == 0 else ORG_S
            box(sl, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, fill=fillc, r=0.12)
            num_badge(sl, i + 1, x + 0.16, y + 0.16, 0.34, fill=NAVY, txt=WHITE, fs=12)
            T(sl, x + 0.62, y + 0.14, w - 0.8, 0.4, title, size=12.5, bold=True, color=NAVY_D)
            T(sl, x + 0.2, y + 0.62, w - 0.4, h - 0.76, desc, size=11, color=TXT)


# =====================================================================
CONTENT = {
    'technical': dict(
        kicker='FOR THE TECHNICAL APPROACH SLIDE', title='Dual-Brain Hardware, Mapped to the Airframe',
        items={
            'nose': ('Dual 4K RGB + LWIR Thermal Camera', 'Co-registers frames for the edge YOLO detector.'),
            'antenna': ('SX1262 LoRa Radio', '17-byte packet burst over 5+ km, 868 MHz.'),
            'body_l': ('STM32U5 Flight MCU', '250 Hz deterministic stabilization loop, Zephyr RTOS.'),
            'body_r': ('QRB2210 Mission Computer', 'Runs INT8 YOLO edge AI and the optical-to-ground ray-caster.'),
            'belly': ('IMU + Barometer + LiDAR', 'State estimation, altitude hold, downward ranging.'),
            'motor': ('Brushless Motors × 4', '350 Hz PWM direct motor control.'),
        }),
    'feasibility': dict(
        kicker='FOR THE FEASIBILITY & VIABILITY SLIDE', title='Why the Airframe Is Buildable and Legal to Fly',
        items={
            'nose': ('Compact Payload Bay', 'Houses the dual-camera and compute stack inside a 1.58 kg AUW.'),
            'antenna': ('LoRa Long-Range Link', 'No cell towers required for field operation.'),
            'body_l': ('Sub-5W Compute Budget', 'Qualcomm NPU preserves 90% of power for rotor propulsion.'),
            'body_r': ('β ≥ 2.0 Thrust-to-Weight', 'Meets the Bouabdallah sizing laws for stable hover.'),
            'belly': ('Quick-Swap 4S LiPo', 'Dual battery tray for continuous sortie coverage.'),
            'motor': ('1.58 kg All-Up-Weight', 'Comfortably under the DGCA 2.0 kg Micro category.'),
        }),
    'impact': dict(
        kicker='FOR THE IMPACT & BENEFITS SLIDE', title='What Each Sortie Delivers in the Field',
        items={
            'nose': ('Thermal Detection Cone', 'Spots living 37°C body heat through smoke, fog and darkness.'),
            'antenna': ('Zero-Tower Telemetry', 'Streams the triage queue to a GCS tablet over 5+ km.'),
            'body_l': ('Autonomous Grid Sweep', 'Covers a 2 km² search polygon in a Boustrophedon pattern.'),
            'body_r': ('Ray-Cast GPS Pin', 'Converts each detection into a Lat/Long survivor marker.'),
            'belly': ('Hazard-Free Routing', 'Ranks victims and charts a safe ground path via Dijkstra.'),
            'motor': ('< 3-Minute Deployment', 'Backpack to airborne search, with no infrastructure needed.'),
        }),
}


def build():
    ensure_drone_icons()
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # ---------------------------------------------------------------- index slide
    s = prs.slides.add_slide(blank)
    box(s, MSO_SHAPE.RECTANGLE, 0, 0, 13.333, 7.5, fill=NAVY_D)
    T(s, 0.7, 0.62, 10, 0.3, 'DRONE GRAPHIC VARIATIONS', size=13, bold=True, color=ORG, spc=1.5)
    T(s, 0.7, 0.94, 11, 0.8, 'Component Callout Assets for the Phoenix Deck', size=30, bold=True, color=WHITE)
    T(s, 0.7, 1.68, 10.5, 0.4, 'Six ready-made graphics — two visual styles × three content sets. Copy whichever slide, or just the drone + a few callouts, into your own deck.', size=13, color='C9D6EA')

    cardw, cardh, gap = 5.85, 2.3, 0.3
    cards = [
        ('STYLE A — SCHEMATIC', 'Fully native PowerPoint shapes (body, arms, motors, camera, antenna). Fully editable: recolor, resize, or rebuild the pose freely.', ORG_D),
        ('STYLE B — ICON', 'A bold flat drone glyph (from your team logo) with callouts around it. Faster to drop in; the drone itself is one image.', NAVY),
    ]
    for i, (t, d, c) in enumerate(cards):
        x = 0.7 + i * (cardw + gap)
        y = 2.5
        box(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cardw, cardh, fill='1E4A7E', line='2C5C96', r=0.14)
        box(s, MSO_SHAPE.RECTANGLE, x, y, 0.09, cardh, fill=c)
        T(s, x + 0.32, y + 0.24, cardw - 0.6, 0.3, t, size=14, bold=True, color=WHITE, spc=0.5)
        T(s, x + 0.32, y + 0.68, cardw - 0.6, 1.4, d, size=12.5, color='C9D6EA')

    rows = [
        ('1-2', 'Technical Approach', 'Maps each callout to a real hardware module (camera, MCU, radio, motors).'),
        ('3-4', 'Feasibility & Viability', 'Points to the specs that make the airframe legal and buildable.'),
        ('5-6', 'Impact & Benefits', 'Points to what each part contributes to a rescue mission.'),
    ]
    ry = 5.1
    T(s, 0.7, ry - 0.32, 6, 0.28, 'SLIDES IN THIS PACK', size=10.5, bold=True, color=ORG, spc=1.2)
    for i, (nums, t, d) in enumerate(rows):
        yy = ry + i * 0.62
        box(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.7, yy, 0.85, 0.42, fill='2C5C96', r=0.1)
        T(s, 0.7, yy, 0.85, 0.42, nums, size=11.5, bold=True, color=WHITE, align='c', anchor='m')
        T(s, 1.75, yy, 3.0, 0.42, t, size=13, bold=True, color=WHITE, anchor='m')
        T(s, 4.9, yy, 7.6, 0.42, d, size=11.5, color='C9D6EA', anchor='m')

    page = 2
    for theme_key in ('technical', 'feasibility', 'impact'):
        theme = CONTENT[theme_key]

        # ---- Style A: schematic
        s = prs.slides.add_slide(blank)
        page_chrome(s, theme['kicker'], theme['title'], 'STYLE A · SCHEMATIC', ORG_S, ORG_T, page)
        anchors = draw_schematic_drone(s, cx=3.35, cy=4.15, scale=1.28)
        draw_callouts(s, anchors, theme['items'], style='A')
        page += 1

        # ---- Style B: icon
        s = prs.slides.add_slide(blank)
        page_chrome(s, theme['kicker'], theme['title'], 'STYLE B · ICON', BLUE_S, BLUE, page)
        anchors = draw_icon_drone(s, cx=3.35, cy=4.15, w=4.6, color_path=DRONE_NAVY)
        draw_callouts(s, anchors, theme['items'], style='B')
        page += 1

    prs.save(OUT)
    print(f'Successfully saved: {OUT} | Slides: {len(prs.slides)}')


if __name__ == '__main__':
    build()
