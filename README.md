# Phoenix-SIH26177-SAR-UAV: Autonomous AI-Powered Search and Rescue (SAR) UAV for Disaster Reconnaissance

[![Smart India Hackathon 2026](https://img.shields.io/badge/SIH-2026-orange.svg)](https://sih.gov.in/)
[![Problem Statement](https://img.shields.io/badge/PS_ID-SIH26177-blue.svg)](https://sih.gov.in/)
[![Sponsoring Organization](https://img.shields.io/badge/Sponsor-Qualcomm_Inc.-red.svg)](https://www.qualcomm.com/)
[![Category](https://img.shields.io/badge/Category-Hardware_%7C_Robotics_%26_Drones-green.svg)](#)
[![Phase](https://img.shields.io/badge/Phase-Theoretical_Design_%26_Systems_Engineering-purple.svg)](#)

---

## 1. Project Context & Objectives

* **Project Title**: Autonomous AI-Powered Search and Rescue (SAR) UAV for Disaster Reconnaissance
* **Team**: Team Phoenix
* **Hackathon**: Smart India Hackathon (SIH) 2026
* **Problem Statement ID**: SIH26177
* **Sponsoring Organization**: Qualcomm Inc.
* **Category**: Hardware | **Theme**: Robotics and Drones
* **Current Phase**: Theoretical Modeling, Systems Architecture Design, Mathematical Formulations, and SIH Proposal Formulation (*No Code Implementation Phase*)

---

## 2. Executive Abstract

In the aftermath of catastrophic disasters—such as severe earthquakes, flash floods, landslides, and urban structural collapses—the first **72 hours ("The Golden Window")** dictate survival probability. Traditional first-responder reconnaissance is impeded by debris blockages, hazardous structural instability, thermal/smoke occlusion, damaged cellular towers, and compromised GNSS availability.

**Team Phoenix** presents an autonomous, edge-intelligent Unmanned Aerial Vehicle (UAV) platform engineered for rapid disaster reconnaissance and survivor triage under severe real-world constraints. Powered by the **Qualcomm Flight™ RB5 Platform (Snapdragon® QRB5165)** and operating within an ultra-strict **10W–15W compute envelope**, the UAV executes:
1. **Multi-Spectral Perception**: Real-time fusion of 4K High-Dynamic-Range (HDR) RGB and Long-Wave Infrared (LWIR) radiometric thermal imaging.
2. **On-Device Neural Acceleration**: Quantized (INT8) human and survivor detection accelerated via the **Qualcomm® Neural Processing Engine (SNPE)** on the Hexagon™ Vector Extensions (HVX) DSP and NPU (15 TOPS).
3. **Ray-Casting Geolocation Engine**: Exact trigonometric ray-projection mapping target bounding-box centroids from pixel space to WGS-84 coordinates within $\pm 2.5\text{ m}$ accuracy without requiring cloud offloading.
4. **Resilient Communications & Cyber Security**: High-bandwidth dual-band 5G/Wi-Fi 6 links paired with an autonomous ultra-low-power Long-Range (LoRa 868/915 MHz) tactical mesh fallback for emergency micro-telemetry broadcasting in complete cellular/Wi-Fi blackouts.
5. **Failover State Machine**: Autonomous contingency handling for simultaneous GNSS jamming/denial and telemetry loss.

---

## 3. Repository Architecture

```text
Phoenix-SIH26177-SAR-UAV/
├── README.md                          # Master project documentation & system overview
├── docs/
│   ├── problem_statement_analysis.md  # Deep dive into Qualcomm's prompt, requirements & edge cases
│   ├── system_architecture.md         # End-to-end block diagrams, data-flow, and subsystem specs
│   ├── operational_workflow.md        # ConOps (Concept of Operations) in earthquake/flood scenarios
│   ├── sensor_fusion_theory.md        # Mathematical formulations (RGB + Thermal fusion, Ray-casting)
│   └── trade_off_studies.md           # Comparative analysis (Quad vs Hex, RGB vs Thermal, Comms links)
│
├── presentation/                      # SIH PPT Submission Decks & Scripts
│   ├── sih_official_deck_outline.md   # 6-Slide presentation architecture matching SIH rubric
│   ├── slide_by_slide_script.md       # 3-minute verbal pitch script & defense FAQ
│   └── diagrams/                      # ASCII/Mermaid architectural and data-flow diagrams
│
├── research_papers/                   # Literature Review & Scientific Grounding
│   ├── literature_survey.md           # Summaries of state-of-the-art IEEE/arXiv papers on SAR drones
│   └── references.bib                 # Formal BibTeX citations for SIH proposal and PPT
│
└── hardware_bom/                      # Feasibility & Cost Analysis
    ├── component_selection_matrix.md  # Trade-offs (Qualcomm RB5 vs Jetson Orin vs Raspberry Pi 5)
    └── preliminary_cost_estimate.md   # Bill of Materials (BOM) with 3-tier budget modeling
```

---

## 4. Key Systems Engineering Innovations

* **Hardware-Native Qualcomm Optimization**: Instead of generic heavy GPU architectures consuming 30W–60W, Team Phoenix leverages the heterogeneous Qualcomm Kryo™ 585 CPU + Adreno™ 650 GPU + Hexagon™ 698 DSP/NPU compute pipeline, maximizing flight endurance by 28–35%.
* **False-Positive Suppression Engine**: Synergistic spatio-temporal fusion combining radiometric thermal thresholds ($35^\circ\text{C} - 38^\circ\text{C}$) with visible structural features to reject solar-heated asphalt, hot rocks, and machinery.
* **Store-and-Forward Cryptographic Telemetry**: When telemetry links are lost, geocoded triage metadata is cryptographically signed (Ed25519) and logged in non-volatile flash, immediately synching upon reconnection or bursting across the LoRa mesh.

---

## 5. Team Phoenix
* **Disciplines**: Computer Science & Engineering, Artificial Intelligence & Data Science, Cyber Security
* **Target Hackathon**: Smart India Hackathon (SIH) 2026
* **Problem Statement ID**: SIH26177 (Qualcomm Inc.)
