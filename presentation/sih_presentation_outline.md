# Smart India Hackathon (SIH) 2026 — Official Idea Submission Deck
**Project Title:** PROJECT PHOENIX: Autonomous Multi-Spectral Edge-AI UAV for Rapid Disaster Reconnaissance & Survivor Geotagging  
**Problem Statement ID:** SIH26177  
**Sponsoring Organization:** Qualcomm Inc.  
**Theme:** Robotics and Drones | **Category:** Hardware  
**Team Name:** Team Phoenix  
**Team Background:** 2nd-Year Undergraduates (CSE, AI & Data Science, Cyber Security)  
**Editable PPT File:** [`presentation/Team_Phoenix_SIH26177_Official_Deck.pptx`](Team_Phoenix_SIH26177_Official_Deck.pptx)

---

## Slide 1: Cover Slide
* **Title:** PROJECT PHOENIX: Autonomous Search & Rescue UAV
* **Subtitle:** Deployable Multi-Spectral Edge-AI Drone for Rapid Victim Localization & Hazard Reconnaissance in Communication-Denied Disasters
* **Metadata:**
  * SIH Problem Statement ID: **SIH26177**
  * Sponsoring Organization: **Qualcomm Inc.**
  * Category: **Hardware** | Theme: **Robotics and Drones**
  * Team: **Team Phoenix** (CSE + AI/DS + Cyber Security)

---

## Slide 2: Problem Statement & Field Background
* **Title:** The Critical Need: Disaster Reconnaissance in the "Golden 72 Hours"
* **Real-World Context:** The Wayanad Landslides (July 2024) & Himalayan Disasters
* **Pillar 1: Communication Blackout**
  * Cellular towers (4G/5G) and electrical grids are instantly severed in disaster zones.
  * Cloud-dependent drones and internet-reliant AI models become 100% inoperable.
  * Ground teams operate in an information vacuum.
* **Pillar 2: Environmental Occlusion**
  * Mud slush, collapsed rubble, thick rain clouds, and smoke camouflage victims from ordinary RGB cameras.
  * Search operations are traditionally halted at sunset when visual light drops to zero, wasting critical survival hours.
* **Pillar 3: Responder Hazard & High Mortality**
  * Victim survival probability plummets after the first 72 hours.
  * Ground search teams (NDRF/SDRF) blindly navigate secondary hazards: gas leaks, live submerged cables, and secondary mudslides.

---

## Slide 3: Proposed Solution & Key Innovations
* **Title:** Proposed Solution: Project Phoenix Autonomous SAR UAV
* **Core Solution Overview:**
  * **100% Onboard Edge Intelligence:** Performs autonomous search sweeps and deep learning detection without any internet or cloud connection.
  * **Multi-Spectral Vision Core:** Dual-stream co-registered RGB + Long-Wave Infrared (LWIR) thermal sensors detect living human body heat signatures (36°C–38°C) through smoke, mud, and night darkness.
  * **Tait-Bryan Ray-Casting Geolocation:** Instantly calculates real-world ground GPS coordinates for detected survivors without hovering overhead.
  * **Offline First-Responder GCS:** Beams victim pins and hazard heatmaps directly to local rugged tablets over long-range radio.
* **Key Innovations:**
  * **Dual-Brain Architecture on Single Board:** Powered by the **Arduino UNO Q**, integrating the **Qualcomm Dragonwing™ QRB2210 Linux MPU** with an **STM32U585 Real-Time MCU** (replaces a flight controller + companion computer in just 40g).
  * **Sub-5W Edge Deep Learning:** INT8-quantized YOLO model running on the Qualcomm NPU; complies with Bouabdallah's 90/10 power law.
  * **Dual-Tier Resilient Telemetry:** Wi-Fi mesh for short-range video + ultra-reliable **LoRa (868 MHz)** emergency beacon transmitting coordinates over 5+ km.
  * **Anti-Compass Drift Heading:** Fuses Visual-Inertial Odometry (VIO) / Optical Flow to reject magnetic distortions in steel-reinforced rubble.

---

## Slide 4: Technical Architecture & Methodology
* **Title:** Technical Architecture: The Dual-Brain Edge Pipeline
* **Step 1: Sensing Layer**
  * OmniVision 1080p RGB Camera + Melexis MLX90640 LWIR Thermal Sensor on a damped mount.
  * Downward LiDAR/Sonar for precision altitude hold and terrain following.
  * Silicone dampening mounts to isolate high-frequency propeller vibrations.
* **Step 2: Real-Time MCU (STM32U585 @ 250 Hz)**
  * Runs Zephyr RTOS with hard-deterministic 4ms PID flight stabilization loops.
  * Joop Broking YMFC-32 flight stabilization heritage.
  * 350 Hz patched PWM for direct brushless ESC motor control.
  * Asynchronous RPC bridge prevents Linux tasks from blocking flight stability.
* **Step 3: Edge AI MPU (Qualcomm Dragonwing QRB2210)**
  * Debian Linux host executing INT8-quantized YOLO-nano at 10–15 FPS.
  * Multi-spectral late fusion: blends RGB visual features with thermal heat signatures.
  * Tait-Bryan Ray-Casting engine calculates ground Lat/Long coordinates.
* **Step 4: Tactical Ground Station (GCS)**
  * Offline-first React + Leaflet web dashboard.
  * Automated Survivor Priority Triage Queue (timestamps, confidence, body heat).
  * Dijkstra shortest safe-path routing for ground rescue crews.

---

## Slide 5: Engineering Feasibility & Commercial Viability
* **Title:** Engineering Feasibility & Commercial Viability
* **Mathematical Sizing (Bouabdallah Sizing Laws):**
  * **Thrust-to-Weight Ratio $\beta \ge 2.0$:** Provides 50% thrust margin for turbulence, heavy wind, and evasive climb in disaster rubble.
  * **38% Battery Mass Fraction:** Sized via Bouabdallah's Cost Factor ($C$) and Autonomy ($Au$) optimization; avoids payload-diminishing returns.
  * **Weight Budget (Under DGCA 2.0 kg Micro-Drone Category):**
    * Airframe & 4x BLDC Motors + Props: 720g
    * Battery (4S 5200mAh LiPo): 560g
    * Dual-Brain Avionics (UNO Q + Sensors): 120g
    * Dual-Camera Gimbal Payload: 180g
    * Total All-Up-Weight (AUW): **1.58 kg** (Safe margin below 2.0 kg).
* **Market & Cost Viability Comparison:**
  * **Commercial Standard (DJI Matrice 30T):** ₹9,00,000 – ₹14,00,000; closed ecosystem; foreign server telemetry risk; no custom edge AI.
  * **Project Phoenix Platform:** **₹85,000 – ₹1,40,000 (1/8th of commercial cost)**; 100% Indian data sovereignty; programmable edge AI; swappable batteries; deployable in $< 3$ minutes.
  * **Swarm Scalable:** A single disaster battalion can deploy **5 Phoenix units** for the price of one proprietary enterprise drone.

---

## Slide 6: Research Foundations & Team Competency
* **Title:** Research Foundations & Team Phoenix Competency
* **Academic References & Prior Art:**
  1. *Dr. Samir Bouabdallah (EPFL Thesis No. 3727, 2007):* Grounded our 12-state rigid body dynamics, spectral loop separation, and 90/10 electrical power sizing laws.
  2. *NASA Technical Memorandum 4741 (NASA Langley, 1996):* Informed selection of zero-pitching-moment ($C_{m, c/4} = 0$) reflexed airfoils to eliminate blade flutter and IMU vibrations.
  3. *JRFCQAI Open-Source Dual-Brain Architecture (Ravi Butani, 2024):* Validated Zephyr RTOS (STM32U5) + Debian Linux (Qualcomm QRB2210) on Arduino UNO Q for UAV flight.
* **Team Phoenix Division of Labor (2nd-Year Undergrads):**
  * **AI & Data Science (AD):** Multi-spectral dataset curation; INT8 model quantization for the Qualcomm Dragonwing NPU.
  * **Computer Science & Engineering (CSE):** Tait-Bryan Ray-Casting coordinate projection; offline Web GCS (React + Leaflet).
  * **Cyber Security (CY):** Telemetry packet HMAC authentication; LoRa emergency fallback protocol and store-and-forward sync.
