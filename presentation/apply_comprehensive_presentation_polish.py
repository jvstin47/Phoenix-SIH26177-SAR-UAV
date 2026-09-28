"""
Comprehensive, jury-grade presentation overhaul for Copy of SIH26177_v7.pptx.pptx:
1. Fix all text visibility issues (change invisible dark-blue text on dark navy cards to crisp white #FFFFFF / gold #FBBF24 / cyan #38BDF8).
2. Fix all text box overflows (adjust font sizes, margins, line spacings).
3. Bold and ALL-CAPS leading keywords across all slides for instant skimming.
4. Reframe 'NATIONAL DATA SOVEREIGNTY' -> 'AIR-GAPPED TACTICAL RESILIENCE'.
5. Prominently emphasize the ARDUINO UNO Q (Qualcomm Dragonwing QRB2210 + STM32U585) across all slides.
6. Replace remaining Bouabdallah references on Slide 6 with hardware_viva_defense_guide.md.
7. Ensure all sentences are complete, grammatically sound, and 100% defensible under hostile hardware jury interrogation.
"""

import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

TARGET_PPTX = "Copy of SIH26177_v7.pptx.pptx"

def set_run(r, text, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=False, italic=False):
    r.text = text
    r.font.name = font
    if size_pt:
        r.font.size = Pt(size_pt)
    if color:
        r.font.color.rgb = RGBColor(*color)
    r.font.bold = bold
    r.font.italic = italic

def polish_deck():
    prs = pptx.Presentation(TARGET_PPTX)
    print("Beginning comprehensive deck polish...")

    # =========================================================================
    # SLIDE 1: Title & Hero Slide (Emphasize Arduino UNO Q)
    # =========================================================================
    slide1 = prs.slides[0]
    
    # 1. Category badge (Group 10 -> TextBox 12)
    for s in slide1.shapes:
        if s.shape_type == 6 and s.name == "Group 10":
            for sub in s.shapes:
                if sub.name == "TextBox 12":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "HARDWARE EDITION  |  POWERED BY ARDUINO UNO Q (QUALCOMM INC.)", font="Calibri", size_pt=16.0, color=(179, 90, 0), bold=True)
                    print("Slide 1: Updated category badge with Arduino UNO Q")

    # 2. Subtitle (TextBox 14)
    for s in slide1.shapes:
        if s.name == "TextBox 14":
            s.text_frame.clear()
            p = s.text_frame.paragraphs[0]
            r = p.add_run()
            set_run(r, "Arduino UNO Q Dual-Brain Edge-AI Scout for Zero-Infrastructure Disaster Reconnaissance", font="Calibri", size_pt=23.0, color=(86, 96, 116), bold=False)
            print("Slide 1: Updated subtitle with Arduino UNO Q")

    # 3. Right feature badges (TextBox 73, TextBox 80)
    for s in slide1.shapes:
        if s.shape_type == 6:
            for sub in s.shapes:
                if sub.name == "TextBox 73":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "Arduino UNO Q Dual-Brain SBC", font="Calibri", size_pt=18.0, color=(31, 73, 125), bold=True)
                    print("Slide 1: Updated Badge 1 to Arduino UNO Q Dual-Brain SBC")
                elif sub.name == "TextBox 80":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "QRB2210 Linux + STM32U5 RTOS", font="Calibri", size_pt=18.0, color=(31, 73, 125), bold=True)
                    print("Slide 1: Updated Badge 2 to QRB2210 Linux + STM32U5 RTOS")

    # =========================================================================
    # SLIDE 2: Problem Statement & Proposed Solution
    # =========================================================================
    slide2 = prs.slides[1]
    
    # 1. Left Card: Problem Statement (TextBox 156)
    for s in slide2.shapes:
        if s.name == "TextBox 156":
            tf = s.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(4)
            r0 = p0.add_run()
            set_run(r0, "CRITICAL DISASTER BARRIERS — FOUR OPERATIONAL FAILURES:", font="Calibri", size_pt=14.0, color=(180, 40, 30), bold=True)

            bullets = [
                ("01 — TOTAL COMMS BLACKOUT: ", "Cellular and Wi-Fi networks down; cloud-reliant commercial drones fail immediately."),
                ("02 — ZERO OPTICAL VISIBILITY: ", "Darkness, dense smoke, and debris dust blind conventional visible-light RGB cameras."),
                ("03 — UNLOCALIZED CASUALTIES: ", "Visual spotting lacks coordinates; rescue teams dig blindly without actionable GPS fixes."),
                ("04 — SECONDARY RESCUER HAZARDS: ", "Live electrical lines, shifting rubble piles, and gas voids endanger ground rescue crews.")
            ]
            for head, body in bullets:
                p = tf.add_paragraph()
                p.space_after = Pt(3)
                r_h = p.add_run()
                set_run(r_h, head, font="Calibri", size_pt=13.0, color=(30, 38, 56), bold=True)
                r_b = p.add_run()
                set_run(r_b, body, font="Calibri", size_pt=13.0, color=(50, 60, 80), bold=False)
            print("Slide 2: Formatted Problem Statement with bold leading keywords")

    # 2. Right Card: Proposed Solution (TextBox 157) - FIX INVISIBLE TEXT!
    for s in slide2.shapes:
        if s.name == "TextBox 157":
            tf = s.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(4)
            r0 = p0.add_run()
            set_run(r0, "PROJECT PHOENIX: ARDUINO UNO Q DUAL-BRAIN ARCHITECTURE", font="Calibri", size_pt=14.0, color=(56, 189, 248), bold=True)

            sol_bullets = [
                ("ARDUINO UNO Q DUAL-BRAIN: ", "QRB2210 MPU performs INT8 edge-AI on Linux; STM32U585 MCU runs deterministic 250 Hz flight loop on Zephyr."),
                ("1080P + THERMAL FUSION: ", "Fuses 1080p optical with 8–14μm LWIR to detect human heat signatures in darkness, smoke & debris."),
                ("CONTINUOUS GEOREFERENCING: ", "Synchronized GNSS, attitude, camera geometry & ToF altitude georeference victims in real time without hovering."),
                ("OFFLINE RESCUE ROUTING: ", "Prioritizes triage on-chip; broadcasts 17-byte LoRa packets to chart Dijkstra corridors avoiding hazards [1, 3].")
            ]
            for head, body in sol_bullets:
                p = tf.add_paragraph()
                p.space_after = Pt(3)
                r_h = p.add_run()
                set_run(r_h, head, font="Calibri", size_pt=13.0, color=(251, 191, 36), bold=True) # Bright gold/amber
                r_b = p.add_run()
                set_run(r_b, body, font="Calibri", size_pt=13.0, color=(255, 255, 255), bold=False) # Crisp white!
            print("Slide 2: Fixed Proposed Solution with high-contrast white & gold text on dark navy")

    # 3. Bottom 5 Innovation Cards (TextBox 158 to 162)
    innovations = [
        ("TextBox 158", "ARDUINO UNO Q SBC (4GB/32GB): ", "Qualcomm Dragonwing QRB2210 MPU + STM32U585 MCU on a single 42g board."),
        ("TextBox 159", "SUB-5W HETEROGENEOUS AI: ", "QRB2210 CPU/GPU/DSP executes INT8 YOLO inference, preserving battery for flight."),
        ("TextBox 160", "REAL-TIME GEOREFERENCING: ", "Tait-Bryan ray projection calculates ground WGS-84 coordinates on the fly without hovering."),
        ("TextBox 161", "17-BYTE LORA TELEMETRY: ", "Off-grid bit-packed triage stream reaches 3–5+ km in complete cellular blackouts [3]."),
        ("TextBox 162", "ANTI-DRIFT VIO NAVIGATION: ", "Visual-Inertial Odometry overrides compromised magnetometers in metallic rubble environments.")
    ]
    for tb_name, head, body in innovations:
        for s in slide2.shapes:
            if s.name == tb_name:
                tf = s.text_frame
                tf.clear()
                p = tf.paragraphs[0]
                r_h = p.add_run()
                set_run(r_h, head, font="Calibri", size_pt=12.8, color=(30, 38, 56), bold=True)
                r_b = p.add_run()
                set_run(r_b, body, font="Calibri", size_pt=12.8, color=(60, 70, 90), bold=False)
                print(f"Slide 2: Formatted {tb_name} with bold leading keyword")

    # =========================================================================
    # SLIDE 3: Technical Approach / System Architecture (Fix Invisible Text & Overflow)
    # =========================================================================
    slide3 = prs.slides[2]

    # 1. Left Workflow Steps (1 to 6)
    workflow_steps = [
        ("TextBox 36", "OFFLINE SECTOR SETUP: ", "Operator defines 2 km² search polygon on tactical tablet; autonomous launch in < 3 minutes."),
        ("TextBox 46", "TERRAIN-FOLLOWING GRID: ", "Boustrophedon sweep with 60% sidelap; downward ToF altimeter maintains constant GSD over sloped terrain."),
        ("TextBox 56", "1080P + THERMAL FUSION: ", "Dual 1080p RGB + LWIR thermal fusion; edge YOLO detects survivor heat anomalies in darkness, smoke & debris."),
        ("TextBox 66", "INSTANT GEOREFERENCING: ", "Synchronized GNSS, attitude, camera geometry & ToF altitude georeference victims on the fly without hovering."),
        ("TextBox 76", "17-BYTE LORA BURST: ", "Onboard edge triage scores urgency and broadcasts compact binary frame over 868 MHz UART LoRa [3]."),
        ("TextBox 85", "DYNAMIC SAFE ROUTING: ", "Tactical GCS runs Dijkstra graph search [1] to generate hazard-free ground ingress corridors for first responders.")
    ]
    for tb_name, head, body in workflow_steps:
        for s in slide3.shapes:
            if s.name == tb_name:
                tf = s.text_frame
                tf.clear()
                p = tf.paragraphs[0]
                r_h = p.add_run()
                set_run(r_h, head, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=True)
                r_b = p.add_run()
                set_run(r_b, body, font="Calibri", size_pt=14.0, color=(60, 70, 90), bold=False)
                print(f"Slide 3: Formatted workflow {tb_name}")

    # 2. System Architecture Title: Emphasize Arduino UNO Q
    for s in slide3.shapes:
        if s.shape_type == 6 and s.name == "Group 93":
            for sub in s.shapes:
                if sub.name == "TextBox 95":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "Dual-Brain Hardware Split (Arduino UNO Q 4GB/32GB):", font="Calibri", size_pt=17.5, color=(255, 255, 255), bold=True)
                    print("Slide 3: Emphasized Arduino UNO Q 4GB/32GB in System Architecture title")

    # 3. Real-Time Flight Controller (STM32U585) - TextBox 101: FIX INVISIBLE TEXT!
    for s in slide3.shapes:
        if s.name == "TextBox 101":
            tf = s.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(2)
            r0 = p0.add_run()
            set_run(r0, "• 250 Hz (4ms) deterministic flight stabilization loop; direct 350 Hz PWM motor control", 
                    font="Calibri", size_pt=11.5, color=(255, 255, 255), bold=False)
            p1 = tf.add_paragraph()
            r1 = p1.add_run()
            set_run(r1, "• I2C: MPU6050 IMU + MS5611 Baro + VL53L1X ToF // UART: u-blox NEO-M8N GNSS", 
                    font="Calibri", size_pt=11.0, color=(203, 213, 225), bold=False)
            print("Slide 3: Fixed STM32 card text color to high-contrast white & light-slate")

    # 4. Mission Computer (QRB2210) - TextBox 112: FIX OVERFLOW & TEXT COLOR!
    for s in slide3.shapes:
        if s.name == "TextBox 112":
            s.width = Inches(5.10)
            s.height = Inches(0.55)
            tf = s.text_frame
            tf.margin_top = 0
            tf.margin_bottom = 0
            tf.margin_left = 0
            tf.margin_right = 0
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(2)
            r0 = p0.add_run()
            set_run(r0, "• Qualcomm Dragonwing QRB2210 MPU (Debian Linux — 4GB RAM, 32GB eMMC)", 
                    font="Calibri", size_pt=11.2, color=(255, 255, 255), bold=False)
            p1 = tf.add_paragraph()
            r1 = p1.add_run()
            set_run(r1, "• Sub-5W Heterogeneous AI // Georeferencing Engine // E22 UART LoRa [3]", 
                    font="Calibri", size_pt=10.8, color=(203, 213, 225), bold=False)
            print("Slide 3: Fixed QRB2210 Mission Computer overflow and text colors")

    # =========================================================================
    # SLIDE 4: Feasibility & Viability (Reframe Data Sovereignty & Bold Headings)
    # =========================================================================
    slide4 = prs.slides[3]

    # 1. Technical Feasibility (TextBox 38)
    for s in slide4.shapes:
        if s.name == "TextBox 38":
            tf = s.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(3)
            r0_h = p0.add_run()
            set_run(r0_h, "THRUST HEADROOM: ", font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=True)
            r0_b = p0.add_run()
            set_run(r0_b, "2.23:1 maximum thrust-to-weight ratio provides substantial control authority in wind gusts.", font="Calibri", size_pt=15.0, color=(60, 70, 90), bold=False)
            
            p1 = tf.add_paragraph()
            r1_h = p1.add_run()
            set_run(r1_h, "SUB-5W COMPUTE: ", font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=True)
            r1_b = p1.add_run()
            set_run(r1_b, "Arduino UNO Q heterogeneous AI consumes <4% of power, reserving energy for rotor flight.", font="Calibri", size_pt=15.0, color=(60, 70, 90), bold=False)
            print("Slide 4: Formatted Technical Feasibility")

    # 2. Operational Feasibility (TextBox 46)
    for s in slide4.shapes:
        if s.name == "TextBox 46":
            tf = s.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(3)
            r0_h = p0.add_run()
            set_run(r0_h, "RAPID SETUP: ", font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=True)
            r0_b = p0.add_run()
            set_run(r0_b, "< 3 minutes from rugged backpack unboxing to active search flight.", font="Calibri", size_pt=15.0, color=(60, 70, 90), bold=False)
            
            p1 = tf.add_paragraph()
            r1_h = p1.add_run()
            set_run(r1_h, "CONTINUOUS SORTIES: ", font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=True)
            r1_b = p1.add_run()
            set_run(r1_b, "Dual-pack quick-swap batteries support rolling 100% duty-cycle rescue sweeps.", font="Calibri", size_pt=15.0, color=(60, 70, 90), bold=False)
            print("Slide 4: Formatted Operational Feasibility")

    # 3. Financial Feasibility (TextBox 54)
    for s in slide4.shapes:
        if s.name == "TextBox 54":
            tf = s.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.space_after = Pt(3)
            r0_h = p0.add_run()
            set_run(r0_h, "PROTOTYPE BUILD (₹37,400): ", font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=True)
            r0_b = p0.add_run()
            set_run(r0_b, "Genuine Arduino UNO Q 4GB/32GB build for full hardware evaluation.", font="Calibri", size_pt=15.0, color=(60, 70, 90), bold=False)
            
            p1 = tf.add_paragraph()
            r1_h = p1.add_run()
            set_run(r1_h, "PRODUCTION BOM (₹1.2 LAKH): ", font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=True)
            r1_b = p1.add_run()
            set_run(r1_b, "Enterprise-grade SAR UAV at 1/10th the cost of imported commercial drones.", font="Calibri", size_pt=15.0, color=(60, 70, 90), bold=False)
            print("Slide 4: Formatted Financial Feasibility")

    # 4. Viability Column:
    # A. Economic Viability (TextBox 96)
    for s in slide4.shapes:
        if s.name == "TextBox 96":
            tf = s.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            r_h = p.add_run()
            set_run(r_h, "FLEET SCALABILITY: ", font="Calibri", size_pt=15.5, color=(255, 255, 255), bold=True)
            r_b = p.add_run()
            set_run(r_b, "NDRF battalions can deploy a 10-drone swarm for the acquisition cost of 1 imported drone.", font="Calibri", size_pt=15.0, color=(228, 236, 247), bold=False)
            print("Slide 4: Formatted Fleet Scalability")

    # B. REFRAME 'NATIONAL DATA SOVEREIGNTY' -> 'AIR-GAPPED TACTICAL RESILIENCE'
    for s in slide4.shapes:
        if s.shape_type == 6 and s.name == "Group 101":
            for sub in s.shapes:
                if sub.name == "TextBox 103":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "AIR-GAPPED TACTICAL RESILIENCE", font="Calibri", size_pt=16.5, color=(255, 179, 92), bold=True)
                    print("Slide 4: Reframed title from 'NATIONAL DATA SOVEREIGNTY' -> 'AIR-GAPPED TACTICAL RESILIENCE'")

    for s in slide4.shapes:
        if s.name == "TextBox 104":
            tf = s.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            r_h = p.add_run()
            set_run(r_h, "100% OFFLINE DATA PRIVACY: ", font="Calibri", size_pt=15.5, color=(255, 255, 255), bold=True)
            r_b = p.add_run()
            set_run(r_b, "Zero cloud dependencies; all sensor feeds and victim GPS fixes remain strictly local on tactical responder tablets.", font="Calibri", size_pt=15.0, color=(228, 236, 247), bold=False)
            print("Slide 4: Reframed text for Air-Gapped Tactical Resilience")

    # C. Deployment Ecosystem (TextBox 112)
    for s in slide4.shapes:
        if s.name == "TextBox 112":
            tf = s.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            r_h = p.add_run()
            set_run(r_h, "FIELD-READY INTEGRATION: ", font="Calibri", size_pt=15.5, color=(255, 255, 255), bold=True)
            r_b = p.add_run()
            set_run(r_b, "Native protocol compatibility with NDRF, SDRF, and civil disaster response command units.", font="Calibri", size_pt=15.0, color=(228, 236, 247), bold=False)
            print("Slide 4: Formatted Deployment Ecosystem")

    # 5. Challenges to Strategies (TextBox 126, 135, 144, 153, 162)
    challenges = [
        ("TextBox 126", "868 MHZ LORA BRIDGE: ", "Sustains NLoS micro-telemetry packet link [2] without cellular towers (DOI: 10.1109/ACCESS.2026.3731317)."),
        ("TextBox 135", "LWIR THERMAL DETECTION: ", "8–14μm radiometric array isolates 37°C casualties through smoke, dust, and debris [1] (Siotia, IEEE Access 2026)."),
        ("TextBox 144", "ANTI-DRIFT VIO NAVIGATION: ", "Visual-Inertial Odometry overrides compromised magnetometers in collapsed steel rubble (IEEE standard)."),
        ("TextBox 153", "HARMONIC NOTCH FILTERING: ", "Silicone damping mounts + software notch filtering eliminate ESC/motor noise on 250Hz EKF loop."),
        ("TextBox 162", "ANTI-WINDUP PID CLAMPING: ", "Dynamic integrator clamping prevents control surface saturation during aggressive gusts.")
    ]
    for tb_name, head, body in challenges:
        for s in slide4.shapes:
            if s.name == tb_name:
                tf = s.text_frame
                tf.clear()
                p = tf.paragraphs[0]
                r_h = p.add_run()
                set_run(r_h, head, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=True)
                r_b = p.add_run()
                set_run(r_b, body, font="Calibri", size_pt=14.0, color=(60, 70, 90), bold=False)
                print(f"Slide 4: Formatted challenge {tb_name}")

    # =========================================================================
    # SLIDE 5: Impact & Benefits (Bold Leading Keywords Across Pipeline & Cards)
    # =========================================================================
    slide5 = prs.slides[4]

    # 1. 4 Stakeholder Cards (TextBox 29, 39, 49, 59)
    card_bullets = [
        ("TextBox 29", [
            ("GOLDEN 72H WINDOW: ", "Rapid discovery within critical survival timeframe"),
            ("DEBRIS & SMOKE SENSING: ", "Thermal lock in zero-light and smoky collapse voids"),
            ("TRIAGE PRIORITIZATION: ", "Instant medical urgency rating streamed to rescue teams"),
            ("SURVIVAL MULTIPLIER: ", "Dramatically cuts time-to-extraction under rubble")
        ]),
        ("TextBox 39", [
            ("ADVANCE HAZARD MAPPING: ", "Flags live high-voltage cables, gas leaks & floodwaters"),
            ("SAFE ROUTE NAVIGATION: ", "Dynamic Dijkstra corridor guides rescuers around hazards [1]"),
            ("TACTICAL AWARENESS: ", "Crews proceed straight to verified survivor coordinates"),
            ("FATIGUE REDUCTION: ", "Replaces blind shovel digs with targeted extraction")
        ]),
        ("TextBox 49", [
            ("UNIFIED COMMON PICTURE: ", "Real-time casualty mapping with micro-telemetry tracking"),
            ("ZERO CLOUD DEPENDENCY: ", "100% operational during complete cellular & power blackouts"),
            ("DYNAMIC SECTOR LOGS: ", "Autonomous coverage tracking ensures no sector is missed"),
            ("17-BYTE LORA STREAM: ", "Ultra-compact bit-packed alerts arrive in under 3 seconds [3]")
        ]),
        ("TextBox 59", [
            ("TARGETED RESOURCE DROPS: ", "Prioritized airlift and medical kits based on triage data"),
            ("AFFORDABLE PROCUREMENT: ", "Deploy 10 Phoenix drones for the price of 1 enterprise UAV"),
            ("AUDITABLE EVENT LOGS: ", "Tamper-evident onboard flight logs for post-incident review"),
            ("SCALABLE STOCKPILING: ", "Standardized COTS electronics enable rapid state-wide rollout")
        ])
    ]
    for tb_name, b_list in card_bullets:
        for s in slide5.shapes:
            if s.name == tb_name:
                tf = s.text_frame
                tf.clear()
                for bi, (head, body) in enumerate(b_list):
                    p = tf.paragraphs[0] if bi == 0 else tf.add_paragraph()
                    p.space_after = Pt(2)
                    r_h = p.add_run()
                    set_run(r_h, head, font="Calibri", size_pt=13.0, color=(30, 38, 56), bold=True)
                    r_b = p.add_run()
                    set_run(r_b, body, font="Calibri", size_pt=13.0, color=(60, 70, 90), bold=False)
                print(f"Slide 5: Formatted stakeholder card {tb_name}")

    # 2. Impact Pipeline (Rows 1 & 2 TextBoxes: 84, 85, 99, 100, 114, 115, 129, 130, 144, 145)
    pipeline_texts = [
        ("TextBox 84", "BACKPACK DEPLOY: ", "Unbox to autonomous flight in < 3 minutes"),
        ("TextBox 85", "ZERO INFRASTRUCTURE: ", "Search begins immediately upon arrival"),
        ("TextBox 99", "BOUSTROPHEDON SWEEP: ", "Autonomous dual 1080p + thermal grid coverage"),
        ("TextBox 100", "ALL-WEATHER SCAN: ", "Continuous search in smoke, dust & darkness"),
        ("TextBox 114", "INSTANT GEOREFERENCING: ", "Tait-Bryan projection calculates exact ground GPS"),
        ("TextBox 115", "ZERO SEARCH DELAY: ", "Rescuers proceed straight to survivor coordinates"),
        ("TextBox 129", "TRIAGE & HAZARD ROUTE: ", "Ranks casualties & computes Dijkstra safe corridors [1]"),
        ("TextBox 130", "CREW PROTECTION: ", "Rescuers avoid live power cables & gas hazards"),
        ("TextBox 144", "FLEET ECONOMICS: ", "Full autonomous capability at 1/10th enterprise cost"),
        ("TextBox 145", "LIVES SAVED: ", "Accelerates extraction within the Golden 72 hours")
    ]
    for tb_name, head, body in pipeline_texts:
        for s in slide5.shapes:
            if s.name == tb_name:
                tf = s.text_frame
                tf.clear()
                p = tf.paragraphs[0]
                r_h = p.add_run()
                set_run(r_h, head, font="Calibri", size_pt=12.5, color=(31, 73, 125) if "84" in tb_name or "99" in tb_name or "114" in tb_name or "129" in tb_name or "144" in tb_name else (30, 38, 56), bold=True)
                r_b = p.add_run()
                set_run(r_b, body, font="Calibri", size_pt=12.5, color=(60, 70, 90), bold=False)
                print(f"Slide 5: Formatted pipeline step {tb_name}")

    # =========================================================================
    # SLIDE 6: Research & References (Purge Bouabdallah thesis doc reference)
    # =========================================================================
    slide6 = prs.slides[5]

    for s in slide6.shapes:
        if s.name == "TextBox 103":
            tf = s.text_frame
            tf.clear()
            docs_list = [
                "1. docs/research_papers_synthesis_2026.md",
                "2. docs/prototype_bom_and_financial_viability.md",
                "3. docs/ros_lora_mission_critical_uav_swarm_research.md",
                "4. docs/hardware_viva_defense_guide.md"
            ]
            for di, doc_item in enumerate(docs_list):
                p = tf.paragraphs[0] if di == 0 else tf.add_paragraph()
                p.space_after = Pt(2)
                r = p.add_run()
                set_run(r, doc_item, font="Calibri", size_pt=13.5, color=(30, 38, 56), bold=False)
            print("Slide 6: Replaced Bouabdallah doc with docs/hardware_viva_defense_guide.md")

    prs.save(TARGET_PPTX)
    print(f"\nSuccessfully polished and saved presentation to {TARGET_PPTX}")

if __name__ == "__main__":
    polish_deck()
