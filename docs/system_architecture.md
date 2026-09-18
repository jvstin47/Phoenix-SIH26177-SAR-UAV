# End-to-End System Architecture Specification

**Project**: Phoenix-SIH26177-SAR-UAV  
**Problem Statement ID**: SIH26177 (Qualcomm Inc.)  
**Subsystem**: Hardware & Software Systems Engineering  

---

## 1. High-Level Subsystem Block Diagram

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AIRBORNE PLATFORM (UAV)                              │
│                                                                                  │
│  ┌───────────────────────┐                 ┌──────────────────────────────────┐  │
│  │   PERCEPTION SENSORS  │                 │     FLIGHT CONTROL AVIONICS      │  │
│  │ 4K RGB Camera         │                 │ Pixhawk / STM32 (PX4 Autopilot)  │  │
│  │ LWIR Radiometric IR   │                 │ Triple Redundant IMU             │  │
│  │ Downward LiDAR (ToF)  │                 │ Barometer + Compass              │  │
│  │ Dual-Axis Gimbal      │                 │ CAN/DShot Electronic Speed Ctrl  │  │
│  └───────────┬───────────┘                 └────────────────┬─────────────────┘  │
│              │ MIPI CSI-2                                   │ MAVLink / UART     │
│              ▼                                              ▼                    │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │             QUALCOMM FLIGHT™ RB5 5G PLATFORM (QRB5165 SoC)                  │  │
│  │                                                                             │  │
│  │  ┌────────────────────┐ ┌────────────────────┐ ┌─────────────────────────┐  │  │
│  │  │ Qualcomm Spectra™  │ │ Qualcomm Kryo™ 585 │ │ Qualcomm Hexagon™ 698   │  │  │
│  │  │ 480 ISP Engine     │ │ Octa-Core CPU      │ │ DSP + Tensor NPU        │  │  │
│  │  │ - 4K/HDR Ingest    │ │ - ROS2 Humble Core │ │ - INT8 Quantized YOLO   │  │  │
│  │  │ - Dual-Stream Sync │ │ - Ray-Casting Math │ │ - SNPE Neural Engine    │  │  │
│  │  │ - Hardware Debayer │ │ - Failover FSM     │ │ - 15 TOPS @ < 10 Watts  │  │  │
│  │  └────────────────────┘ └────────────────────┘ └─────────────────────────┘  │  │
│  └──────────────────────────────────────┬──────────────────────────────────────┘  │
│                                         │                                         │
│                                         ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │                       COMMUNICATIONS & TELEMETRY                            │  │
│  │  • Qualcomm FastConnect™ 6800 (Wi-Fi 6 / 5G sub-6) [High Bandwidth Video]   │  │
│  │  • SX1262 LoRa 868/915 MHz Transceiver [Long-Range Resilient Triage Mesh]   │  │
│  │  • Ed25519 Cryptographic Packet Signing Engine                             │  │
│  └──────────────────────────────────────┬──────────────────────────────────────┘  │
└─────────────────────────────────────────┼─────────────────────────────────────────┘
                                          │ 868 MHz LoRa / 5G / Wi-Fi
                                          ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                       GROUND CONTROL STATION (GCS) / FIRST RESPONDERS            │
│  • Tactical Ruggedized Tablet / Laptop (Offline OpenStreetMap / QGIS)            │
│  • NDRF / SDRF Search Team Handheld LoRa Pager Terminals                         │
│  • Live Geotagged Casualty Map & Instant Triage Priority Heatmaps                │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Subsystem Specifications

### 2.1 Compute Engine: Qualcomm Flight™ RB5
* **SoC**: Qualcomm® QRB5165
* **CPU**: 8x Qualcomm® Kryo™ 585 (up to 2.84 GHz)
* **NPU / DSP**: Qualcomm® Hexagon™ 698 DSP with Hexagon Vector eXtensions (HVX) and Hexagon Tensor Accelerator (HTA) providing up to **15 TOPS** of AI inference capability.
* **ISP**: Qualcomm Spectra™ 480 Image Signal Processor (up to 2 Gigapixels/sec processing, supporting multi-camera concurrency).
* **Thermal Envelope**: 10W–15W typical operating draw under continuous inferencing.
* **OS / Middleware**: Ubuntu Linux (LTS) / Yocto Linux with **Qualcomm Snapdragon Neural Processing Engine (SNPE) SDK** and **ROS 2 Humble**.

### 2.2 Dual-Spectral Perception Subsystem
* **Visible Stream**: Sony IMX586 (48 MP raw, binned to 4K @ 30 FPS HDR) for fine-grained morphological details, gestures, and clothing contrast.
* **Thermal Stream**: FLIR Lepton 3.5 or InfiRay Micro LWIR ($640 \times 512$ radiometric sensor, $8 - 14\,\mu\text{m}$, $<50\text{ mK}$ NETD thermal sensitivity) capturing absolute temperature values.
* **Stabilization**: 2-Axis brushless gimbal with high-accuracy 14-bit magnetic absolute encoders for accurate ray-casting ground projection.

### 2.3 Flight Avionics & Autopilot
* **Flight Controller**: Pixhawk 6X / Holybro Kakute H7 running PX4 Autopilot firmware.
* **Inter-System Protocol**: High-baud MAVLink 2.0 communication over hardware UART with telemetry heartbeat monitoring.
* **State Estimation**: Extended Kalman Filter (EKF3) fusing multi-constellation GNSS (GPS, GLONASS, NavIC, Galileo), dual IMU, barometric pressure, and downward-facing optical flow/LiDAR for terrain following.

### 2.4 Resilient Dual-Tier Telemetry Architecture
* **Tier 1 (High Bandwidth / Local)**: Wi-Fi 6 / 5G for streaming live multi-spectral video when within operational proximity of base camp.
* **Tier 2 (Long-Range Tactical Mesh)**: Semtech SX1262 LoRa module (868 MHz in India, compliant with national unlicensed frequency allocations). Transmits ultra-compact (64-byte) encrypted triage packets up to 10–15 km in Line-of-Sight (LoS) or 3–5 km non-LoS over devastated urban topology.
