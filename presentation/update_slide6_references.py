import sys
import pptx
from pptx.dml.color import RGBColor
from pptx.util import Pt

def update_presentation():
    input_file = "Copy of SIH26177_v6.pptx.pptx"
    prs = pptx.Presentation(input_file)
    slide = prs.slides[5] # Slide 6 (0-indexed)

    # 1. Update Card 02 (Group 44 & TextBox 47) -> IIT Jodhpur & Manipal (IEEE Access, Sept 2026)
    # Header: Group 44, shape 1 (TextBox 46)
    header_g44 = slide.shapes[17].shapes[1]
    p = header_g44.text_frame.paragraphs[0]
    p.text = "IIT Jodhpur & Manipal (IEEE Access, Sept 2026)"
    for r in p.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(21.74)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    # Body: TextBox 47 (Shape 18)
    body_tb47 = slide.shapes[18].text_frame
    p0 = body_tb47.paragraphs[0]
    p0.text = "• 'SwarmSAR-FW: Drone-Based Swarm Search and Rescue in Fire and Water Disasters'"
    for r in p0.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(86, 96, 116)
    
    p1 = body_tb47.paragraphs[1] if len(body_tb47.paragraphs) > 1 else body_tb47.add_paragraph()
    p1.text = "• Sourced & validated Hazard-Aware Safe Access Ingress Routing for ground crews & 98.7% triage."
    for r in p1.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.color.rgb = RGBColor(30, 38, 56)

    # 2. Update Card 03 (Group 53 & TextBox 56) -> UPC Spain & Souli et al. (IEEE Access 2026 / Elsevier 2024)
    # Header: Group 53, shape 1 (TextBox 55)
    header_g53 = slide.shapes[21].shapes[1]
    p = header_g53.text_frame.paragraphs[0]
    p.text = "UPC Spain & Souli et al. (IEEE Access 2026 / Elsevier 2024)"
    for r in p.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(21.74)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    # Body: TextBox 56 (Shape 22)
    body_tb56 = slide.shapes[22].text_frame
    p0 = body_tb56.paragraphs[0]
    p0.text = "• 'Long-Range BLE Detection via Drone LoRa Relays' & 'Mission-Critical ROS-LoRa Architecture'"
    for r in p0.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(86, 96, 116)
    
    p1 = body_tb56.paragraphs[1] if len(body_tb56.paragraphs) > 1 else body_tb56.add_paragraph()
    p1.text = "• Sourced 868 MHz LoRa off-grid data bridge & 17-byte binary telemetry in cellular blackout zones."
    for r in p1.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.color.rgb = RGBColor(30, 38, 56)

    # 3. Update Card 04 (Group 62 & TextBox 65) -> TalTech Estonia (IEEE Access, 2023)
    # Header: Group 62, shape 1 (TextBox 64)
    header_g62 = slide.shapes[25].shapes[1]
    p = header_g62.text_frame.paragraphs[0]
    p.text = "TalTech Estonia (IEEE Access, 2023)"
    for r in p.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(21.74)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    # Body: TextBox 65 (Shape 26)
    body_tb65 = slide.shapes[26].text_frame
    p0 = body_tb65.paragraphs[0]
    p0.text = "• 'Applying RIS-Based Communication for Collaborative Computing in a Swarm of Drones'"
    for r in p0.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(86, 96, 116)
    
    p1 = body_tb65.paragraphs[1] if len(body_tb65.paragraphs) > 1 else body_tb65.add_paragraph()
    p1.text = "• Validated decentralized swarm edge-computing without cloud servers (-32% energy, -18% latency)."
    for r in p1.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.color.rgb = RGBColor(30, 38, 56)

    # 4. Also update Card 01 text slightly to ensure bullets align
    body_tb38 = slide.shapes[14].text_frame
    p0 = body_tb38.paragraphs[0]
    if not p0.text.startswith("• "):
        p0.text = "• " + p0.text
    for r in p0.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(15.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(86, 96, 116)
    
    if len(body_tb38.paragraphs) > 1:
        p1 = body_tb38.paragraphs[1]
        if not p1.text.startswith("• "):
            p1.text = "• " + p1.text
        for r in p1.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(15.5)
            r.font.color.rgb = RGBColor(30, 38, 56)

    # 5. Update Documented Subsystems: Shape 43 (TextBox 103)
    tb103 = slide.shapes[43].text_frame
    tb103.clear()
    
    items = [
        "1. docs/research_papers_synthesis_2026.md",
        "2. docs/prototype_bom_and_financial_viability.md",
        "3. docs/ros_lora_mission_critical_uav_swarm_research.md",
        "4. docs/bouabdallah_quadrotor_research_findings.md"
    ]
    for idx, item in enumerate(items):
        if idx == 0:
            p = tb103.paragraphs[0]
        else:
            p = tb103.add_paragraph()
        p.text = item
        for r in p.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(16.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(30, 38, 56)

    # 6. Update Github Repo link text in Group 96 shape 1
    gh_tb = slide.shapes[40].shapes[1]
    p_gh = gh_tb.text_frame.paragraphs[0]
    p_gh.text = "github.com/jvstin47/Phoenix-SIH26177-SAR-UAV"
    for r in p_gh.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(27, 85, 226)

    # Save to original and to an updated copy
    output_updated = "Copy of SIH26177_v6.pptx.pptx"
    prs.save(output_updated)
    print(f"Successfully updated and saved {output_updated}")

if __name__ == "__main__":
    update_presentation()
