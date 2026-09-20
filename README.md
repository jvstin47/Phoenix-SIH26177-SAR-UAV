# Team Phoenix — Autonomous AI Search and Rescue (SAR) UAV System
> **Smart India Hackathon (SIH) 2026**  
> **Problem Statement ID:** SIH26177  
> **Sponsoring Organization:** Qualcomm Inc.  
> **Category:** Hardware | **Theme:** Robotics and Drones  

---

## 📌 Project Overview
**Team Phoenix** is designing a field-deployable, edge-AI-powered autonomous Unmanned Aerial Vehicle (UAV) tailored for emergency disaster reconnaissance (earthquakes, structural collapses, floods, and industrial hazards). 

The platform is engineered to operate in **GPS-denied, communication-constrained environments**, combining on-device multi-spectral computer vision (RGB + LWIR Thermal) with autonomous frontier exploration and real-time survivor geo-localization.

---

## 🚀 Key Theoretical Pillars & Research Foundations

The system architecture and mathematical dynamics are built upon the foundational work by **Dr. Samir Bouabdallah** (*Design and Control of Quadrotors with Application to Autonomous Flying*, EPFL Thesis No. 3727, 2007).

* **12-State Rigid Body Dynamics:** Complete 6-DOF nonlinear equations of motion incorporating rotor gyroscopic precession and actuator dynamic lag.
* **Camera-to-Ground Ray-Casting Geolocation:** Utilizing the complete Tait-Bryan rotation matrix $R(\phi, \theta, \psi)$ to project 2D camera detections into ground GPS coordinates without hovering directly overhead.
* **Cascaded Dual-Loop Spectral Separation:** Decoupled inner attitude loop (100–250 Hz) and outer position navigation loop (20–50 Hz).
* **System Sizing Optimization:** Designed with a $2:1$ thrust-to-weight ratio ($\beta \ge 2.0$) and an optimal $35\%-44\%$ battery mass fraction.
* **Disaster-Resilient Heading (Anti-Compass Drift):** Overcomes motor current and reinforced steel magnetic distortions by fusing Visual-Inertial Odometry (VIO) / Optical Flow with rate gyros.

For full mathematical derivations, design indicators, and benchmarks, see:  
📖 **[`docs/bouabdallah_quadrotor_research_findings.md`](docs/bouabdallah_quadrotor_research_findings.md)**

---

## 📂 Repository Directory Structure

```text
Phoenix-SIH26177-SAR-UAV/
├── README.md                          # Project landing page & executive summary
│
├── docs/                              # Research & System Design Documentation
│   ├── bouabdallah_quadrotor_research_findings.md  # Synthesized EPFL thesis foundations & math
│   ├── problem_statement_analysis.md  # Qualcomm problem statement breakdown & edge cases
│   ├── system_architecture.md         # Full subsystem block diagrams & data flows
│   └── references.bib                 # Academic and technical citations
│
├── presentation/                      # SIH PPT Presentation & Defense Assets
│   ├── sih_presentation_outline.md   # Slide-by-slide script & pitch talking points
│   └── diagrams/                      # System architecture and workflow schematics
│
└── hardware_bom/                      # Engineering Sizing & Feasibility
    ├── component_sizing_matrix.md     # Motor KV, propeller size, and battery sizing models
    └── preliminary_cost_estimate.md   # Tiered Bill of Materials (BOM)
```

---

## 👥 Team Phoenix Roles & Responsibilities

| Subsystem Domain | Team Specialization | Key Deliverables |
| :--- | :--- | :--- |
| **Edge AI & Computer Vision** | AI & Data Science (AD) | Quantized multi-spectral detection (YOLOv11/v8 INT8), RGB + Thermal late fusion, hazard segmentation. |
| **Flight Dynamics & Autonomy** | Computer Science (CSE) | ROS2 / PX4 flight simulation, Boustrophedon grid coverage path planning, target ray-casting engine. |
| **Ground Control & C2 Dashboard**| Computer Science (CSE) | Offline-first tactical map (React/Leaflet), telemetry bus, survivor priority triage queue. |
| **Secure Comms & Reliability** | Cyber Security (CY) | Telemetry HMAC packet authentication, store-and-forward buffer synchronization, LoRa fallback beacon. |

---

## 📚 References
* Bouabdallah, S. (2007). *Design and Control of Quadrotors with Application to Autonomous Flying*. Doctoral Thesis No. 3727, École Polytechnique Fédérale de Lausanne (EPFL).
* Bouabdallah, S., & Siegwart, R. (2005). *Backstepping and Sliding-Mode Techniques Applied to an Indoor Micro Quadrotor*. IEEE ICRA.
