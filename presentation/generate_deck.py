import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_sih_deck(output_path):
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    DARK_BLUE = RGBColor(15, 23, 42)      # #0F172A Slate 900
    NAVY = RGBColor(30, 41, 59)           # #1E293B Slate 800
    AMBER = RGBColor(245, 158, 11)        # #F59E0B Amber 500
    LIGHT_BG = RGBColor(248, 250, 252)    # #F8FAFC Slate 50
    CARD_BG = RGBColor(255, 255, 255)     # White
    TEXT_DARK = RGBColor(30, 41, 59)
    TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500
    BORDER_COLOR = RGBColor(226, 232, 240)# Slate 200
    ACCENT_BLUE = RGBColor(37, 99, 235)   # Blue 600

    def add_header(slide, title_text, category_text="SMART INDIA HACKATHON 2026 | PROBLEM STATEMENT ID: SIH26177"):
        # Top bar
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = AMBER
        p_cat.space_after = Pt(4)

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = DARK_BLUE

        # Bottom accent line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.45), Inches(11.7), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = AMBER
        line.line.color.rgb = AMBER

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        return shape

    # =========================================================================
    # SLIDE 1: COVER SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = DARK_BLUE
    bg1.line.fill.background()

    # Title Box
    t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(3.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "SMART INDIA HACKATHON 2026 | HARDWARE EDITION"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = AMBER
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "PROJECT PHOENIX: AUTONOMOUS SEARCH & RESCUE UAV"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(8)

    p2 = tf1.add_paragraph()
    p2.text = "Deployable Multi-Spectral Edge-AI Drone for Rapid Victim Localization & Hazard Reconnaissance in Communication-Denied Disasters"
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(203, 213, 225)

    # Details Card on Slide 1
    c1 = add_card(slide1, Inches(1.0), Inches(4.5), Inches(11.3), Inches(2.2), bg_color=NAVY, border_color=AMBER)
    dt_box = slide1.shapes.add_textbox(Inches(1.3), Inches(4.7), Inches(10.7), Inches(1.8))
    dt_tf = dt_box.text_frame
    dt_tf.word_wrap = True

    dp1 = dt_tf.paragraphs[0]
    dp1.text = "• Problem Statement ID: SIH26177  |  Theme: Robotics and Drones  |  Category: Hardware"
    dp1.font.size = Pt(14)
    dp1.font.bold = True
    dp1.font.color.rgb = RGBColor(255, 255, 255)
    dp1.space_after = Pt(6)

    dp2 = dt_tf.add_paragraph()
    dp2.text = "• Sponsoring Organization: Qualcomm Inc."
    dp2.font.size = Pt(14)
    dp2.font.bold = True
    dp2.font.color.rgb = AMBER
    dp2.space_after = Pt(6)

    dp3 = dt_tf.add_paragraph()
    dp3.text = "• Team Name: Team Phoenix  |  Domain: CSE + AI & Data Science + Cyber Security (2nd Year Undergraduates)"
    dp3.font.size = Pt(14)
    dp3.font.color.rgb = RGBColor(226, 232, 240)

    # =========================================================================
    # SLIDE 2: THE PROBLEM (GROUND REALITY & CONTEXT)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "The Critical Need: Disaster Reconnaissance in the 'Golden 72 Hours'")

    # 3 Cards for Problem Breakdown
    card_w = Inches(3.64)
    card_h = Inches(5.2)

    # Problem Card 1
    add_card(slide2, Inches(0.8), Inches(1.7), card_w, card_h)
    tb = slide2.shapes.add_textbox(Inches(1.0), Inches(1.9), card_w - Inches(0.4), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Communication Blackout"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_BLUE; p.space_after = Pt(10)
    p = tf.add_paragraph()
    p.text = "• Severe Disconnection: Earthquakes, landslides (e.g. Wayanad 2024), and floods instantly sever 4G/5G mobile towers and electrical grids.\n\n• Cloud-AI Fails: Standard consumer drones rely on cellular telemetry or cloud processing, rendering them completely blind and inoperable in the disaster epicentre.\n\n• First Responder Disconnect: Ground crews operate with zero real-time situational awareness."
    p.font.size = Pt(13); p.font.color.rgb = TEXT_DARK

    # Problem Card 2
    add_card(slide2, Inches(4.84), Inches(1.7), card_w, card_h)
    tb = slide2.shapes.add_textbox(Inches(5.04), Inches(1.9), card_w - Inches(0.4), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2. Environmental Occlusion"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_BLUE; p.space_after = Pt(10)
    p = tf.add_paragraph()
    p.text = "• Slush, Smoke & Darkness: Debris, thick rain clouds, and smoke plumes camouflage survivors from ordinary visual (RGB) aerial cameras.\n\n• Night Stoppage: Search operations are traditionally halted at sunset when optical visibility drops to zero, wasting crucial survival hours.\n\n• The Rubble Trap: Survivors trapped under light sheet debris remain invisible to human spotters."
    p.font.size = Pt(13); p.font.color.rgb = TEXT_DARK

    # Problem Card 3
    add_card(slide2, Inches(8.88), Inches(1.7), card_w, card_h)
    tb = slide2.shapes.add_textbox(Inches(9.08), Inches(1.9), card_w - Inches(0.4), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "3. Responder Hazard & Latency"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_BLUE; p.space_after = Pt(10)
    p = tf.add_paragraph()
    p.text = "• High Mortality Curve: Victim survival drops precipitously after the first 72 hours; manual foot sweeps take days to cover a 2 km² disaster area.\n\n• Secondary Disasters: Responders walk blindly into secondary hazards: active gas leaks, submerged live powerlines, and unstable structural slopes.\n\n• Solution Mandate: Need rapid autonomous aerial triage before deploying ground rescuers."
    p.font.size = Pt(13); p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 3: PROPOSED SOLUTION & INNOVATION
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Proposed Solution: Project Phoenix Autonomous SAR UAV")

    # 2 Big Columns: Left = Core Solution, Right = Technical Innovations
    col_w = Inches(5.65)
    col_h = Inches(5.2)

    # Solution Left Column
    add_card(slide3, Inches(0.8), Inches(1.7), col_w, col_h)
    tb = slide3.shapes.add_textbox(Inches(1.0), Inches(1.9), col_w - Inches(0.4), col_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Core Solution Overview"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = DARK_BLUE; p.space_after = Pt(10)
    p = tf.add_paragraph()
    p.text = "Project Phoenix is a deployable autonomous multirotor UAV designed to act as an offline-first aerial reconnaissance scout for NDRF and SDRF teams:\n\n" \
             "• 100% Onboard Edge Intelligence: Operates without internet, cellular connectivity, or external cloud infrastructure.\n\n" \
             "• Multi-Spectral Vision Core: Co-registered RGB + Long-Wave Infrared (LWIR) thermal sensors detect living human body heat signatures (36°C-38°C) through smoke, mud, and total night darkness.\n\n" \
             "• Tait-Bryan Ray-Casting Geolocation: Instantly converts 2D bounding boxes into real-world GPS coordinates without hovering overhead.\n\n" \
             "• Offline Responder GCS: Displays live victim pins, hazard heatmaps, and shortest hazard-free ground rescue routes on a local tablet."
    p.font.size = Pt(13); p.font.color.rgb = TEXT_DARK

    # Innovations Right Column
    add_card(slide3, Inches(6.85), Inches(1.7), col_w, col_h)
    tb = slide3.shapes.add_textbox(Inches(7.05), Inches(1.9), col_w - Inches(0.4), col_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Key Technical Innovations"
    p.font.size = Pt(18); p.font.bold = True; p.font.color.rgb = AMBER; p.space_after = Pt(10)
    p = tf.add_paragraph()
    p.text = "• Dual-Brain Architecture on Single Board:\n" \
             "  Powered by the Arduino UNO Q integrating the Qualcomm Dragonwing™ QRB2210 Linux MPU with an STM32U585 Real-Time MCU (replaces both flight controller & companion computer in 40g).\n\n" \
             "• Sub-5W Edge Deep Learning:\n" \
             "  INT8-quantized YOLO model running on the Qualcomm NPU; complies with Bouabdallah's 90/10 power rule (actuators consume 90%, compute draws < 10%).\n\n" \
             "• Dual-Tier Resilient Telemetry:\n" \
             "  High-bandwidth Wi-Fi mesh for nearby video + ultra-reliable LoRa (868 MHz) emergency beacon transmitting coordinates over 5+ km.\n\n" \
             "• Anti-Compass Drift Heading:\n" \
             "  Visual-Inertial Odometry overrides magnetometers in steel rubble."
    p.font.size = Pt(13); p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 4: TECHNICAL ARCHITECTURE & WORKFLOW
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Technical Architecture: The Dual-Brain Edge Pipeline")

    # 4 Workflow Steps horizontally across the slide
    step_w = Inches(2.7)
    step_h = Inches(5.2)

    steps_data = [
        ("Step 1: Sensing", "Dual-Band Sensor Suite", 
         "• Sony 4K RGB Camera for terrain context & visual markers.\n\n• Infiray / FLIR LWIR Thermal Sensor (8-14μm) for human heat anomalies.\n\n• Downward LiDAR/Sonar for precise ground distance and altitude.\n\n• Anti-vibration silicone dampening platform."),
        ("Step 2: Real-Time MCU", "STM32U585 Core @ 250Hz",
         "• Runs Zephyr RTOS with hard-deterministic 4ms PID flight loops.\n\n• Inherits Joop Broking YMFC-32 flight stabilization heritage.\n\n• 350Hz patched PWM for direct brushless ESC response.\n\n• Asynchronous RPC bridge prevents Linux tasks from blocking flight."),
        ("Step 3: Edge AI MPU", "Qualcomm QRB2210 Core",
         "• Debian Linux host executing INT8 quantized YOLO-nano.\n\n• Multi-spectral late fusion: blends RGB confidence with thermal heat.\n\n• Tait-Bryan Ray-Casting: Calculates victim Lat/Long using drone altitude and gimbal attitude.\n\n• Sub-5W power draw."),
        ("Step 4: Tactical GCS", "Offline Ground Station",
         "• Dual comms: Local Wi-Fi video stream + LoRa 868MHz packet telemetry.\n\n• Offline vector disaster mapping (Leaflet / Mapbox tiles).\n\n• Automated Triage Queue (coordinates, confidence, heat).\n\n• Dijkstra safe-path routing for ground search crews.")
    ]

    for idx, (step_title, sub_title, body_text) in enumerate(steps_data):
        left_pos = Inches(0.8 + idx * 2.95)
        add_card(slide4, left_pos, Inches(1.7), step_w, step_h)
        tb = slide4.shapes.add_textbox(left_pos + Inches(0.15), Inches(1.9), step_w - Inches(0.3), step_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = step_title
        p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = AMBER; p.space_after = Pt(2)

        p = tf.add_paragraph()
        p.text = sub_title
        p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = DARK_BLUE; p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = body_text
        p.font.size = Pt(11.5); p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 5: FEASIBILITY, VIABILITY & SIZING
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Engineering Feasibility & Commercial Viability")

    # Left: Sizing & Mass Budget (Bouabdallah Sizing Laws)
    add_card(slide5, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.2))
    tb = slide5.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.25), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Mathematical Sizing (Bouabdallah Sizing Laws)"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = DARK_BLUE; p.space_after = Pt(8)
    p = tf.add_paragraph()
    p.text = "• Thrust-to-Weight Ratio: β ≥ 2.0 (50% thrust margin for turbulence, heavy wind, and evasive climb in disaster zones).\n\n" \
             "• 38% Battery Mass Fraction: Sized via Bouabdallah's Cost Factor (C) and Autonomy (Au) optimization; prevents payload-diminishing returns.\n\n" \
             "• Weight Budget (Under DGCA 2kg Micro Limit):\n" \
             "  - Airframe & 4x BLDC Motors + Props: 720g\n" \
             "  - Battery (4S 5200mAh LiPo): 560g\n" \
             "  - Dual-Brain Avionics (UNO Q + Sensors): 120g\n" \
             "  - Dual-Camera Gimbal Payload: 180g\n" \
             "  - Total All-Up-Weight (AUW): 1.58 kg (< 2.0 kg Micro Category)\n\n" \
             "• 30-Minute Search Window: Covers 1.5 km² grid per battery sortie."
    p.font.size = Pt(12.5); p.font.color.rgb = TEXT_DARK

    # Right: Market Viability vs Enterprise Drones
    add_card(slide5, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.2))
    tb = slide5.shapes.add_textbox(Inches(7.05), Inches(1.9), Inches(5.25), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Market & Cost Viability Comparison"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = ACCENT_BLUE; p.space_after = Pt(8)
    p = tf.add_paragraph()
    p.text = "Current Commercial Standard (e.g. DJI Matrice 30T):\n" \
             "• Unit Cost: ₹9,00,000 to ₹14,00,000 (Exorbitant for regional SDRF)\n" \
             "• Closed Ecosystem: Locked firmware, foreign server telemetry risk.\n" \
             "• No Custom Edge AI: Cannot deploy custom disaster hazard models.\n\n" \
             "Project Phoenix SAR Platform:\n" \
             "• Estimated Unit Cost: ₹85,000 to ₹1,40,000 (1/8th of the cost!)\n" \
             "• Open-Source Dual-Brain Stack: 100% Indian data sovereignty.\n" \
             "• Edge Programmability: Deploy updated neural models over USB.\n" \
             "• Rapid Deployment: < 3 minutes from unboxing to takeoff.\n" \
             "• Swarm Scalable: 1 disaster battalion can deploy 5 Phoenix units for the price of 1 proprietary enterprise drone."
    p.font.size = Pt(12.5); p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 6: RESEARCH REFERENCES & TEAM COMPETENCY
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Research Foundations & Team Phoenix Competency")

    # Left: Academic Foundations
    add_card(slide6, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.2))
    tb = slide6.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.25), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Research Foundations & Prior Art"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = DARK_BLUE; p.space_after = Pt(8)
    p = tf.add_paragraph()
    p.text = "1. Dr. Samir Bouabdallah (EPFL Thesis No. 3727, 2007):\n" \
             "   • 'Design and Control of Quadrotors with Application to Autonomous Flying'\n" \
             "   • Grounded our 12-state rigid body dynamics, spectral loop separation, and the 90/10 electrical power sizing law.\n\n" \
             "2. NASA Technical Memorandum 4741 (NASA Langley, 1996):\n" \
             "   • Informed selection of zero-pitching-moment (Cm=0) reflexed airfoils to eliminate blade flutter and IMU vibration.\n\n" \
             "3. JRFCQAI Open-Source Dual-Brain Architecture (Ravi Butani, 2024):\n" \
             "   • Established the viability of Zephyr RTOS (STM32U5) + Debian Linux (Qualcomm QRB2210) on the Arduino UNO Q for UAV flight."
    p.font.size = Pt(12.5); p.font.color.rgb = TEXT_DARK

    # Right: Team Competency (2nd Year Undergrads)
    add_card(slide6, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.2))
    tb = slide6.shapes.add_textbox(Inches(7.05), Inches(1.9), Inches(5.25), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Team Phoenix Synergy & Execution Plan"
    p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = AMBER; p.space_after = Pt(8)
    p = tf.add_paragraph()
    p.text = "• AI & Data Science (AD):\n" \
             "  - Multi-spectral RGB + Thermal dataset curation & augmentation.\n" \
             "  - INT8 model quantization for the Qualcomm Dragonwing NPU.\n\n" \
             "• Computer Science & Engineering (CSE):\n" \
             "  - Tait-Bryan Ray-Casting coordinate projection engine.\n" \
             "  - Offline Web Ground Station (React + Leaflet + WebSocket bus).\n\n" \
             "• Cyber Security (CY):\n" \
             "  - Telemetry packet authentication & anti-spoofing.\n" \
             "  - LoRa emergency telemetry fallback protocol & store-and-forward sync.\n\n" \
             "GitHub Repository: github.com/jvstin47/Phoenix-SIH26177-SAR-UAV"
    p.font.size = Pt(12.5); p.font.color.rgb = TEXT_DARK

    prs.save(output_path)
    print(f"Presentation successfully saved to {output_path}")

if __name__ == "__main__":
    out = "/Users/justin/.gemini/antigravity/scratch/Phoenix-SIH26177-SAR-UAV/presentation/Team_Phoenix_SIH26177_Official_Deck.pptx"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    create_sih_deck(out)
