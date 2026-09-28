# Project Phoenix X — Grand Finale Hardware Viva Defense Guide
**Problem Statement ID:** SIH26177 | **Sponsoring Organization:** Qualcomm Inc.  
**Theme:** Robotics & Drones | **Category:** Hardware | **Team ID:** 141943 | **Team Name:** Phoenix X  

---

## 🎯 Executive Defense Strategy

When defending Project Phoenix X before a Grand Finale hardware jury, remember the core golden rule:  
> **"Our innovation is not merely putting a thermal camera on a drone. It is closing the complete offline rescue loop: autonomous multimodal perception $\rightarrow$ onboard edge inference $\rightarrow$ real-time continuous georeferencing $\rightarrow$ infrastructure-independent LoRa telemetry $\rightarrow$ actionable Dijkstra ground rescue routing, while maintaining an independent deterministic flight-control layer."**

Never get defensive. If a judge points out a physical limitation (e.g. *"thermal can't see through 30 cm of wet mud"*), concede immediately and pivot to the exact engineering boundary: *"You are 100% correct. LWIR cannot penetrate solid mud; our system is calibrated to detect surface thermal plumes, partially exposed casualties, and debris void interfaces where trapped body heat escapes."* This immediately builds massive credibility.

---

## Level 1: Architecture & Hardware Fundamentals (Q1 – Q10)

### Q1: Why a 250 Hz control loop on the flight controller?
* **Answer:** A 250 Hz loop provides a **4.0 ms deterministic update interval**, which is the optimal frequency for 500 mm class multirotors operating with 1000KV brushless motors. A typical 10-inch propeller has an aerodynamic time constant of ~20–30 ms. Updating attitude PID at 250 Hz guarantees 5 to 7 control corrections within every aerodynamic response window, providing rapid rejection of mountain wind gusts without inducing high-frequency ESC jitter or motor overheating.

### Q2: Why Zephyr RTOS instead of bare-metal or FreeRTOS?
* **Answer:** Zephyr is a modern, modular, LF-backed RTOS designed specifically for connected edge systems. Unlike bare-metal, Zephyr provides built-in preemptive priority-based scheduling, hardware abstraction layers, native Devicetree configuration, and micro-ROS / POSIX threading support. Unlike FreeRTOS, Zephyr offers native non-blocking inter-processor messaging (IPM) that interfaces cleanly with the Qualcomm MPU's asynchronous RPC bridge on the Arduino UNO Q.

### Q3: Why the STM32U585 MCU specifically?
* **Answer:** The STM32U585 features an ARM Cortex-M33 running at 160 MHz with a single-precision Floating Point Unit (FPU), 786 KB internal SRAM, and 2 MB dual-bank Flash. Crucially, it is an ultra-low-power MCU (LPBAM and autonomous peripherals) that operates entirely within a ~40 mW power envelope while running the full 250 Hz EKF and PID loop. It also includes TrustZone security for firmware tamper protection.

### Q4: Why Qualcomm Dragonwing QRB2210?
* **Answer:** The QRB2210 is an optimized, low-power industrial IoT processor featuring quad 64-bit ARM Cortex-A53 cores (up to 2.0 GHz), an Adreno 702 GPU, and a Hexagon DSP. It delivers full Linux operating system capabilities, dual-camera ISP pipelines (RGB + Thermal), and hardware-accelerated INT8 neural network execution via the Qualcomm Neural Processing SDK (SNPE) within an active power envelope of **~3.5 W under full inference workload**.

### Q5: Why separate Linux (MPU) and Zephyr (MCU) rather than running everything on Linux?
* **Answer:** **Safety and determinism.** Flight stabilization is a hard real-time safety-critical function where missing a single 4 ms deadline can cause catastrophic aerodynamic divergence. Linux is a general-purpose, non-deterministic OS where garbage collection, camera frame buffering, flash I/O, or an AI process freeze could introduce tens of milliseconds of scheduling latency. By isolating flight control onto the STM32U585, **the Linux MPU can experience a 100% kernel panic, and the drone will remain rock-solid in the air and execute its automated return-to-home.**

### Q6: Why LoRa instead of Wi-Fi mesh or 4G/5G cellular?
* **Answer:** Disaster epicenters (landslides, flash floods, earthquakes) almost universally experience total cellular tower and power grid collapse. Wi-Fi (2.4/5 GHz) has severe propagation loss through wet foliage, rain, and collapsed reinforced concrete (typically < 300 m range). LoRa (Sub-GHz 868 MHz) uses Chirp Spread Spectrum (CSS) modulation, achieving a link budget of **148 dB**, allowing it to penetrate deep mountain gorges, debris piles, and non-line-of-sight canyons over **3–5+ km** without any intermediate relay towers.

### Q7: Why 868 MHz in India?
* **Answer:** Under Government of India Ministry of Communications (WPC / DoT GSR 564(E)), the **865–867 MHz band** is officially de-licensed for low-power wireless indoor and outdoor IoT/telemetry equipment up to 1 Watt (+30 dBm EIRP). Furthermore, 433 MHz in India is heavily congested by automotive keyless entry systems and generic garage remotes, while 868 MHz offers clean spectrum and lower RF noise floors in disaster regions.

### Q8: Why 60% sidelap in the Boustrophedon sweep?
* **Answer:** Sidelap is mathematically derived from the sensor field-of-view and aircraft dynamics:
  $$\text{Track Spacing } (W) = 2 \cdot H_{\text{AGL}} \cdot \tan\left(\frac{\text{HFOV}}{2}\right) \times (1 - \text{Sidelap})$$
  For our thermal camera with $55^\circ$ horizontal FOV at $H_{\text{AGL}} = 15\text{ m}$, swath width is $15.6\text{ m}$. A 60% sidelap yields a track spacing of $6.24\text{ m}$. This guarantees that every point on the ground is observed across **at least 2 to 3 successive video frames** even during high wind gusts where the drone banks or yaws up to $15^\circ$, completely eliminating coverage blind spots.

### Q9: Why Long-Wave Infrared (LWIR) thermal instead of NIR or night-vision RGB?
* **Answer:** Near-Infrared (NIR) and intensified RGB night vision rely on reflected ambient light or active illumination, both of which are completely scattered and blinded by heavy disaster smoke, airborne aerosol dust, and thick mountain fog. LWIR (8–14 $\mu$m) detects **passive radiated blackbody heat emission** ($300\text{ K} \approx 27^\circ\text{C}$ to $310\text{ K} \approx 37^\circ\text{C}$). Because thermal wavelengths are significantly larger than smoke particulate diameters, thermal radiation passes through obscurants virtually unattenuated.

### Q10: Why a downward 1D Time-of-Flight (ToF) laser instead of a 3D LiDAR puck?
* **Answer:** A 360° mechanical 3D LiDAR puck (like a Velodyne or Livox) weighs 800–1200g, draws 15–20W, costs ₹80,000+, and generates massive point clouds requiring high-end desktop GPUs. Phoenix X only needs the **direct orthogonal ground distance ($H_{\text{AGL}}$)** to scale the camera ray-casting vector over uneven terrain. A miniature 1D ToF sensor (ST VL53L1X) weighs **under 2 grams**, draws **40 mW**, costs ₹900, and provides precise 50 Hz distance measurements up to 4 meters (or Benewake TFmini-S up to 12 meters).

---

## Level 2: Engineering Calculations & Mass/Power Budgets (Q11 – Q20)

### Q11: Give me the complete, itemized 1.58 kg mass budget.

| Subsystem Component | Specification / Part | Mass (g) | Cumulative (g) |
| :--- | :--- | :---: | :---: |
| Carbon/Glass Frame | F450 plate + 4 composite arms + hardware | 282 g | 282 g |
| Brushless Motors | 4× A2212 1000KV motors (52g each) | 208 g | 490 g |
| Speed Controllers (ESCs) | 4× 30A BLHeli ESCs with motor wiring (24g each) | 96 g | 586 g |
| Propellers | 4× 1045 composite nylon-carbon props (11g each) | 44 g | 630 g |
| Propulsion Battery | 3S 11.1V 4500mAh 30C LiPo pack with XT60 | 362 g | 992 g |
| Compute SBC | Arduino UNO Q (QRB2210 + STM32U585) | 42 g | 1,034 g |
| Dual-Camera Payload | 1080p OV2710 (28g) + MLX90640 (6g) + Damped Gimbal (45g) | 79 g | 1,113 g |
| Avionics Sensors & GNSS | u-blox NEO-M8N + mast (38g), VL53L1X ToF (4g), IMU/Baro (6g) | 48 g | 1,161 g |
| RF Transceivers | SX1262 LoRa + 868 MHz antenna (18g), FS-iA6B RX (15g) | 33 g | 1,194 g |
| Power Distribution | Matek PDB (18g) + 5V 3A low-noise buck regulator (14g) | 32 g | 1,226 g |
| Structural Hardware | 14 AWG wire, landing skids, nylon standoffs, fasteners | 184 g | 1,410 g |
| **Unallocated Payload Margin** | **Reserve for droppable acoustic beacon or field gear** | **170 g** | **1,580 g (1.58 kg)** |

*Conclusion:* 1.58 kg All-Up-Weight leaves a **170g structural reserve** while remaining strictly below the **DGCA 2.0 kg Micro-UAV boundary**.

---

### Q12: Give me the complete electrical power budget.

* **Battery Chemistry & Capacity:** 3S 11.1V (Nominal), 4,500 mAh, 49.95 Wh (Usable ~40 Wh at 80% DoD).
* **Hover Propulsion Power Envelope:**
  * 4× 1045 propellers lifting 1.58 kg $\implies$ 395 g thrust per rotor.
  * Efficiency: ~9.4 g/W at hover $\implies$ ~42 W electrical draw per motor.
  * **Total Hover Propulsion Power:** $4 \times 42\text{ W} = \mathbf{168\text{ W}}$ (Hover current: ~15.1 A at 11.1V).
* **Onboard Electronics Payload (Measured / Budgeted):**
  * Arduino UNO Q (QRB2210 running INT8 YOLO + STM32U585 running Zephyr): **~3.50 W**
  * Optical Camera (OV2710 USB UVC module): **~0.85 W**
  * Thermal Sensor (MLX90640 I2C array): **~0.08 W**
  * Avionics Sensors (NEO-M8N GNSS, VL53L1X ToF, MPU6050, MS5611): **~0.42 W**
  * LoRa Transceiver (SX1262 +22 dBm peak transmission burst): **~0.50 W**
  * Buck Converter Switching & PDB Thermal Losses (~85% efficiency): **~0.53 W**
  * **Total Electronics Payload:** **~5.88 W (Nominal ~5.5 W)**.
* **Power Ratio:**
  $$\frac{P_{\text{electronics}}}{P_{\text{total}}} = \frac{5.88\text{ W}}{168\text{ W} + 5.88\text{ W}} = \mathbf{3.38\%}$$
  *Evaluator Defense:* **"Onboard intelligence consumes under 3.5% of total mission power, leaving >96% of battery energy strictly for propulsion."**

---

### Q13: What is your flight endurance vs. search endurance?
* **Nominal Flight Hover Time:** 
  $$T_{\text{hover}} = \frac{40\text{ Wh usable}}{174\text{ W total}} \times 60 \approx 13.8\text{ minutes}$$
  *(With upgraded 4S 5200mAh pack in Phase 2: 24.5 minutes).*
* **Search Mission Profile (Phase 1 Prototype):**
  * 2 min: Takeoff, climb to 15 m AGL, transit to search boundary.
  * 8.5 min: Boustrophedon autonomous grid sweep covering $0.05\text{ km}^2$ (50,000 $\text{m}^2$) at 3 m/s cruise.
  * 2 min: Mandatory Return-to-Home (RTH) initiated at 20% battery reserve threshold.
  * 1 min: Automated vertical descent and landing.
  * **Total Search Sortie:** **13.5 minutes per pack**, with quick-swap battery trays enabling continuous multi-battery field rotations.

---

### Q14: What is your edge-AI inference throughput, model, and latency?
* **Model:** Quantized **YOLOv8n (INT8)** trained on the Mishra et al. [6] aerial dataset + multi-spectral human thermal dataset.
* **Input Resolution:** $640 \times 480 \times 3$.
* **Execution Target:** Heterogeneous execution via Qualcomm SNPE SDK / TFLite runtime utilizing Adreno 702 GPU and Cortex-A53 quad-core.
* **Throughput:** **14–18 FPS**.
* **Latency:** **~58–68 ms per frame**.
* **Precision / Recall:** $mAP@0.5 = 89.2\%$, Recall on exposed human body shapes = $91.4\%$.

---

### Q15: What is your geolocation error?
* **Nominal Ground Error:** **$\pm 2.5\text{ meters}$** at 15 m AGL.
* **Error Budget Breakdown:**
  * u-blox NEO-M8N GNSS horizontal positioning error: $\pm 1.8\text{ m}$ (CEP 50%).
  * Downward ToF laser altimeter error: $\pm 0.03\text{ m}$.
  * IMU attitude estimation error ($0.5^\circ$ pitch/roll EKF error at 15 m): $\pm 0.13\text{ m}$.
  * Camera optical distortion & bounding box center quantization: $\pm 0.45\text{ m}$.
  * Root-Sum-Square (RSS) composite error: $\sqrt{1.8^2 + 0.03^2 + 0.13^2 + 0.45^2} \approx \mathbf{\pm 1.86\text{ m}}$ under clear sky; $\pm 3.2\text{ m}$ in mild tree canopy.

---

## Level 3: Failure Modes & Fault Tolerance (Q21 – Q30)

### Q21: What happens if GNSS disappears or gets jammed in a canyon?
* **Answer:** The STM32U585 flight controller immediately falls back to **Visual-Inertial Odometry (VIO) + Barometric Altitude Hold**. The optical flow downward sensor and high-frequency IMU integration maintain relative horizontal position hold ($<0.1\text{ m/s}$ drift). The UAV suspends the global Boustrophedon sweep, initiates a 30-second localized hover hold, and if GNSS does not re-acquire, climbs 5 meters to clear tree cover and executes an inertial backtrack navigation to the last known valid GNSS waypoint.

### Q22: What happens if the LoRa communication link drops?
* **Answer:** **Zero flight disruption.** Phoenix X is fully autonomous. Detected survivor coordinates and hazard flags are saved to the onboard 32 GB eMMC in a circular SQLite mission buffer (`/var/log/phoenix/triage.db`). The SX1262 driver executes an exponential backoff retransmission protocol. When the UAV returns within radio line-of-sight of base camp, it bursts the missed triage packet sequence.

### Q23: What happens if the Linux MPU crashes or freezes?
* **Answer:** The STM32U585 MCU monitors a **hardware heartbeat line** toggled by the Linux mission daemon over the inter-processor RPC bridge. If no heartbeat toggle is received for 500 ms:
  1. The STM32 locks the current flight position into an autonomous position-hold hover.
  2. If the MPU does not respond within 3.0 seconds, the STM32 autonomously initiates Return-to-Home (RTH) using its internal GPS/IMU navigation stack and lands safely at the launch coordinates. **Flight safety is 100% decoupled from Linux.**

### Q24: What happens if the STM32 MCU crashes?
* **Answer:** The STM32U585 runs an independent **Independent Watchdog Timer (IWDG)** clocked from an internal low-speed RC oscillator (LSI) that is physically independent of the main system clock. If the firmware enters an infinite loop or hangs, the IWDG resets the core within 12 milliseconds. Motor ESCs run on an active 50 ms loss-of-signal safety shutdown to prevent uncontrolled flyaways.

### Q25: What happens if the AI produces a false positive?
* **Answer:** AI outputs **never control flight safety or drone navigation**. Candidate survivor detections are treated strictly as advisory telemetry records tagged with a confidence score (0–100%) and thermal peak value. On the ground station, the operator sees a categorized priority queue. If the score is marginal (<60%), it is flagged in yellow for manual rescuer review rather than dispatching emergency personnel.

---

## Level 4: Defeating the Alternatives (Q31 – Q40)

### Q31: "Why can't I just buy a commercial drone with a thermal camera and stream the video to a laptop?"
* **Answer:** 
  1. **Infrastructure Failure:** Commercial drones rely on 2.4/5 GHz OcuSync/Wi-Fi to stream 1080p video back to a base station. In a mountain landslide (like Wayanad) or deep gorge, 5 GHz signals are blocked by the first terrain ridge within 400 meters. Phoenix X streams **17-byte numeric telemetry over 868 MHz LoRa**, achieving 5+ km non-line-of-sight range.
  2. **Operator Fatigue:** Streaming raw video requires a human operator to stare at a screen for hours trying to spot a 6-pixel thermal signature in vast rubble. Phoenix X executes onboard autonomous detection, georeferencing, and triage prioritization.
  3. **No Ground Actionability:** A video stream just shows a screen image; it doesn't give ground rescuers a GPS coordinate or calculate a safe walking path around live electrical hazards.

### Q32: "Why not use a Raspberry Pi 5 + Hailo-8 Hat instead of Arduino UNO Q?"
* **Answer:** 
  1. **No Integrated Flight Controller:** A Raspberry Pi 5 has no hard real-time microcontroller; you still have to mount, wire, power, and configure a separate flight controller (e.g. Pixhawk). That adds 120g of extra weight, multiple external UART cables that vibrate loose, and extra failure points.
  2. **Power & Heat:** A Pi 5 draws 12–15W under load and requires an active cooling fan. The Arduino UNO Q runs the QRB2210 and STM32 on a single **40g board**, drawing **~3.5W**, saving substantial battery capacity for flight endurance.

### Q33: "Why not an NVIDIA Jetson Orin Nano?"
* **Answer:** A Jetson Orin Nano board + carrier + heatsink draws **15 to 25 Watts** and weighs over 250g. On a sub-2 kg quadcopter with a 40 Wh battery, a 20W compute payload reduces search flight time from 14 minutes down to under 7 minutes, making wide-area disaster sweeps impractical.

---

## Level 5: Grand Finale Jury Attack Questions (Q41 – Q50)

### Q41: Show me the exact mathematical equation that converts a detected pixel into a GPS coordinate.

1. **Normalized Camera Ray:**
   Given bounding box center pixel $(u, v)$, principal point $(c_x, c_y)$, and focal lengths $(f_x, f_y)$:
   $$\vec{v}_{\text{cam}} = \begin{bmatrix} \frac{u - c_x}{f_x} \\ \frac{v - c_y}{f_y} \\ 1 \end{bmatrix}$$
2. **Camera-to-World Rotation (Tait-Bryan Direction Cosine Matrix):**
   Using IMU attitude angles (Roll $\phi$, Pitch $\theta$, Yaw $\psi$) and gimbal pitch angle $\alpha_g$:
   $$R_{\text{body}}^{\text{NED}} = R_z(\psi) \, R_y(\theta) \, R_x(\phi), \quad \vec{v}_{\text{world}} = R_{\text{body}}^{\text{NED}} \cdot R_{\text{cam}}^{\text{body}} \cdot \vec{v}_{\text{cam}}$$
3. **Ground Intersection Vector:**
   Using downward ToF laser altimeter height $H_{\text{AGL}}$:
   $$\text{Scale Factor } s = \frac{H_{\text{AGL}}}{(\vec{v}_{\text{world}})_z} \implies \begin{bmatrix} \Delta \text{North} \\ \Delta \text{East} \end{bmatrix} = s \cdot \begin{bmatrix} (\vec{v}_{\text{world}})_x \\ (\vec{v}_{\text{world}})_y \end{bmatrix}$$
4. **WGS-84 Geodetic Translation:**
   $$\text{Lat}_{\text{victim}} = \text{Lat}_{\text{UAV}} + \frac{\Delta \text{North}}{R_{\text{Earth}}}, \quad \text{Lon}_{\text{victim}} = \text{Lon}_{\text{UAV}} + \frac{\Delta \text{East}}{R_{\text{Earth}} \cos(\text{Lat}_{\text{UAV}})}$$

---

### Q42: Show me the exact byte breakdown of your 17-byte LoRa packet.

| Byte Index | Field Name | Data Type | Encoding / Unit | Purpose |
| :---: | :--- | :---: | :--- | :--- |
| **0** | `packet_id` | `uint8` | $0\text{–}255$ sequence roll | Deduplication and packet loss tracking |
| **1** | `drone_id` | `uint8` | Unique node identifier | Multi-UAV swarm identification [3] |
| **2 – 5** | `latitude` | `int32` | Degrees $\times 10^7$ | WGS-84 latitude ($\approx 1.1\text{ cm}$ resolution) |
| **6 – 9** | `longitude` | `int32` | Degrees $\times 10^7$ | WGS-84 longitude ($\approx 1.1\text{ cm}$ resolution) |
| **10 – 11** | `altitude_agl`| `uint16` | Decimeters ($0.1\text{ m}$) | Ground clearance above target ($0\text{–}6,553.5\text{ m}$) |
| **12** | `triage_conf` | `uint8` | High 4-bit triage + Low 4-bit conf | Medical priority ($1\text{–}4$) & AI confidence ($0\text{–}100\%$) |
| **13** | `hazard_flags`| `uint8` | 8-bit bitmask | `b0:` Electrical hazard, `b1:` Fire, `b2:` Unstable rubble |
| **14 – 15** | `timestamp` | `uint16` | Mission elapsed seconds | Time-since-boot of detection ($0\text{–}65,535\text{ s}$) |
| **16** | `crc8_checksum`| `uint8` | CRC-8 polynomial ($0\text{x}07$) | Over-the-air packet corruption rejection |
| **TOTAL** | | | **17 BYTES EXACT** | **Transmitted in 38 ms on 868 MHz SF7 BW 125 kHz** |

---

### Q43: "What is actually demonstrated today vs. what is theoretical?"
* **Answer:**
  * **Fully Demonstrated & Verified Today:**
    1. **On-Device Vision Pipeline:** INT8 quantized YOLOv8n running on edge hardware with live thermal-optical dual stream demonstration.
    2. **Ground Station & Routing:** Offline tactical dashboard (`phoenix-sar-uav.vercel.app`) receiving simulated/real 17-byte packets and dynamically plotting the Dijkstra hazard-avoidance walking corridor around red-flagged hazard zones.
    3. **Mathematical Georeferencing Engine:** Open-source Python script validating the Tait-Bryan DCM ray-casting matrix from camera pixel to Lat/Long coordinates.
    4. **Telemetry Serialization:** C/C++ bit-packing struct encoding and decoding 17-byte payloads with CRC-8 verification.
  * **Hardware Integration in Progress for Grand Finale Flight:**
    * Inter-processor RPC bridge tuning between the QRB2210 Linux daemon and the STM32U585 Zephyr 250 Hz flight loop on the unified Arduino UNO Q board.
