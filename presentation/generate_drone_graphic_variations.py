#!/usr/bin/env python3
"""
Phoenix X Tactical SAR UAV — Creative Visual Presentation Master Pack
Produces high-resolution, self-explanatory aerospace infographics matching Team Phoenix SIH26177 Deck v2.
Integrates 3D studio product renders, in-flight dual-beam perception shots, and NDRF tactical GIS tablet field visuals.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, 'assets')
OUT_PPTX = os.path.join(SCRIPT_DIR, 'Phoenix_Drone_Graphic_Variations.pptx')

# Image Assets
IMG_STUDIO_DRONE = os.path.join(ASSETS_DIR, 'phoenix_tactical_drone_render.jpg')
IMG_DUAL_BEAM    = os.path.join(ASSETS_DIR, 'phoenix_drone_dual_beam_action.jpg')
IMG_TABLET_GCS   = os.path.join(ASSETS_DIR, 'tactical_gcs_safe_route_tablet.jpg')

# Professional Aerospace Color Palette
SLATE_900 = RGBColor(15, 23, 42)      # #0F172A
SLATE_800 = RGBColor(30, 41, 59)      # #1E293B
SLATE_700 = RGBColor(51, 65, 85)      # #334155
SLATE_600 = RGBColor(71, 85, 105)     # #475569
SLATE_500 = RGBColor(100, 116, 139)   # #64748B
SLATE_200 = RGBColor(226, 232, 240)   # #E2E8F0
SLATE_100 = RGBColor(241, 245, 249)   # #F1F5F9
SLATE_50  = RGBColor(248, 250, 252)   # #F8FAFC
WHITE     = RGBColor(255, 255, 255)

# High-Tech Aerospace Accents
ORANGE_HERO   = RGBColor(234, 88, 12)   # #EA580C Qualcomm / SAR Orange
ORANGE_LIGHT  = RGBColor(255, 247, 237) # #FFF7ED
ORANGE_BORDER = RGBColor(254, 215, 170)
SKY_BLUE      = RGBColor(2, 132, 199)   # #0284C7 Telemetry Blue
SKY_LIGHT     = RGBColor(240, 249, 255) # #F0F9FF
SKY_BORDER    = RGBColor(186, 230, 253)
TEAL_GREEN    = RGBColor(13, 148, 136)  # #0D9488 Triage Green
TEAL_LIGHT    = RGBColor(240, 253, 250)
VIOLET        = RGBColor(124, 58, 237)  # #7C3AED AI / Compute Purple
VIOLET_LIGHT  = RGBColor(245, 243, 255)
RED_ACCENT    = RGBColor(225, 29, 72)   # #E11D48 Hazard Red
RED_LIGHT     = RGBColor(255, 241, 242)

# Normalized coordinates for the 3D studio render
PIN_ANCHORS = {
    'nose':    (490 / 1376, 530 / 768),
    'antenna': (930 / 1376, 140 / 768),
    'body_l':  (640 / 1376, 330 / 768),
    'body_r':  (780 / 1376, 240 / 768),
    'belly':   (740 / 1376, 460 / 768),
    'motor':   (890 / 1376, 540 / 768),
}


def add_shape_shadow(sp):
    eff = etree.SubElement(sp._element.spPr, qn('a:effectLst'))
    sh = etree.SubElement(eff, qn('a:outerShdw'), blurRad='101600', dist='25400', dir='5400000', algn='t', rotWithShape='0')
    c = etree.SubElement(sh, qn('a:srgbClr'), val='0F172A')
    etree.SubElement(c, qn('a:alpha'), val='10000')


def add_header(slide, kicker_text, title_text, badge_text, badge_col, badge_bg, badge_border):
    # Project Pill Left
    proj_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.3), Inches(1.85), Inches(0.42))
    proj_pill.fill.solid()
    proj_pill.fill.fore_color.rgb = WHITE
    proj_pill.line.color.rgb = SLATE_200
    proj_pill.line.width = Pt(1)
    tf_p = proj_pill.text_frame
    tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_p = tf_p.paragraphs[0]
    p_p.alignment = PP_ALIGN.CENTER
    r_p = p_p.add_run()
    r_p.text = "PHOENIX X · SIH26177"
    r_p.font.name = "Calibri"
    r_p.font.size = Pt(9.5)
    r_p.font.bold = True
    r_p.font.color.rgb = SLATE_800

    # Kicker
    kicker_box = slide.shapes.add_textbox(Inches(2.6), Inches(0.24), Inches(7.6), Inches(0.24))
    tf_k = kicker_box.text_frame
    tf_k.margin_left = tf_k.margin_right = tf_k.margin_top = tf_k.margin_bottom = 0
    p_k = tf_k.paragraphs[0]
    r_k = p_k.add_run()
    r_k.text = kicker_text
    r_k.font.name = "Calibri"
    r_k.font.size = Pt(9.5)
    r_k.font.bold = True
    r_k.font.color.rgb = ORANGE_HERO

    # Title
    title_box = slide.shapes.add_textbox(Inches(2.6), Inches(0.48), Inches(7.6), Inches(0.45))
    tf_t = title_box.text_frame
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = title_text
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(17)
    r_t.font.bold = True
    r_t.font.color.rgb = SLATE_900

    # Theme Pill Right
    theme_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.3), Inches(0.3), Inches(2.4), Inches(0.42))
    theme_pill.fill.solid()
    theme_pill.fill.fore_color.rgb = badge_bg
    theme_pill.line.color.rgb = badge_border
    theme_pill.line.width = Pt(1)
    tf_th = theme_pill.text_frame
    tf_th.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_th = tf_th.paragraphs[0]
    p_th.alignment = PP_ALIGN.CENTER
    r_th = p_th.add_run()
    r_th.text = badge_text
    r_th.font.name = "Calibri"
    r_th.font.size = Pt(9.5)
    r_th.font.bold = True
    r_th.font.color.rgb = badge_col


def build_hardware_mapping_slide(prs, theme_key):
    """Renders the 3D studio render with interactive numbered beacon pins and glassmorphic cards."""
    data = {
        'technical': {
            'kicker': 'TECHNICAL APPROACH · DUAL-BRAIN AVIONICS ARCHITECTURE',
            'title': 'Hardware Subsystem Mapping on the Phoenix X Airframe',
            'badge_text': 'AVIONICS & PAYLOAD',
            'theme_color': SKY_BLUE,
            'badge_bg': SKY_LIGHT,
            'badge_border': SKY_BORDER,
            'items': [
                {'zone': 'nose', 'title': 'Dual-Spectral Vision Gimbal', 'spec': '1080p Optical + 8-14μm Radiometric LWIR', 'desc': 'Fuses visual contours with thermal emissivity (37.0°C biological lock). Rejects solar heat false positives.', 'accent': ORANGE_HERO},
                {'zone': 'antenna', 'title': 'SX1262 LoRa RF Telemetry', 'spec': '868 MHz P2P Sub-GHz Link · +22 dBm', 'desc': 'Transmits Souli et al. (Elsevier 2024) 17-byte encrypted binary packets over 3–5 km without cellular towers.', 'accent': SKY_BLUE},
                {'zone': 'body_l', 'title': 'STM32U585 Flight Core (MCU)', 'spec': 'Zephyr RTOS @ 250 Hz Loop · 350 Hz PWM', 'desc': 'Deterministic 4ms PID motor loop. Completely isolated from AI workload to guarantee zero flight jitter.', 'accent': TEAL_GREEN},
                {'zone': 'body_r', 'title': 'Qualcomm QRB2210 Mission MPU', 'spec': 'Quad-Core Linux + Hexagon NPU (< 5W)', 'desc': 'Runs INT8-quantized YOLO object detection and 6-DOF Tait-Bryan ray-casting geodetics in under 60 ms.', 'accent': VIOLET},
                {'zone': 'belly', 'title': '1D ToF Laser + 3S Power Tray', 'spec': 'VL53L1X Laser Ranging + 4500mAh LiPo', 'desc': 'Measures true AGL ground clearance for terrain-following and ray-casting. Quick-swap battery rail.', 'accent': ORANGE_HERO},
                {'zone': 'motor', 'title': 'Propulsion & Power Dynamics', 'spec': '4× 2212/2216 BLDC + 1045 Carbon Props', 'desc': 'Delivers 2.4 kg peak thrust. Adheres to Bouabdallah sizing laws for stable hover in gusty disaster winds.', 'accent': SKY_BLUE}
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
                {'zone': 'nose', 'title': 'Modular Quick-Release Gimbal', 'spec': 'Vibration-Damped Payload Bay', 'desc': 'Houses dual sensors inside strict weight limits. Silicone dampers eliminate high-frequency motor vibration.', 'accent': ORANGE_HERO},
                {'zone': 'antenna', 'title': 'Indian WPC De-Licensed Band', 'spec': '865–867 MHz Compliant (GSR 564(E))', 'desc': '100% legal for disaster operations in India. Bypasses jammed 433 MHz and severed 4G/5G mobile towers.', 'accent': SKY_BLUE},
                {'zone': 'body_l', 'title': 'Sub-5W Ultra-Low Power Draw', 'spec': 'Qualcomm Dragonwing Energy Budget', 'desc': 'Preserves >90% of total electrical power for rotor lift, achieving 28–32 minutes search sortie endurance.', 'accent': TEAL_GREEN},
                {'zone': 'body_r', 'title': 'Bouabdallah Dynamic Stability', 'spec': 'Thrust-to-Weight Ratio β ≥ 1.65 – 2.0', 'desc': 'Sized via EPFL thesis laws. Anti-windup integrator clamping prevents motor saturation during heavy wind gusts.', 'accent': VIOLET},
                {'zone': 'belly', 'title': 'All-Up-Weight: 1.58 kg Total', 'spec': 'Safely under DGCA 2.0 kg Micro Limit', 'desc': 'Requires no complex enterprise flight licensing for disaster response drills. Deploys from backpack in <3 minutes.', 'accent': ORANGE_HERO},
                {'zone': 'motor', 'title': 'Disruptive Unit Economics', 'spec': '₹35.8k Prototype ➔ ₹1.2L Production', 'desc': 'Delivers tactical thermal SAR at 1/10th the cost of commercial enterprise imports (₹14 Lakh DJI Matrice 30T).', 'accent': SKY_BLUE}
            ]
        }
    }[theme_key]

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_50
    bg.line.fill.background()

    add_header(slide, data['kicker'], data['title'], data['badge_text'], data['theme_color'], data['badge_bg'], data['badge_border'])

    # Left Hero Container
    hero_card_x, hero_card_y, hero_card_w, hero_card_h = Inches(0.6), Inches(1.15), Inches(6.5), Inches(5.85)
    hero_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hero_card_x, hero_card_y, hero_card_w, hero_card_h)
    hero_card.fill.solid()
    hero_card.fill.fore_color.rgb = WHITE
    hero_card.line.color.rgb = SLATE_200
    hero_card.line.width = Pt(1.2)
    add_shape_shadow(hero_card)

    accent_bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hero_card_x + Inches(0.2), hero_card_y + Inches(0.18), Inches(1.6), Inches(0.06))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = ORANGE_HERO
    accent_bar.line.fill.background()

    tag_box = slide.shapes.add_textbox(hero_card_x + Inches(0.2), hero_card_y + Inches(0.3), Inches(4.5), Inches(0.3))
    tf_tag = tag_box.text_frame
    tf_tag.margin_left = tf_tag.margin_right = tf_tag.margin_top = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    r_tag1 = p_tag.add_run()
    r_tag1.text = "TACTICAL RECONNAISSANCE AIRFRAME "
    r_tag1.font.bold = True
    r_tag1.font.size = Pt(10)
    r_tag1.font.color.rgb = SLATE_900
    r_tag2 = p_tag.add_run()
    r_tag2.text = "· 3D PRODUCT SCHEMATIC"
    r_tag2.font.size = Pt(10)
    r_tag2.font.color.rgb = SLATE_500

    img_x, img_y, img_w, img_h = hero_card_x + Inches(0.25), hero_card_y + Inches(0.8), Inches(6.0), Inches(3.35)
    slide.shapes.add_picture(IMG_STUDIO_DRONE, img_x, img_y, img_w, img_h)

    for i, item in enumerate(data['items']):
        zone = item['zone']
        nx, ny = PIN_ANCHORS[zone]
        px, py = img_x + img_w * nx, img_y + img_h * ny

        halo = slide.shapes.add_shape(MSO_SHAPE.OVAL, px - Inches(0.22), py - Inches(0.22), Inches(0.44), Inches(0.44))
        halo.fill.solid()
        halo.fill.fore_color.rgb = item['accent']
        halo.line.fill.background()
        sf = halo.fill.fore_color._xFill.find(qn('a:srgbClr'))
        if sf is not None:
            a = etree.SubElement(sf, qn('a:alpha'))
            a.set('val', '35000')

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

    specs_y, specs_w, specs_h = hero_card_y + Inches(4.35), Inches(1.9), Inches(1.25)
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
        r2.font.size = Pt(13)
        r2.font.bold = True
        r2.font.color.rgb = col

        p3 = tf_sb.add_paragraph()
        r3 = p3.add_run()
        r3.text = sub
        r3.font.size = Pt(8.5)
        r3.font.color.rgb = SLATE_700

    # Right Side Cards (2x3 Grid)
    card_w, card_h, gap_x, gap_y = Inches(2.65), Inches(1.82), Inches(0.2), Inches(0.18)
    col_x = [Inches(7.35), Inches(7.35) + card_w + gap_x]
    row_y = [Inches(1.15), Inches(1.15) + card_h + gap_y, Inches(1.15) + 2 * (card_h + gap_y)]

    for i, item in enumerate(data['items']):
        c, r = i % 2, i // 2
        x, y = col_x[c], row_y[r]

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = SLATE_200
        card.line.width = Pt(1.0)
        add_shape_shadow(card)

        stripe = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(0.08), card_h)
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = item['accent']
        stripe.line.fill.background()

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

        tb_head = slide.shapes.add_textbox(x + Inches(0.58), y + Inches(0.12), card_w - Inches(0.68), Inches(0.38))
        tf_h = tb_head.text_frame
        tf_h.margin_left = tf_h.margin_right = tf_h.margin_top = tf_h.margin_bottom = 0
        p_h = tf_h.paragraphs[0]
        r_h = p_h.add_run()
        r_h.text = item['title']
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = SLATE_900

        sp_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.16), y + Inches(0.55), card_w - Inches(0.32), Inches(0.26))
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

        tb_body = slide.shapes.add_textbox(x + Inches(0.16), y + Inches(0.88), card_w - Inches(0.32), card_h - Inches(0.95))
        tf_b = tb_body.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        r_b = p_b.add_run()
        r_b.text = item['desc']
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = SLATE_700


def build_dual_beam_action_slide(prs):
    """Creative Slide: In-Flight Dual-Spectral Perception & 3D Ray-Casting in Action."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_50
    bg.line.fill.background()

    add_header(
        slide,
        'MULTI-SPECTRAL PERCEPTION · REAL-TIME TARGET ACQUISITION',
        'How Phoenix X Detects Living Survivors Through Dense Smoke & Debris',
        'DUAL-BEAM TACTICAL HUD',
        ORANGE_HERO, ORANGE_LIGHT, ORANGE_BORDER
    )

    # Left Hero Container: In-Action Cinematic Render
    hero_w, hero_h = Inches(7.8), Inches(5.85)
    hx, hy = Inches(0.6), Inches(1.15)

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hx, hy, hero_w, hero_h)
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = SLATE_200
    card.line.width = Pt(1.2)
    add_shape_shadow(card)

    # Insert the in-flight dual-beam render
    slide.shapes.add_picture(IMG_DUAL_BEAM, hx + Inches(0.15), hy + Inches(0.15), hero_w - Inches(0.3), hero_h - Inches(0.3))

    # Right Explanatory Stack (3 Interactive Breakdown Cards)
    rx = Inches(8.65)
    rw = Inches(4.08)
    cards_info = [
        (
            "1. DUAL-SPECTRAL CONICAL SENSING",
            "Cyan Beam: 1080p Optical Geometry\nOrange Beam: 8–14μm Radiometric LWIR",
            "Standard RGB cameras blind at dusk and in smoke plumes. Phoenix X projects co-registered optical and thermal fields-of-view, continuously scanning rubble crevices for human infrared emissions.",
            SKY_BLUE, SKY_LIGHT, SKY_BORDER
        ),
        (
            "2. RADIOMETRIC CORE HEAT FILTER",
            "Gated Detection: 36.5°C to 37.5°C\nNoise Equivalent Temp Diff: NETD < 50 mK",
            "Solar radiation heats tin roofs, wet mud, and rocks to over 45°C. Phoenix X isolates true biological core temperature profiles, instantly discarding thermal false alarms before passing tensors to the NPU.",
            ORANGE_HERO, ORANGE_LIGHT, ORANGE_BORDER
        ),
        (
            "3. 6-DOF TAIT-BRYAN RAY-CASTING",
            "Optical-to-Ground Vector Projection\nAccuracy: WGS-84 within ±2.1m SEP",
            "Hovering overhead puts drones at risk of collision. The drone flies at an oblique standoff angle; its onboard NPU projects camera bounding-box pixels directly onto a local DEM elevation grid in < 60 ms.",
            TEAL_GREEN, TEAL_LIGHT, TEAL_GREEN
        )
    ]

    for idx, (head, pill_txt, desc, col, bg_col, bdr_col) in enumerate(cards_info):
        cy = Inches(1.15) + idx * (Inches(1.82) + Inches(0.19))
        c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, cy, rw, Inches(1.82))
        c.fill.solid()
        c.fill.fore_color.rgb = WHITE
        c.line.color.rgb = SLATE_200
        c.line.width = Pt(1)
        add_shape_shadow(c)

        # Left stripe
        st = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, cy, Inches(0.08), Inches(1.82))
        st.fill.solid()
        st.fill.fore_color.rgb = col
        st.line.fill.background()

        tf_c = c.text_frame
        tf_c.margin_left = Inches(0.22)
        tf_c.margin_right = Inches(0.2)
        tf_c.margin_top = Inches(0.14)
        tf_c.vertical_anchor = MSO_ANCHOR.TOP

        p0 = tf_c.paragraphs[0]
        r0 = p0.add_run()
        r0.text = head + "\n"
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = SLATE_900

        p1 = tf_c.add_paragraph()
        r1 = p1.add_run()
        r1.text = pill_txt + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = col

        p2 = tf_c.add_paragraph()
        r2 = p2.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = SLATE_600


def build_gcs_safe_route_slide(prs):
    """Creative Slide: NDRF First Responder Holding Tactical GCS Tablet with Dijkstra Safe Route."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_50
    bg.line.fill.background()

    add_header(
        slide,
        'INCIDENT COMMAND & GIS ROUTING · FIRST RESPONDER INTEGRATION',
        'From Airborne Detection to Boots-on-Ground Extraction in < 5 Minutes',
        'TACTICAL RESCUE GCS',
        TEAL_GREEN, TEAL_LIGHT, TEAL_GREEN
    )

    # Left Hero Container: NDRF Rescuer with Field Tablet
    hero_w, hero_h = Inches(7.8), Inches(5.85)
    hx, hy = Inches(0.6), Inches(1.15)

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hx, hy, hero_w, hero_h)
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = SLATE_200
    card.line.width = Pt(1.2)
    add_shape_shadow(card)

    slide.shapes.add_picture(IMG_TABLET_GCS, hx + Inches(0.15), hy + Inches(0.15), hero_w - Inches(0.3), hero_h - Inches(0.3))

    # Right Explanatory Stack (3 Interactive Breakdown Cards)
    rx = Inches(8.65)
    rw = Inches(4.08)
    cards_info = [
        (
            "1. 17-BYTE LORA PACKET INGESTION",
            "Zero Cloud / Zero Internet Architecture\nAir-Gapped Local Tactical Mesh (868 MHz)",
            "Incoming telemetry packets unpack victim coordinates, biological body temperature (37.0°C), and triage status directly into the offline Leaflet GIS dashboard in milliseconds without commercial cellular service.",
            SKY_BLUE
        ),
        (
            "2. HAZARD-AWARE DIJKSTRA ROUTING",
            "Dynamic Obstacle & Danger Buffers\nAvoids: 11kV Severed Wires, Landslides, Fires",
            "Rescuers walking blindly into disaster zones suffer secondary casualties. Phoenix X plots an automated, hazard-weighted pedestrian extraction path navigating safely around verified hazards.",
            RED_ACCENT
        ),
        (
            "3. 5-MINUTE TACTICAL CYCLE",
            "Golden 72 Hours Response Compression\nInstant Triage Priority for NDRF / SDRF",
            "What traditionally takes hours of agonizing, dangerous foot searches across square kilometers of debris is compressed into a rapid sub-5-minute autonomous sortie from unboxing to casualty recovery.",
            TEAL_GREEN
        )
    ]

    for idx, (head, pill_txt, desc, col) in enumerate(cards_info):
        cy = Inches(1.15) + idx * (Inches(1.82) + Inches(0.19))
        c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, cy, rw, Inches(1.82))
        c.fill.solid()
        c.fill.fore_color.rgb = WHITE
        c.line.color.rgb = SLATE_200
        c.line.width = Pt(1)
        add_shape_shadow(c)

        # Left stripe
        st = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, cy, Inches(0.08), Inches(1.82))
        st.fill.solid()
        st.fill.fore_color.rgb = col
        st.line.fill.background()

        tf_c = c.text_frame
        tf_c.margin_left = Inches(0.22)
        tf_c.margin_right = Inches(0.2)
        tf_c.margin_top = Inches(0.14)
        tf_c.vertical_anchor = MSO_ANCHOR.TOP

        p0 = tf_c.paragraphs[0]
        r0 = p0.add_run()
        r0.text = head + "\n"
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = SLATE_900

        p1 = tf_c.add_paragraph()
        r1 = p1.add_run()
        r1.text = pill_txt + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = col

        p2 = tf_c.add_paragraph()
        r2 = p2.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = SLATE_600


def build_mission_pipeline_slide(prs):
    """Creative Slide: The End-to-End Autonomous Lifesaver Pipeline (5 Step Horizontal Chevrons)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_50
    bg.line.fill.background()

    add_header(
        slide,
        'OPERATIONAL PIPELINE · ZERO-CONNECTIVITY RECONNAISSANCE',
        'End-to-End Autonomous Reconnaissance & Survivor Extraction Flow',
        'RAPID SORTIE PIPELINE',
        ORANGE_HERO, ORANGE_LIGHT, ORANGE_BORDER
    )

    steps = [
        (
            "1. RAPID SORTIE LAUNCH",
            "< 3 Minutes Deployment",
            "Operator outlines 2 km² search polygon on offline tablet. UAV unboxes from rugged backpack and auto-launches.",
            ORANGE_HERO
        ),
        (
            "2. BOUSTROPHEDON SWEEP",
            "STM32U5 @ 250 Hz Loop",
            "Autonomous lawnmower search trajectory at 25-30m AGL. 1D ToF laser altimeter maintains terrain contour following.",
            SKY_BLUE
        ),
        (
            "3. 37°C THERMAL LOCK",
            "Qualcomm NPU (< 5W)",
            "Quantized INT8 YOLO model fuses daylight contours with radiometric 8-14μm body heat, spotting trapped survivors.",
            VIOLET
        ),
        (
            "4. 17-BYTE LORA BURST",
            "Souli et al. (Elsevier 2024)",
            "Tait-Bryan ray-caster projects pixel to WGS-84 pin. Lat/Long/Temp compressed into 17-byte HMAC-SHA256 packet.",
            SKY_BLUE
        ),
        (
            "5. SAFE ROUTE EXTRACTION",
            "Hazard-Aware Dijkstra",
            "Offline Ground Station instantly charts safe walking corridor bypassing 11kV wires directly to casualty.",
            TEAL_GREEN
        )
    ]

    cw = Inches(2.28)
    ch = Inches(5.6)
    gap = Inches(0.18)

    for i, (title, sub, body, accent) in enumerate(steps):
        cx = Inches(0.6) + i * (cw + gap)
        cy = Inches(1.25)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, cw, ch)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = SLATE_200
        card.line.width = Pt(1.2)
        add_shape_shadow(card)

        # Top Accent Header
        top_bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, cw, Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = accent
        top_bar.line.fill.background()

        # Step Number Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, cx + Inches(0.2), cy + Inches(0.25), Inches(0.52), Inches(0.52))
        badge.fill.solid()
        badge.fill.fore_color.rgb = accent
        badge.line.color.rgb = WHITE
        badge.line.width = Pt(1.5)
        tf_b = badge.text_frame
        tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_b = tf_b.paragraphs[0]
        p_b.alignment = PP_ALIGN.CENTER
        r_b = p_b.add_run()
        r_b.text = f"0{i+1}"
        r_b.font.bold = True
        r_b.font.size = Pt(13)
        r_b.font.color.rgb = WHITE

        tf = card.text_frame
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.95)
        tf.vertical_anchor = MSO_ANCHOR.TOP

        p1 = tf.paragraphs[0]
        r1 = p1.add_run()
        r1.text = title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = SLATE_900

        p2 = tf.add_paragraph()
        r2 = p2.add_run()
        r2.text = sub + "\n\n"
        r2.font.bold = True
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = accent

        p3 = tf.add_paragraph()
        r3 = p3.add_run()
        r3.text = body
        r3.font.size = Pt(9.5)
        r3.font.color.rgb = SLATE_600


def build_comparison_slide(prs):
    """Creative Slide: Traditional Ground Search vs. Phoenix X Autonomous Aerial Triage."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_50
    bg.line.fill.background()

    add_header(
        slide,
        'TACTICAL PARADIGM SHIFT · FIRST RESPONDER RESILIENCE',
        'Traditional Foot Search vs. Project Phoenix X Autonomous Triage',
        'OPERATIONAL IMPACT',
        ORANGE_HERO, ORANGE_LIGHT, ORANGE_BORDER
    )

    box_w = Inches(5.85)
    box_h = Inches(5.6)
    by = Inches(1.25)

    # Left: Traditional Foot Search (Problem / Failure)
    left_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), by, box_w, box_h)
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = WHITE
    left_card.line.color.rgb = RED_LIGHT
    left_card.line.width = Pt(1.5)
    add_shape_shadow(left_card)

    top_red = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), by, box_w, Inches(0.08))
    top_red.fill.solid()
    top_red.fill.fore_color.rgb = RED_ACCENT
    top_red.line.fill.background()

    tf_l = left_card.text_frame
    tf_l.margin_left = tf_l.margin_right = Inches(0.35)
    tf_l.margin_top = Inches(0.3)
    tf_l.vertical_anchor = MSO_ANCHOR.TOP

    p_lh = tf_l.paragraphs[0]
    r_lh = p_lh.add_run()
    r_lh.text = "TRADITIONAL DISASTER RECONNAISSANCE\n"
    r_lh.font.bold = True
    r_lh.font.size = Pt(13)
    r_lh.font.color.rgb = RED_ACCENT

    p_ls = tf_l.add_paragraph()
    r_ls = p_ls.add_run()
    r_ls.text = "Manual Foot Sweeps & Standard Visual Cameras\n\n"
    r_ls.font.size = Pt(10)
    r_ls.font.color.rgb = SLATE_500

    left_points = [
        ("❌ Blind Foot Patrols:", " Rescuers sweep unstable terrain on foot across square kilometers; takes 4 to 8 hours per sector."),
        ("❌ Darkness & Smoke Blockade:", " Operations halt at sunset; dust and thick smoke plumes completely blind standard optical cameras."),
        ("❌ Rescuer Secondary Casualties:", " Crews step blindly into severed 11kV live powerlines, gas leaks, and secondary mudslide slip planes."),
        ("❌ Cellular Infrastructure Collapse:", " Drones relying on 4G/5G mobile towers or Wi-Fi stream fail instantly when towers collapse.")
    ]
    for bold_txt, norm_txt in left_points:
        p = tf_l.add_paragraph()
        rb = p.add_run()
        rb.text = bold_txt
        rb.font.bold = True
        rb.font.size = Pt(10)
        rb.font.color.rgb = SLATE_900

        rn = p.add_run()
        rn.text = norm_txt + "\n\n"
        rn.font.size = Pt(10)
        rn.font.color.rgb = SLATE_600

    # Right: Project Phoenix X (The Solution)
    right_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.88), by, box_w, box_h)
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = WHITE
    right_card.line.color.rgb = TEAL_LIGHT
    right_card.line.width = Pt(1.5)
    add_shape_shadow(right_card)

    top_teal = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.88), by, box_w, Inches(0.08))
    top_teal.fill.solid()
    top_teal.fill.fore_color.rgb = TEAL_GREEN
    top_teal.line.fill.background()

    tf_r = right_card.text_frame
    tf_r.margin_left = tf_r.margin_right = Inches(0.35)
    tf_r.margin_top = Inches(0.3)
    tf_r.vertical_anchor = MSO_ANCHOR.TOP

    p_rh = tf_r.paragraphs[0]
    r_rh = p_rh.add_run()
    r_rh.text = "PROJECT PHOENIX X AUTONOMOUS TRIAGE\n"
    r_rh.font.bold = True
    r_rh.font.size = Pt(13)
    r_rh.font.color.rgb = TEAL_GREEN

    p_rs = tf_r.add_paragraph()
    r_rs = p_rs.add_run()
    r_rs.text = "Dual-Brain Tactical Edge AI & Long-Range Telemetry\n\n"
    r_rs.font.size = Pt(10)
    r_rs.font.color.rgb = SLATE_500

    right_points = [
        ("✓ Rapid Aerial Grid Sweep:", " Covers 2.0 km² in <15 minutes. Launches from backpack in under 3 minutes without infrastructure."),
        ("✓ 24/7 Radiometric Thermal Lock:", " Penetrates fog and darkness; locks living 37°C body heat through crevices using NETD < 50 mK LWIR."),
        ("✓ Automated Safe-Path Routing:", " Hazard-aware Dijkstra pathfinding calculates pedestrian extraction route avoiding live 11kV lines."),
        ("✓ 100% Offline 868 MHz LoRa Link:", " Souli et al. (Elsevier 2024) 17-byte binary bit-packing beams coordinates across 3–5 km reliably.")
    ]
    for bold_txt, norm_txt in right_points:
        p = tf_r.add_paragraph()
        rb = p.add_run()
        rb.text = bold_txt
        rb.font.bold = True
        rb.font.size = Pt(10)
        rb.font.color.rgb = SLATE_900

        rn = p.add_run()
        rn.text = norm_txt + "\n\n"
        rn.font.size = Pt(10)
        rn.font.color.rgb = SLATE_600


def build_index_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SLATE_900
    bg.line.fill.background()

    k = slide.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(10), Inches(0.3))
    tf_k = k.text_frame
    p_k = tf_k.paragraphs[0]
    r_k = p_k.add_run()
    r_k.text = "PHOENIX X · HARDWARE PRESENTATION GRAPHIC MASTER PACK"
    r_k.font.bold = True
    r_k.font.size = Pt(11)
    r_k.font.color.rgb = ORANGE_HERO

    t = slide.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.5), Inches(0.8))
    tf_t = t.text_frame
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = "Self-Explanatory Aerospace Infographics & Drone Renders"
    r_t.font.bold = True
    r_t.font.size = Pt(26)
    r_t.font.color.rgb = WHITE

    sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.75), Inches(11.5), Inches(0.4))
    tf_sub = sub.text_frame
    p_sub = tf_sub.paragraphs[0]
    r_sub = p_sub.add_run()
    r_sub.text = "A complete visual asset library for SIH26177: 3D product callouts, in-flight dual-beam perception, and NDRF tactical tablet routing."
    r_sub.font.size = Pt(12.5)
    r_sub.font.color.rgb = SLATE_200

    catalog = [
        ("SLIDE 2: HARDWARE SCHEMATIC", "Avionics & Compute Partition", "3D Studio render with 6 interactive numbered beacon pins.", SKY_BLUE),
        ("SLIDE 3: FEASIBILITY & SIZING", "Buildability & Legal Viability", "DGCA 1.58 kg AUW, Bouabdallah β ≥ 2.0 sizing, sub-5W compute.", TEAL_GREEN),
        ("SLIDE 4: IN-FLIGHT DUAL-BEAM", "Optical + Radiometric LWIR", "Hero in-action render: Cyan optical + orange 37°C thermal lock.", ORANGE_HERO),
        ("SLIDE 5: 5-MINUTE SORTIE PIPELINE", "Autonomous Mission Flow", "Horizontal 5-step chevron from unboxing to safe route.", VIOLET),
        ("SLIDE 6: FIRST RESPONDER GCS", "NDRF Tactical Tablet Field Action", "Hazard-aware Dijkstra safe rescue route around 11kV wires.", TEAL_GREEN),
        ("SLIDE 7: PARADIGM COMPARISON", "Foot Search vs. Phoenix X", "High-contrast split comparison proving operational disruption.", RED_ACCENT)
    ]

    card_w = Inches(3.68)
    card_h = Inches(2.2)
    gap_x = Inches(0.24)
    gap_y = Inches(0.2)

    for idx, (head, sub_t, desc, accent) in enumerate(catalog):
        c_idx = idx % 3
        r_idx = idx // 3
        cx = Inches(0.8) + c_idx * (card_w + gap_x)
        cy = Inches(2.45) + r_idx * (card_h + gap_y)

        c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, card_w, card_h)
        c.fill.solid()
        c.fill.fore_color.rgb = SLATE_800
        c.line.color.rgb = SLATE_700
        c.line.width = Pt(1.0)

        acc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, card_w, Inches(0.06))
        acc.fill.solid()
        acc.fill.fore_color.rgb = accent
        acc.line.fill.background()

        tf = c.text_frame
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.22)
        tf.vertical_anchor = MSO_ANCHOR.TOP

        p1 = tf.paragraphs[0]
        r1 = p1.add_run()
        r1.text = head + "\n"
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = accent

        p2 = tf.add_paragraph()
        r2 = p2.add_run()
        r2.text = sub_t + "\n\n"
        r2.font.bold = True
        r2.font.size = Pt(12.5)
        r2.font.color.rgb = WHITE

        p3 = tf.add_paragraph()
        r3 = p3.add_run()
        r3.text = desc
        r3.font.size = Pt(9.5)
        r3.font.color.rgb = SLATE_200


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    print("Generating Slide 1: Visual Asset Index...")
    build_index_slide(prs)

    print("Generating Slide 2: Hardware Subsystem Mapping (3D Studio Render)...")
    build_hardware_mapping_slide(prs, 'technical')

    print("Generating Slide 3: Feasibility & Sizing Laws...")
    build_hardware_mapping_slide(prs, 'feasibility')

    print("Generating Slide 4: In-Flight Dual-Beam Perception (Action Hero)...")
    build_dual_beam_action_slide(prs)

    print("Generating Slide 5: 5-Minute Lifesaver Operational Pipeline...")
    build_mission_pipeline_slide(prs)

    print("Generating Slide 6: First Responder GCS & Safe Route Tablet...")
    build_gcs_safe_route_slide(prs)

    print("Generating Slide 7: Traditional Search vs Phoenix X Comparison...")
    build_comparison_slide(prs)

    prs.save(OUT_PPTX)
    print(f"\n🎉 Successfully compiled 7-slide Creative Presentation Master Pack: {OUT_PPTX}")


if __name__ == '__main__':
    main()
