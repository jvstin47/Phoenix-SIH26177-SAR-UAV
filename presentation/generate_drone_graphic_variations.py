#!/usr/bin/env python3
"""
Phoenix X Tactical SAR UAV — Aesthetic Presentation Asset Pack Generator
Produces high-resolution, defense-grade PowerPoint slides matching Team Phoenix SIH26177 Deck v2.
Integrates 3D studio product renders, interactive callout beacons, and glassmorphic card layouts.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, 'assets')
RENDER_IMG = os.path.join(ASSETS_DIR, 'phoenix_tactical_drone_render.jpg')
OUT_PPTX = os.path.join(SCRIPT_DIR, 'Phoenix_Drone_Graphic_Variations.pptx')

# Professional Aerospace Color Palette (Aligned with SIH26177 Deck v2)
SLATE_900 = RGBColor(15, 23, 42)      # #0F172A Deep Slate
SLATE_800 = RGBColor(30, 41, 59)      # #1E293B Card Headers
SLATE_700 = RGBColor(51, 65, 85)      # #334155 Subtext
SLATE_500 = RGBColor(100, 116, 139)   # #64748B Muted Meta
SLATE_200 = RGBColor(226, 232, 240)   # #E2E8F0 Subtle Borders
SLATE_100 = RGBColor(241, 245, 249)   # #F1F5F9 Badge Background
SLATE_50  = RGBColor(248, 250, 252)   # #F8FAFC Canvas Background
WHITE     = RGBColor(255, 255, 255)

# High-Tech Aerospace Accents
ORANGE_HERO = RGBColor(234, 88, 12)   # #EA580C Qualcomm / SAR Orange
ORANGE_LIGHT = RGBColor(255, 247, 237) # #FFF7ED
ORANGE_BORDER = RGBColor(254, 215, 170)
SKY_BLUE    = RGBColor(2, 132, 199)   # #0284C7 Telemetry Blue
SKY_LIGHT   = RGBColor(240, 249, 255) # #F0F9FF
SKY_BORDER  = RGBColor(186, 230, 253)
TEAL_GREEN  = RGBColor(13, 148, 136)  # #0D9488 Triage Green
TEAL_LIGHT  = RGBColor(240, 253, 250)
VIOLET      = RGBColor(124, 58, 237)  # #7C3AED AI / Compute Purple
VIOLET_LIGHT = RGBColor(245, 243, 255)

# Normalized coordinate anchor points on the 3D drone product render (1376x768)
PIN_ANCHORS = {
    'nose':    (490 / 1376, 530 / 768),  # Dual-Spectral Gimbal Camera
    'antenna': (930 / 1376, 140 / 768),  # 868 MHz LoRa Telemetry Whip
    'body_l':  (640 / 1376, 330 / 768),  # STM32U585 Real-Time Flight MCU
    'body_r':  (780 / 1376, 240 / 768),  # Qualcomm Dragonwing QRB2210 MPU
    'belly':   (740 / 1376, 460 / 768),  # Downward ToF Rangefinder & LiPo
    'motor':   (890 / 1376, 540 / 768),  # Brushless Motors & Carbon Props
}

CONTENT = {
    'technical': {
        'kicker': 'TECHNICAL APPROACH · DUAL-BRAIN AVIONICS ARCHITECTURE',
        'title': 'Hardware Subsystem Mapping on the Phoenix X Airframe',
        'badge_text': 'AVIONICS & PAYLOAD',
        'theme_color': SKY_BLUE,
        'badge_bg': SKY_LIGHT,
        'badge_border': SKY_BORDER,
        'items': [
            {
                'zone': 'nose',
                'title': 'Dual-Spectral Vision Gimbal',
                'spec': '1080p Optical + 8-14μm Radiometric LWIR',
                'desc': 'Fuses daylight contours with thermal core-emissivity (37.0°C biological lock). Rejects solar heat false positives.',
                'accent': ORANGE_HERO
            },
            {
                'zone': 'antenna',
                'title': 'SX1262 LoRa RF Telemetry',
                'spec': '868 MHz P2P Sub-GHz Link · +22 dBm',
                'desc': 'Transmits Souli et al. (Elsevier 2024) 17-byte encrypted binary packets over 3–5 km without cellular towers.',
                'accent': SKY_BLUE
            },
            {
                'zone': 'body_l',
                'title': 'STM32U585 Flight Core (MCU)',
                'spec': 'Zephyr RTOS @ 250 Hz Loop · 350 Hz PWM',
                'desc': 'Deterministic 4ms PID motor loop. Completely isolated from AI workload to guarantee zero flight jitter.',
                'accent': TEAL_GREEN
            },
            {
                'zone': 'body_r',
                'title': 'Qualcomm QRB2210 Mission MPU',
                'spec': 'Quad-Core Linux + Hexagon NPU (< 5W)',
                'desc': 'Runs INT8-quantized YOLO object detection and 6-DOF Tait-Bryan ray-casting geodetics in under 60 ms.',
                'accent': VIOLET
            },
            {
                'zone': 'belly',
                'title': '1D ToF Laser + 3S Power Tray',
                'spec': 'VL53L1X Laser Ranging + 4500mAh LiPo',
                'desc': 'Measures true AGL ground clearance for terrain-following and ray-casting. Quick-swap battery rail.',
                'accent': ORANGE_HERO
            },
            {
                'zone': 'motor',
                'title': 'Propulsion & Power Dynamics',
                'spec': '4× 2212/2216 BLDC + 1045 Carbon Props',
                'desc': 'Delivers 2.4 kg peak thrust. Adheres to Bouabdallah sizing laws for stable hover in gusty disaster winds.',
                'accent': SKY_BLUE
            }
        ]
    },
    'feasibility': {
        'kicker': 'FEASIBILITY & VIABILITY · COMPLIANCE & SIZING LAWS',
        'title': 'Why the Airframe Is Structurally Sized, Legal & Scalable',
        'badge_text': 'DGCA MICRO-DRONE CLASS',
        'theme_color': TEAL_GREEN,
        'badge_bg': TEAL_LIGHT,
        'badge_border': TEAL_GREEN,
        'items': [
            {
                'zone': 'nose',
                'title': 'Modular Quick-Release Gimbal',
                'spec': 'Vibration-Damped Payload Bay',
                'desc': 'Houses dual sensors inside strict weight limits. Silicone dampers eliminate high-frequency motor vibration.',
                'accent': ORANGE_HERO
            },
            {
                'zone': 'antenna',
                'title': 'Indian WPC De-Licensed Band',
                'spec': '865–867 MHz Compliant (GSR 564(E))',
                'desc': '100% legal for disaster operations in India. Bypasses jammed 433 MHz and severed 4G/5G mobile towers.',
                'accent': SKY_BLUE
            },
            {
                'zone': 'body_l',
                'title': 'Sub-5W Ultra-Low Power Draw',
                'spec': 'Qualcomm Dragonwing Energy Budget',
                'desc': 'Preserves >90% of total electrical power for rotor lift, achieving 28–32 minutes search sortie endurance.',
                'accent': TEAL_GREEN
            },
            {
                'zone': 'body_r',
                'title': 'Bouabdallah Dynamic Stability',
                'spec': 'Thrust-to-Weight Ratio β ≥ 1.65 – 2.0',
                'desc': 'Sized via EPFL thesis laws. Anti-windup integrator clamping prevents motor saturation during heavy wind gusts.',
                'accent': VIOLET
            },
            {
                'zone': 'belly',
                'title': 'All-Up-Weight: 1.58 kg Total',
                'spec': 'Safely under DGCA 2.0 kg Micro Limit',
                'desc': 'Requires no complex enterprise flight licensing for disaster response drills. Deploys from backpack in <3 minutes.',
                'accent': ORANGE_HERO
            },
            {
                'zone': 'motor',
                'title': 'Disruptive Unit Economics',
                'spec': '₹35.8k Prototype ➔ ₹1.2L Production',
                'desc': 'Delivers tactical thermal SAR at 1/10th the cost of commercial enterprise imports (₹14 Lakh DJI Matrice 30T).',
                'accent': SKY_BLUE
            }
        ]
    },
    'impact': {
        'kicker': 'MISSION IMPACT · DISASTER TRIAGE & EXTRACTION',
        'title': 'How Aerial Intelligence Compresses the Golden 72 Hours',
        'badge_text': 'FIRST RESPONDER ADVANTAGE',
        'theme_color': ORANGE_HERO,
        'badge_bg': ORANGE_LIGHT,
        'badge_border': ORANGE_BORDER,
        'items': [
            {
                'zone': 'nose',
                'title': 'Zero-Visibility Human Lock',
                'spec': 'Penetrates Smoke, Fog & Dust Plumes',
                'desc': 'Spots living survivors obscured under tree canopies and light sheet rubble where RGB cameras fail completely.',
                'accent': ORANGE_HERO
            },
            {
                'zone': 'antenna',
                'title': 'Instant Ground Command Sync',
                'spec': 'Zero-Drop Telemetry Broadcast',
                'desc': 'Instantly beams casualty coordinates to portable tactical tablets up to 5 km away across debris hills.',
                'accent': SKY_BLUE
            },
            {
                'zone': 'body_l',
                'title': 'Autonomous Boustrophedon Sweep',
                'spec': '2.0 km² Coverage in < 15 Minutes',
                'desc': 'Replaces exhausting, hazardous foot search patrols with systematic, automated aerial lawnmower sweep grids.',
                'accent': TEAL_GREEN
            },
            {
                'zone': 'body_r',
                'title': 'Millimeter Ray-Casting Geodetics',
                'spec': 'WGS-84 Coordinate Output (SEP ±2.1m)',
                'desc': 'Eliminates dangerous overhead hovering. Converts oblique camera pixels into exact GPS coordinates in real time.',
                'accent': VIOLET
            },
            {
                'zone': 'belly',
                'title': 'Hazard-Aware Dijkstra Routing',
                'spec': 'Safe Pedestrian Rescue Corridors',
                'desc': 'Charts safe walking paths for NDRF teams that actively route around live 11kV wires, landslides, and fire lines.',
                'accent': ORANGE_HERO
            },
            {
                'zone': 'motor',
                'title': 'Sub-5-Minute Response Cycle',
                'spec': 'Instant Launch to Boots-on-Ground',
                'desc': 'Compresses hours of manual searching into minutes—delivering urgent medical triage within the Golden 72 Hours.',
                'accent': SKY_BLUE
            }
        ]
    }
}


def add_shape_shadow(sp):
    """Adds a subtle, modern diffused drop shadow."""
    eff = etree.SubElement(sp._element.spPr, qn('a:effectLst'))
    sh = etree.SubElement(
        eff, qn('a:outerShdw'),
        blurRad='101600', dist='25400', dir='5400000', algn='t', rotWithShape='0'
    )
    c = etree.SubElement(sh, qn('a:srgbClr'), val='0F172A')
    etree.SubElement(c, qn('a:alpha'), val='10000')


def build_slide(prs, theme_key):
    data = CONTENT[theme_key]
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # 1. Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_50
    bg.line.fill.background()

    # 2. Header Area
    # Project Pill Left
    proj_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.32), Inches(1.85), Inches(0.44))
    proj_pill.fill.solid()
    proj_pill.fill.fore_color.rgb = WHITE
    proj_pill.line.color.rgb = SLATE_200
    proj_pill.line.width = Pt(1)
    tf_p = proj_pill.text_frame
    tf_p.word_wrap = False
    tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_p = tf_p.paragraphs[0]
    p_p.alignment = PP_ALIGN.CENTER
    r_p = p_p.add_run()
    r_p.text = "PHOENIX X · SIH26177"
    r_p.font.name = "Calibri"
    r_p.font.size = Pt(10)
    r_p.font.bold = True
    r_p.font.color.rgb = SLATE_800

    # Kicker
    kicker_box = slide.shapes.add_textbox(Inches(2.6), Inches(0.28), Inches(7.5), Inches(0.24))
    tf_k = kicker_box.text_frame
    tf_k.margin_left = tf_k.margin_right = tf_k.margin_top = tf_k.margin_bottom = 0
    p_k = tf_k.paragraphs[0]
    r_k = p_k.add_run()
    r_k.text = data['kicker']
    r_k.font.name = "Calibri"
    r_k.font.size = Pt(10)
    r_k.font.bold = True
    r_k.font.color.rgb = ORANGE_HERO

    # Title
    title_box = slide.shapes.add_textbox(Inches(2.6), Inches(0.52), Inches(7.5), Inches(0.48))
    tf_t = title_box.text_frame
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = data['title']
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(18)
    r_t.font.bold = True
    r_t.font.color.rgb = SLATE_900

    # Theme Pill Right
    theme_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.3), Inches(0.35), Inches(2.4), Inches(0.42))
    theme_pill.fill.solid()
    theme_pill.fill.fore_color.rgb = data['badge_bg']
    theme_pill.line.color.rgb = data['badge_border']
    theme_pill.line.width = Pt(1)
    tf_th = theme_pill.text_frame
    tf_th.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_th = tf_th.paragraphs[0]
    p_th.alignment = PP_ALIGN.CENTER
    r_th = p_th.add_run()
    r_th.text = data['badge_text']
    r_th.font.name = "Calibri"
    r_th.font.size = Pt(10)
    r_th.font.bold = True
    r_th.font.color.rgb = data['theme_color']

    # 3. Left Hero Container: 3D Tactical Drone Render
    hero_card_x = Inches(0.6)
    hero_card_y = Inches(1.15)
    hero_card_w = Inches(6.5)
    hero_card_h = Inches(5.85)

    hero_card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        hero_card_x, hero_card_y, hero_card_w, hero_card_h
    )
    hero_card.fill.solid()
    hero_card.fill.fore_color.rgb = WHITE
    hero_card.line.color.rgb = SLATE_200
    hero_card.line.width = Pt(1.2)
    add_shape_shadow(hero_card)

    # Top accent line for hero card
    accent_bar = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        hero_card_x + Inches(0.2), hero_card_y + Inches(0.18), Inches(1.6), Inches(0.06)
    )
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = ORANGE_HERO
    accent_bar.line.fill.background()

    # Hero Card Title Tag
    tag_box = slide.shapes.add_textbox(hero_card_x + Inches(0.2), hero_card_y + Inches(0.3), Inches(4.5), Inches(0.3))
    tf_tag = tag_box.text_frame
    tf_tag.margin_left = tf_tag.margin_right = tf_tag.margin_top = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    r_tag1 = p_tag.add_run()
    r_tag1.text = "TACTICAL RECONNAISSANCE AIRFRAME "
    r_tag1.font.bold = True
    r_tag1.font.size = Pt(10.5)
    r_tag1.font.color.rgb = SLATE_900

    r_tag2 = p_tag.add_run()
    r_tag2.text = "· 3D PRODUCT SCHEMATIC"
    r_tag2.font.size = Pt(10.5)
    r_tag2.font.color.rgb = SLATE_500

    # Embed High-Resolution 3D Drone Product Render
    img_x = hero_card_x + Inches(0.25)
    img_y = hero_card_y + Inches(0.8)
    img_w = Inches(6.0)
    img_h = Inches(3.35)  # 1376x768 aspect ratio
    slide.shapes.add_picture(RENDER_IMG, img_x, img_y, img_w, img_h)

    # Add 6 Precise Interactive Beacon Pins over the 3D Render
    pin_coords = {}
    for i, item in enumerate(data['items']):
        zone = item['zone']
        nx, ny = PIN_ANCHORS[zone]
        px = img_x + img_w * nx
        py = img_y + img_h * ny
        pin_coords[zone] = (px, py)

        # Outer pulsing glow halo
        halo = slide.shapes.add_shape(MSO_SHAPE.OVAL, px - Inches(0.22), py - Inches(0.22), Inches(0.44), Inches(0.44))
        halo.fill.solid()
        halo.fill.fore_color.rgb = item['accent']
        halo.line.fill.background()
        # Set transparency via oxml
        sf = halo.fill.fore_color._xFill.find(qn('a:srgbClr'))
        if sf is not None:
            a = etree.SubElement(sf, qn('a:alpha'))
            a.set('val', '35000')

        # Solid numbered pin badge
        pin = slide.shapes.add_shape(MSO_SHAPE.OVAL, px - Inches(0.16), py - Inches(0.16), Inches(0.32), Inches(0.32))
        pin.fill.solid()
        pin.fill.fore_color.rgb = item['accent']
        pin.line.color.rgb = WHITE
        pin.line.width = Pt(1.5)
        tf_pin = pin.text_frame
        tf_pin.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_pin = tf_pin.paragraphs[0]
        p_pin.alignment = PP_ALIGN.CENTER
        r_pin = p_pin.add_run()
        r_pin.text = str(i + 1)
        r_pin.font.name = "Calibri"
        r_pin.font.size = Pt(11)
        r_pin.font.bold = True
        r_pin.font.color.rgb = WHITE

    # Bottom Specs Banner inside Hero Card
    specs_y = hero_card_y + Inches(4.35)
    specs_w = Inches(1.9)
    specs_h = Inches(1.25)
    specs_data = [
        ("AUW MASS BUDGET", "1.58 kg", "DGCA Micro Category", TEAL_GREEN, TEAL_LIGHT),
        ("DUAL-BRAIN CHIPS", "QRB2210 + STM32", "Linux NPU + Zephyr RTOS", VIOLET, VIOLET_LIGHT),
        ("OFF-GRID TELEMETRY", "868 MHz LoRa", "17-byte P2P (3–5 km)", SKY_BLUE, SKY_LIGHT)
    ]
    for idx, (label, val, sub, col, bg_col) in enumerate(specs_data):
        sp_x = hero_card_x + Inches(0.22) + idx * (specs_w + Inches(0.14))
        sb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sp_x, specs_y, specs_w, specs_h)
        sb.fill.solid()
        sb.fill.fore_color.rgb = bg_col
        sb.line.color.rgb = SLATE_200
        sb.line.width = Pt(0.75)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_right = tf_sb.margin_top = Inches(0.12)
        tf_sb.vertical_anchor = MSO_ANCHOR.TOP

        p1 = tf_sb.paragraphs[0]
        r1 = p1.add_run()
        r1.text = label + "\n"
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = SLATE_500

        p2 = tf_sb.add_paragraph()
        r2 = p2.add_run()
        r2.text = val + "\n"
        r2.font.size = Pt(13.5)
        r2.font.bold = True
        r2.font.color.rgb = col

        p3 = tf_sb.add_paragraph()
        r3 = p3.add_run()
        r3.text = sub
        r3.font.size = Pt(8.5)
        r3.font.color.rgb = SLATE_700

    # 4. Right Side Feature Cards: 2 Columns × 3 Rows
    card_w = Inches(2.65)
    card_h = Inches(1.82)
    gap_x = Inches(0.2)
    gap_y = Inches(0.18)
    col_x = [Inches(7.35), Inches(7.35) + card_w + gap_x]
    row_y = [
        Inches(1.15),
        Inches(1.15) + card_h + gap_y,
        Inches(1.15) + 2 * (card_h + gap_y)
    ]

    for i, item in enumerate(data['items']):
        c = i % 2
        r = i // 2
        x = col_x[c]
        y = row_y[r]

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = SLATE_200
        card.line.width = Pt(1.0)
        add_shape_shadow(card)

        # Left Vertical Accent Stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(0.08), card_h)
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = item['accent']
        stripe.line.fill.background()

        # Number Badge
        nb = slide.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.16), y + Inches(0.14), Inches(0.34), Inches(0.34))
        nb.fill.solid()
        nb.fill.fore_color.rgb = item['accent']
        nb.line.color.rgb = WHITE
        nb.line.width = Pt(1)
        tf_nb = nb.text_frame
        tf_nb.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_nb = tf_nb.paragraphs[0]
        p_nb.alignment = PP_ALIGN.CENTER
        r_nb = p_nb.add_run()
        r_nb.text = str(i + 1)
        r_nb.font.bold = True
        r_nb.font.size = Pt(11)
        r_nb.font.color.rgb = WHITE

        # Header Text
        tb_head = slide.shapes.add_textbox(x + Inches(0.58), y + Inches(0.12), card_w - Inches(0.68), Inches(0.38))
        tf_h = tb_head.text_frame
        tf_h.margin_left = tf_h.margin_right = tf_h.margin_top = tf_h.margin_bottom = 0
        p_h = tf_h.paragraphs[0]
        r_h = p_h.add_run()
        r_h.text = item['title']
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = SLATE_900

        # Spec Sub-pill
        sp_box = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x + Inches(0.16), y + Inches(0.55), card_w - Inches(0.32), Inches(0.26)
        )
        sp_box.fill.solid()
        sp_box.fill.fore_color.rgb = SLATE_100
        sp_box.line.color.rgb = SLATE_200
        sp_box.line.width = Pt(0.5)
        tf_sp = sp_box.text_frame
        tf_sp.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf_sp.margin_left = Inches(0.08)
        p_sp = tf_sp.paragraphs[0]
        r_sp = p_sp.add_run()
        r_sp.text = item['spec']
        r_sp.font.bold = True
        r_sp.font.size = Pt(8.5)
        r_sp.font.color.rgb = SLATE_700

        # Description Body
        tb_body = slide.shapes.add_textbox(
            x + Inches(0.16), y + Inches(0.88), card_w - Inches(0.32), card_h - Inches(0.95)
        )
        tf_b = tb_body.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        r_b = p_b.add_run()
        r_b.text = item['desc']
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = SLATE_700


def build_index_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_900
    bg.line.fill.background()

    # Kicker
    k = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(10), Inches(0.3))
    tf_k = k.text_frame
    p_k = tf_k.paragraphs[0]
    r_k = p_k.add_run()
    r_k.text = "PHOENIX X · HARDWARE PRESENTATION ASSET PACK"
    r_k.font.bold = True
    r_k.font.size = Pt(11)
    r_k.font.color.rgb = ORANGE_HERO

    # Title
    t = slide.shapes.add_textbox(Inches(0.8), Inches(1.05), Inches(11), Inches(0.8))
    tf_t = t.text_frame
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = "High-Resolution Airframe Graphics & Callouts"
    r_t.font.bold = True
    r_t.font.size = Pt(28)
    r_t.font.color.rgb = WHITE

    # Subtitle
    sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.85), Inches(11), Inches(0.4))
    tf_sub = sub.text_frame
    p_sub = tf_sub.paragraphs[0]
    r_sub = p_sub.add_run()
    r_sub.text = "Studio 3D tactical renders with interactive numbered beacons, aligned 1:1 with SIH26177 Deck v2."
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = SLATE_200

    # 3 Summary Cards
    cards_data = [
        ("SLIDE 2: TECHNICAL APPROACH", "Avionics & Compute Partition", "Dual-stream EO/IR, QRB2210 Linux MPU, STM32U5 Zephyr RTOS, 17-byte LoRa packet, ToF altimeter.", SKY_BLUE),
        ("SLIDE 3: FEASIBILITY & SIZING", "Buildability & Legal Viability", "DGCA 1.58 kg AUW, Bouabdallah β ≥ 2.0 sizing laws, WPC 868 MHz compliance, sub-5W compute.", TEAL_GREEN),
        ("SLIDE 4: MISSION IMPACT", "Golden 72h Search Deliverables", "Smoke penetration, Dijkstra safe pedestrian routing, WGS-84 ray-casting, sub-5 min response.", ORANGE_HERO)
    ]
    for idx, (title, sub_title, desc, accent) in enumerate(cards_data):
        cx = Inches(0.8) + idx * Inches(3.9)
        cy = Inches(2.6)
        cw = Inches(3.65)
        ch = Inches(3.8)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, cw, ch)
        card.fill.solid()
        card.fill.fore_color.rgb = SLATE_800
        card.line.color.rgb = SLATE_700
        card.line.width = Pt(1.2)

        # Top Accent
        acc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, cw, Inches(0.08))
        acc.fill.solid()
        acc.fill.fore_color.rgb = accent
        acc.line.fill.background()

        tf_c = card.text_frame
        tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = Inches(0.3)
        tf_c.vertical_anchor = MSO_ANCHOR.TOP

        p1 = tf_c.paragraphs[0]
        r1 = p1.add_run()
        r1.text = title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = accent

        p2 = tf_c.add_paragraph()
        r2 = p2.add_run()
        r2.text = sub_title + "\n\n"
        r2.font.bold = True
        r2.font.size = Pt(15)
        r2.font.color.rgb = WHITE

        p3 = tf_c.add_paragraph()
        r3 = p3.add_run()
        r3.text = desc
        r3.font.size = Pt(11)
        r3.font.color.rgb = SLATE_200


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    build_index_slide(prs)
    build_slide(prs, 'technical')
    build_slide(prs, 'feasibility')
    build_slide(prs, 'impact')

    prs.save(OUT_PPTX)
    print(f"Successfully generated high-aesthetic presentation: {OUT_PPTX} ({len(prs.slides)} slides)")


if __name__ == '__main__':
    main()
