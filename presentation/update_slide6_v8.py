"""
Update Slide 6 of SIH26177_v8.pptx to feature exactly 6 research papers, all dated >= 2023:
- Card 1: Siotia et al. (IIT Jodhpur / Manipal), IEEE Access, 2026 [1]
- Card 2: Pérez-Díaz-de-Cerio et al. (UPC Spain) & Souli et al. (Cyprus), IEEE Access 2026 / Elsevier 2024 [2, 3]
- Card 3: Rahbari et al. (TalTech Estonia), IEEE Access, 2023 [4]
- Card 4: Zhou et al. (IEEE TGRS 2023) [5] & Li et al. (IEEE TGRS 2023) [6]

DO NOT TOUCH ANYTHING ELSE IN THE PRESENTATION.
"""

import pptx
from pptx.util import Pt
from pptx.dml.color import RGBColor

TARGET_PPTX = "SIH26177_v8.pptx"

def set_run(r, text, font="Calibri", size_pt=14.5, color=(30, 38, 56), bold=False, italic=False):
    r.text = text
    r.font.name = font
    if size_pt:
        r.font.size = Pt(size_pt)
    if color:
        r.font.color.rgb = RGBColor(*color)
    r.font.bold = bold
    r.font.italic = italic

def update_slide6():
    prs = pptx.Presentation(TARGET_PPTX)
    slide6 = prs.slides[5] # Index 5 is Slide 6

    print("Loaded Slide 6 from", TARGET_PPTX)

    # -------------------------------------------------------------------------
    # CARD 1: Paper [1] - Siotia et al. (2026)
    # -------------------------------------------------------------------------
    # Title in Group 50 -> TextBox 52
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 50":
            for sub in s.shapes:
                if sub.name == "TextBox 52":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "IIT Jodhpur & Manipal Univ. (IEEE Access, Sept 2026) [1]", font="Calibri", size_pt=20.0, color=(31, 73, 125), bold=True)

    # Body in TextBox 53
    tb53 = [s for s in slide6.shapes if s.name == "TextBox 53"][0]
    tb53.text_frame.clear()
    
    p0 = tb53.text_frame.paragraphs[0]
    p0.space_after = Pt(2)
    r0 = p0.add_run()
    set_run(r0, "• 'SwarmSAR-FW: Drone-Based Swarm Search and Rescue in Fire and Water Disasters'", font="Calibri", size_pt=14.5, color=(86, 96, 116), bold=False)

    p1 = tb53.text_frame.add_paragraph()
    p1.space_after = Pt(2)
    r1_h = p1.add_run()
    set_run(r1_h, "• HAZARD-AWARE DIJKSTRA ROUTING: ", font="Calibri", size_pt=14.5, color=(30, 38, 56), bold=True)
    r1_b = p1.add_run()
    set_run(r1_b, "Validates safe ingress routing (98.7% triage accuracy, 4.1s) avoiding debris & power lines.", font="Calibri", size_pt=14.5, color=(60, 70, 90), bold=False)

    p2 = tb53.text_frame.add_paragraph()
    r2_h = p2.add_run()
    set_run(r2_h, "DOI: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
    r2_u = p2.add_run()
    set_run(r2_u, "10.1109/ACCESS.2026.3730315 (Direct IEEE Document Link)", font="Calibri", size_pt=12.0, color=(0, 0, 255), bold=False)

    print("Card 1 updated.")

    # -------------------------------------------------------------------------
    # CARD 2: Papers [2, 3] - Pérez-Díaz-de-Cerio (2026) & Souli et al. (2024)
    # -------------------------------------------------------------------------
    # Title in Group 62 -> TextBox 64
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 62":
            for sub in s.shapes:
                if sub.name == "TextBox 64":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "UPC Spain & Souli et al. (IEEE Access 2026 / Elsevier 2024) [2, 3]", font="Calibri", size_pt=20.0, color=(31, 73, 125), bold=True)

    # Body in TextBox 65
    tb65 = [s for s in slide6.shapes if s.name == "TextBox 65"][0]
    tb65.text_frame.clear()

    p0 = tb65.text_frame.paragraphs[0]
    p0.space_after = Pt(2)
    r0 = p0.add_run()
    set_run(r0, "• 'Long-Range BLE via Drone LoRa Relays' [2] & 'Mission-Critical ROS-LoRa Architecture' [3]", font="Calibri", size_pt=14.5, color=(86, 96, 116), bold=False)

    p1 = tb65.text_frame.add_paragraph()
    p1.space_after = Pt(2)
    r1_h = p1.add_run()
    set_run(r1_h, "• 868 MHZ LORA & 17-BYTE TELEMETRY: ", font="Calibri", size_pt=14.5, color=(30, 38, 56), bold=True)
    r1_b = p1.add_run()
    set_run(r1_b, "Validates off-grid NLoS canyon relay and 17-byte bit-packed triage frames during blackouts.", font="Calibri", size_pt=14.5, color=(60, 70, 90), bold=False)

    p2 = tb65.text_frame.add_paragraph()
    r2_h = p2.add_run()
    set_run(r2_h, "DOIs: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
    r2_u = p2.add_run()
    set_run(r2_u, "10.1109/ACCESS.2026.3731317 [2]  |  10.1016/j.comcom.2024.04.015 [3]", font="Calibri", size_pt=12.0, color=(0, 0, 255), bold=False)

    print("Card 2 updated.")

    # -------------------------------------------------------------------------
    # CARD 3: Paper [4] - Rahbari et al. (TalTech Estonia, 2023)
    # -------------------------------------------------------------------------
    # Title in Group 74 -> TextBox 76
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 74":
            for sub in s.shapes:
                if sub.name == "TextBox 76":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "TalTech Estonia (IEEE Access, July 2023) [4]", font="Calibri", size_pt=20.0, color=(31, 73, 125), bold=True)

    # Body in TextBox 77
    tb77 = [s for s in slide6.shapes if s.name == "TextBox 77"][0]
    tb77.text_frame.clear()

    p0 = tb77.text_frame.paragraphs[0]
    p0.space_after = Pt(2)
    r0 = p0.add_run()
    set_run(r0, "• 'Applying RIS-Based Communication for Collaborative Computing in a Swarm of Drones'", font="Calibri", size_pt=14.5, color=(86, 96, 116), bold=False)

    p1 = tb77.text_frame.add_paragraph()
    p1.space_after = Pt(2)
    r1_h = p1.add_run()
    set_run(r1_h, "• DECENTRALIZED EDGE COMPUTE: ", font="Calibri", size_pt=14.5, color=(30, 38, 56), bold=True)
    r1_b = p1.add_run()
    set_run(r1_b, "Validates autonomous on-device computing (-32% energy, -18% latency) with zero cloud reliance.", font="Calibri", size_pt=14.5, color=(60, 70, 90), bold=False)

    p2 = tb77.text_frame.add_paragraph()
    r2_h = p2.add_run()
    set_run(r2_h, "DOI: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
    r2_u = p2.add_run()
    set_run(r2_u, "10.1109/ACCESS.2023.3293737 (Direct IEEE Document Link)", font="Calibri", size_pt=12.0, color=(0, 0, 255), bold=False)

    print("Card 3 updated.")

    # -------------------------------------------------------------------------
    # CARD 4: Papers [5, 6] - IEEE TGRS 2023 (Multimodal RGB-T & VIO)
    # -------------------------------------------------------------------------
    # Title in Group 86 -> TextBox 88
    for s in slide6.shapes:
        if s.shape_type == 6 and s.name == "Group 86":
            for sub in s.shapes:
                if sub.name == "TextBox 88":
                    sub.text_frame.clear()
                    p = sub.text_frame.paragraphs[0]
                    r = p.add_run()
                    set_run(r, "IEEE Trans. Geoscience & Remote Sensing (IEEE TGRS 2023) [5, 6]", font="Calibri", size_pt=19.5, color=(31, 73, 125), bold=True)

    # Body in TextBox 89
    tb89 = [s for s in slide6.shapes if s.name == "TextBox 89"][0]
    tb89.text_frame.clear()

    p0 = tb89.text_frame.paragraphs[0]
    p0.space_after = Pt(2)
    r0 = p0.add_run()
    set_run(r0, "• 'Unregistered RGB-T Salient Detection' [5] & 'Monocular VIO in GNSS-Denied Zone' [6]", font="Calibri", size_pt=14.5, color=(86, 96, 116), bold=False)

    p1 = tb89.text_frame.add_paragraph()
    p1.space_after = Pt(2)
    r1_h = p1.add_run()
    set_run(r1_h, "• MULTI-SPECTRAL AI & VIO SLAM: ", font="Calibri", size_pt=14.5, color=(30, 38, 56), bold=True)
    r1_b = p1.add_run()
    set_run(r1_b, "Validates 1080p RGB + LWIR thermal fusion and anti-drift VIO state estimation in metallic rubble.", font="Calibri", size_pt=14.5, color=(60, 70, 90), bold=False)

    p2 = tb89.text_frame.add_paragraph()
    r2_h = p2.add_run()
    set_run(r2_h, "DOIs: ", font="Calibri", size_pt=12.0, color=(179, 90, 0), bold=True)
    r2_u = p2.add_run()
    set_run(r2_u, "10.1109/TGRS.2023.3332179 [5]  |  10.1109/TGRS.2023.3323519 [6]", font="Calibri", size_pt=12.0, color=(0, 0, 255), bold=False)

    print("Card 4 updated.")

    prs.save(TARGET_PPTX)
    print("Successfully updated Slide 6 of", TARGET_PPTX)

if __name__ == "__main__":
    update_slide6()
