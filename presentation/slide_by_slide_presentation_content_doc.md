# Team Phoenix — Slide-by-Slide Master Content & Presentation Script
**Project Title:** PROJECT PHOENIX: Autonomous Multi-Spectral Edge-AI UAV for Rapid Disaster Reconnaissance & Survivor Geotagging  
**Problem Statement ID:** SIH26177 (Smart India Hackathon 2026)  
**Sponsoring Organization:** Qualcomm Inc.  
**Theme:** Robotics and Drones | **Category:** Hardware  
**Target Delivery:** 6-Minute Official SIH Presentation (1 minute per slide)  
**Associated Presentation Files:**  
* Latest Deck: [`presentation/Team_Phoenix_SIH26177_Deck_v2.pptx`](Team_Phoenix_SIH26177_Deck_v2.pptx)  
* Baseline Deck: [`presentation/Team_Phoenix_SIH26177_Deck_v1.pptx`](Team_Phoenix_SIH26177_Deck_v1.pptx)  

---

## SECTION 1: SLIDE 1 — TITLE & PROJECT IDENTITY

### 1.1 Visual Layout & Framing
* **Header:** SMART INDIA HACKATHON 2026 — HARDWARE EDITION
* **Sub-Header:** Ministry of Education & Qualcomm Inc.
* **Main Card (Left):** Key Hackathon & Problem Identifiers
* **Hero Accent Card (Right - Blue Gradient):** Quick System Highlights (Dual-Brain, Sub-5W compute, 3–5 km LoRa)
* **Footer:** Project Phoenix | SIH26177 | Team Specialization

### 1.2 Exact On-Slide Content
```text
[Main Details Box]
• Problem Statement ID: SIH26177
• Problem Statement Title: A deployable AI-powered autonomous drone that aids search-and-rescue 
  operations by detecting people and hazards, thereby improving responder safety and reducing 
  victim discovery time.
• Sponsoring Organization: Qualcomm Inc.
• Theme: Robotics and Drones  |  Category: Hardware
• Team Name: Team Phoenix
• Team Specialization: 2nd-Year Undergraduates (CSE + AI & Data Science + Cyber Security)

[Hero Highlight Box]
PROJECT PHOENIX SAR UAV
Dual-Brain Edge-AI Scout for Zero-Infrastructure Disaster Reconnaissance
✓ Qualcomm Dragonwing™ QRB2210 Linux MPU
✓ STM32U5 Zephyr RTOS Flight Stabilization
✓ Dual-Stream Co-Registered RGB + Thermal Fusion
✓ 3-5 km Non-Line-of-Sight LoRa Telemetry
✓ Tait-Bryan Ray-Casting Target Geolocation
```

### 1.3 Speaker Verbal Script (45 Seconds)
> *"Respected judges and representatives from Qualcomm, we are Team Phoenix, representing an interdisciplinary team across Computer Science, AI, and Cyber Security.  
> We are here to present our solution for Problem Statement SIH26177: an autonomous, edge-native Search and Rescue UAV engineered specifically for communication-severed disaster zones.  
> By leveraging a breakthrough dual-brain hardware architecture powered by the Qualcomm Dragonwing processor on the Arduino UNO Q, our drone delivers real-time survivor detection, instant GPS coordinate projection, and long-range emergency telemetry—operating with zero cloud or cellular dependency."*

### 1.4 Judge Q&A Defense
* **Q: Why does a 2nd-year undergraduate team think they can build an autonomous UAV?**
  * **Answer:** *"We did not start from scratch in an isolated bubble. We built our systems architecture on three validated scientific pillars: Bouabdallah’s rotor dynamic laws from EPFL, the open-source JRFCQAI flight architecture on Qualcomm silicon, and the latest 2024 Elsevier research on ROS-LoRa disaster bridges. Our team divides the workload strictly across our domain specializations: AI for model quantization, CSE for ray-casting and offline GCS, and Cyber Security for packet encryption and resilient radio protocols."*

---

## SECTION 2: SLIDE 2 — PROBLEM STATEMENT & PROPOSED SOLUTION

### 2.1 Visual Layout & Framing
* **Top Header:** Disaster Reconnaissance & Emergency Survivor Triage
* **Left Card (Red Badge):** PROBLEM STATEMENT & Critical Operational Gaps
* **Right Card (Teal Badge):** PROPOSED SOLUTION & Key Capabilities
* **Middle Strip (5 Purple Pills):** Core Innovations (Dual-Brain, Sub-5W AI, Ray-casting, LoRa, VIO)
* **Bottom Comparison Bar:** Traditional Foot Search (Red) vs. Phoenix Autonomous Aerial Triage (Green)

### 2.2 Exact On-Slide Content
```text
[Badge: PROBLEM STATEMENT]
During catastrophic disasters (e.g., Wayanad landslides, earthquakes), emergency response hits three fatal barriers:
• Comms Blackout: Cellular 4G/5G towers and power grids are wiped out; cloud-dependent AI drones fail instantly.
• Environmental Occlusion: Mud slush, torrential rain, thick smoke, and darkness blind standard visual cameras.
• The "Golden 72 Hours" Mortality Curve: Victim survival plummets after 72 hours; slow manual foot sweeps take days.
• First Responder Hazard: Rescue teams walk blindly into secondary hazards: gas leaks, live cables, and shifting rubble.

[Badge: PROPOSED SOLUTION]
Project Phoenix: A deployable autonomous multirotor scout engineered for zero-connectivity disaster zones:
• 100% Onboard Edge AI: Runs deep learning models directly on an onboard Qualcomm NPU with zero internet reliance.
• Dual-Band Sensing: Fuses 4K RGB with LWIR Thermal (8-14μm) to detect living body heat (36°C-38°C) through fog and darkness.
• Tait-Bryan Ray-Casting: Calculates victim Lat/Long GPS coordinates instantly from altitude without hovering overhead.
• Offline Tactical GCS: Displays live victim pins, thermal readings, and safe ground rescue routes on local tablets.

[Badge: INNOVATION / UNIQUENESS - 5 Rounded Pills]
1. Dual-Brain Architecture: Arduino UNO Q uniting Qualcomm QRB2210 MPU + STM32U5 MCU in 40g.
2. Sub-5W Edge YOLO: INT8 quantized neural model running on NPU; preserves 90% power for flight.
3. Ray-Cast Geolocation: Tait-Bryan rotation matrix projects bounding boxes to ground GPS pins.
4. ROS-LoRa P2P Bridge: 17-byte bit-packed telemetry stream over 5+ km (Souli et al., Elsevier 2024).
5. Anti-Compass Drift VIO: Visual Odometry heading overrides magnetometer in steel rubble (Bouabdallah 2007).

[Bottom Contrast Bar]
• TRADITIONAL SEARCH: Manual Foot Sweeps ➔ Blind Rubble Digging ➔ Halted at Sunset ➔ High Casualty Risk
• VS. PHOENIX APPROACH: Autonomous Aerial Sweep ➔ 24/7 Thermal Night Vision ➔ Exact GPS Ray-Casting ➔ Safe Rescuer Route
```

### 2.3 Speaker Verbal Script (60 Seconds)
> *"In disasters like the July 2024 Wayanad landslides, the first 72 hours determine whether trapped victims live or die. But rescue crews faced an impossible situation: cell towers were down, roads were washed out, and survivors were submerged in thick mud slush that completely camouflaged them from standard cameras.  
>  
> Traditional drones failed because they require internet connections or stream video that ground operators have to manually watch for hours.  
>  
> Project Phoenix changes this paradigm. Our drone is 100% edge-native. It sweeps an autonomous search grid, uses thermal imaging to spot the 37°C body heat of living victims through mud or smoke, mathematically projects their exact GPS coordinates in real-time, and beams these coordinates over a 5 km LoRa link to first responders—enabling targeted extraction while keeping rescue teams safe from unstable terrain."*

---

## SECTION 3: SLIDE 3 — TECHNICAL APPROACH & ARCHITECTURE

### 3.1 Visual Layout & Framing
* **Top Header:** Technical Approach: Dual-Brain Architecture & Workflow
* **Left Column (Blue Cards):** 6-Step Implementation Workflow with circular numbered badges
* **Right Column Top (Purple Card):** Dual-Brain Hardware Architecture & RPC Bridge Split
* **Right Column Bottom (Green Card):** Verified Open-Source Tech Stack

### 3.2 Exact On-Slide Content
```text
[Badge: IMPLEMENTATION WORKFLOW - 6 Numbered Steps]
1. Sector Partition & Rapid Launch:
   Operator outlines a 2 km² search grid on an offline tablet GCS; UAV launches in under 3 minutes.
2. Autonomous Grid Sweep:
   Executes Boustrophedon lawnmower search trajectory powered by the STM32U5 / Zephyr RTOS at 250 Hz.
3. Multi-Spectral Perception:
   Co-registered RGB + LWIR Thermal sensors detect human body contours; INT8 YOLO model outputs bounding boxes.
4. Ray-Cast Geolocation Engine:
   Tait-Bryan rotation matrix converts image coordinates + LiDAR altitude into real-world Lat/Long coordinates.
5. Binary LoRa Packet Burst:
   Souli et al. (2024) protocol compresses victim coordinates into an ultra-compact 17-byte binary packet (868 MHz).
6. Tactical GCS Triage & Safe Routing:
   GCS ranks survivors by body temperature urgency and charts a hazard-free ground route for NDRF crews.

[Badge: SYSTEM ARCHITECTURE - Dual-Brain Split]
• Real-Time MCU (STM32U585 running Zephyr RTOS @ 250 Hz):
  - Deterministic 4ms PID flight stabilization loop (Joop Broking YMFC-32 flight heritage)
  - 350 Hz patched PWM for direct brushless motor ESC response
  - Interfaces MPU6050 (IMU), MS5611 (Barometer), and downward LiDAR
• Mission Computer (Qualcomm Dragonwing™ QRB2210 running Debian Linux):
  - Asynchronous non-blocking RPC bridge (ensures zero flight loop jitter)
  - Onboard INT8 YOLO object detection running on Qualcomm NPU (< 5W power draw)
  - Semtech SX1262 LoRa telemetry driver

[Badge: TECH STACK]
• Flight Control: Zephyr RTOS, YMFC-32 Core, PX4 Autopilot
• Edge AI & Vision: Qualcomm SNPE, ONNX Runtime INT8, OpenCV
• Middleware: ROS2 Humble, MAVLink v2, micro-ROS
• Telemetry: Semtech SX1262 Raw LoRa P2P (868 MHz)
• Ground Station: React, Leaflet, Tailwind CSS, WebSockets
• Security: HMAC-SHA256 Telemetry Authentication
```

### 3.3 Speaker Verbal Script (60 Seconds)
> *"On the technical side, the biggest failure in DIY autonomous drones is computational lag: if an AI model freezes the flight controller for even 50 milliseconds, the drone crashes.  
>  
> To solve this, we implement a **Dual-Brain Architecture on a single Arduino UNO Q board**:  
> The **STM32U5 core** runs Zephyr RTOS, executing a deterministic 250 Hz flight loop with patched 350 Hz PWM motor control. It does not touch the AI.  
> Meanwhile, the **Qualcomm Dragonwing QRB2210 core** runs Linux, executing our quantized INT8 YOLO model on the NPU and calculating target geolocation via ray-casting.  
> An asynchronous RPC bridge connects both brains without jitter. When a victim is located, their position is compressed into a 17-byte binary packet and transmitted via an SX1262 LoRa transceiver to our offline React/Leaflet dashboard."*

---

## SECTION 4: SLIDE 4 — FEASIBILITY, CHALLENGES & VIABILITY

### 4.1 Visual Layout & Framing
* **Top Header:** Feasibility, Challenges-to-Strategies & Market Viability
* **3-Column Layout:**
  * **Column 1 (Blue):** Technical, Operational & Financial Feasibility
  * **Column 2 (Purple):** Challenges $\longrightarrow$ Strategies (5 Critical Disaster Edge Cases)
  * **Column 3 (Green):** Economic Viability, Data Sovereignty & Swarm Scalability

### 4.2 Exact On-Slide Content
```text
[Badge: FEASIBILITY (Column 1)]
• Technical Feasibility:
  - Sized via Bouabdallah (2007) sizing laws: 38% battery mass fraction, β ≥ 2.0 thrust-to-weight ratio.
  - All-Up-Weight: 1.58 kg (Comfortably beneath the DGCA 2.0 kg Micro-Drone threshold; no complex licensing).
  - Sub-5W Compute: Qualcomm NPU preserves 90% of total electrical power for rotor flight endurance.
• Operational Feasibility:
  - Rapid Deployment: Under 3 minutes from rugged backpack unboxing to active airborne sweep.
  - Quick-Swap Battery: Dual 4S LiPo sliding tray allows continuous sortie rotations.
• Financial Feasibility:
  - Bill of Materials: ₹85,000 to ₹1,40,000 per operational unit.

[Badge: CHALLENGES ➔ STRATEGIES (Column 2)]
1. Complete Comms Blackout in Deep Canyons:
   ➔ Strategy: Raw LoRa P2P 868MHz binary packet burst; zero dependence on cellular or cloud infrastructure.
2. Mud Slush, Foliage & Night Darkness:
   ➔ Strategy: Dual-band 8-14μm LWIR Thermal fusion spots living body heat (37°C) even when buried under light debris.
3. Compass Distortion in Reinforced Steel Rubble:
   ➔ Strategy: Visual Inertial Odometry (VIO) overrides magnetometer heading to eliminate compass spinning.
4. Sensor Noise from High-RPM Motor Vibration:
   ➔ Strategy: Reflexed zero-pitching-moment airfoils (NASA TM-4741) + silicone IMU dampening + Butterworth filtering.
5. Motor Saturation during Violent Wind Gusts:
   ➔ Strategy: Anti-windup integrator clamping prevents post-maneuver controller overshoot (Bouabdallah Algorithm 2).

[Badge: VIABILITY (Column 3)]
• Economic Disruption:
  - Commercial enterprise drones (e.g. DJI Matrice 30T) cost ₹12,00,000 to ₹14,00,000.
  - Project Phoenix delivers autonomous multi-spectral reconnaissance at 1/8th of the cost (₹1.2 Lakh).
• National Data Sovereignty:
  - 100% Air-Gapped system: Zero telemetry transmitted to foreign servers; compliant with Indian MHA cyber security standards.
• Swarm Multiplier:
  - A single regional SDRF battalion can deploy a coordinated swarm of 5 Phoenix UAVs for the price of 1 proprietary enterprise drone.
```

### 4.3 Speaker Verbal Script (60 Seconds)
> *"Judges often ask: Is this feasible on a student budget, and can it survive in the field?  
>  
> Mathematically, our drone adheres strictly to Bouabdallah’s sizing laws: with a 38% battery fraction, our All-Up-Weight is just 1.58 kg—keeping it legally inside India’s DGCA Micro-drone category.  
>  
> Operationally, we solved the five major failure points of disaster drones:  
> When cell towers collapse, we use Raw LoRa.  
> When fog or mud obscures survivors, our thermal sensor detects body heat.  
> When steel rubble distorts electronic compasses, our Visual Odometry maintains stable heading.  
>  
> Economically, enterprise drones like the DJI Matrice 30T cost ₹12 to ₹14 Lakhs and upload telemetry to foreign servers. Project Phoenix costs ₹1.2 Lakh, keeps all defense data 100% local, and allows disaster battalions to deploy entire drone swarms cost-effectively."*

---

## SECTION 5: SLIDE 5 — IMPACT & MULTI-STAKEHOLDER BENEFITS

### 5.1 Visual Layout & Framing
* **Top Header:** Mission Impact & Multi-Stakeholder Benefits
* **4 Vertical Stakeholder Cards Across Top:**
  1. Trapped Victims (Green)
  2. NDRF / SDRF Teams (Blue)
  3. Disaster Management Authorities (Purple)
  4. District Governance (Amber)
* **Bottom Bar:** The Impact Pipeline (Horizontal Flow Chevron)

### 5.2 Exact On-Slide Content
```text
[Card 1: TRAPPED VICTIMS (Green Badge)]
• Discovered within the critical "Golden 72 Hours" before mortality spikes.
• Located even when trapped in mud slush, night darkness, or light sheet debris.
• Urgent medical conditions flagged via onboard thermal temperature profiling.
• Dramatically increases overall probability of survival.

[Card 2: NDRF / SDRF RESCUE TEAMS (Blue Badge)]
• Receive advance aerial reconnaissance before entering unstable zones.
• Avoid live downed powerlines, active gas leaks, and secondary mudslide paths.
• Automated safe-route navigation guidance directly to victim locations.
• Eliminates exhausting, redundant manual search foot patrols.

[Card 3: STATE DISASTER AUTHORITIES (SDMA) (Purple Badge)]
• Unified local tactical map showing verified survivor pins and danger zones.
• Zero dependency on commercial telecommunication networks.
• Coordinated sector-by-sector coverage logging with real-time audit trails.
• Multi-UAV swarm synchronization for wide-area disaster mapping.

[Card 4: DISTRICT GOVERNANCE & POLICE (Amber Badge)]
• Objective, real-time data for prioritizing helicopter airlifts and medical supply drops.
• 1/8th the procurement cost allows wide distribution across every regional taluk/district.
• 100% compliant with national data privacy and emergency response directives.

[Bottom Impact Bar: Horizontal Process Flow]
RAPID UNBOXING (< 3 min) ➔ AUTONOMOUS THERMAL SWEEP ➔ EXACT GPS RAY-CASTING ➔ ZERO-DROP LORA BEACON ➔ MAXIMIZED LIVES SAVED
```

### 5.3 Speaker Verbal Script (45 Seconds)
> *"The impact of Project Phoenix spans the entire disaster response chain:  
> For trapped victims, discovery time is slashed from hours to minutes, ensuring extraction within the Golden 72 Hours.  
> For NDRF rescue workers, our hazard heatmaps prevent secondary casualties from gas leaks or collapsing slopes.  
> For district administrators, our offline tactical dashboard provides verified, georeferenced ground intelligence to deploy medical helicopters where they are needed most.  
> Ultimately, by replacing slow manual searches with autonomous aerial intelligence, we maximize the number of lives saved."*

---

## SECTION 6: SLIDE 6 — RESEARCH FOUNDATIONS & PROTOTYPE VERIFICATION

### 6.1 Visual Layout & Framing
* **Top Header:** Academic Research Foundations & Prototype Verification
* **Left Card:** Research Foundations & Prior Art (Formal Academic Citations)
* **Right Card:** Working Prototype Deliverables & Open-Source GitHub Repository
* **Footer:** Scannable QR Code and direct links

### 6.2 Exact On-Slide Content
```text
[Badge: RESEARCH & REFERENCES (Left Column)]
1. Dr. Samir Bouabdallah (EPFL Doctoral Thesis No. 3727, 2007):
   • "Design and Control of Quadrotors with Application to Autonomous Flying"
   • Grounded our 12-state rigid body equations of motion, cascaded dual-loop spectral separation, 
     and the 90/10 motor-to-compute electrical power sizing law.
2. Souli, Karatzia, Georgiades, Kolios, & Ellinas (Elsevier, Computer Communications, 2024):
   • "Mission-critical UAV swarm coordination using an integrated ROS-LoRa architecture" (Vol. 225)
   • Provided our 17-byte binary bit-packing telemetry compression and peer-to-peer LoRa bridge.
3. NASA Technical Memorandum 4741 (NASA Langley Research Center, 1996):
   • "Computer Program To Obtain Ordinates for NACA Airfoils"
   • Grounded selection of zero-pitching-moment (Cm=0) reflexed airfoils to eliminate blade flutter.
4. JRFCQAI Platform (Ravi Butani, 2024):
   • "Dual-Brain Physical AI Flight Controller on Arduino UNO Q"
   • Validated Zephyr RTOS (STM32U5) + Debian Linux (Qualcomm QRB2210) on Arduino UNO Q for UAV flight.

[Badge: PROTOTYPE PROOF (Right Column)]
• Official GitHub Repository:
  https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV
• Documented Subsystem Deliverables:
  1. docs/bouabdallah_quadrotor_research_findings.md (Flight dynamics & sizing derivations)
  2. docs/ros_lora_mission_critical_uav_swarm_research.md (Elsevier 2024 comms architecture)
  3. docs/aerodynamic_airfoil_considerations.md (NASA rotorcraft flutter prevention)
  4. presentation/Team_Phoenix_SIH26177_Deck_v2.pptx (Editable master presentation deck)
• Working Prototype Deliverables:
  - React/Leaflet Offline Tactical Ground Station (Live map & survivor triage queue)
  - 17-Byte Binary Bit-Packing Serialization Module (Python / C++)
  - Tait-Bryan Camera-to-Ground Ray-Casting Geolocation Engine
  - Multi-Spectral Dual Stream (RGB + Thermal HUD simulator)
```

### 6.3 Speaker Verbal Script (45 Seconds)
> *"To conclude, Project Phoenix is grounded in validated science and open-source verification.  
> Our dynamics follow Bouabdallah’s EPFL thesis; our propeller stability follows NASA aerodynamic guidelines; our long-range disaster comms implement the 2024 Elsevier ROS-LoRa architecture; and our compute platform builds upon the open-source JRFCQAI dual-brain flight stack on Qualcomm silicon.  
>  
> All mathematical derivations, sizing calculations, and prototype code are completely open-source and documented on our GitHub repository.  
> Thank you, and we look forward to your questions."*

---

### 6.4 Key Technical Viva Q&A Cheat-Sheet

| Likely Judge Question | Winning Technical Response |
| :--- | :--- |
| **"Why not just stream video over 4G/5G or Wi-Fi?"** | *"In real disasters like Wayanad or earthquake zones, 4G/5G towers are destroyed. Wi-Fi has a practical range of under 80 meters behind trees and rubble. That is why we implement the 2024 Souli et al. architecture: raw P2P LoRa compresses critical GPS coordinates into 17-byte binary packets, transmitting reliably across 3 to 5 km with zero infrastructure."* |
| **"How can an Arduino UNO Q run YOLO?"** | *"The UNO Q is not an 8-bit board. It has a Qualcomm Dragonwing QRB2210 processor with a quad-core 64-bit Arm CPU and dedicated NPU running Debian Linux. By quantizing YOLOv8-nano to INT8 precision, it runs at 10–15 FPS on under 5 Watts—leaving the STM32U5 core completely dedicated to the 250 Hz flight loop."* |
| **"What happens if the electronic compass spins in collapsed buildings?"** | *"As Dr. Bouabdallah documented in his EPFL thesis, motor currents and ferromagnetic steel rubble distort magnetometers by up to 14° in 5 seconds. Our firmware disables compass-based heading in high magnetic anomaly zones and switches to Visual-Inertial Odometry (VIO) / Optical Flow to maintain heading stability."* |
| **"What is the total flight time and weight?"** | *"Applying Bouabdallah's optimal 38% battery mass fraction, our All-Up-Weight is exactly 1.58 kg carrying a 4S 5200mAh LiPo. This achieves a 28-to-32-minute operational search sortie with a 2:1 thrust-to-weight ratio, staying safely under the DGCA 2.0 kg Micro-drone legal limit."* |
