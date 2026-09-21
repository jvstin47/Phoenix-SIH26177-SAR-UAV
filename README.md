# Team Phoenix — Autonomous AI Search and Rescue (SAR) UAV System
> **Smart India Hackathon (SIH) 2026**  
> **Problem Statement ID:** SIH26177  
> **Sponsoring Organization:** Qualcomm Inc.  
> **Category:** Hardware | **Theme:** Robotics and Drones  
> **Interactive Web Demo:** [`web_demo/index.html`](web_demo/index.html) (Run locally on port 8080)  
> **Master Presentation (Latest):** [`presentation/Team_Phoenix_SIH26177_Deck_v2.pptx`](presentation/Team_Phoenix_SIH26177_Deck_v2.pptx)  
> **Slide-by-Slide Master Document & Script:** [`presentation/slide_by_slide_presentation_content_doc.md`](presentation/slide_by_slide_presentation_content_doc.md)  

---

## 📌 Project Overview
**Team Phoenix** is designing a field-deployable, edge-AI-powered autonomous Unmanned Aerial Vehicle (UAV) tailored for emergency disaster reconnaissance (earthquakes, structural collapses, floods, and industrial hazards). 

The platform is engineered to operate in **GPS-denied, communication-constrained environments**, combining on-device multi-spectral computer vision (RGB + LWIR Thermal) with autonomous frontier exploration, real-time survivor geo-localization, and long-range LoRa peer-to-peer telemetry.

---

## 🚀 Key Theoretical Pillars & Research Foundations

The system architecture, aerodynamics, communications, and mathematical dynamics are built upon rigorous academic research:

1. **12-State Rigid Body Dynamics & Sizing Laws:** Complete 6-DOF nonlinear equations of motion incorporating rotor gyroscopic precession, actuator dynamic lag, and sizing optimization rules from **Dr. Samir Bouabdallah** (*EPFL Thesis No. 3727, 2007*).
2. **Integrated ROS-LoRa Mission-Critical Telemetry:** Grounded in recent breakthrough research by **Souli, Karatzia, Kolios, & Ellinas** (*Computer Communications, Elsevier, Vol. 225, 2024*), utilizing 17-byte binary bit-packing and priority-based queueing over raw LoRa (868 MHz) to stream survivor coordinates over 3–5+ km during cellular/Wi-Fi blackouts.
3. **Dual-Brain Edge Compute on Single Board:** Extending the open-source **JRFCQAI platform** (*Ravi Butani, 2024*), combining the **Qualcomm Dragonwing™ QRB2210 Linux MPU** for INT8 YOLO vision with an **STM32U585 MCU running Zephyr RTOS** at 250 Hz on the **Arduino UNO Q**.
4. **Camera-to-Ground Ray-Casting Geolocation:** Utilizing the complete Tait-Bryan rotation matrix $R(\phi, \theta, \psi)$ to project 2D camera detections into ground GPS coordinates without hovering directly overhead.
5. **Rotor Airfoil Selection & Vibration Control:** Grounded in **NASA TM-4741** (Langley Research Center), utilizing zero-pitching-moment ($C_{m, c/4} = 0$) reflexed/semi-symmetric airfoils to eliminate torsional blade flutter and protect flight controller IMUs.

---

## 🖥️ Interactive Demonstration Platform (`web_demo/`)

A self-contained aerospace mission control demonstration platform is included in [`web_demo/`](web_demo/):
* **Multi-Spectral Perception Lab**: Interactive wipe slider comparing 4K Visible (EO) with calibrated Radiometric LWIR Thermal (8–14 μm).
* **Tactical Operator Cockpit (FPV HUD)**: Primary flight display featuring Tait-Bryan ray-casting ground geolocation on click.
* **Dual-Brain Hardware Inspector**: Real-time architecture breakdown of the Qualcomm QRB2210 + STM32U585 compute partition.
* **17-Byte Binary LoRa Packer**: Live bit-level serialization of coordinates, altitude, triage, and HMAC signatures.
* **Tactical GCS & Dijkstra Safe Route Planner**: Offline incident map routing ground rescue teams around classified disaster hazards.
* **High-Contrast Light & Dark Modes**: Optimized for field deployment and presentations.

To run locally:
```bash
python3 -m http.server 8080 --directory web_demo
# Open http://localhost:8080 in your browser
```

---

## 📖 Research Documentation Index

* 📄 **[`docs/bouabdallah_quadrotor_research_findings.md`](docs/bouabdallah_quadrotor_research_findings.md)**: Sizing laws, 12-state equations, cascaded dual-loop control, and magnetic compass drift mitigations.
* 📄 **[`docs/ros_lora_mission_critical_uav_swarm_research.md`](docs/ros_lora_mission_critical_uav_swarm_research.md)**: Elsevier 2024 paper synthesis on ROS-LoRa integration, binary packet serialization, and GPS-denied cooperative positioning.
* 📄 **[`docs/aerodynamic_airfoil_considerations.md`](docs/aerodynamic_airfoil_considerations.md)**: NASA TM-4741 rotorcraft airfoil dynamics, lift slopes, and blade flutter prevention.
* 📄 **[`docs/references.bib`](docs/references.bib)**: Complete BibTeX citations for all academic literature.

---

## 📂 Repository Directory Structure

```text
Phoenix-SIH26177-SAR-UAV/
├── README.md                                      # Project landing page & executive summary
│
├── web_demo/                                      # Interactive Aerospace Mission Control Platform
│   ├── index.html                                 # Dashboard UI (Light/Dark themes)
│   ├── css/styles.css                             # Aerospace design system (Plus Jakarta Sans)
│   ├── js/                                        # Modular simulation & perception engines
│   └── images/                                    # Authentic multi-spectral disaster image pairs
│
├── docs/                                          # Research & System Design Documentation
│   ├── bouabdallah_quadrotor_research_findings.md # Synthesized EPFL thesis foundations & math
│   ├── ros_lora_mission_critical_uav_swarm_research.md # Elsevier 2024 ROS-LoRa architecture
│   ├── aerodynamic_airfoil_considerations.md      # NASA TM-4741 airfoil & rotor selection
│   ├── problem_statement_analysis.md              # Qualcomm problem statement breakdown & edge cases
│   ├── system_architecture.md                     # Full subsystem block diagrams & data flows
│   └── references.bib                             # Academic and technical citations (BibTeX)
│
├── presentation/                                  # SIH PPT Presentation Decks & Defense Assets
│   ├── Team_Phoenix_SIH26177_Deck_v2.pptx         # Latest Master Deck (THULYA-style visual cards)
│   ├── Team_Phoenix_SIH26177_Deck_v1.pptx         # Initial Baseline Deck (Preserved)
│   ├── Team_Phoenix_SIH26177_Official_Deck.pptx   # Master Deck Pointer
│   ├── slide_by_slide_presentation_content_doc.md # Slide-by-slide master text & verbal pitch scripts
│   ├── sih_presentation_outline.md               # Quick bullet-point presentation outline
│   └── generate_deck.py                           # Programmatic PPTX builder script
│
└── hardware_bom/                                  # Engineering Sizing & Feasibility
    ├── component_sizing_matrix.md                 # Motor KV, propeller size, and battery sizing models
    └── preliminary_cost_estimate.md               # Tiered Bill of Materials (BOM)
```

---

## 👥 Team Phoenix Roles & Responsibilities

| Subsystem Domain | Team Specialization | Key Deliverables |
| :--- | :--- | :--- |
| **Edge AI & Computer Vision** | AI & Data Science (AD) | Quantized multi-spectral detection (YOLOv11/v8 INT8 on Qualcomm NPU), RGB + Thermal late fusion. |
| **Flight Dynamics & Autonomy** | Computer Science (CSE) | Zephyr RTOS / PX4 flight loop, Boustrophedon grid coverage path planning, Tait-Bryan ray-casting engine. |
| **Ground Control & C2 Dashboard**| Computer Science (CSE) | Offline-first tactical map (React/Leaflet), automated survivor priority triage queue, safe-path routing. |
| **Secure Comms & Reliability** | Cyber Security (CY) | Telemetry HMAC packet authentication, ROS-LoRa binary serialization (Souli et al., 2024), store-and-forward sync. |
