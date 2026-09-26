import pptx
from pptx.dml.color import RGBColor
from pptx.util import Pt

def set_strategy_text(tb_shape, strategy_text):
    tb_shape.clear()
    p = tb_shape.paragraphs[0]
    
    r1 = p.add_run()
    r1.text = "→ Strategy: "
    r1.font.name = "Calibri"
    r1.font.size = Pt(16.0)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0xB3, 0x5A, 0x00) # Deep amber
    
    r2 = p.add_run()
    r2.text = strategy_text
    r2.font.name = "Calibri"
    r2.font.size = Pt(16.0)
    r2.font.color.rgb = RGBColor(0x1E, 0x26, 0x38) # Dark slate

def set_card_header(group_shape, header_text):
    tb = group_shape.shapes[1]
    tf = tb.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = header_text
    r.font.name = "Calibri"
    r.font.size = Pt(21.74)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

def set_card_body(tb_shape, title_text, desc_text):
    tf = tb_shape.text_frame
    tf.clear()
    
    # Paragraph 0 (Paper Title in Italics)
    p0 = tf.paragraphs[0]
    r0 = p0.add_run()
    r0.text = title_text
    r0.font.name = "Calibri"
    r0.font.size = Pt(15.5)
    r0.font.italic = True
    r0.font.color.rgb = RGBColor(86, 96, 116)
    
    # Paragraph 1 (Findings / Engineering Application)
    p1 = tf.add_paragraph()
    r1 = p1.add_run()
    r1.text = desc_text
    r1.font.name = "Calibri"
    r1.font.size = Pt(15.5)
    r1.font.color.rgb = RGBColor(30, 38, 56)

def update_slides():
    filepath = "Copy of SIH26177_v6.pptx.pptx"
    prs = pptx.Presentation(filepath)
    
    # ==========================================
    # 1. UPDATE SLIDE 4: CHALLENGES → STRATEGIES (IEEE SOTA)
    # ==========================================
    slide4 = prs.slides[3] # Slide 4 (0-indexed)
    
    # Challenge 1 (TextBox 126, shape index 45): Comms Blackout
    set_strategy_text(
        slide4.shapes[45].text_frame,
        "868MHz LoRa packet bridge in NLoS canyons (Pérez-Díaz-de-Cerio et al., IEEE Access 2026)."
    )
    
    # Challenge 2 (TextBox 135, shape index 49): Smoke, Mud Slush & Darkness
    set_strategy_text(
        slide4.shapes[49].text_frame,
        "8-14μm LWIR thermal fusion in dense smoke & fire (Siotia et al., IEEE Access 2026)."
    )
    
    # Challenge 3 (TextBox 144, shape index 53): Rubble Steel Magnetometer Distortion
    set_strategy_text(
        slide4.shapes[53].text_frame,
        "Visual-Inertial Odometry overrides magnetometer in collapsed rebar (IEEE)."
    )
    
    # Challenge 4 (TextBox 153, shape index 57): Propeller Vibration Sensor Noise
    set_strategy_text(
        slide4.shapes[57].text_frame,
        "Notch-filtered EKF & harmonic vibration dampening (Bouabdallah, IEEE IROS)."
    )
    
    # Challenge 5 (TextBox 162, shape index 61): Actuator Saturation in Gusts
    set_strategy_text(
        slide4.shapes[61].text_frame,
        "Anti-windup integrator clamping on 400Hz PID loop (Bouabdallah, IEEE ICRA)."
    )
    
    # ==========================================
    # 2. UPDATE SLIDE 6: RESEARCH & REFERENCES (CHRONOLOGICAL DESCENDING)
    # ==========================================
    slide6 = prs.slides[5] # Slide 6 (0-indexed)
    
    # CARD 01: [SEPTEMBER 2026] IIT Jodhpur & Manipal (IEEE Access)
    # Group 35 (shape 13), TextBox 38 (shape 14)
    set_card_header(slide6.shapes[13], "IIT Jodhpur & Manipal (IEEE Access, Sept 2026)")
    set_card_body(
        slide6.shapes[14],
        "• 'SwarmSAR-FW: Drone-Based Swarm Search and Rescue in Fire and Water Disasters'",
        "• Sourced & validated Hazard-Aware Safe Access Ingress Routing for ground crews & 98.7% triage."
    )
    
    # CARD 02: [SEPTEMBER 2026 / 2024] UPC Spain & Souli et al. (IEEE Access / Elsevier)
    # Group 44 (shape 17), TextBox 47 (shape 18)
    set_card_header(slide6.shapes[17], "UPC Spain & Souli et al. (IEEE Access 2026 / Elsevier 2024)")
    set_card_body(
        slide6.shapes[18],
        "• 'Long-Range BLE Detection via Drone LoRa Relays' & 'Mission-Critical ROS-LoRa Architecture'",
        "• Sourced 868 MHz LoRa off-grid data bridge & 17-byte binary telemetry in cellular blackout zones."
    )
    
    # CARD 03: [JULY 2023] TalTech Estonia (IEEE Access)
    # Group 53 (shape 21), TextBox 56 (shape 22)
    set_card_header(slide6.shapes[21], "TalTech Estonia (IEEE Access, 2023)")
    set_card_body(
        slide6.shapes[22],
        "• 'Applying RIS-Based Communication for Collaborative Computing in a Swarm of Drones'",
        "• Validated decentralized swarm edge-computing without cloud servers (-32% energy, -18% latency)."
    )
    
    # CARD 04: [2007] Dr. Samir Bouabdallah (EPFL / IEEE ICRA)
    # Group 62 (shape 25), TextBox 65 (shape 26)
    set_card_header(slide6.shapes[25], "Dr. Samir Bouabdallah (EPFL Thesis 3727 / IEEE ICRA, 2007)")
    set_card_body(
        slide6.shapes[26],
        "• 'Design and Control of Quadrotors with Application to Autonomous Flying'",
        "• Sourced 12-state rigid-body dynamics, 90/10 electrical propulsion ratio, and anti-windup integrator."
    )
    
    prs.save(filepath)
    print(f"Successfully updated Slide 4 and Slide 6 in {filepath}!")

if __name__ == "__main__":
    update_slides()
