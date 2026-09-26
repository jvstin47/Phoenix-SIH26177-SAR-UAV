# End-to-End System Architecture Specification

**Project**: Project Phoenix X — Phoenix-SIH26177-SAR-UAV  
**Problem Statement ID**: SIH26177 (Qualcomm Inc.)  
**Team**: Phoenix X (ID: 141943)  
**Subsystem**: Hardware & Software Systems Engineering  
**Last Updated**: September 2026

---

## 1. High-Level Subsystem Block Diagram

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                    AIRBORNE PLATFORM — PHOENIX X QUADCOPTER                      │
│                    Custom Carbon-Fibre | 1.58 kg AUW | DGCA Micro (<2 kg)        │
│                                                                                  │
│  ┌───────────────────────────┐             ┌──────────────────────────────────┐  │
│  │    PERCEPTION SENSORS     │             │     FLIGHT CONTROL AVIONICS      │  │
│  │                           │             │                                  │  │
│  │  4K RGB Camera (EO)       │             │  STM32U585 — Zephyr RTOS         │  │
│  │  LWIR Thermal (8–14 µm)   │             │  250 Hz control loop (4 ms)      │  │
│  │  Downward Optical Flow    │             │  Anti-windup cascaded PID        │  │
│  │  Barometric Altimeter     │             │  PWM/DShot ESC Output (4× ESC)   │  │
│  │  2-Axis Brushless Gimbal  │             │  IMU + Barometer + Compass       │  │
│  └────────────┬──────────────┘             └──────────────┬───────────────────┘  │
│               │ MIPI CSI-2 / I²C                          │ SPI / UART           │
│               ▼                                           ▼                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │         ARDUINO UNO Q — DUAL-BRAIN COMPUTE MODULE                           │  │
│  │                                                                             │  │
│  │  ┌──────────────────────────────────────┐  ┌───────────────────────────┐   │  │
│  │  │  QUALCOMM DRAGONWING™ QRB2210        │  │  STM32U585 (Zephyr RTOS)  │   │  │
│  │  │  (Linux SoC + Qualcomm NPU)          │  │                           │   │  │
│  │  │                                      │  │  • 250 Hz PID loop        │   │  │
│  │  │  • Cortex-A53 Quad-Core CPU          │  │  • 4 ms deterministic     │   │  │
│  │  │  • Qualcomm NPU — INT8 YOLOv8n       │  │    flight control cycle   │   │  │
│  │  │  • Linux OS (AI/Vision pipeline)     │  │  • PWM ESC control        │   │  │
│  │  │  • Boustrophedon path planning       │  │  • IMU data acquisition   │   │  │
│  │  │  • Tait-Bryan ray-cast geolocation   │  │  • Sensor fusion (EKF)    │   │  │
│  │  │  • Dijkstra safe-route planner       │  │  • Safe-arm/disarm logic  │   │  │
│  │  │  • LoRa packet serialisation         │  │                           │   │  │
│  │  └──────────────────────────────────────┘  └───────────────────────────┘   │  │
│  └──────────────────────────────────┬──────────────────────────────────────────┘  │
│                                     │                                             │
│                                     ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │                      COMMUNICATIONS & TELEMETRY                              │  │
│  │                                                                             │  │
│  │  • Semtech SX1262 LoRa 868 MHz [Long-Range Off-Grid Triage Mesh]            │  │
│  │    17-byte binary packets | HMAC-signed | 3.5–12 km range                   │  │
│  │  • ExpressLRS (ELRS) 2.4 GHz [RC Manual Safety Override]                    │  │
│  │                                                                             │  │
│  └──────────────────────────────────┬──────────────────────────────────────────┘  │
└─────────────────────────────────────┼───────────────────────────────────────────┘
                                      │ 868 MHz LoRa (3.5–12 km, infrastructure-free)
                                      ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                  GROUND CONTROL STATION (GCS) / FIRST RESPONDERS                 │
│  • Tactical Ruggedised Tablet (Offline OpenStreetMap / QGIS)                     │
│  • NDRF / SDRF Handheld LoRa Pager Terminals                                     │
│  • Live Geotagged Casualty Map & Dijkstra Safe-Route Overlay                     │
│  • Survivor Priority Triage Queue (auto-sorted by thermal confidence)            │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. 5-Step Operational Pipeline

```text
 STEP 1              STEP 2                STEP 3
 LAUNCH              SWEEP                 DETECT
 ──────              ─────                 ──────
 Phoenix X           STM32U585 +           QRB2210 NPU runs
 deployed in         Zephyr RTOS           INT8 YOLOv8n on
 < 8 min after       executes              LWIR thermal stream;
 site arrival        Boustrophedon         locks onto 37°C
                     lawnmower             body-heat signatures
                     grid coverage         through smoke & dark

       ▼                   ▼                      ▼

 STEP 5              STEP 4
 ROUTE               TRANSMIT
 ─────               ────────
 Dijkstra            17-byte LoRa burst:
 safe-path           GPS coords + triage
 planner guides      class + HMAC auth
 rescue team         → relayed 3.5–12 km
 around rubble       off-grid to GCS tablet
 to survivor
```

### Pipeline Timing Budget

| Step | Operation | Max Latency |
|:-----|:----------|:------------|
| Inference | INT8 YOLOv8n on Qualcomm NPU | < 30 ms |
| Flight Control | STM32U585 PID loop (Zephyr RTOS) | 4 ms (250 Hz) |
| LoRa Transmit | 17-byte packet over SX1262 | < 500 ms |
| Geolocation | Tait-Bryan ray-cast computation | < 5 ms |
| Route Planning | Dijkstra on local hazard graph | < 100 ms |

---

## 3. Subsystem Specifications

### 3.1 Primary Compute: Qualcomm Dragonwing™ QRB2210 (Arduino UNO Q)

| Parameter | Value |
|:----------|:------|
| **Board** | Arduino UNO Q |
| **SoC** | Qualcomm Dragonwing™ QRB2210 |
| **CPU** | Cortex-A53 Quad-Core |
| **AI Accelerator** | Qualcomm Neural Processing Unit (NPU) |
| **AI Workload** | INT8 YOLOv8n thermal object detection |
| **Operating System** | Linux (Yocto / Ubuntu) |
| **Key Software** | Python AI pipeline, LoRa packet engine, path planner |
| **Interface to STM32** | SPI / UART (shared bus on UNO Q) |

### 3.2 Flight Controller: STM32U585 (Arduino UNO Q, Zephyr RTOS)

| Parameter | Value |
|:----------|:------|
| **MCU** | STM32U585 |
| **RTOS** | Zephyr RTOS |
| **Control Loop Rate** | **250 Hz (4 ms deterministic cycle)** |
| **PID Architecture** | Anti-windup cascaded dual-loop (Bouabdallah 2005) |
| **Motor Output** | 4× PWM / DShot ESC signals |
| **Sensors** | IMU (accel + gyro), barometer, compass |
| **State Estimation** | Extended Kalman Filter (EKF) |
| **Failsafe** | Safe-arm/disarm, motor-out detection |

### 3.3 Airframe

| Parameter | Value |
|:----------|:------|
| **Configuration** | **Quadcopter (4-rotor)** |
| **Frame Material** | Carbon-fibre composite |
| **All-Up Weight (AUW)** | **1.58 kg** |
| **DGCA Category** | **Micro (<2 kg) — UAS Rules 2021** |
| **Max Operational Wind** | Up to 10 m/s |
| **Max Altitude** | 400 ft AGL (DGCA Micro limit) |
| **Target Endurance** | >20 min with full sensor suite |

> **Note**: Phoenix X deliberately targets the DGCA Micro (<2 kg) category to minimise regulatory burden. No DGCA Remote Pilot Certificate required for Green Zones under existing rules.

### 3.4 Dual-Spectral Perception Subsystem

| Stream | Sensor | Specification |
|:-------|:-------|:-------------|
| **Thermal (LWIR)** | Radiometric LWIR sensor | 8–14 µm, <50 mK NETD, detects 37°C body heat |
| **Visible (EO)** | 4K RGB camera | 30 FPS HDR, morphological & gesture detail |
| **Stabilisation** | 2-Axis brushless gimbal | 14-bit absolute encoders for ray-casting accuracy |
| **Fusion** | Late-fusion CNN pipeline | Thermal detection + RGB confirmation |

### 3.5 Long-Range Resilient Telemetry

| Parameter | Value |
|:----------|:------|
| **Module** | Semtech SX1262 |
| **Frequency** | **868 MHz** (India unlicensed band, WPC compliant) |
| **Range (LoS)** | Up to 12 km |
| **Range (NLoS / Urban Rubble)** | 3.5–5 km |
| **Packet Size** | **17 bytes** (GPS lat/lon + altitude + triage class + HMAC) |
| **Authentication** | HMAC packet signing (tamper-proof) |
| **Power Draw** | ~150 mW transmit |
| **Research Basis** | Souli et al., *Elsevier Computer Comms*, 2024 |

---

## 4. Software Architecture

### 4.1 QRB2210 Linux Process Architecture

```text
┌─────────────────────────────────────────────────────┐
│           QRB2210 Linux Process Space               │
│                                                     │
│  ┌─────────────────┐   ┌──────────────────────────┐ │
│  │  vision_pipeline│   │  mission_controller      │ │
│  │  ─────────────  │   │  ──────────────────────  │ │
│  │  LWIR ingest     │   │  Boustrophedon planner   │ │
│  │  INT8 YOLOv8n    │   │  Tait-Bryan ray-casting  │ │
│  │  (Qualcomm NPU)  │   │  Dijkstra route engine   │ │
│  │  37°C heat lock  │   │  Survivor priority queue │ │
│  └────────┬─────────┘   └──────────┬───────────────┘ │
│           │                        │                  │
│           └────────────┬───────────┘                  │
│                        ▼                              │
│  ┌──────────────────────────────────────────────────┐ │
│  │            lora_telemetry_node                   │ │
│  │  • 17-byte binary serialiser (Souli et al. 2024) │ │
│  │  • HMAC-SHA256 packet signing                    │ │
│  │  • Store-and-forward queue                       │ │
│  │  • SX1262 SPI driver                             │ │
│  └──────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
             │ SPI / UART
             ▼
┌─────────────────────────────────────────────────────┐
│         STM32U585 — Zephyr RTOS (250 Hz)            │
│  • IMU acquisition → EKF state estimation           │
│  • Anti-windup PID (roll/pitch/yaw/altitude)        │
│  • 4× PWM ESC motor mixing                         │
│  • Safe-arm / failsafe watchdog                     │
└─────────────────────────────────────────────────────┘
```

### 4.2 Communication Data Flow

```text
QRB2210 (Survivor Detection)
    │
    │  GPS (lat, lon) + altitude + triage class + timestamp
    ▼
17-Byte Binary Pack (HMAC-signed)
    │
    │  SPI → SX1262 LoRa 868 MHz
    ▼
GCS Tablet (Offline OSM)
    │
    │  Dijkstra hazard-aware routing
    ▼
Rescue Team Route Guidance
```

---

## 5. Research Foundations

| Claim | Source | Citation |
|:------|:-------|:---------|
| Quadrotor 12-state dynamics & anti-windup PID | Bouabdallah, EPFL Thesis 3727 / IEEE ICRA 2005 | `[1]` |
| 17-byte LoRa binary telemetry & priority queuing | Souli et al., Elsevier Computer Comms 2024 | `[2]` |
| Aerial CNN survivor detection (LWIR + RGB) | Mishra et al., Elsevier Computer Comms 2020 | `[3]` |
| Hazard-aware swarm SAR routing | Siotia et al., IEEE Access Sept 2, 2026 | `[4]` |
| LoRa 868 MHz off-grid relay for BLE victims | Pérez-Díaz-de-Cerio et al., IEEE Access Sept 7, 2026 | `[5]` |
| Decentralized edge computing, no cloud | Rahbari et al., IEEE Access July 2023 | `[6]` |
| RF victim localization baseline (comparison) | Albanese et al. SARDO, IEEE TMC 2022 | `[7]` |
| First clinical evidence of UAV-SAR efficacy | Van Tilburg, Wilderness & Env. Med. 2017 | `[8]` |

Full BibTeX citations: [`docs/references.bib`](references.bib)
