# Project Phoenix X — Prototype Bill of Materials (BOM) & Financial Viability
**Problem Statement ID:** SIH26177 | **Sponsoring Organization:** Qualcomm Inc.  
**Theme:** Robotics & Drones | **Category:** Hardware | **Team ID:** 141943 | **Team Name:** Team Phoenix X  

---

## 1. Executive Summary

A core operational requirement of **SIH26177** is engineering an autonomous tactical UAV that can be deployed rapidly and affordably by state and regional disaster management forces (NDRF / SDRF) without requiring multi-million rupee proprietary imports.

This document details the **calibrated Bill of Materials (BOM)** across two distinct development tiers:
1. **Phase 1: Working Hackathon Evaluation Prototype (₹37,400)** — An airframe and compute payload built to validate the dual-brain architecture (Arduino UNO Q with 4GB LPDDR4 and 32GB eMMC), Zephyr RTOS flight loops, quantized edge-AI inference on heterogeneous Qualcomm silicon, and 17-byte LoRa packet telemetry.
2. **Phase 2: Industrial Field-Deployment Unit (₹85,000 – ₹1,20,000)** — A ruggedized, all-weather search-and-rescue UAV with high-resolution radiometric thermal imaging (FLIR Lepton 3.5 / InfiRay) and RTK-GPS centimeter geodetics, delivering enterprise capabilities at **1/10th the cost** of commercial alternatives like the DJI Matrice 30T (₹12,00,000 – ₹14,00,000).

---

## 2. Phase 1: Working Prototype Bill of Materials (BOM)

| No. | Subsystem / Component | Qty. | Specification / Suggested Part | Avg. Unit Cost | Total | Interface & Operational Role |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **1** | **Main Compute (Dual-Brain SBC)** | 1 | **Arduino UNO Q** (ABX00163, 4 GB RAM / 32 GB eMMC)<br>• *Qualcomm Dragonwing QRB2210 MPU (Debian Linux)*<br>• *STM32U585 MCU (250 Hz Zephyr RTOS loop)* | ₹8,800 | **₹8,800** | **Internal Shared Memory IPC.** Heterogeneous on-device AI (CPU/Adreno GPU/Hexagon DSP via Qualcomm SNPE) + hard real-time 250 Hz flight loop on STM32. |
| **2** | **Quadcopter Frame + Propulsion** | 1 set | • F450 / S500 carbon/glass composite frame<br>• 4× A2212 1000KV BLDC motors<br>• 4× 30A SimonK / BLHeli ESCs<br>• 2 pairs 1045 nylon-carbon composite propellers | ₹4,800 | **₹4,800** | **350 Hz PWM.** Delivers calculated $\beta = 2.23$ thrust-to-weight ratio to lift the 1.58 kg platform and provide substantial thrust headroom for maneuvering. |
| **3** | **Avionics Sensors & GNSS Suite** | 1 set | • **u-blox NEO-M8N GNSS** with compass mast<br>• **MPU6050** 6-DOF IMU (accelerometer + gyro)<br>• **MS5611** high-precision barometric altimeter<br>• **VL53L1X** 1D Time-of-Flight (ToF) downward laser | ₹4,200 | **₹4,200** | **I²C Bus (IMU/Baro/ToF) & UART (GNSS @ 10Hz).** Multi-sensor EKF state estimation on STM32; downward ToF feeds ground altitude to ray-casting projection. |
| **4** | **LiPo Battery + Balance Charger** | 1 set | • **3S 11.1V 4500mAh 30C LiPo** battery pack<br>• **iMAX B6** 80W digital balance charger<br>• 12V 5A regulated AC/DC power supply | ₹4,000 | **₹4,000** | **XT60 Heavy Rail.** Delivers 13.8 minutes theoretical hover endurance (10.0 minute planned search mission leaving ~27.5% energy reserve). |
| **5** | **Manual RC Safety Failover Link** | 1 set | • **FlySky FS-i6** 6-channel 2.4 GHz AFHDS transmitter<br>• **FS-iA6B** 6-channel receiver (iBus / PPM protocol) | ₹3,900 | **₹3,900** | **UART (iBus serial @ 115200).** Emergency pilot takeover channel for field safety redundancy and fail-safe override compliance. |
| **6** | **Optical Vision Camera (RGB)** | 1 | • **1080p Full HD UVC USB Camera Module**<br>• OmniVision OV2710 sensor, 120° wide-angle M12 lens | ₹1,100 | **₹1,100** | **USB 2.0 Host (V4L2 driver).** Daylight stream for visual confirmation of clothing, gestures, and identification of electrical hazards & debris. |
| **7** | **Thermal Camera Module (LWIR)** | 1 | • **Melexis MLX90640-BAA** Radiometric Thermal Array<br>• $32 \times 24$ pixels, 8–14 $\mu$m LWIR, $55^\circ \times 35^\circ$ FOV | ₹3,400 | **₹3,400** | **I²C Bus 1 (400 kHz to Linux).** Darkness and smoke penetration; detects human thermal signatures and surface heat anomalies at debris interfaces. |
| **8** | **Long-Range RF Telemetry (LoRa)** | 2 | • **Ebyte E22-900T22S (Semtech SX1262)**<br>• 868 MHz band (Indian WPC de-licensed), +22 dBm, UART<br>*(1× on UAV, 1× ground USB station bridge)* | ₹850 | **₹1,700** | **UART / TTL Serial (to Linux MPU).** Broadcasts 17-byte binary bit-packed triage telemetry over 3–5+ km NLoS range during complete cellular blackouts. |
| **9** | **Power Distribution & Integration** | 1 lot | • Matek PDB with dual 5V/12V BECs<br>• 5V 3A low-noise buck converter (for Arduino UNO Q)<br>• Silicone anti-vibration damping ball gimbal mount<br>• 14 AWG wiring, XT60 connectors, landing skids, hardware | ₹5,500 | **₹5,500** | **Regulated Power Tree.** Harmonic vibration isolation protecting flight IMU; clean, brownout-free regulated power rail to Qualcomm MPU mission board. |
| | **TOTAL PROTOTYPE COST** | | | | **₹37,400** | **Fully functional, edge-AI capable autonomous SAR scout** |

---

## 3. Engineering & Architectural Validations

### 3.1 Structured Electrical Power Budget (Calculated / Datasheet-Derived)

To ensure rigorous power accounting, consumption is analyzed across physical voltage rails and upstream regulator conversion efficiencies:

| Subsystem Device | Operating Rail Voltage | Rail Current Draw | Rail Power Draw | Upstream Conversion Efficiency | Battery-Side Power Draw (11.1V) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Arduino UNO Q (QRB2210 + STM32U585)** | 5.0 V DC | ~700 mA | 3.50 W | 92% (5V Buck Regulator) | **3.80 W** |
| **OV2710 1080p USB Camera** | 5.0 V DC | ~170 mA | 0.85 W | 92% (5V Buck Regulator) | **0.92 W** |
| **u-blox NEO-M8N GNSS Module** | 5.0 V DC | ~65 mA | 0.33 W | 92% (5V Buck Regulator) | **0.36 W** |
| **FlySky FS-iA6B RC Receiver** | 5.0 V DC | ~35 mA | 0.18 W | 92% (5V Buck Regulator) | **0.20 W** |
| **MLX90640 LWIR Thermal Array** | 3.3 V DC | ~24 mA | 0.08 W | 88% (UNO Q 3.3V LDO) | **0.09 W** |
| **ST VL53L1X Downward ToF Laser** | 3.3 V DC | ~12 mA | 0.04 W | 88% (UNO Q 3.3V LDO) | **0.05 W** |
| **InvenSense MPU6050 + MS5611 Baro** | 3.3 V DC | ~8 mA | 0.03 W | 88% (UNO Q 3.3V LDO) | **0.03 W** |
| **E22-900T22S LoRa (SX1262 Peak Burst)**| 3.3 V DC | ~120 mA | 0.40 W | 88% (UNO Q 3.3V LDO) | **0.45 W** *(38ms bursts)* |
| **Matek PDB Internal Resistance Losses** | 11.1 V DC | ~0.55 A | — | 100% | **0.20 W** |
| **SUBTOTAL ELECTRONICS LOAD** | | | **5.41 W** | | **6.10 W (Peak) / ~5.50 W (Nominal)** |
| **4× A2212 Motors + ESCs (Hover @ 1.58kg)**| 11.1 V DC | ~15.1 A | 168.0 W | Direct LiPo XT60 Rail | **168.0 W (Calculated)** |
| **TOTAL AIRCRAFT HOVER POWER** | **11.1 V DC** | **~15.65 A** | | | **~174.1 W** |

*Conclusion:* The compute, sensing, and telemetry stack operates within a **sub-6 W battery-side envelope**, minimizing non-propulsion energy consumption and preserving the vast majority of battery capacity for flight.

---

### 3.2 Corrected Flight Endurance & Mission Profile

* **Battery Parameters:** 3S 11.1V 4,500 mAh $\implies$ 49.95 Wh gross energy. At an 80% Depth-of-Discharge (DoD) cutoff to protect cell cycle life:
  $$\text{Usable Battery Energy} = 49.95\text{ Wh} \times 0.80 = \mathbf{39.96\text{ Wh (3.60 Ah)}}$$
* **Theoretical Continuous Hover Endurance:**
  $$T_{\text{hover}} = \frac{39.96\text{ Wh}}{174.1\text{ W}} \times 60\text{ min/hr} = \mathbf{13.77\text{ minutes (~13.8 min)}}$$
* **Planned Operational Search Mission Profile:**
  * **2.0 min:** Takeoff, climb to 15 m AGL, and transit to search sector boundary.
  * **6.0 min:** Autonomous Boustrophedon grid search at 3.0 m/s cruise covering ~67,000 $\text{m}^2$.
  * **2.0 min:** Return-to-Home (RTH) transit and automated vertical descent.
  * **Total Planned Mission:** **10.0 minutes**.
  * **Remaining Theoretical Energy Reserve:**
    $$\text{Reserve Margin} = \frac{13.77\text{ min} - 10.00\text{ min}}{13.77\text{ min}} = \mathbf{27.38\%\text{ (~27.5\% Energy Reserve / 3.8 min Contingency)}}$$

---

### 3.3 Mass Budget Accounting (1.58 kg Total)

| Component / Subsystem | Part Description | Mass (g) | Cumulative Mass (g) |
| :--- | :--- | :---: | :---: |
| **Carbon/Glass-Fiber Frame** | F450 plate & composite arms | 282 g | 282 g |
| **Propulsion Motors** | 4× A2212 1000KV brushless motors (52g each) | 208 g | 490 g |
| **Electronic Speed Controllers** | 4× 30A BLHeli ESCs with motor wiring (24g each) | 96 g | 586 g |
| **Propellers** | 4× 1045 composite propellers (11g each) | 44 g | 630 g |
| **Main Battery** | 3S 11.1V 4500mAh 30C LiPo pack with XT60 | 362 g | 992 g |
| **Main Compute SBC** | Arduino UNO Q (QRB2210 + STM32U585) | 42 g | 1,034 g |
| **Cameras & Optical Mount** | 1080p OV2710 (28g) + MLX90640 (6g) + Damped Mount (45g) | 79 g | 1,113 g |
| **Sensors & Navigation** | NEO-M8N GPS + mast (38g), VL53L1X ToF (4g), IMU/Baro (6g) | 48 g | 1,161 g |
| **Installed Radio Assembly** | E22 LoRa module + antenna + pigtail + FS-iA6B RX | 33 g | 1,194 g |
| **Power Distribution & Regulators** | Matek PDB (18g), 5V 3A buck regulator (14g) | 32 g | 1,226 g |
| **Wiring, Fasteners & Landing Gear** | 14 AWG silicone wire, landing skids, nylon standoffs, screws | 184 g | 1,410 g |
| **Unallocated Design Margin** | Unused mass allowance (no baseline auxiliary payload assumed) | 170 g | **1,580 g (1.58 kg)** |

*Conclusion:* The aircraft achieves an all-up mass of **1.58 kg**, remaining below the 2.0 kg mass threshold used in our design classification.

---

### 3.4 Hardware-to-Silicon Interface Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               ARDUINO UNO Q DUAL-BRAIN                                 │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│  MISSION COMPUTER: Qualcomm QRB2210 (Linux)│ FLIGHT CONTROLLER: STM32U585 (Zephyr RTOS) │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ • USB 2.0 Host ──► OV2710 1080p RGB (V4L2)│ • I2C Bus ─────► MPU6050 IMU (Addr 0x68)   │
│ • I2C 1 Bus   ──► MLX90640 Thermal (Addr  │ • I2C Bus ─────► MS5611 Baro (Addr 0x77)   │
│                   0x33, 400 kHz fast mode)│ • I2C Bus ─────► VL53L1X ToF (Addr 0x29)   │
│ • UART / TTL  ──► E22-900T22S LoRa Module │ • UART 1 ──────► NEO-M8N GNSS (115.2k UBX) │
│                   (SX1262, /dev/ttyHS0)   │ • UART 2 ──────► FS-iA6B RC RX (iBus)      │
│ • 32GB eMMC   ──► Offline Maps & OS Log   │ • 4× Timer PWM ──► 4× 30A Motor ESCs       │
├───────────────────────────────────────────┴────────────────────────────────────────────┤
│ ◄══════ SHARED-MEMORY IPC BRIDGE / ASYNCHRONOUS RPC MESSAGING (Inter-Core) ══════════► │
│   • Linux sends: Flight mode targets, search waypoints, RTH triggers                   │
│   • STM32 sends: 250 Hz EKF attitude (φ, θ, ψ), altitude H_AGL, GNSS coordinates      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Phase 1 Prototype vs. Phase 2 Production Unit

| Subsystem Parameter | Phase-1 Hackathon Prototype | Phase-2 NDRF Production Unit | Commercial Enterprise Drone (e.g., DJI M30T) |
| :--- | :--- | :--- | :--- |
| **Unit Acquisition Cost** | **₹37,400** (Calibrated Build) | **₹85,000 – ₹1,20,000** (~₹1.2 Lakh) | **₹12,00,000 – ₹14,00,000** |
| **Airframe Structure** | F450 Glass-Fiber / Nylon Composite | Toray 3K Foldable Carbon-Fiber Monocoque | Proprietary Magnesium-Aluminum Shell |
| **Thermal Imaging Sensor** | MLX90640 (32×24 Radiometric Array) | FLIR Lepton 3.5 (160×120) or InfiRay LWIR | Proprietary 640×512 Radiometric Sensor |
| **Geodetic Positioning** | u-blox NEO-M8N Multi-GNSS (2.5m CEP) | u-blox ZED-F9P Centimeter RTK-GNSS | Proprietary RTK Module (+₹2 Lakh add-on) |
| **All-Weather Sealing** | Open prototype development chassis | IP54 Conformal-Coated Sealed Enclosure | IP55 Weather Sealing |
| **Data Sovereignty & Cyber** | 100% Air-Gapped (Zero Cloud Uplink) | 100% Air-Gapped, HMAC-SHA256 Encrypted | Foreign cloud infrastructure dependencies |
| **Tactical Fleet Value** | Rapid proof-of-concept verification | **Deploy 10 Phoenix UAVs for cost of 1 M30T** | Single-point-of-failure budget risk |
