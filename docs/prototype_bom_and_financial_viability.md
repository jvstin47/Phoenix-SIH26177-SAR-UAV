# Project Phoenix X — Prototype Bill of Materials (BOM) & Financial Viability
**Problem Statement ID:** SIH26177 | **Sponsoring Organization:** Qualcomm Inc.  
**Theme:** Robotics & Drones | **Category:** Hardware | **Team Name:** Team Phoenix  

---

## 1. Executive Summary

A core operational requirement of **SIH26177** is engineering an autonomous tactical UAV that can be deployed rapidly and affordably by state and regional disaster management forces (NDRF / SDRF) without requiring multi-million rupee proprietary imports.

This document details the **calibrated Bill of Materials (BOM)** across two distinct development tiers:
1. **Phase 1: Working Hackathon Evaluation Prototype (₹35,800)** — An airframe and compute payload built to validate the dual-brain architecture, Zephyr RTOS flight loops, quantized edge-AI inference, and 17-byte LoRa packet telemetry.
2. **Phase 2: Industrial Field-Deployment Unit (₹1,15,000 – ₹1,30,000)** — A ruggedized, all-weather search-and-rescue UAV with high-resolution radiometric thermal imaging (FLIR Lepton 3.5 / InfiRay) and RTK-GPS centimeter geodetics, delivering enterprise capabilities at **1/10th the cost** of commercial alternatives like the DJI Matrice 30T (₹12,00,000 – ₹14,00,000).

---

## 2. Phase 1: Working Prototype Bill of Materials (BOM)

| No. | Component | Qty. | Specification / suggested part | Avg. unit cost | Total |
| :---: | :--- | :---: | :--- | :---: | :---: |
| **1** | **Arduino UNO Q** | 1 | ABX00162, 2 GB RAM model (Qualcomm QRB2210 MPU + STM32U585 MCU) | ₹7,200 | ₹7,200 |
| **2** | **Quadcopter frame + motors + ESCs + propellers** | 1 set | 450–500 mm frame; 2212 1000KV BLDC motors; 30A ESCs; 1045 propellers | ₹4,800 | ₹4,800 |
| **3** | **Flight sensors / GPS / receiver essentials** | 1 set | u-blox NEO-M8N GNSS (with compass mast) + MPU6050 IMU + MS5611 barometer | ₹4,200 | ₹4,200 |
| **4** | **LiPo battery + balance charger** | 1 set | 3S 11.1V 4500mAh 30C LiPo + iMAX B6 balance charger & 12V 5A power supply | ₹4,000 | ₹4,000 |
| **5** | **RC transmitter + receiver** | 1 set | FlySky FS-i6 6-channel 2.4 GHz system with FS-iA6B iBus receiver | ₹3,900 | ₹3,900 |
| **6** | **RGB camera** | 1 | 1080p UVC wide-angle USB camera module (OV2710 sensor, 120° FOV) | ₹1,100 | ₹1,100 |
| **7** | **Thermal camera module** | 1 | MLX90640, 32×24 IR array, ~55°×35° FOV, I2C radiometric interface | ₹3,400 | ₹3,400 |
| **8** | **LoRa modules + antennas** | 2 | Semtech SX1262 / E22-900, 868 MHz, +22 dBm, SPI (1 on drone, 1 on ground) | ₹850 | ₹1,700 |
| **9** | **Power & integration hardware** | 1 lot | Power distribution board with dual BECs, 5V 3A buck converter, XT60/silicone wiring, vibration damping mount, landing gear, spare props/fasteners | ₹5,500 | ₹5,500 |
| | **Estimated prototype cost** | | | | **₹35,800** |

---

## 3. Engineering & Architectural Validations

### 3.1 Memory Budget: Why 2 GB RAM on the Arduino UNO Q is Optimal
The Arduino UNO Q uses a dual-brain physical computing architecture where the **STM32U585 flight microcontroller runs entirely on its internal 786 KB SRAM**, leaving the full **2,048 MB (2 GB) LPDDR4 RAM dedicated exclusively to the Qualcomm Dragonwing QRB2210 Linux MPU**.

| Subsystem / Process | Function in Phoenix X | Memory Footprint (RAM) |
| :--- | :--- | :---: |
| **Headless Debian Linux OS** | Minimal kernel, systemd, drivers, no display server | ~200 MB |
| **Edge-AI Inference (INT8 YOLO)** | Quantized YOLOv8-nano tensor buffers on Qualcomm NPU | ~180 MB |
| **OpenCV & Frame Buffers** | 1080p camera capture + 32×24 thermal interpolation | ~120 MB |
| **Tait-Bryan Ray-Casting Engine** | 6-DOF Euler matrix projection onto DEM grid | ~45 MB |
| **17-Byte Telemetry Serialization** | Bit-packing and Semtech SX1262 SPI driver | ~35 MB |
| **Asynchronous RPC Bridge** | Inter-process messaging with STM32 flight controller | ~40 MB |
| **TOTAL ACTIVE RAM IN FLIGHT** | | **~620 MB** |
| **SAFETY BUFFER / FREE HEADROOM** | **System cache and operational safety margin** | **~1,428 MB (70% Free)** |

*Conclusion:* The 2 GB model delivers 70% headroom while drawing less quiescent DRAM refresh power than 4 GB variants.

### 3.2 Indian RF Compliance: Why Semtech SX1262 (868 MHz)
* **Regulatory Standard:** Under Government of India Ministry of Communications (WPC / DoT GSR 564(E)), the **865–867 MHz band** is officially de-licensed for low-power wireless indoor and outdoor IoT/telemetry equipment up to 1 Watt (+30 dBm).
* **Interference Resistance:** 433 MHz in India is heavily congested by automotive key fobs and generic radio remotes. 868 MHz provides superior non-line-of-sight (NLOS) penetration through collapsed rubble and dense tree foliage.
* **Silicon Choice:** Semtech SX1262 delivers -148 dBm sensitivity with 50% lower receive current compared to legacy SX1278 hardware.

### 3.3 Sensor Clarification: Downward 1D ToF Laser Altimeter vs. 3D LiDAR
Documentation mentions of "LiDAR" specifically refer to a **downward-pointing 1D Time-of-Flight (ToF) laser rangefinder** (e.g. STMicroelectronics VL53L1X or Benewake TFmini-S, ₹800–₹2,500), **not** a heavy 360° spinning LiDAR puck. 
* **Purpose:** Provides direct Above Ground Level ($H_{\text{AGL}}$) distance over sloping landslide slip planes, allowing the Tait-Bryan ray-casting matrix to calculate ground intersection coordinates without elevation error.

---

## 4. Phase 1 Prototype vs. Phase 2 Production Unit

```text
┌───────────────────────────────────────────┬───────────────────────────────────────────┐
│     PHASE 1: HACKATHON EVALUATION         │       PHASE 2: NDRF FIELD PRODUCTION      │
│            Total: ₹35,800                 │           Total: ₹1,15,000 - ₹1,30,000    │
├───────────────────────────────────────────┼───────────────────────────────────────────┤
│ • Glass-Fiber F450 Frame                  │ • Toray 3K Foldable Carbon Fiber Frame    │
│ • A2212 1000KV + Generic 30A ESCs         │ • Sunnysky V2216 + BLHeli_32 DShot ESCs   │
│ • MLX90640 (32x24) Radiometric Array      │ • FLIR Lepton 3.5 (160x120) or InfiRay    │
│ • u-blox NEO-M8N Multi-GNSS               │ • u-blox ZED-F9P Centimeter RTK-GNSS      │
│ • 3S 4500mAh LiPo Pack                    │ • Dual 4S 5200mAh Quick-Swap LiPo Trays   │
│ • Basic USB 1080p Webcam Sensor           │ • Global-Shutter Low-Light 4K EO Sensor   │
│ • Open Prototype Wiring                   │ • IP54 Conformal-Coated Sealed Enclosure  │
└───────────────────────────────────────────┴───────────────────────────────────────────┘
```

### Commercial Comparison:
* **DJI Matrice 30T / Enterprise Dual-Camera Drone:** ₹12,00,000 – ₹14,00,000 (Proprietary, foreign cloud dependency).
* **Project Phoenix X (Phase 2):** **₹1,20,000 (1/10th the cost)**, 100% Indian data sovereignty, air-gapped offline operation.
