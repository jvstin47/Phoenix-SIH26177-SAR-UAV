import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Color Palette matching Team THULYA's winning style
    BG_LIGHT = RGBColor(248, 250, 252)       # Slate 50 (#F8FAFC)
    WHITE = RGBColor(255, 255, 255)
    DARK_HEADER = RGBColor(15, 23, 42)       # Slate 900
    TEXT_MAIN = RGBColor(30, 41, 59)         # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139)     # Slate 500
    BORDER_DEFAULT = RGBColor(226, 232, 240) # Slate 200

    # Accent Colors for Categories & Cards
    RED_ACCENT = RGBColor(225, 29, 72)       # Rose 600 (Problem / Warning)
    RED_BG = RGBColor(255, 241, 242)         # Rose 50
    RED_BORDER = RGBColor(254, 205, 211)     # Rose 200

    GREEN_ACCENT = RGBColor(13, 148, 136)    # Teal 600 (Solution / Success)
    GREEN_BG = RGBColor(240, 253, 250)       # Teal 50
    GREEN_BORDER = RGBColor(153, 246, 228)   # Teal 200

    PURPLE_ACCENT = RGBColor(124, 58, 237)   # Violet 600 (Innovation / Strategy)
    PURPLE_BG = RGBColor(245, 243, 255)      # Violet 50
    PURPLE_BORDER = RGBColor(221, 214, 254)  # Violet 200

    BLUE_ACCENT = RGBColor(2, 132, 199)      # Sky 600 (Technical / Feasibility)
    BLUE_BG = RGBColor(240, 249, 255)        # Sky 50
    BLUE_BORDER = RGBColor(186, 230, 253)    # Sky 200

    AMBER_ACCENT = RGBColor(217, 119, 6)     # Amber 600
    AMBER_BG = RGBColor(254, 243, 199)       # Amber 100
    AMBER_BORDER = RGBColor(253, 230, 138)   # Amber 200

    def draw_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_LIGHT
        bg.line.fill.background()
        return bg

    def add_slide_header(slide, title_text, slide_num_str):
        # Top banner with Team Logo placeholder, Title, and SIH Header
        # Team pill top-left
        team_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.35), Inches(1.8), Inches(0.55))
        team_pill.fill.solid()
        team_pill.fill.fore_color.rgb = WHITE
        team_pill.line.color.rgb = BORDER_DEFAULT
        team_pill.line.width = Pt(1)
        tf_t = team_pill.text_frame
        tf_t.text = "PHOENIX"
        tf_t.paragraphs[0].font.size = Pt(13)
        tf_t.paragraphs[0].font.bold = True
        tf_t.paragraphs[0].font.color.rgb = DARK_HEADER
        tf_t.paragraphs[0].alignment = PP_ALIGN.CENTER

        # Main Title in Center
        tb_title = slide.shapes.add_textbox(Inches(2.6), Inches(0.32), Inches(8.0), Inches(0.65))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_t = tf_title.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(20)
        p_t.font.bold = True
        p_t.font.color.rgb = DARK_HEADER
        p_t.alignment = PP_ALIGN.CENTER

        # SIH Branding top-right
        tb_sih = slide.shapes.add_textbox(Inches(10.8), Inches(0.3), Inches(2.0), Inches(0.65))
        tf_sih = tb_sih.text_frame
        p_sih = tf_sih.paragraphs[0]
        p_sih.text = "SMART INDIA\nHACKATHON 2026"
        p_sih.font.size = Pt(9.5)
        p_sih.font.bold = True
        p_sih.font.color.rgb = DARK_HEADER
        p_sih.alignment = PP_ALIGN.RIGHT

        # Bottom Subtitle Footer Bar
        f_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.15), Inches(13.333), Inches(0.35))
        f_bar.fill.solid()
        f_bar.fill.fore_color.rgb = DARK_HEADER
        f_bar.line.fill.background()
        tf_f = f_bar.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = f"PROJECT PHOENIX: Autonomous Multi-Spectral Edge-AI UAV  |  SIH26177 (Qualcomm Inc.)                                                                   Slide {slide_num_str}"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = WHITE
        p_f.alignment = PP_ALIGN.CENTER

    def add_card(slide, left, top, width, height, bg=WHITE, border=BORDER_DEFAULT, corner_radius=None):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg
        shape.line.color.rgb = border
        shape.line.width = Pt(1.2)
        return shape

    def add_badge(slide, left, top, width, height, text, bg=RED_BG, border=RED_BORDER, text_color=RED_ACCENT):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg
        shape.line.color.rgb = border
        shape.line.width = Pt(1)
        tf = shape.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER
        return shape

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Clean THULYA Style)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    draw_bg(s1)

    # Top SIH Header
    t_hdr = s1.shapes.add_textbox(Inches(1.0), Inches(0.6), Inches(11.333), Inches(0.8))
    tf1 = t_hdr.text_frame
    p = tf1.paragraphs[0]
    p.text = "SMART INDIA HACKATHON 2026"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = DARK_HEADER
    p.alignment = PP_ALIGN.CENTER

    p_sub = tf1.add_paragraph()
    p_sub.text = "HARDWARE EDITION  |  MINISTRY OF EDUCATION & QUALCOMM INC."
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = AMBER_ACCENT
    p_sub.alignment = PP_ALIGN.CENTER

    # Main Card Center
    main_card = add_card(s1, Inches(1.5), Inches(1.8), Inches(10.333), Inches(4.8), bg=WHITE, border=BORDER_DEFAULT)

    # Left: Metadata Details
    meta_box = s1.shapes.add_textbox(Inches(1.9), Inches(2.1), Inches(6.0), Inches(4.2))
    tf_meta = meta_box.text_frame
    tf_meta.word_wrap = True

    items = [
        ("Problem Statement ID", "SIH26177"),
        ("Problem Statement Title", "A deployable AI-powered autonomous drone that aids search-and-rescue operations by detecting people and hazards, thereby improving responder safety and reducing victim discovery time."),
        ("Sponsoring Organization", "Qualcomm Inc."),
        ("Theme", "Robotics and Drones"),
        ("Category", "Hardware"),
        ("Team Name", "Team Phoenix"),
        ("Team Specialization", "CSE + AI & Data Science + Cyber Security (2nd Year Undergrads)")
    ]

    for idx, (label, val) in enumerate(items):
        p_item = tf_meta.paragraphs[0] if idx == 0 else tf_meta.add_paragraph()
        run_lbl = p_item.add_run()
        run_lbl.text = f"• {label}: "
        run_lbl.font.bold = True
        run_lbl.font.size = Pt(11.5)
        run_lbl.font.color.rgb = DARK_HEADER

        run_val = p_item.add_run()
        run_val.text = val
        run_val.font.size = Pt(11)
        run_val.font.color.rgb = TEXT_MAIN
        p_item.space_after = Pt(8)

    # Right: Hero Illustration Box
    right_card = add_card(s1, Inches(8.2), Inches(2.1), Inches(3.2), Inches(4.2), bg=BLUE_BG, border=BLUE_BORDER)
    r_box = s1.shapes.add_textbox(Inches(8.4), Inches(2.4), Inches(2.8), Inches(3.6))
    r_tf = r_box.text_frame
    r_tf.word_wrap = True
    p = r_tf.paragraphs[0]
    p.text = "PROJECT PHOENIX\nSAR UAV"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = BLUE_ACCENT; p.alignment = PP_ALIGN.CENTER; p.space_after = Pt(12)
    p = r_tf.add_paragraph()
    p.text = "Dual-Brain Edge-AI Scout for Zero-Infrastructure Disaster Reconnaissance\n\n" \
             "✓ Qualcomm Dragonwing QRB2210\n" \
             "✓ STM32U5 Zephyr RTOS Flight\n" \
             "✓ Dual RGB + Thermal Fusion\n" \
             "✓ 3-5 km LoRa Telemetry\n" \
             "✓ Tait-Bryan Ray-Casting GPS"
    p.font.size = Pt(10.5); p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & PROPOSED SOLUTION (THULYA Slide 2 Style)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    draw_bg(s2)
    add_slide_header(s2, "Disaster Reconnaissance & Emergency Survivor Triage", "2")

    # Top Left: Problem Statement Card (Red Badge)
    add_card(s2, Inches(0.6), Inches(1.1), Inches(5.9), Inches(2.5), bg=WHITE, border=RED_BORDER)
    add_badge(s2, Inches(0.8), Inches(1.25), Inches(1.8), Inches(0.32), "PROBLEM STATEMENT", bg=RED_BG, border=RED_BORDER, text_color=RED_ACCENT)
    
    tb = s2.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(5.5), Inches(1.85))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "During catastrophic events (e.g. Wayanad landslides, earthquakes), first responders encounter critical operational bottlenecks:"
    p.font.size = Pt(10.5); p.font.bold = True; p.font.color.rgb = DARK_HEADER; p.space_after = Pt(6)
    p = tf.add_paragraph()
    p.text = "• Comms Blackout: Cellular towers & power grids severed; cloud-AI drones are 100% inoperable.\n" \
             "• Environmental Blindness: Mud slush, fog, and darkness camouflage trapped survivors.\n" \
             "• High Mortality Curve: The 'Golden 72 Hours' expire before slow manual foot sweeps cover rubble.\n" \
             "• Responder Hazards: Crews walk blindly into secondary cave-ins, gas leaks, and live cables."
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # Top Right: Proposed Solution Card (Teal Badge)
    add_card(s2, Inches(6.8), Inches(1.1), Inches(5.9), Inches(2.5), bg=WHITE, border=GREEN_BORDER)
    add_badge(s2, Inches(7.0), Inches(1.25), Inches(1.8), Inches(0.32), "PROPOSED SOLUTION", bg=GREEN_BG, border=GREEN_BORDER, text_color=GREEN_ACCENT)
    
    tb = s2.shapes.add_textbox(Inches(7.0), Inches(1.65), Inches(5.5), Inches(1.85))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Project Phoenix: An autonomous, field-deployable multirotor scout engineered for offline disaster zones:"
    p.font.size = Pt(10.5); p.font.bold = True; p.font.color.rgb = DARK_HEADER; p.space_after = Pt(6)
    p = tf.add_paragraph()
    p.text = "• 100% On-Device Edge AI: Executes real-time vision on Qualcomm silicon without internet.\n" \
             "• Multi-Spectral Vision: Fuses 4K RGB with LWIR Thermal (8-14μm) to spot living body heat (37°C).\n" \
             "• Tait-Bryan Ray-Casting: Calculates victim Lat/Long GPS coordinates instantly from altitude.\n" \
             "• Offline Tactical GCS: Streams priority triage queues and safe rescue routes to local tablets."
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # Middle: Innovation / Uniqueness Strip (5 Rounded Pills)
    add_badge(s2, Inches(0.6), Inches(3.75), Inches(2.2), Inches(0.3), "INNOVATION / UNIQUENESS", bg=PURPLE_BG, border=PURPLE_BORDER, text_color=PURPLE_ACCENT)
    
    innovations = [
        ("Dual-Brain Architecture", "Arduino UNO Q combining Qualcomm QRB2210 MPU + STM32U5 MCU in 40g."),
        ("Sub-5W Edge YOLO", "INT8 quantized neural model running on NPU; preserves 90% power for flight."),
        ("Ray-Cast Geolocation", "Tait-Bryan rotation matrix projects bounding boxes to ground GPS pins."),
        ("ROS-LoRa P2P Bridge", "17-byte bit-packed telemetry stream over 5+ km (Souli et al., Elsevier 2024)."),
        ("Anti-Compass Drift VIO", "Visual Odometry heading overrides magnetometer in steel rubble (Bouabdallah 2007).")
    ]
    pill_w = Inches(2.3)
    for idx, (title, desc) in enumerate(innovations):
        x_pos = Inches(0.6 + idx * 2.45)
        add_card(s2, x_pos, Inches(4.15), pill_w, Inches(1.3), bg=WHITE, border=PURPLE_BORDER)
        tb_p = s2.shapes.add_textbox(x_pos + Inches(0.08), Inches(4.2), pill_w - Inches(0.16), Inches(1.2))
        tf_p = tb_p.text_frame; tf_p.word_wrap = True
        p = tf_p.paragraphs[0]
        p.text = title
        p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = PURPLE_ACCENT; p.space_after = Pt(2)
        p = tf_p.add_paragraph()
        p.text = desc
        p.font.size = Pt(8.5); p.font.color.rgb = TEXT_MAIN

    # Bottom: Current Approach vs. Phoenix Approach Comparison Bar
    add_card(s2, Inches(0.6), Inches(5.6), Inches(5.9), Inches(1.4), bg=RED_BG, border=RED_BORDER)
    tb = s2.shapes.add_textbox(Inches(0.8), Inches(5.65), Inches(5.5), Inches(1.3))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "TRADITIONAL DISASTER SEARCH (Current Approach)"
    p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = RED_ACCENT; p.space_after = Pt(2)
    p = tf.add_paragraph()
    p.text = "Manual Foot Sweeps ➔ Blind Rubble Digging ➔ Stalled at Sunset (Darkness) ➔ High Responder Casualty Risk ➔ Critical Hours Lost"
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    add_card(s2, Inches(6.8), Inches(5.6), Inches(5.9), Inches(1.4), bg=GREEN_BG, border=GREEN_BORDER)
    tb = s2.shapes.add_textbox(Inches(7.0), Inches(5.65), Inches(5.5), Inches(1.3))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "PHOENIX AUTONOMOUS SAR (Our Approach)"
    p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = GREEN_ACCENT; p.space_after = Pt(2)
    p = tf.add_paragraph()
    p.text = "Autonomous Aerial Sweep ➔ 24/7 Thermal Night Vision ➔ Instant Survivor GPS Raycasting ➔ Zero-Drop LoRa Telemetry ➔ Safe Responder Path Routing"
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH (THULYA Slide 3 Style)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    draw_bg(s3)
    add_slide_header(s3, "Technical Approach: Dual-Brain Architecture & Workflow", "3")

    # Left Column: Implementation Workflow (6 Numbered Steps)
    add_card(s3, Inches(0.6), Inches(1.1), Inches(6.8), Inches(5.9), bg=WHITE, border=BORDER_DEFAULT)
    add_badge(s3, Inches(0.8), Inches(1.25), Inches(2.4), Inches(0.32), "IMPLEMENTATION WORKFLOW", bg=BLUE_BG, border=BLUE_BORDER, text_color=BLUE_ACCENT)

    tb_flow = s3.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(6.4), Inches(5.2))
    tf_flow = tb_flow.text_frame; tf_flow.word_wrap = True

    steps = [
        ("1. Sector Partition & Launch", "Operator selects 2 km² search polygon on offline tablet; UAV launches in < 3 minutes."),
        ("2. Autonomous Grid Sweep", "Executes Boustrophedon lawnmower coverage flight powered by STM32U5 / Zephyr RTOS at 250 Hz."),
        ("3. Multi-Spectral Perception", "Dual 4K RGB + LWIR Thermal cameras co-register frames; edge YOLO extracts human heat contours."),
        ("4. Ray-Cast Geolocation", "Tait-Bryan DCM matrix converts bounding box center + LiDAR altitude into real-world Lat/Long."),
        ("5. Binary LoRa Packet Burst", "Souli et al. (2024) protocol packs survivor coordinates into 17-byte binary frame; broadcasts over 5+ km."),
        ("6. GCS Triage & Route Planning", "Ground station ranks victims by body temperature urgency; Dijkstra algorithm charts hazard-free ground route.")
    ]

    for idx, (step_t, step_d) in enumerate(steps):
        p = tf_flow.paragraphs[0] if idx == 0 else tf_flow.add_paragraph()
        run_num = p.add_run()
        run_num.text = f"{step_t}\n"
        run_num.font.bold = True
        run_num.font.size = Pt(10.5)
        run_num.font.color.rgb = BLUE_ACCENT

        run_desc = p.add_run()
        run_desc.text = f"{step_d}\n"
        run_desc.font.size = Pt(9)
        run_desc.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # Right Column Top: System Architecture Diagram
    add_card(s3, Inches(7.6), Inches(1.1), Inches(5.1), Inches(3.2), bg=WHITE, border=BORDER_DEFAULT)
    add_badge(s3, Inches(7.8), Inches(1.25), Inches(2.0), Inches(0.32), "SYSTEM ARCHITECTURE", bg=PURPLE_BG, border=PURPLE_BORDER, text_color=PURPLE_ACCENT)

    tb_arch = s3.shapes.add_textbox(Inches(7.8), Inches(1.65), Inches(4.7), Inches(2.5))
    tf_arch = tb_arch.text_frame; tf_arch.word_wrap = True
    p = tf_arch.paragraphs[0]
    p.text = "Dual-Brain Hardware Split (Arduino UNO Q):\n" \
             "• Real-Time MCU (STM32U585 / Zephyr RTOS):\n" \
             "  - 250 Hz (4ms) deterministic flight stabilization loop\n" \
             "  - 350 Hz PWM direct brushless motor control\n" \
             "  - IMU (MPU6050) + Barometer (MS5611) + Downward LiDAR\n\n" \
             "• Mission Computer (Qualcomm Dragonwing QRB2210 / Linux):\n" \
             "  - Asynchronous non-blocking RPC bridge (zero flight jitter)\n" \
             "  - INT8 YOLO Edge AI + Optical-to-Ground Ray-Caster\n" \
             "  - Semtech SX1262 LoRa Telemetry Driver (868 MHz)"
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # Right Column Bottom: Tech Stack Badges
    add_card(s3, Inches(7.6), Inches(4.5), Inches(5.1), Inches(2.5), bg=WHITE, border=BORDER_DEFAULT)
    add_badge(s3, Inches(7.8), Inches(4.65), Inches(1.4), Inches(0.32), "TECH STACK", bg=GREEN_BG, border=GREEN_BORDER, text_color=GREEN_ACCENT)

    tb_tech = s3.shapes.add_textbox(Inches(7.8), Inches(5.05), Inches(4.7), Inches(1.8))
    tf_tech = tb_tech.text_frame; tf_tech.word_wrap = True
    p = tf_tech.paragraphs[0]
    p.text = "• Flight Stack: Zephyr RTOS, YMFC-32 Core, PX4 Autopilot\n" \
             "• Edge AI & Vision: Qualcomm SNPE, ONNX Runtime INT8, OpenCV\n" \
             "• Robotics Middleware: ROS2 Humble, MAVLink v2, micro-ROS\n" \
             "• Long-Range RF Comms: Semtech SX1262 LoRa P2P (868 MHz)\n" \
             "• Tactical GCS: React, Leaflet, Tailwind CSS, WebSockets\n" \
             "• Security: HMAC-SHA256 Telemetry Packet Signatures"
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 4: FEASIBILITY AND VIABILITY (THULYA Slide 4 Style)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    draw_bg(s4)
    add_slide_header(s4, "Feasibility, Challenges-to-Strategies & Market Viability", "4")

    col_w = Inches(3.85)
    col_h = Inches(5.9)

    # Column 1: Feasibility
    add_card(s4, Inches(0.6), Inches(1.1), col_w, col_h, bg=WHITE, border=BLUE_BORDER)
    add_badge(s4, Inches(0.8), Inches(1.25), Inches(1.5), Inches(0.32), "FEASIBILITY", bg=BLUE_BG, border=BLUE_BORDER, text_color=BLUE_ACCENT)
    tb = s4.shapes.add_textbox(Inches(0.8), Inches(1.7), col_w - Inches(0.4), col_h - Inches(0.7))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "TECHNICAL FEASIBILITY\n" \
             "• Bouabdallah Sizing Laws: 38% battery mass fraction, β ≥ 2.0 thrust-to-weight ratio.\n" \
             "• Total All-Up-Weight: 1.58 kg (Comfortably under DGCA 2.0 kg Micro Category).\n" \
             "• Sub-5W Compute: Qualcomm NPU preserves 90% power for rotor propulsion.\n\n" \
             "OPERATIONAL FEASIBILITY\n" \
             "• Setup Time: < 3 minutes from rugged backpack unboxing to flight.\n" \
             "• Quick-Swap Battery: Dual 4S LiPo tray for continuous sortie coverage.\n\n" \
             "FINANCIAL FEASIBILITY\n" \
             "• Bill of Materials: ₹85,000 – ₹1,40,000 per operational unit (1/8th of commercial enterprise drones)."
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # Column 2: Challenges -> Strategies
    add_card(s4, Inches(4.75), Inches(1.1), col_w, col_h, bg=WHITE, border=PURPLE_BORDER)
    add_badge(s4, Inches(4.95), Inches(1.25), Inches(2.2), Inches(0.32), "CHALLENGES ➔ STRATEGIES", bg=PURPLE_BG, border=PURPLE_BORDER, text_color=PURPLE_ACCENT)
    tb = s4.shapes.add_textbox(Inches(4.95), Inches(1.7), col_w - Inches(0.4), col_h - Inches(0.7))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Comms Blackout in Canyons\n" \
             "   ➔ Strategy: Raw LoRa P2P 868MHz packet burst (Souli et al., Elsevier 2024).\n\n" \
             "2. Smoke, Mud Slush & Darkness\n" \
             "   ➔ Strategy: Dual-band 8-14μm LWIR Thermal fusion spots living 37°C body heat.\n\n" \
             "3. Rubble Steel Magnetometer Distortion\n" \
             "   ➔ Strategy: Visual Inertial Odometry (VIO) overrides compass in magnetic fields.\n\n" \
             "4. Propeller Vibration Sensor Noise\n" \
             "   ➔ Strategy: Zero-pitching-moment airfoils (NASA TM-4741) + silicone mounts.\n\n" \
             "5. Actuator Saturation in Gusts\n" \
             "   ➔ Strategy: Anti-windup integrator clamping (Bouabdallah Algorithm 2)."
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # Column 3: Viability
    add_card(s4, Inches(8.9), Inches(1.1), col_w, col_h, bg=WHITE, border=GREEN_BORDER)
    add_badge(s4, Inches(9.1), Inches(1.25), Inches(1.4), Inches(0.32), "VIABILITY", bg=GREEN_BG, border=GREEN_BORDER, text_color=GREEN_ACCENT)
    tb = s4.shapes.add_textbox(Inches(9.1), Inches(1.7), col_w - Inches(0.4), col_h - Inches(0.7))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "ECONOMIC VIABILITY\n" \
             "• Enterprise Drone Disruption: DJI Matrice 30T costs ₹12-14 Lakhs. Phoenix costs ₹1.2 Lakh.\n" \
             "• Fleet Scalability: 1 NDRF battalion can deploy a swarm of 5 Phoenix UAVs for the price of 1 commercial drone.\n\n" \
             "NATIONAL DATA SOVEREIGNTY\n" \
             "• 100% Air-Gapped: Zero telemetry leaked to foreign cloud servers; adheres to Indian Defense & Home Ministry cyber norms.\n\n" \
             "DEPLOYMENT ECOSYSTEM\n" \
             "• Seamless integration into state disaster management authorities (NDRF, SDRF, Indian Army disaster columns)."
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 5: IMPACT AND BENEFITS (THULYA Slide 5 Style)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    draw_bg(s5)
    add_slide_header(s5, "Mission Impact & Multi-Stakeholder Benefits", "5")

    # 4 Stakeholder Cards across top
    stake_w = Inches(2.8)
    stake_h = Inches(4.1)

    stakeholders = [
        ("TRAPPED VICTIMS", GREEN_BG, GREEN_BORDER, GREEN_ACCENT,
         "• Located in Golden 72h window\n• Discovered through mud & debris\n• Rapid medical triage prioritization\n• Maximized chances of survival"),
        ("NDRF / SDRF TEAMS", BLUE_BG, BLUE_BORDER, BLUE_ACCENT,
         "• Advance hazard mapping\n• Avoid live cables & gas leaks\n• Automated safe-route navigation\n• Reduced physical rescuer fatigue"),
        ("DISASTER AUTHORITIES", PURPLE_BG, PURPLE_BORDER, PURPLE_ACCENT,
         "• Unified local tactical map\n• Real-time survivor count & coords\n• Zero dependency on cell towers\n• Dynamic search sector logging"),
        ("DISTRICT GOVERNANCE", AMBER_BG, AMBER_BORDER, AMBER_ACCENT,
         "• Efficient resource allocation\n• Targeted airlift & medical drops\n• Post-disaster audit trails\n• Affordable procurement at scale")
    ]

    for idx, (title, bg, border, accent, text) in enumerate(stakeholders):
        x_pos = Inches(0.6 + idx * 3.05)
        add_card(s5, x_pos, Inches(1.1), stake_w, stake_h, bg=WHITE, border=border)
        add_badge(s5, x_pos + Inches(0.15), Inches(1.25), stake_w - Inches(0.3), Inches(0.32), title, bg=bg, border=border, text_color=accent)
        tb = s5.shapes.add_textbox(x_pos + Inches(0.15), Inches(1.75), stake_w - Inches(0.3), stake_h - Inches(0.75))
        tf = tb.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(10); p.font.color.rgb = TEXT_MAIN

    # Bottom Impact Chevron Flow (THULYA Slide 5 Bottom Bar)
    add_card(s5, Inches(0.6), Inches(5.4), Inches(12.133), Inches(1.5), bg=WHITE, border=BORDER_DEFAULT)
    add_badge(s5, Inches(0.8), Inches(5.55), Inches(1.8), Inches(0.28), "IMPACT PIPELINE", bg=BLUE_BG, border=BLUE_BORDER, text_color=BLUE_ACCENT)

    flow_box = s5.shapes.add_textbox(Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.85))
    tf_fl = flow_box.text_frame; tf_fl.word_wrap = True
    p = tf_fl.paragraphs[0]
    p.text = "RAPID UNBOXING (<3 min)   ➔   AUTONOMOUS THERMAL SWEEP   ➔   EXACT GPS RAY-CASTING   ➔   ZERO-DROP LORA BEACON   ➔   MAXIMIZED LIVES SAVED"
    p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = GREEN_ACCENT; p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 6: RESEARCH FOUNDATIONS & PROTOTYPE (THULYA Slide 6 Style)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    draw_bg(s6)
    add_slide_header(s6, "Academic Research Foundations & Prototype Verification", "6")

    # Left: Research Foundations Card
    add_card(s6, Inches(0.6), Inches(1.1), Inches(6.0), Inches(5.9), bg=WHITE, border=BORDER_DEFAULT)
    add_badge(s6, Inches(0.8), Inches(1.25), Inches(2.2), Inches(0.32), "RESEARCH & REFERENCES", bg=BLUE_BG, border=BLUE_BORDER, text_color=BLUE_ACCENT)

    tb_ref = s6.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(5.6), Inches(5.1))
    tf_ref = tb_ref.text_frame; tf_ref.word_wrap = True

    refs = [
        ("1. Dr. Samir Bouabdallah (EPFL Thesis 3727, 2007)", 
         "• 'Design and Control of Quadrotors with Application to Autonomous Flying'\n• Sourced 12-state rigid-body dynamics, 90/10 electrical power rule, and anti-windup integrator."),
        ("2. Souli, Karatzia, Kolios, Ellinas (Elsevier, 2024)", 
         "• 'Mission-critical UAV swarm coordination using integrated ROS-LoRa architecture' (Computer Communications, Vol. 225)\n• Sourced 17-byte binary bit-packing & P2P LoRa telemetry."),
        ("3. NASA Technical Memorandum 4741 (NASA Langley, 1996)", 
         "• 'Computer Program To Obtain Ordinates for NACA Airfoils'\n• Sourced zero-pitching-moment (Cm=0) reflexed airfoil theory to eliminate blade flutter and IMU noise."),
        ("4. JRFCQAI Dual-Brain Platform (Ravi Butani, 2024)", 
         "• 'Dual-Brain Physical AI Flight Controller on Arduino UNO Q'\n• Established Zephyr RTOS + Debian Linux on Qualcomm QRB2210.")
    ]

    for idx, (rtitle, rdesc) in enumerate(refs):
        p = tf_ref.paragraphs[0] if idx == 0 else tf_ref.add_paragraph()
        run_t = p.add_run()
        run_t.text = f"{rtitle}\n"
        run_t.font.bold = True
        run_t.font.size = Pt(10)
        run_t.font.color.rgb = DARK_HEADER

        run_d = p.add_run()
        run_d.text = f"{rdesc}\n"
        run_d.font.size = Pt(8.5)
        run_d.font.color.rgb = TEXT_MAIN
        p.space_after = Pt(4)

    # Right: Prototype Card with QR code placeholder and UI mockups
    add_card(s6, Inches(6.9), Inches(1.1), Inches(5.8), Inches(5.9), bg=WHITE, border=BORDER_DEFAULT)
    add_badge(s6, Inches(7.1), Inches(1.25), Inches(1.6), Inches(0.32), "PROTOTYPE PROOF", bg=GREEN_BG, border=GREEN_BORDER, text_color=GREEN_ACCENT)

    tb_proto = s6.shapes.add_textbox(Inches(7.1), Inches(1.65), Inches(5.4), Inches(5.1))
    tf_pr = tb_proto.text_frame; tf_pr.word_wrap = True

    p = tf_pr.paragraphs[0]
    p.text = "OPEN-SOURCE REPOSITORY & VERIFICATION ASSETS"
    p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_HEADER; p.space_after = Pt(6)

    p = tf_pr.add_paragraph()
    p.text = "• Official GitHub Repository:\n" \
             "  https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV\n\n" \
             "• Documented Subsystems:\n" \
             "  1. docs/bouabdallah_quadrotor_research_findings.md\n" \
             "  2. docs/ros_lora_mission_critical_uav_swarm_research.md\n" \
             "  3. docs/aerodynamic_airfoil_considerations.md\n" \
             "  4. presentation/sih_presentation_outline.md\n\n" \
             "• Prototype Architecture Deliverables:\n" \
             "  - Live Web GCS Tactical Dashboard (React + Leaflet)\n" \
             "  - Multi-Spectral Dual Stream (RGB + LWIR Thermal HUD)\n" \
             "  - LoRa 17-Byte Binary Bit-Packing Serialization Module\n" \
             "  - Ray-Casting Geolocation Python Engine"
    p.font.size = Pt(9.5); p.font.color.rgb = TEXT_MAIN

    out_file = "/Users/justin/.gemini/antigravity/scratch/Phoenix-SIH26177-SAR-UAV/presentation/Team_Phoenix_SIH26177_Official_Deck.pptx"
    prs.save(out_file)
    print(f"Deck successfully generated and saved to: {out_file}")

if __name__ == "__main__":
    build_deck()
