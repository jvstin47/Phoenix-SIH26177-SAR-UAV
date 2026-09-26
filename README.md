<div align="center">

# 🔥 Project Phoenix X

### *Autonomous AI Search & Rescue UAV System*

[![SIH 2026](https://img.shields.io/badge/Smart%20India%20Hackathon-2026-orange?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTV6TTIgMTdsOCA0IDgtNE0yIDEybDggNCA4LTQiLz48L3N2Zz4=)](https://sih.gov.in)
[![Qualcomm Sponsored](https://img.shields.io/badge/Sponsored%20by-Qualcomm%20Inc.-3253DC?style=for-the-badge&logo=qualcomm&logoColor=white)](https://qualcomm.com)
[![Hardware Category](https://img.shields.io/badge/Category-Hardware%20%7C%20Robotics%20%26%20Drones-red?style=for-the-badge&logo=drone&logoColor=white)](https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV)
[![Team ID](https://img.shields.io/badge/Team%20ID-141943-blueviolet?style=for-the-badge)](https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-phoenix--sar--uav.vercel.app-22c55e?style=for-the-badge)](https://phoenix-sar-uav.vercel.app)

**Problem Statement ID:** `SIH26177` &nbsp;|&nbsp; **Team:** Phoenix X &nbsp;|&nbsp; **Team ID:** 141943

</div>

---

> **Edge-AI quadcopter that sees through smoke and darkness, transmits survivor coordinates over 5 km without cell towers, and guides rescuers around rubble — all within the 72-hour golden window.**

---

## 📋 Table of Contents

1. [The Problem](#-the-problem-statement)
2. [Phoenix X Solution](#-the-phoenix-x-solution)
3. [Key Capabilities](#-key-capabilities)
4. [Operational Pipeline](#-5-step-operational-pipeline)
5. [IEEE Research Foundations](#-ieee-research-foundations)
6. [Live Web Demo](#️-interactive-web-demo)
7. [Repository Structure](#-repository-structure)
8. [Hardware Specifications](#️-hardware-specifications)
9. [Bill of Materials](#-bill-of-materials-summary)
10. [Team Phoenix X](#-team-phoenix-x)
11. [License & Acknowledgements](#-license--acknowledgements)

---

## 🌏 The Problem Statement

> *"In the 2024 Wayanad landslides, 400+ lives were lost. Rescue teams arrived within hours — but couldn't locate survivors buried under metres of debris for days."*

Disaster zones like **Wayanad (2024)**, Joshimath (2023), and the Turkey earthquake (2023) share four lethal barriers that cost lives every hour:

| Barrier | Real-World Impact |
|:--------|:-----------------|
| 📡 **Communications Blackout** | Cell towers collapse first; no GPS, no network for 40–80 km² |
| 🌫️ **Zero Visibility** | Smoke, dust, darkness make optical search impossible |
| ⏱️ **72-Hour Golden Window** | Survival probability drops from 91% → 22% after 72 hours |
| ⚠️ **Responder Hazards** | Secondary collapses kill first responders entering unstable zones |

**Traditional search methods** — foot patrols, rescue dogs, thermal helicopters — are too slow, too dangerous, or grounded by debris-choked terrain. India needs an **autonomous, intelligent first-responder** that arrives in the first hour, not the first day.

---

## 🚀 The Phoenix X Solution

Phoenix X is a **DGCA-compliant Micro-UAV** (<2 kg AUW) powered by a **dual-brain compute architecture** that fuses Qualcomm's edge AI silicon with a hard real-time flight controller — delivering military-grade reconnaissance at a fraction of the cost.

```
┌─────────────────────────────────────────────────────────────────────┐
│   PHOENIX X — PROJECT AT A GLANCE                                   │
├────────────────────────┬────────────────────────────────────────────┤
│  Airframe              │  Custom Carbon-Fibre Quadcopter            │
│  AUW                   │  1.58 kg  (DGCA Micro-UAV < 2 kg)         │
│  Regulatory Class      │  DGCA UAS Rule 2021 — Micro Category       │
│  AI Brain              │  Qualcomm Dragonwing QRB2210 (Linux + NPU) │
│  Flight Controller     │  STM32U585 / Zephyr RTOS @ 250 Hz          │
│  Vision                │  RGB 4K + LWIR Thermal 8–14 µm             │
│  Long-Range Comms      │  SX1262 LoRa 868 MHz, 3.5–12 km            │
│  Sponsor               │  Qualcomm Inc. (SIH26177)                  │
│  Prototype Cost        │  ₹ 35,800                                   │
│  Production Cost       │  ₹ 85,000 – ₹ 1,20,000 per unit            │
└────────────────────────┴────────────────────────────────────────────┘
```

---

## ⚡ Key Capabilities

| Capability | Technology | Performance |
|:-----------|:-----------|:------------|
| 🔥 **Thermal Survivor Detection** | LWIR radiometric sensor (8–14 µm, <50 mK NETD) | 37°C body-heat lock through smoke, dust, darkness |
| 🤖 **On-Device AI Inference** | INT8 YOLOv8n on Qualcomm NPU | <30 ms latency, no cloud required |
| 📡 **Off-Grid Telemetry** | SX1262 LoRa 868 MHz, 17-byte binary packets | 3.5–12 km range, 0 infrastructure |
| 🗺️ **Autonomous Area Search** | Boustrophedon lawnmower path planning | 100% coverage, no operator joystick |
| 📍 **Precision Geolocation** | Tait-Bryan ray-casting (φ, θ, ψ rotation matrix) | GPS coordinate from 2D pixel hit |
| 🛡️ **Safe Route Planning** | Dijkstra's algorithm on hazard-tagged OSM graph | Guides rescuers around rubble & collapse zones |
| 🔐 **Secure Comms** | HMAC-signed 17-byte LoRa packets | Tamper-proof casualty reports, no spoofing |
| ⚡ **Hard Real-Time Flight** | STM32U585 + Zephyr RTOS, 4 ms deterministic loop | Anti-windup PID, 250 Hz IMU fusion |
| 🌐 **GPS-Denied Operation** | Optical flow + barometric altimeter fusion | Works where satellites don't |
| 🧠 **Decentralized Swarm** | RIS-based collaborative edge compute (no cloud) | Multi-UAV coordination without infrastructure |

---

## 🔄 5-Step Operational Pipeline

```
  [1] LAUNCH              [2] SWEEP               [3] DETECT
  ──────────              ─────────               ──────────
  Ground crew             Boustrophedon           LWIR thermal locks
  deploys Phoenix X       lawnmower path          onto 37°C body-heat
  within 8 minutes        covers assigned         signature through
  of arrival at site      grid sector             smoke & darkness
       │                       │                       │
       └───────────────────────┴───────────────────────┘
                                   │
                    ┌──────────────┴───────────────┐
                    │                              │
              [4] TRANSMIT                   [5] ROUTE
              ────────────                   ──────
              17-byte LoRa burst             Dijkstra safe-path
              with GPS coords,               planner routes rescue
              triage class, HMAC             team around hazards
              → 3.5–12 km range              to survivor location
```

---

## 📚 IEEE Research Foundations

All design decisions are grounded in peer-reviewed academic literature:

| # | Paper & Authors | Venue | Phoenix X Application |
|:--|:----------------|:------|:----------------------|
| 1 | **SwarmSAR-FW** — Siotia et al. (IIT Jodhpur & Manipal) | *IEEE Access*, Sept 2, 2026 | Hazard-aware safe ingress/egress routing; swarm coordination in fire & flood disasters |
| 2 | **BLE Detection via Drone LoRa Relays** — Pérez-Díaz-de-Cerio et al. (UPC Spain) | *IEEE Access*, Sept 7, 2026 | Validates 868 MHz LoRa as off-grid bridge; BLE victim beacon relay architecture |
| 3 | **RIS-Based Collaborative Swarm Computing** — Rahbari et al. (TalTech Estonia) | *IEEE Access*, July 2023 | Decentralized edge computing without cloud; multi-UAV consensus without infrastructure |
| 4 | **12-State Quadrotor Dynamics** — Bouabdallah (EPFL Thesis 3727 / IEEE ICRA 2005) | *EPFL / IEEE ICRA*, 2005 | 6-DOF nonlinear equations of motion, anti-windup cascaded PID, motor-rotor sizing laws |
| 5 | **17-Byte LoRa Binary Telemetry** — Souli et al. | *Elsevier Computer Comms*, 2024 | Binary bit-packing of GPS + triage + HMAC into 17 bytes; priority queueing over raw LoRa |
| 6 | **Aerial CNN Survivor Detection** — Mishra et al. (BITS Pilani & Bennett Univ.) | *Elsevier Computer Comms*, 2020 | Thermal + RGB CNN fusion for aerial survivor detection in dense rubble environments |
| 7 | **SARDO** — Albanese et al. | *IEEE TMC*, 2022 | RF-based victim localization baseline; Phoenix X outperforms via thermal + LoRa fusion |
| 8 | **First Drones in SAR** — Van Tilburg | *Wilderness & Environmental Medicine*, 2017 | Foundational clinical evidence for UAV-based SAR; medical outcome validation |

---

## 🖥️ Interactive Web Demo

**🌐 Live:** [phoenix-sar-uav.vercel.app](https://phoenix-sar-uav.vercel.app)

A self-contained aerospace mission control simulation platform demonstrating every Phoenix X subsystem:

| Module | What It Shows |
|:-------|:--------------|
| 🌡️ **Multi-Spectral Perception Lab** | Interactive RGB/Thermal wipe slider — real disaster imagery (Wayanad, earthquake, night smoke) |
| 🎮 **Tactical Operator HUD (FPV)** | Primary flight display; click-to-geolocate via Tait-Bryan ray-casting |
| 🧠 **Dual-Brain Hardware Inspector** | Live QRB2210 + STM32U585 compute partition breakdown with simulated loads |
| 📦 **17-Byte LoRa Packer** | Bit-level binary serialization — watch coordinates become 17 bytes in real time |
| 🗺️ **Tactical GCS & Dijkstra Router** | Offline hazard map; route rescue teams around collapse zones |
| 🌙 **High-Contrast Dark / Light Modes** | Optimised for outdoor field tablets and presentation halls |

### Run Locally

```bash
# Clone the repo
git clone https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV.git
cd Phoenix-SIH26177-SAR-UAV

# Serve web demo (no build step needed — pure HTML/JS/CSS)
python3 -m http.server 8080 --directory web_demo

# Open in browser
open http://localhost:8080
```

---

## 📂 Repository Structure

```text
Phoenix-SIH26177-SAR-UAV/
│
├── README.md                                         # ← You are here
├── CONTRIBUTING.md                                   # Contribution guide & doc conventions
├── .gitignore
│
├── web_demo/                                         # Interactive Mission Control Platform
│   ├── index.html                                    # Dashboard UI (Light/Dark themes)
│   ├── css/styles.css                                # Aerospace design system
│   └── js/
│       ├── mission_controller.js                     # Mission FSM & state management
│       ├── mission_state.js                          # Shared state bus
│       ├── perception.js                             # Thermal/RGB fusion renderer
│       ├── network_simulator.js                      # LoRa packet simulation
│       ├── operator_hud.js                           # FPV HUD & ray-casting
│       ├── tech_showcase.js                          # Hardware inspector
│       └── audio.js                                  # Mission audio feedback
│
├── docs/                                             # Research & System Design Documentation
│   ├── system_architecture.md                        # Full subsystem block diagrams & data flows
│   ├── bouabdallah_quadrotor_research_findings.md    # EPFL thesis: 12-state dynamics & PID
│   ├── ros_lora_mission_critical_uav_swarm_research.md  # Elsevier 2024 ROS-LoRa architecture
│   ├── aerodynamic_airfoil_considerations.md         # NASA TM-4741 airfoil & rotor selection
│   ├── sensor_fusion_theory.md                       # Kalman filter & multi-spectral fusion math
│   ├── problem_statement_analysis.md                 # SIH26177 breakdown & edge cases
│   ├── research_papers_synthesis_2026.md             # 2026 IEEE paper synthesis
│   └── references.bib                                # BibTeX citations (all 8 IEEE papers)
│
├── hardware_bom/
│   └── component_selection_matrix.md                 # Trade-off tables & BOM summary
│
└── presentation/                                     # SIH Presentation Decks & Assets
    ├── Team_Phoenix_SIH26177_Official_Deck.pptx      # Official submission deck
    ├── Team_Phoenix_SIH26177_Deck_v2.pptx            # Latest iterated deck
    ├── slide_by_slide_presentation_content_doc.md    # Slide-by-slide master script
    ├── team_video_presentation_scripts.md            # 6-speaker video scripts
    └── assets/                                       # Drone renders & scenario images
```

---

## 🛠️ Hardware Specifications

### Compute Architecture: Dual-Brain

| Subsystem | Component | Key Specs |
|:----------|:----------|:----------|
| **AI Brain** | Qualcomm Dragonwing™ QRB2210 *(on Arduino UNO Q)* | Cortex-A53 quad-core + Qualcomm NPU, Linux OS, INT8 YOLOv8n inference |
| **Flight Controller** | STM32U585 *(on Arduino UNO Q)* | Zephyr RTOS, 250 Hz control loop, 4 ms deterministic cycle, PWM ESC output |
| **Thermal Camera** | LWIR Radiometric Sensor | 8–14 µm, <50 mK NETD, detects 37°C body heat through smoke |
| **RGB Camera** | 4K Visible (EO) | 30 FPS HDR, dual-stream sync with thermal |
| **Gimbal** | 2-Axis Brushless | 14-bit magnetic absolute encoders for Tait-Bryan ray-casting |
| **Long-Range Radio** | Semtech SX1262 LoRa | 868 MHz (India unlicensed band), 3.5–12 km, 17-byte binary packets |
| **RC Override** | ExpressLRS (ELRS) 2.4 GHz | Manual safety takeover, 250 Hz telemetry |
| **Power** | LiPo Battery Pack | Sized for >20 min flight endurance with full sensor suite |

### Airframe

| Parameter | Value |
|:----------|:------|
| **Configuration** | Quadcopter (4-rotor) |
| **All-Up Weight (AUW)** | **1.58 kg** |
| **Regulatory Category** | DGCA UAS Rules 2021 — **Micro (<2 kg)** |
| **Frame Material** | Carbon-fibre composite |
| **Wind Resistance** | Up to 10 m/s operational |
| **Max Altitude** | 400 ft AGL (DGCA Micro limit) |

> [!IMPORTANT]
> Phoenix X is classified as a **DGCA Micro-UAV** (AUW < 2 kg), placing it in the lowest regulatory burden category. No DGCA operator permit required for green zones. This was a deliberate design constraint.

---

## 💰 Bill of Materials Summary

### Phase 1 — Functional Prototype

| Category | Key Components | Approx. Cost |
|:---------|:---------------|:-------------|
| Compute | Arduino UNO Q (QRB2210 + STM32U585) | ₹ 8,500 |
| Airframe | Carbon-fibre frame, motors, ESCs, props | ₹ 9,200 |
| Sensors | LWIR thermal camera + RGB module | ₹ 8,400 |
| Comms | SX1262 LoRa module + antenna | ₹ 1,800 |
| Power | LiPo pack + BMS + charger | ₹ 4,200 |
| Miscellaneous | Wiring, connectors, gimbal, fasteners | ₹ 3,700 |
| **Phase 1 Total** | **Functional flying prototype** | **₹ 35,800** |

### Phase 2 — Production Unit

| Configuration | Per-Unit Cost | Notes |
|:--------------|:-------------|:------|
| Standard (India) | **₹ 85,000** | Domestic sourcing, volume pricing |
| Advanced (Export) | **₹ 1,20,000** | Enhanced thermal, IP65 enclosure, ruggedised |

> [!NOTE]
> Full component-by-component breakdown with trade-off rationale is in [`hardware_bom/component_selection_matrix.md`](hardware_bom/component_selection_matrix.md) and [`docs/prototype_bom_and_financial_viability.md`](docs/prototype_bom_and_financial_viability.md).

---

## 👥 Team Phoenix X

**Team ID:** 141943 &nbsp;|&nbsp; **Institution:** SIH 2026 Participants

| Specialization Domain | Key Deliverables |
|:----------------------|:----------------|
| 🤖 **Edge AI & Computer Vision** | INT8 YOLOv8n on Qualcomm NPU, RGB + LWIR thermal late-fusion, 37°C survivor lock |
| ✈️ **Flight Dynamics & Autonomy** | Zephyr RTOS flight loop (250 Hz), Boustrophedon path planning, Tait-Bryan ray-casting |
| 🗺️ **Ground Control & C2 Dashboard** | Offline tactical map, Dijkstra safe-route planner, survivor priority triage queue |
| 🔐 **Secure Comms & Reliability** | HMAC-signed LoRa packets, 17-byte binary serialization, store-and-forward sync |

---

## 📄 License & Acknowledgements

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- 🏛️ **Qualcomm Inc.** — Problem statement sponsor (SIH26177) and hardware ecosystem (Arduino UNO Q / Dragonwing QRB2210)
- 🎓 **EPFL** — Dr. Samir Bouabdallah, Thesis No. 3727 (quadrotor dynamics foundations)
- 🛰️ **IEEE** — SwarmSAR-FW (Siotia et al.), SARDO (Albanese et al.), RIS Swarm (Rahbari et al.)
- 📡 **Elsevier** — Souli et al. (2024) LoRa telemetry, Mishra et al. (2020) aerial survivor CNN
- 🏔️ **Wilderness & Environmental Medicine** — Van Tilburg (2017) UAV-SAR clinical evidence
- 🇮🇳 **Smart India Hackathon 2026** — Ministry of Education, Government of India

---

<div align="center">

**Built with ❤️ for India's disaster responders**

[🌐 Live Demo](https://phoenix-sar-uav.vercel.app) &nbsp;|&nbsp; [📂 Repository](https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV) &nbsp;|&nbsp; [📊 Presentation](presentation/Team_Phoenix_SIH26177_Official_Deck.pptx)

*Project Phoenix X — SIH26177 — Team 141943*

</div>
