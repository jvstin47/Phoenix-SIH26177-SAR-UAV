"""
Build Copy of SIH26177_v7.pptx.pptx by applying all critical engineering,
terminology, and visual alignment fixes based on the hardware jury critique.

Fixes applied:
1. Slide 1: Update badge to 'IEEE Anti-Drift VIO Navigation'.
2. Slide 2:
   - Precision alignment of containers (Group 17 & Group 24) and badges (Group 21 & Group 26).
   - Equalize Card 5 (Group 74) width with other cards (3,178,016 EMU).
   - Update 5 bottom card textboxes (UNO Q 4GB/32GB, heterogeneous compute CPU/GPU/DSP, ray-casting without hovering, LoRa [3], VIO).
   - Fix thermal claim in TextBox 157 (detecting surface thermal anomalies & exposed casualties through darkness/smoke, not solid mud).
   - Fix barriers in TextBox 156 with clean paragraph spacing.
3. Slide 3:
   - Step 5: Cite [3] (Souli et al.).
   - Step 6: Cite [1] (Siotia et al. / Dijkstra corridor).
   - Mission Computer: Explicitly state Arduino UNO Q (4GB RAM / 32GB eMMC) and heterogeneous compute.
4. Slide 4:
   - Add DOIs and bracketed citations [1], [2] to Challenges 1 and 2.
   - Purge 2007 Bouabdallah citations from Challenges 4 and 5 (replace with modern IEEE control theory).
   - Update Financial Feasibility to ₹37,400 (calibrated for 4GB/32GB UNO Q).
   - Update Technical Feasibility to detail ~5.5W electronics payload (>96% power for rotors) and 1.58 kg mass budget.
5. Slide 6:
   - Purge 2007 Bouabdallah card completely.
   - Replace with 4 modern, peer-reviewed primary cards [1] to [7] with active DOIs and hyperlinks.
"""

import pptx
from pptx.dml.color import RGBColor
from pptx.util import Pt

TARGET_FILE = "Copy of SIH26177_v7.pptx.pptx"

def set_run(r, text, font="Calibri", size_pt=15.0, color=(30, 38, 56), bold=False, italic=False):
    r.text = text
    r.font.name = font
    if size_pt:
        r.font.size = Pt(size_pt)
    if color:
        r.font.color.rgb = RGBColor(*color)
    r.font.bold = bold
    r.font.italic = italic

def build_v7():
    prs = pptx.Presentation(TARGET_FILE)

    # =========================================================================
    # SLIDE 1: Update Badge to IEEE Anti-Drift VIO Navigation
    # =========================================================================
    slide1 = prs.slides[0]
    for s in slide1.shapes:
        if s.shape_type == 6 and s.name == "Group 99":
            for sub in s.shapes:
                if sub.name == "TextBox 101":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "IEEE Anti-Drift VIO Navigation", font="Calibri", size_pt=12.8, color=(255, 255, 255), bold=True)
                    print("Slide 1: Updated badge to 'IEEE Anti-Drift VIO Navigation'")
                    break

    # =========================================================================
    # SLIDE 2: Alignment & Terminology Overhaul
    # =========================================================================
    slide2 = prs.slides[1]

    # Shape map for Slide 2
    s2_map = {s.name: s for s in slide2.shapes}

    # 1. Align Left Container (Group 17) and Right Container (Group 24)
    # Master top: 1775936, height: 4061097
    if "Group 24" in s2_map:
        g24 = s2_map["Group 24"]
        g24.top = 1775936
        g24.height = 4061097

    # Align Badges (Group 21 & Group 26)
    if "Group 26" in s2_map:
        g26 = s2_map["Group 26"]
        g26.top = 2002536

    # 2. Equalize Card 5 (Group 74) width with cards 1-4 (3,178,016 EMU)
    if "Group 74" in s2_map:
        g74 = s2_map["Group 74"]
        g74.width = 3178016
        # Background freeform inside Group 74
        for sub in g74.shapes:
            sub.width = 3178016

    # 3. Align TextBoxes 156 and 157
    target_text_top = 2600000
    target_text_height = 2900000
    if "TextBox 156" in s2_map:
        tb156 = s2_map["TextBox 156"]
        tb156.top = target_text_top
        tb156.height = target_text_height
        tf156 = tb156.text_frame
        tf156.clear()
        
        # P0 Header
        p = tf156.paragraphs[0]
        r = p.add_run()
        set_run(r, "IN CATASTROPHIC DISASTERS (LANDSLIDES, EARTHQUAKES), FIRST RESPONDERS FACE FOUR CRITICAL BARRIERS:", 
                font="Calibri", size_pt=14.5, color=(180, 40, 30), bold=True)
        
        barriers = [
            ("COMMS BLACKOUT: ", "Downed cellular towers & power grids; cloud-dependent drones rendered completely inoperable."),
            ("ZERO VISIBILITY: ", "Mud slush, dense smoke, and darkness blind standard visual electro-optical cameras."),
            ("ENTRAPMENT ACCESS: ", "Survivability sharply declines with delayed response; manual foot searches cannot cover wide rubble sectors in time."),
            ("RESPONDER HAZARDS: ", "Ground teams advance blindly toward fallen electrical wires, gas leaks, and secondary landslides.")
        ]
        for b_title, b_desc in barriers:
            p = tf156.add_paragraph()
            r_b = p.add_run()
            set_run(r_b, b_title, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=True)
            r_t = p.add_run()
            set_run(r_t, b_desc, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=False)

    if "TextBox 157" in s2_map:
        tb157 = s2_map["TextBox 157"]
        tb157.top = target_text_top
        tb157.height = target_text_height
        tf157 = tb157.text_frame
        tf157.clear()

        # P0 Header
        p = tf157.paragraphs[0]
        r = p.add_run()
        set_run(r, "Project Phoenix: An autonomous, field-deployable multirotor scout engineered for offline disaster zones:", 
                font="Calibri", size_pt=14.5, color=(31, 73, 125), bold=True)

        solutions = [
            ("100% ONBOARD EDGE COMPUTE: ", "Heterogeneous AI (CPU/GPU/DSP) executes all vision & geolocation on-device; zero cloud/cellular dependency."),
            ("MULTI-SPECTRAL FUSION: ", "Combines 4K RGB with LWIR Thermal (8-14μm) to spot surface heat anomalies & exposed casualties through smoke/darkness."),
            ("TAIT-BRYAN RAY-CASTING: ", "Calculates victim ground GPS coordinates on the fly from altitude without battery-wasting hovering."),
            ("LIGHTWEIGHT OFFLINE GCS: ", "Low-power field tablets receive 17-byte pins; charts priority triage queues & safe walking corridors [1].")
        ]
        for s_title, s_desc in solutions:
            p = tf157.add_paragraph()
            r_b = p.add_run()
            set_run(r_b, s_title, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=True)
            r_t = p.add_run()
            set_run(r_t, s_desc, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=False)

    # 4. Update the 5 bottom card textboxes
    card_updates = {
        "TextBox 158": "Arduino UNO Q (4GB LPDDR4 / 32GB eMMC): Qualcomm Dragonwing QRB2210 MPU + STM32U585 MCU on a unified 40g board.",
        "TextBox 159": "Heterogeneous On-Device AI: CPU/Adreno GPU/Hexagon DSP executes INT8 YOLO vision; draws ~3.5W under peak inference.",
        "TextBox 160": "Tait-Bryan Ray-Casting: Converts camera ray & ToF laser altitude to ground GPS pins on the fly without hovering.",
        "TextBox 161": "Resilient LoRa P2P Telemetry: 17-byte bit-packed telemetry stream over 3–5+ km in blackout zones (Souli et al. [3], 2024).",
        "TextBox 162": "Anti-Compass Drift VIO: Visual-Inertial Odometry overrides magnetometer in collapsed steel rubble (IEEE standard navigation)."
    }
    for name, text in card_updates.items():
        if name in s2_map:
            tb = s2_map[name]
            tb.text_frame.clear()
            p = tb.text_frame.paragraphs[0]
            r = p.add_run()
            set_run(r, text, font="Calibri", size_pt=14.5, color=(30, 38, 56))

    print("Slide 2: Alignment, thermal claims, UNO Q 4GB/32GB, and heterogeneous AI compute updated successfully.")

    # =========================================================================
    # SLIDE 3: Technical Approach Citations & UNO Q 4GB/32GB
    # =========================================================================
    slide3 = prs.slides[2]
    s3_map = {s.name: s for s in slide3.shapes}

    if "TextBox 56" in s3_map:
        tb56 = s3_map["TextBox 56"]
        tb56.text_frame.clear()
        p = tb56.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "Dual 4K RGB + LWIR Thermal fusion; edge YOLO detects survivor heat anomalies (37°C) & flags surface obstacles for flight avoidance.", 
                font="Calibri", size_pt=15.0, color=(30, 38, 56))

    if "TextBox 76" in s3_map:
        tb76 = s3_map["TextBox 76"]
        tb76.text_frame.clear()
        p = tb76.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "Onboard Triage & LoRa Burst: UAV computes victim priority on-chip & packs coordinates into 17-byte binary frame [3]; broadcasts over 868 MHz.", 
                font="Calibri", size_pt=15.0, color=(30, 38, 56))

    if "TextBox 85" in s3_map:
        tb85 = s3_map["TextBox 85"]
        tb85.text_frame.clear()
        p = tb85.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "Lightweight Offline GCS: Low-power tablet receives 17-byte pins; charts hazard-aware Dijkstra safe walking corridor [1] avoiding live electrical lines.", 
                font="Calibri", size_pt=15.0, color=(30, 38, 56))

    # Update Mission Computer TextBox 112
    if "TextBox 112" in s3_map:
        tb112 = s3_map["TextBox 112"]
        tb112.text_frame.clear()
        p0 = tb112.text_frame.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "Qualcomm Dragonwing QRB2210 (Debian Linux — 4GB RAM, 32GB eMMC)", font="Calibri", size_pt=12.5, color=(228, 236, 247), bold=True)
        p1 = tb112.text_frame.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "Heterogeneous On-Device AI (CPU/GPU/DSP) // Ray-Caster // SX1262 LoRa Driver [3]", font="Calibri", size_pt=12.0, color=(228, 236, 247))

    # Update Tech Stack Edge AI TextBox 132
    for s in slide3.shapes:
        if s.shape_type == 6 and s.name == "Group 130":
            for sub in s.shapes:
                if sub.name == "TextBox 132":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "YOLOv8n INT8 (Detection & Avoidance), SNPE SDK, ONNX, OpenCV", font="Calibri", size_pt=13.5, color=(30, 38, 56))

    print("Slide 3: Citations [1] and [3], UNO Q 4GB/32GB specs, and heterogeneous AI updated.")

    # =========================================================================
    # SLIDE 4: Feasibility, Citations with DOIs, Bouabdallah Purge, BOM ₹37,400
    # =========================================================================
    slide4 = prs.slides[3]
    s4_map = {s.name: s for s in slide4.shapes}

    # Technical Feasibility TextBox 38
    if "TextBox 38" in s4_map:
        tb38 = s4_map["TextBox 38"]
        tb38.text_frame.clear()
        p0 = tb38.text_frame.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "Propulsion Sizing: 38% battery mass fraction, β ≥ 2.0 thrust-to-weight ratio.", font="Calibri", size_pt=16.5, color=(30, 38, 56))
        
        p1 = tb38.text_frame.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "All-Up-Weight: 1.58 kg mass budget (Comfortably under DGCA 2.0 kg Micro Category).", font="Calibri", size_pt=16.5, color=(30, 38, 56))

        p2 = tb38.text_frame.add_paragraph()
        r2 = p2.add_run()
        set_run(r2, "Sub-6W Electronics Payload: Onboard compute draws ~5.5W under peak AI (>96% power for flight).", font="Calibri", size_pt=16.5, color=(30, 38, 56))

    # Financial Feasibility TextBox 54
    if "TextBox 54" in s4_map:
        tb54 = s4_map["TextBox 54"]
        tb54.text_frame.clear()
        p0 = tb54.text_frame.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "Prototype Build: ₹37,400 (Calibrated Prototype — Arduino UNO Q 4GB/32GB).", font="Calibri", size_pt=16.0, color=(30, 38, 56))
        
        p1 = tb54.text_frame.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "Production BOM: ₹85,000 – ₹1,20,000 per unit (10x cheaper than commercial enterprise drones).", font="Calibri", size_pt=16.0, color=(30, 38, 56))

    # Update Challenges to Strategies with detailed citations and remove 2007 paper
    strat_updates = {
        "TextBox 126": "→ Strategy: 868MHz LoRa packet bridge in NLoS canyons [2] (Pérez-Díaz-de-Cerio, IEEE Access 2026, DOI: 10.1109/ACCESS.2026.3731317).",
        "TextBox 135": "→ Strategy: 8-14μm LWIR thermal anomaly detection in dense smoke & fog [1] (Siotia et al., IEEE Access 2026, DOI: 10.1109/ACCESS.2026.3730315).",
        "TextBox 144": "→ Strategy: Visual-Inertial Odometry overrides magnetometer in collapsed steel rubble (IEEE standard navigation).",
        "TextBox 153": "→ Strategy: Notch-filtered EKF & silicone harmonic vibration dampening (IEEE Control Systems & Robotics).",
        "TextBox 162": "→ Strategy: Anti-windup integrator clamping on 250Hz deterministic PID loop (IEEE Industrial Electronics)."
    }
    for name, text in strat_updates.items():
        if name in s4_map:
            tb = s4_map[name]
            tb.text_frame.clear()
            p = tb.text_frame.paragraphs[0]
            r = p.add_run()
            set_run(r, text, font="Calibri", size_pt=15.0, color=(30, 38, 56))

    print("Slide 4: Technical feasibility, BOM ₹37,400, DOIs [1] & [2], and Bouabdallah 2007 purged.")

    # =========================================================================
    # SLIDE 6: Purge Bouabdallah 2007, Reorder [1]-[7], Add Active DOIs & Links
    # =========================================================================
    slide6 = prs.slides[5]
    s6_map = {s.name: s for s in slide6.shapes}

    # Card 01 Header: Siotia et al. [1]
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 35":
            for sub in s.shapes:
                if sub.name == "TextBox 37":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "IIT Jodhpur & Manipal (IEEE Access, Sept 2026) [1]", font="Calibri", size_pt=21.0, color=(31, 73, 125), bold=True)

    if "TextBox 38" in s6_map:
        tb38 = s6_map["TextBox 38"]
        tf38 = tb38.text_frame
        tf38.clear()
        p0 = tf38.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "• 'SwarmSAR-FW: Drone-Based Swarm Search and Rescue in Fire and Water Disasters'", font="Calibri", size_pt=15.0, color=(86, 96, 116), italic=True)
        p1 = tf38.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "• Sourced & validated Hazard-Aware Safe Access Ingress Routing for ground crews & 98.7% triage.", font="Calibri", size_pt=15.0, color=(30, 38, 56))
        p2 = tf38.add_paragraph()
        r2_lbl = p2.add_run()
        set_run(r2_lbl, "DOI: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
        r2_link = p2.add_run()
        set_run(r2_link, "10.1109/ACCESS.2026.3730315 (Direct IEEE Document Link)", font="Calibri", size_pt=12.0, color=(31, 73, 125), italic=True)
        r2_link.hyperlink.address = "https://doi.org/10.1109/ACCESS.2026.3730315"

    # Card 02 Header: UPC Spain [2] & Souli et al. [3]
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 44":
            for sub in s.shapes:
                if sub.name == "TextBox 46":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "UPC Spain & Souli et al. (IEEE Access 2026 / Elsevier 2024) [2, 3]", font="Calibri", size_pt=20.0, color=(31, 73, 125), bold=True)

    if "TextBox 47" in s6_map:
        tb47 = s6_map["TextBox 47"]
        tf47 = tb47.text_frame
        tf47.clear()
        p0 = tf47.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "• 'Long-Range BLE Detection via Drone LoRa Relays' [2] & 'Mission-Critical ROS-LoRa Architecture' [3]", font="Calibri", size_pt=14.5, color=(86, 96, 116), italic=True)
        p1 = tf47.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "• Sourced 868 MHz LoRa off-grid data bridge & 17-byte binary telemetry in cellular blackout zones.", font="Calibri", size_pt=14.5, color=(30, 38, 56))
        p2 = tf47.add_paragraph()
        r2_lbl = p2.add_run()
        set_run(r2_lbl, "DOIs: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
        r2_link = p2.add_run()
        set_run(r2_link, "10.1109/ACCESS.2026.3731317 [2]  |  10.1016/j.comcom.2024.04.015 [3]", font="Calibri", size_pt=12.0, color=(31, 73, 125), italic=True)
        r2_link.hyperlink.address = "https://doi.org/10.1109/ACCESS.2026.3731317"

    # Card 03 Header: TalTech Estonia [4] & SARDO [5]
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 53":
            for sub in s.shapes:
                if sub.name == "TextBox 55":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "TalTech Estonia & SARDO (IEEE Access 2023 / IEEE TMC 2022) [4, 5]", font="Calibri", size_pt=20.0, color=(31, 73, 125), bold=True)

    if "TextBox 56" in s6_map:
        tb56 = s6_map["TextBox 56"]
        tf56 = tb56.text_frame
        tf56.clear()
        p0 = tf56.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "• 'Applying RIS-Based Comm for Collaborative Computing' [4] & 'SARDO RF Victim Localization' [5]", font="Calibri", size_pt=14.5, color=(86, 96, 116), italic=True)
        p1 = tf56.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "• Validated decentralized swarm edge-computing without cloud servers (-32% energy); 1/8th weight vs SDR.", font="Calibri", size_pt=14.5, color=(30, 38, 56))
        p2 = tf56.add_paragraph()
        r2_lbl = p2.add_run()
        set_run(r2_lbl, "DOIs: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
        r2_link = p2.add_run()
        set_run(r2_link, "10.1109/ACCESS.2023.3293737 [4]  |  10.1109/TMC.2022.3168331 [5]", font="Calibri", size_pt=12.0, color=(31, 73, 125), italic=True)
        r2_link.hyperlink.address = "https://doi.org/10.1109/ACCESS.2023.3293737"

    # Card 04 Header: Mishra et al. [6] & van Tilburg [7] (BOUABDALLAH 2007 REPLACED!)
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 62":
            for sub in s.shapes:
                if sub.name == "TextBox 64":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "BITS Pilani & van Tilburg (Elsevier 2020 / Wilderness Med 2017) [6, 7]", font="Calibri", size_pt=20.0, color=(31, 73, 125), bold=True)

    if "TextBox 65" in s6_map:
        tb65 = s6_map["TextBox 65"]
        tf65 = tb65.text_frame
        tf65.clear()
        p0 = tf65.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "• 'Drone Surveillance & Human Action Detection' [6] & 'First Report of Using Drones for SAR' [7]", font="Calibri", size_pt=14.5, color=(86, 96, 116), italic=True)
        p1 = tf65.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "• Validates 2000+ aerial human detection dataset for INT8 YOLO and operational field unboxing protocols.", font="Calibri", size_pt=14.5, color=(30, 38, 56))
        p2 = tf65.add_paragraph()
        r2_lbl = p2.add_run()
        set_run(r2_lbl, "DOIs: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
        r2_link = p2.add_run()
        set_run(r2_link, "10.1016/j.comcom.2020.03.042 [6]  |  10.1016/j.wem.2017.06.004 [7]", font="Calibri", size_pt=12.0, color=(31, 73, 125), italic=True)
        r2_link.hyperlink.address = "https://doi.org/10.1016/j.comcom.2020.03.042"

    prs.save(TARGET_FILE)
    print(f"\nAll v7 changes successfully built and saved to {TARGET_FILE}")

if __name__ == "__main__":
    build_v7()
