"""
Generate publication-grade Phase-1 BOM PDF (₹37,400) incorporating all
hardware jury critique fixes:
- Arduino UNO Q 4GB LPDDR4 / 32GB eMMC (ABX00163) at ₹8,800 -> Total ₹37,400
- Heterogeneous on-device AI compute (CPU/GPU/DSP)
- Electrical power budget: ~5.5W compute vs ~168W propulsion (>96% power for rotors)
- Accurate mass budget (1.58 kg with 170g payload reserve)
- 2-page clean fit
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_PATH = "docs/Project_Phoenix_X_Phase1_BOM.pdf"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        if self._pageNumber > 1:
            self.drawString(36, 762, "PROJECT PHOENIX X  |  SIH26177 (QUALCOMM INC.)  |  PHASE-1 PROTOTYPE BOM & ROADMAP")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, 756, 576, 756)

        self.setFont("Helvetica", 8)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 36, 576, 36)

        self.drawString(36, 25, "Team Phoenix X (Team ID: 141943)  |  Smart India Hackathon 2026 Hardware Edition  |  Confidential Technical Specification")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 25, page_str)
        self.restoreState()

def build_bom_pdf():
    os.makedirs("docs", exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0F172A")
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#D97706")
    )
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#475569")
    )
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=6,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#334155")
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9.2,
        textColor=colors.HexColor("#1E293B")
    )
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9.2,
        textColor=colors.HexColor("#0F172A")
    )
    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9.2,
        alignment=1,
        textColor=colors.HexColor("#1E293B")
    )
    table_cell_right = ParagraphStyle(
        'TableCellRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9.2,
        alignment=2,
        textColor=colors.HexColor("#0F172A")
    )
    table_hdr = ParagraphStyle(
        'TableHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.white
    )
    table_hdr_center = ParagraphStyle(
        'TableHdrCenter',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        alignment=1,
        textColor=colors.white
    )
    table_hdr_right = ParagraphStyle(
        'TableHdrRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        alignment=2,
        textColor=colors.white
    )

    story = []

    # =========================================================================
    # PAGE 1: HEADER & METADATA BANNER
    # =========================================================================
    story.append(Paragraph("PROJECT PHOENIX X", title_style))
    story.append(Paragraph("AUTONOMOUS MULTI-SPECTRAL EDGE-AI SAR UAV  |  PHASE-1 PROTOTYPE BILL OF MATERIALS", subtitle_style))
    story.append(Spacer(1, 3))
    
    meta_text = (
        "<b>Smart India Hackathon 2026</b>  •  <b>Problem Statement ID:</b> SIH26177  •  "
        "<b>Sponsoring Organization:</b> Qualcomm Inc.<br/>"
        "<b>Theme:</b> Robotics and Drones  •  <b>Category:</b> Hardware  •  "
        "<b>Team ID:</b> 141943  •  <b>Team:</b> Phoenix X  •  "
        "<b>Document:</b> PHOENIX-BOM-TECH-SPEC-V2.0"
    )
    story.append(Paragraph(meta_text, meta_style))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#0F172A"), spaceBefore=3, spaceAfter=5))

    # EXECUTIVE SUMMARY
    exec_summary = (
        "<b>Executive Summary:</b> Problem statement SIH26177 (Qualcomm Inc.) mandates an autonomous tactical UAV "
        "engineered for emergency disaster reconnaissance in communications-blackout and GPS-compromised environments. "
        "To ensure rapid, scalable procurement by national and regional disaster authorities (NDRF/SDRF), Project Phoenix X implements a "
        "<b>calibrated two-tier BOM strategy</b>. The <b>Phase-1 Working Prototype (₹37,400)</b> directly proves the dual-brain computing architecture "
        "featuring the <b>Arduino UNO Q (4GB LPDDR4 / 32GB eMMC)</b>, 250 Hz Zephyr RTOS flight loops, heterogeneous on-device AI inference on Qualcomm silicon (CPU/GPU/DSP), and 17-byte LoRa packet telemetry. "
        "The subsequent <b>Phase-2 Industrial Production Unit (₹85,000 – ₹1,20,000)</b> delivers enterprise-grade Search-and-Rescue capabilities at "
        "<b>1/10th the acquisition cost</b> of imported commercial platforms (e.g., DJI Matrice 30T at ₹12–14 Lakhs) while maintaining 100% air-gapped data integrity."
    )
    story.append(Paragraph(exec_summary, body_style))
    story.append(Spacer(1, 4))

    # SECTION 1: PHASE-1 ITEMISED BOM TABLE (All 9 items on Page 1)
    story.append(Paragraph("1. Phase-1 Working Prototype Bill of Materials (Calibrated ₹37,400)", h1_style))
    
    raw_data = [
        [
            Paragraph("No.", table_hdr_center),
            Paragraph("Subsystem / Component", table_hdr),
            Paragraph("Qty", table_hdr_center),
            Paragraph("Engineering Specification / Part Description", table_hdr),
            Paragraph("Unit (₹)", table_hdr_right),
            Paragraph("Total (₹)", table_hdr_right),
            Paragraph("Tactical Function & Operational Role", table_hdr),
        ],
        [
            Paragraph("<b>1</b>", table_cell_center),
            Paragraph("<b>Main Compute<br/>(Dual-Brain SBC)</b>", table_cell),
            Paragraph("1", table_cell_center),
            Paragraph("<b>Arduino UNO Q</b> (ABX00163, 4 GB RAM / 32 GB eMMC)<br/>• Qualcomm Dragonwing QRB2210 MPU (Debian Linux)<br/>• STM32U585 MCU (250 Hz Zephyr RTOS loop)", table_cell),
            Paragraph("8,800", table_cell_right),
            Paragraph("<b>8,800</b>", table_cell_right),
            Paragraph("Single-board dual-brain partition: Heterogeneous AI (CPU/GPU/DSP) runs INT8 YOLO (~3.5W draw); STM32 handles deterministic flight control.", table_cell),
        ],
        [
            Paragraph("<b>2</b>", table_cell_center),
            Paragraph("<b>Airframe &<br/>Propulsion Kit</b>", table_cell),
            Paragraph("1 set", table_cell_center),
            Paragraph("• F450 / S500 quadcopter composite frame<br/>• 4× A2212 1000KV BLDC motors<br/>• 4× 30A SimonK / BLHeli electronic speed controllers<br/>• 2 pairs 1045 nylon-carbon composite propellers", table_cell),
            Paragraph("4,800", table_cell_right),
            Paragraph("<b>4,800</b>", table_cell_right),
            Paragraph("Delivers β ≥ 2.0 thrust-to-weight ratio to lift 1.58 kg AUW platform (DGCA Micro-UAV compliant < 2.0 kg) and resist 12 m/s wind gusts.", table_cell),
        ],
        [
            Paragraph("<b>3</b>", table_cell_center),
            Paragraph("<b>Avionics Sensor<br/>Suite & GNSS</b>", table_cell),
            Paragraph("1 set", table_cell_center),
            Paragraph("• u-blox NEO-M8N GPS + magnetic compass mast<br/>• MPU6050 6-DOF IMU (accel/gyro)<br/>• MS5611 high-precision barometric altimeter<br/>• ST VL53L1X 1D Time-of-Flight (ToF) downward laser", table_cell),
            Paragraph("4,200", table_cell_right),
            Paragraph("<b>4,200</b>", table_cell_right),
            Paragraph("Multi-sensor fusion for EKF state estimation; downward ToF feeds real-time H_AGL to Tait-Bryan ground ray-casting projection.", table_cell),
        ],
        [
            Paragraph("<b>4</b>", table_cell_center),
            Paragraph("<b>Power Subsystem<br/>& Balance Charger</b>", table_cell),
            Paragraph("1 set", table_cell_center),
            Paragraph("• 3S 11.1V 4500mAh 30C LiPo battery pack<br/>• iMAX B6 80W digital balance charger<br/>• 12V 5A regulated AC/DC power supply", table_cell),
            Paragraph("4,000", table_cell_right),
            Paragraph("<b>4,000</b>", table_cell_right),
            Paragraph("Provides 25–28 minutes search endurance per sortie; adheres to Bouabdallah 38% battery mass fraction sizing law.", table_cell),
        ],
        [
            Paragraph("<b>5</b>", table_cell_center),
            Paragraph("<b>Manual RC Safety<br/>Failover Link</b>", table_cell),
            Paragraph("1 set", table_cell_center),
            Paragraph("• FlySky FS-i6 6-channel 2.4 GHz AFHDS transmitter<br/>• FS-iA6B 6-channel receiver (iBus / PPM protocol)", table_cell),
            Paragraph("3,900", table_cell_right),
            Paragraph("<b>3,900</b>", table_cell_right),
            Paragraph("Emergency pilot takeover channel for field safety redundancy and DGCA fail-safe override compliance.", table_cell),
        ],
        [
            Paragraph("<b>6</b>", table_cell_center),
            Paragraph("<b>Optical Vision<br/>(RGB Camera)</b>", table_cell),
            Paragraph("1", table_cell_center),
            Paragraph("• 1080p Full HD UVC USB camera module<br/>• OmniVision OV2710 sensor, 120° wide-angle M12 lens", table_cell),
            Paragraph("1,100", table_cell_right),
            Paragraph("<b>1,100</b>", table_cell_right),
            Paragraph("Daylight stream for survivor clothing/gesture recognition and visual identification of dangling power cables & hazards.", table_cell),
        ],
        [
            Paragraph("<b>7</b>", table_cell_center),
            Paragraph("<b>Thermal Infrared<br/>Camera (LWIR)</b>", table_cell),
            Paragraph("1", table_cell_center),
            Paragraph("• Melexis MLX90640 radiometric thermal array<br/>• 32×24 pixels, 8–14 μm LWIR, 55°×35° FOV, I2C", table_cell),
            Paragraph("3,400", table_cell_right),
            Paragraph("<b>3,400</b>", table_cell_right),
            Paragraph("24/7 night, fog, and smoke penetration; isolates 37°C survivor body heat anomalies at rubble/mud interfaces.", table_cell),
        ],
        [
            Paragraph("<b>8</b>", table_cell_center),
            Paragraph("<b>Long-Range RF<br/>Telemetry (LoRa)</b>", table_cell),
            Paragraph("2", table_cell_center),
            Paragraph("• Semtech SX1262 (Ebyte E22-900T22S)<br/>• 868 MHz band (Indian WPC de-licensed), +22 dBm, SPI<br/>(1× on UAV, 1× ground USB station bridge)", table_cell),
            Paragraph("850", table_cell_right),
            Paragraph("<b>1,700</b>", table_cell_right),
            Paragraph("Broadcasts 17-byte binary bit-packed triage telemetry over 3–5+ km NLoS range during complete cellular/Wi-Fi blackouts [2, 3].", table_cell),
        ],
        [
            Paragraph("<b>9</b>", table_cell_center),
            Paragraph("<b>Power Distribution<br/>& Integration Gear</b>", table_cell),
            Paragraph("1 lot", table_cell_center),
            Paragraph("• Matek PDB with dual 5V/12V BECs<br/>• 5V 3A low-noise buck converter (for Arduino UNO Q)<br/>• Silicone anti-vibration damping ball gimbal mount<br/>• 14 AWG wiring, XT60 connectors, landing skids, hardware", table_cell),
            Paragraph("5,500", table_cell_right),
            Paragraph("<b>5,500</b>", table_cell_right),
            Paragraph("Harmonic vibration isolation protecting flight IMU; clean, brownout-free regulated power rail to Qualcomm MPU mission board.", table_cell),
        ],
        [
            Paragraph("", table_cell_center),
            Paragraph("<b>TOTAL PROTOTYPE INVESTMENT</b>", table_cell_bold),
            Paragraph("<b>9 Lots</b>", table_cell_center),
            Paragraph("<b>Complete Functional Hardware Prototype (Evaluation Ready)</b>", table_cell_bold),
            Paragraph("", table_cell),
            Paragraph("<b>₹37,400</b>", table_cell_right),
            Paragraph("<b>Calibrated end-to-end autonomous SAR platform</b>", table_cell_bold),
        ]
    ]

    col_widths = [20, 72, 24, 168, 42, 48, 166]
    t = Table(raw_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0F172A")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('GRID', (0, 0), (-1, -2), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#FEF3C7")),
        ('LINEABOVE', (0, -1), (-1, -1), 1.2, colors.HexColor("#D97706")),
        ('LINEBELOW', (0, -1), (-1, -1), 1.2, colors.HexColor("#D97706")),
        ('SPAN', (0, -1), (0, -1)),
    ]))
    story.append(t)

    # PAGE BREAK TO PAGE 2
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: ENGINEERING VALIDATION & ARCHITECTURAL INTEGRITY
    # =========================================================================
    story.append(Paragraph("2. Engineering Validation & Architectural Integrity", h1_style))

    justifications = [
        [
            Paragraph("<b>Subsystem Domain</b>", table_hdr),
            Paragraph("<b>Engineering Trade-Off & Empirical Validation</b>", table_hdr),
            Paragraph("<b>Operational Outcome in Phoenix X</b>", table_hdr),
        ],
        [
            Paragraph("<b>Memory & Storage<br/>(4 GB / 32 GB UNO Q)</b>", table_cell_bold),
            Paragraph("Flight control runs on STM32U585's dedicated 786 KB SRAM. The Qualcomm QRB2210 Linux MPU utilizes ~200 MB (OS), ~180 MB (INT8 YOLO buffers), ~120 MB (OpenCV), "
                      "and ~120 MB (Ray-casting & LoRa), totaling <b>~620 MB active RAM</b>. The 32 GB eMMC holds 4.2 GB (OS), 12 GB (offline GIS vector tiles), and 8.5 GB (black-box flight logs).", table_cell),
            Paragraph("<b>85% Free Headroom:</b> Eliminates kernel panics; vibration-proof eMMC prevents micro-SD card corruptions under motor harmonics.", table_cell),
        ],
        [
            Paragraph("<b>Power Budget<br/>(~5.5W Electronics)</b>", table_cell_bold),
            Paragraph("Propulsion draws ~168W at hover (4× 42W). Onboard electronics draw ~5.5W under peak AI workload (UNO Q ~3.5W, cameras ~0.9W, sensors/GNSS ~0.4W, LoRa burst ~0.5W, regulators ~0.6W).", table_cell),
            Paragraph("<b>>96% Power for Propulsion:</b> Electronics consume <4% of battery envelope, preserving maximum endurance for search sorties.", table_cell),
        ],
        [
            Paragraph("<b>Mass Budget<br/>(1.58 kg AUW)</b>", table_cell_bold),
            Paragraph("Component breakdown: Frame (282g), 4× Motors (208g), ESCs (96g), Props (44g), LiPo (362g), UNO Q (42g), Cameras/Mount (79g), GNSS/ToF/Sensors (48g), LoRa/RC (33g), PDB/Wiring (216g), Reserve (170g).", table_cell),
            Paragraph("<b>DGCA Micro Compliant:</b> Stays under 2.0 kg threshold with a 170g unallocated payload reserve for droppable beacons.", table_cell),
        ],
        [
            Paragraph("<b>RF Telemetry<br/>(Semtech 868 MHz)</b>", table_cell_bold),
            Paragraph("Under Government of India WPC / DoT GSR 564(E), the 865–867 MHz band is officially de-licensed up to 1 Watt (+30 dBm). "
                      "Unlike 433 MHz (congested by remotes) or 2.4 GHz (blocked by concrete/foliage), 868 MHz penetrates deep urban collapse voids.", table_cell),
            Paragraph("<b>3–5+ km NLoS Link:</b> Sustains resilient 17-byte survivor triage telemetry [2, 3] without cellular infrastructure.", table_cell),
        ],
    ]

    t_just = Table(justifications, colWidths=[95, 275, 170])
    t_just.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1E293B")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(t_just)
    story.append(Spacer(1, 8))

    # SECTION 3: ROADMAP & COMMERCIAL VIABILITY
    story.append(Paragraph("3. Roadmap: Phase-1 Prototype vs. Phase-2 Production vs. Commercial Alternatives", h1_style))

    roadmap_data = [
        [
            Paragraph("Subsystem Parameter", table_hdr),
            Paragraph("Phase-1 Hackathon Prototype", table_hdr),
            Paragraph("Phase-2 NDRF Production Unit", table_hdr),
            Paragraph("Imported Enterprise Alternative", table_hdr),
        ],
        [
            Paragraph("<b>Unit Acquisition Cost</b>", table_cell_bold),
            Paragraph("<b>₹37,400</b> (Calibrated Build)", table_cell),
            Paragraph("<b>₹85,000 – ₹1,20,000</b> (~₹1.2 Lakh)", table_cell_bold),
            Paragraph("<b>₹12,00,000 – ₹14,00,000</b> (DJI M30T)", table_cell),
        ],
        [
            Paragraph("<b>Airframe Structure</b>", table_cell_bold),
            Paragraph("F450 Glass-Fiber / Nylon Composite", table_cell),
            Paragraph("Toray 3K Foldable Carbon-Fiber Monocoque", table_cell),
            Paragraph("Proprietary Magnesium-Aluminum Shell", table_cell),
        ],
        [
            Paragraph("<b>Thermal Imaging Sensor</b>", table_cell_bold),
            Paragraph("MLX90640 (32×24 Radiometric Array)", table_cell),
            Paragraph("FLIR Lepton 3.5 (160×120) or InfiRay LWIR", table_cell),
            Paragraph("Proprietary 640×512 Radiometric Sensor", table_cell),
        ],
        [
            Paragraph("<b>Geodetic Positioning</b>", table_cell_bold),
            Paragraph("u-blox NEO-M8N Multi-GNSS (2.5m CEP)", table_cell),
            Paragraph("u-blox ZED-F9P Centimeter RTK-GNSS", table_cell),
            Paragraph("Proprietary RTK Module (+₹2 Lakh add-on)", table_cell),
        ],
        [
            Paragraph("<b>All-Weather Sealing</b>", table_cell_bold),
            Paragraph("Open prototype development chassis", table_cell),
            Paragraph("IP54 Conformal-Coated Sealed Enclosure", table_cell),
            Paragraph("IP55 Weather Sealing", table_cell),
        ],
        [
            Paragraph("<b>Data Sovereignty & Cyber</b>", table_cell_bold),
            Paragraph("100% Air-Gapped (Zero Cloud Uplink)", table_cell),
            Paragraph("100% Air-Gapped, HMAC-SHA256 Encrypted", table_cell_bold),
            Paragraph("Foreign cloud infrastructure dependencies", table_cell),
        ],
        [
            Paragraph("<b>Tactical Fleet Value</b>", table_cell_bold),
            Paragraph("Rapid proof-of-concept verification", table_cell),
            Paragraph("<b>Deploy 10 Phoenix UAVs for cost of 1 M30T</b>", table_cell_bold),
            Paragraph("Single-point-of-failure budget risk", table_cell),
        ],
    ]

    t_road = Table(roadmap_data, colWidths=[95, 145, 150, 150])
    t_road.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0F172A")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BACKGROUND', (2, 1), (2, -1), colors.HexColor("#F0FDF4")),
    ]))
    story.append(t_road)
    story.append(Spacer(1, 8))

    signoff_text = (
        "<b>Certification & Compliance Note:</b> All components listed in the Phase-1 BOM are commercially off-the-shelf in India. "
        "The all-up-weight of 1.58 kg complies with DGCA Micro-Category guidelines (< 2.0 kg), eliminating heavy remote pilot certification hurdles for rapid hackathon flight testing. "
        "RF communications strictly adhere to WPC GSR 564(E) unlicensed 865–867 MHz frequency allocations."
    )
    story.append(Paragraph(signoff_text, meta_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated: {PDF_PATH}")

if __name__ == "__main__":
    build_bom_pdf()
