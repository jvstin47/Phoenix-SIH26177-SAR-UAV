"""
Apply all 10 remaining critique refinements to Copy of SIH26177_v7.pptx.pptx:
1. Purge "NPU" -> "heterogeneous edge-AI compute (CPU/GPU/DSP)" / "QRB2210 performs INT8 inference onboard".
2. Purge "through mud" -> "detect human thermal signatures in darkness, smoke-obscured environments, and partially exposed debris".
3. Purge "preserves 90% power" -> "sub-5 W electronics power budget, minimizing non-propulsion energy consumption".
4. Upgrade Geolocation -> "synchronized GNSS, attitude estimation, camera geometry and downward ToF altitude to georeference victims in real time without hovering".
5. Purge "live wires" -> "detected electrical hazards and unstable debris".
6. Purge "sovereign" -> "infrastructure-independent, offline-capable aerial reconnaissance".
7. Refactor Slide 2 Barriers to the 4 Operational Failures (Connectivity, Visibility, Localization, Access).
8. Refactor Slide 2 Solution box with the exact refined pitch text.
"""

import pptx
from pptx.dml.color import RGBColor
from pptx.util import Pt

TARGET_FILE = "Copy of SIH26177_v7.pptx.pptx"

def set_run(r, text, font="Calibri", size_pt=14.0, color=(30, 38, 56), bold=False, italic=False):
    r.text = text
    r.font.name = font
    if size_pt:
        r.font.size = Pt(size_pt)
    if color:
        r.font.color.rgb = RGBColor(*color)
    r.font.bold = bold
    r.font.italic = italic

def apply_bulletproof_refinements():
    prs = pptx.Presentation(TARGET_FILE)

    # =========================================================================
    # SLIDE 2: Refined Four Operational Failures & Precise Solution Pitch
    # =========================================================================
    slide2 = prs.slides[1]
    s2_map = {s.name: s for s in slide2.shapes}

    # TextBox 156: The Four Operational Failures
    if "TextBox 156" in s2_map:
        tb156 = s2_map["TextBox 156"]
        tf156 = tb156.text_frame
        tf156.clear()

        p = tf156.paragraphs[0]
        r = p.add_run()
        set_run(r, "CRITICAL DISASTER BARRIERS — FOUR OPERATIONAL FAILURES:", 
                font="Calibri", size_pt=14.5, color=(180, 40, 30), bold=True)

        failures = [
            ("01 — CONNECTIVITY: ", "Cellular and power infrastructure may be unavailable; cloud-dependent drones rendered completely inoperable."),
            ("02 — VISIBILITY: ", "Darkness, smoke and dense debris severely constrain conventional RGB electro-optical observation."),
            ("03 — LOCALIZATION: ", "Spotting a casualty is not enough; rescue teams require precise, actionable ground GPS coordinates."),
            ("04 — ACCESS: ", "Secondary hazards (electrical lines, shifting rubble, gas voids) make direct rescue paths dangerous.")
        ]
        for f_title, f_desc in failures:
            p = tf156.add_paragraph()
            r_b = p.add_run()
            set_run(r_b, f_title, font="Calibri", size_pt=13.5, color=(30, 38, 56), bold=True)
            r_t = p.add_run()
            set_run(r_t, f_desc, font="Calibri", size_pt=13.5, color=(30, 38, 56), bold=False)

    # TextBox 157: The Closed-Loop Rescue Solution Pitch
    if "TextBox 157" in s2_map:
        tb157 = s2_map["TextBox 157"]
        tf157 = tb157.text_frame
        tf157.clear()

        p = tf157.paragraphs[0]
        r = p.add_run()
        set_run(r, "Project Phoenix: Autonomous, field-deployable multirotor closing the aerial-to-ground rescue loop:", 
                font="Calibri", size_pt=14.5, color=(31, 73, 125), bold=True)

        solutions = [
            ("DUAL-BRAIN HARDWARE SPLIT: ", "QRB2210 MPU performs INT8 edge-AI on Linux; STM32U585 MCU runs deterministic 250 Hz flight loop on Zephyr."),
            ("MULTIMODAL PERCEPTION: ", "Fuses 4K RGB + LWIR thermal (8–14μm) to detect human heat signatures in darkness, smoke & partially exposed debris."),
            ("CONTINUOUS GEOREFERENCING: ", "Synchronized GNSS, attitude, camera geometry & ToF altitude georeference victims in real time without hovering."),
            ("OFFLINE RESCUE ROUTING: ", "Prioritizes triage on-chip; broadcasts 17-byte LoRa packets to chart Dijkstra corridors avoiding hazards [1, 3].")
        ]
        for s_title, s_desc in solutions:
            p = tf157.add_paragraph()
            r_b = p.add_run()
            set_run(r_b, s_title, font="Calibri", size_pt=13.5, color=(30, 38, 56), bold=True)
            r_t = p.add_run()
            set_run(r_t, s_desc, font="Calibri", size_pt=13.5, color=(30, 38, 56), bold=False)

    # Bottom Cards: Precise wording
    bottom_cards = {
        "TextBox 158": "Arduino UNO Q (4GB LPDDR4 / 32GB eMMC): Qualcomm Dragonwing QRB2210 MPU + STM32U585 MCU on a unified 40g board.",
        "TextBox 159": "Sub-5W Edge AI: QRB2210 heterogeneous compute executes INT8 YOLO inference, minimizing non-propulsion power draw.",
        "TextBox 160": "Dynamic Georeferencing: Synchronized attitude, camera ray & ToF altitude pin ground GPS in real time without hovering.",
        "TextBox 161": "Compact LoRa Telemetry: 17-byte bit-packed triage stream over 3–5+ km in blackout zones (Souli et al. [3], 2024).",
        "TextBox 162": "Anti-Compass Drift VIO: Visual-Inertial Odometry overrides magnetometer in collapsed steel rubble (IEEE standard navigation)."
    }
    for name, text in bottom_cards.items():
        if name in s2_map:
            tb = s2_map[name]
            tb.text_frame.clear()
            p = tb.text_frame.paragraphs[0]
            r = p.add_run()
            set_run(r, text, font="Calibri", size_pt=14.0, color=(30, 38, 56))

    print("Slide 2: Four Failures, Closed-Loop Solution, and Bottom Cards refined cleanly.")

    # =========================================================================
    # SLIDE 3: Technical Approach Steps & Architecture
    # =========================================================================
    slide3 = prs.slides[2]
    s3_map = {s.name: s for s in slide3.shapes}

    # Step 3: Thermal perception
    if "TextBox 56" in s3_map:
        tb56 = s3_map["TextBox 56"]
        tb56.text_frame.clear()
        p = tb56.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "Dual 4K RGB + LWIR Thermal fusion; edge YOLO detects survivor heat anomalies in darkness, smoke & partially exposed debris.", 
                font="Calibri", size_pt=14.5, color=(30, 38, 56))

    # Step 4: Georeferencing
    if "TextBox 66" in s3_map:
        tb66 = s3_map["TextBox 66"]
        tb66.text_frame.clear()
        p = tb66.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "Synchronized GNSS, attitude, camera geometry & downward ToF altitude georeference detected victims on the fly without hovering.", 
                font="Calibri", size_pt=14.5, color=(30, 38, 56))

    # Step 6: Route planning
    if "TextBox 85" in s3_map:
        tb85 = s3_map["TextBox 85"]
        tb85.text_frame.clear()
        p = tb85.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "Offline GCS converts survivor pins & mapped hazards into an actionable Dijkstra rescue corridor [1], avoiding electrical & debris hazards.", 
                font="Calibri", size_pt=14.5, color=(30, 38, 56))

    # Mission Computer Box
    if "TextBox 112" in s3_map:
        tb112 = s3_map["TextBox 112"]
        tb112.text_frame.clear()
        p0 = tb112.text_frame.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "Qualcomm Dragonwing QRB2210 (Debian Linux — 4GB RAM, 32GB eMMC)", font="Calibri", size_pt=12.5, color=(228, 236, 247), bold=True)
        p1 = tb112.text_frame.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "Onboard INT8 Edge-AI Inference // Georeferencing Pipeline // SX1262 LoRa Telemetry Driver [3]", font="Calibri", size_pt=12.0, color=(228, 236, 247))

    print("Slide 3: Perception, georeferencing, and rescue routing refined.")

    # =========================================================================
    # SLIDE 4: Feasibility & Strategy Claims
    # =========================================================================
    slide4 = prs.slides[3]
    s4_map = {s.name: s for s in slide4.shapes}

    # Technical Feasibility
    if "TextBox 38" in s4_map:
        tb38 = s4_map["TextBox 38"]
        tb38.text_frame.clear()
        p0 = tb38.text_frame.paragraphs[0]
        r0 = p0.add_run()
        set_run(r0, "Propulsion Sizing: 38% battery mass fraction, β ≥ 2.0 thrust-to-weight ratio.", font="Calibri", size_pt=16.0, color=(30, 38, 56))
        
        p1 = tb38.text_frame.add_paragraph()
        r1 = p1.add_run()
        set_run(r1, "Aircraft Mass: 1.58 kg measured mass budget (Compliant with DGCA Micro-UAV < 2.0 kg).", font="Calibri", size_pt=16.0, color=(30, 38, 56))

        p2 = tb38.text_frame.add_paragraph()
        r2 = p2.add_run()
        set_run(r2, "Electronics Budget: Sub-5 W onboard compute & sensing stack, minimizing non-propulsion energy draw.", font="Calibri", size_pt=16.0, color=(30, 38, 56))

    # Challenge 2 Strategy
    if "TextBox 135" in s4_map:
        tb135 = s4_map["TextBox 135"]
        tb135.text_frame.clear()
        p = tb135.text_frame.paragraphs[0]
        r = p.add_run()
        set_run(r, "→ Strategy: 8–14μm LWIR thermal detection of casualties & debris interfaces in smoke/fog [1] (Siotia, IEEE Access 2026).", 
                font="Calibri", size_pt=15.0, color=(30, 38, 56))

    print("Slide 4: Sub-5W electronics budget and thermal strategy refined.")

    prs.save(TARGET_FILE)
    print(f"\nAll bulletproof refinements saved to {TARGET_FILE}")

if __name__ == "__main__":
    apply_bulletproof_refinements()
