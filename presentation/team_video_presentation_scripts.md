# Project Phoenix X — 6-Speaker Video Presentation Master Script
**Problem Statement ID:** SIH26177 | **Sponsoring Organization:** Qualcomm Inc.  
**Team Name:** Team Phoenix | **Category:** Hardware | **Theme:** Robotics & Drones  
**Associated Presentation Deck:** [`Team_Phoenix_SIH26177_Deck_v2.pptx`](Team_Phoenix_SIH26177_Deck_v2.pptx)  
**Slide-by-Slide Content Spec:** [`slide_by_slide_presentation_content_doc.md`](slide_by_slide_presentation_content_doc.md)

---

## 1. Alignment Matrix: Video Script vs. Official SIH Presentation Deck

Each team member's script maps directly to specific slides in [`Team_Phoenix_SIH26177_Deck_v2.pptx`](Team_Phoenix_SIH26177_Deck_v2.pptx):

| Speaker | Specialization Role | PPT Slide Mapping | Key Technical Focus & Expanded Acronyms |
| :--- | :--- | :--- | :--- |
| **Speaker 1** | **Mission Architect & Systems Engineering Lead** | **Slide 1 & Slide 2:** Title, Problem Statement, The Golden 72 Hours | Smart India Hackathon (SIH), Unmanned Aerial Vehicle (UAV), Qualcomm Inc., zero-infrastructure reconnaissance. |
| **Speaker 2** | **Computer Vision & Edge AI Lead** | **Slide 2 & Slide 3:** Multi-Spectral Fusion & Radiometric Perception | Electro-Optical (EO), Long-Wave Infrared (LWIR), Noise Equivalent Temperature Difference (NETD), 37°C biological verification. |
| **Speaker 3** | **Navigation, Avionics & Geolocation Lead** | **Slide 2 & Slide 3:** Oblique Ray-Casting & Photogrammetric Geodetics | Real-Time Kinematic Global Positioning System (RTK-GPS), Inertial Measurement Unit (IMU), Tait-Bryan 6-DOF, Digital Elevation Model (DEM), World Geodetic System 1984 (WGS-84). |
| **Speaker 4** | **Embedded Systems & Flight Dynamics Lead** | **Slide 3 & Slide 4:** Dual-Brain Compute Partitioning & Flight Control | Microprocessor Unit (MPU), Microcontroller Unit (MCU), Real-Time Operating System (RTOS), Remote Procedure Call (RPC), Neural Processing Unit (NPU). |
| **Speaker 5** | **RF Communications & Cyber Security Lead** | **Slide 3, 4 & 6:** Off-Grid Telemetry, Bit-Packing & Cryptography | Long Range radio (LoRa), Peer-to-Peer (P2P), Hash-based Message Authentication Code (HMAC-SHA256), Souli et al. (Elsevier 2024). |
| **Speaker 6** | **Incident Command, GIS & Operations Lead** | **Slide 5 & Slide 6:** Ground Station Triage, Safe Routing & Impact | Ground Control Station (GCS), Geographic Information System (GIS), Dijkstra algorithm, National Disaster Response Force (NDRF). |

---

## 2. Audio & Video Recording Instructions for the 6 Speakers

1. **How the Extended Overlap System Works:**
   - Every transition between speakers features **two full shared sentences** (~35 to 45 words).
   - **Speaker A reads the shared lines at the end of their recording.**
   - **Speaker B reads the exact same shared lines at the beginning of their recording.**
   - *Why this is critical:* The video editor has complete editorial freedom to make J-cuts, L-cuts, or choose the cleanest vocal delivery without abrupt audio jumps.
2. **Read Continuously:**
   - Read the entire script block in one uninterrupted take.
   - Do **not** pause or stop when you reach the shared bridge sentences—deliver them with natural energy as part of your paragraph.
3. **Pacing and Tempo:**
   - Maintain a deliberate, authoritative pace of **125 to 135 words per minute**.
   - Speak technical acronyms and full forms crisply.
4. **Microphone Setup:**
   - Position your microphone or smartphone **6 to 8 inches** from your mouth, angled at **45 degrees** to avoid plosive breath pops on letters P, T, and B.
5. **Full-Form Spoken Reference Guide:**
   - **UAV:** *"Unmanned Aerial Vehicle, or UAV"*
   - **LWIR:** *"Long-Wave Infrared, or LWIR"*
   - **NETD:** *"Noise Equivalent Temperature Difference, or NETD"*
   - **RTK-GPS:** *"Real-Time Kinematic Global Positioning System"*
   - **IMU:** *"Inertial Measurement Unit"*
   - **Tait-Bryan:** *"Tate-Bryan intrinsic rotation"*
   - **WGS-84:** *"World Geodetic System 1984"*
   - **QRB2210:** *"Qualcomm Dragonwing Q-R-B twenty-two ten"*
   - **STM32U585:** *"S-T-M thirty-two U five-eighty-five"*
   - **RTOS:** *"Real-Time Operating System"*
   - **RPC:** *"Remote Procedure Call"*
   - **LoRa:** *"Low-Rah point-to-point radio"*
   - **HMAC-SHA256:** *"Hash-based Message Authentication Code using SHA-256"*
   - **GCS:** *"Ground Control Station"*
   - **GIS:** *"Geographic Information System"*
   - **NDRF:** *"National Disaster Response Force"*

---

## 3. The 6 Master Script Blocks (Copy & Paste Ready)

---

### 👤 SPEAKER 1: Mission Architect & Systems Engineering Lead
* **Visual Track:** On-camera intro, transition to UAV 3D structural model, then disaster zone footage.  
* **Estimated Spoken Runtime:** ~45 seconds (~130 words)  

```text
In the critical golden seventy-two hours following an earthquake, landslide, or flash flood, the single greatest operational barrier is the catastrophic breakdown of situational awareness. Commercial cellular towers collapse, access roads are severed by debris, and first responders are forced to conduct slow, blind foot searches across square kilometers of treacherous rubble. That is the urgent challenge we solved with Project Phoenix X for Qualcomm Incorporated in Smart India Hackathon problem statement SIH26177. Rather than depending on vulnerable cloud networks, we engineered an autonomous Unmanned Aerial Vehicle, or UAV, purpose-built to deploy in under three minutes into zero-connectivity disaster zones, detect human survivors through smoke and rubble, and broadcast verified coordinates back to command teams. Finding human beings trapped under collapsed debris begins with solving the perception barrier in zero-visibility environments. When conventional optical sensors fail, multi-spectral intelligence is our first line of detection.
```

---

### 👤 SPEAKER 2: Computer Vision & Edge AI Lead
* **Visual Track:** Screen capture of Dual-Spectral EO/LWIR live feed, Ironbow thermal palette, 37.0°C bounding box lock.  
* **Estimated Spoken Runtime:** ~48 seconds (~145 words)  

```text
Finding human beings trapped under collapsed debris begins with solving the perception barrier in zero-visibility environments. When conventional optical sensors fail, multi-spectral intelligence is our first line of detection. Standard Red-Green-Blue visual cameras are completely blinded by nightfall, thick dust, and smoke plumes. To break this barrier, Phoenix X integrates a dual-spectral payload combining high-resolution Electro-Optical imaging with an uncooled Long-Wave Infrared, or LWIR, thermal sensor operating across the eight to fourteen micrometer spectrum with a Noise Equivalent Temperature Difference under fifty millikelvins. Our edge-AI detection model does not rely on simple color thresholds; it cross-references visual contour geometry against radiometric human biological core emissivity between thirty-six point five and thirty-seven point five degrees Celsius, eliminating false positives caused by solar-heated tin roofs or rocks. An image on a screen is completely useless to ground rescue teams unless we convert that two-dimensional camera pixel into an exact geographic coordinate on the earth's surface. Without millimeter-precise mathematical projection, responders are left searching blind in three dimensions.
```

---

### 👤 SPEAKER 3: Navigation, Avionics & Geolocation Lead
* **Visual Track:** Primary Flight Display HUD, pitch/roll attitude ladder, DEM terrain intersection, ±2.1m SEP target crosshair.  
* **Estimated Spoken Runtime:** ~48 seconds (~145 words)  

```text
An image on a screen is completely useless to ground rescue teams unless we convert that two-dimensional camera pixel into an exact geographic coordinate on the earth's surface. Without millimeter-precise mathematical projection, responders are left searching blind in three dimensions. Hovering directly overhead destabilizes unstable debris with dangerous rotor downwash. Phoenix X avoids this by operating in an oblique standoff trajectory. Our avionics pipeline ingests real-time telemetry from an onboard Real-Time Kinematic Global Positioning System, barometric altimeter, and three-axis Inertial Measurement Unit. Applying an intrinsic camera calibration matrix alongside a six-degree-of-freedom Tait-Bryan intrinsic Euler rotation matrix, the drone casts an optical ray from the camera center straight down to intersect a local Digital Elevation Model. In under sixty milliseconds, target pixels are resolved into World Geodetic System 1984 coordinates with a Spherical Error Probable under two point one meters. Projecting millimeter-accurate coordinates while executing high-speed neural networks alongside sub-millisecond flight dynamics demands an uncompromising embedded hardware architecture. Traditional single-board flight controllers crash under heavy computational load, making a dedicated dual-brain partition an absolute operational necessity.
```

---

### 👤 SPEAKER 4: Embedded Systems & Flight Dynamics Lead
* **Visual Track:** Arduino UNO Q PCB schematic, Qualcomm QRB2210 MPU vs. STM32U585 MCU block diagram, 5W thermal badge.  
* **Estimated Spoken Runtime:** ~45 seconds (~135 words)  

```text
Projecting millimeter-accurate coordinates while executing high-speed neural networks alongside sub-millisecond flight dynamics demands an uncompromising embedded hardware architecture. Traditional single-board flight controllers crash under heavy computational load, making a dedicated dual-brain partition an absolute operational necessity. Phoenix X implements a dual-brain compute partition on the compact Arduino UNO Q. Mission compute runs on the Qualcomm Dragonwing QRB2210 quad-core Microprocessor Unit running Debian Linux, executing quantized INT8 neural inference on its dedicated Neural Processing Unit under a strict five-watt power envelope. Simultaneously, mission-critical flight stabilization and motor mixing are isolated on an STMicroelectronics STM32U585 Microcontroller Unit executing the Zephyr Real-Time Operating System at a deterministic two hundred and fifty hertz. Both brains communicate over an asynchronous, non-blocking Remote Procedure Call bridge, ensuring that peak AI computational load never causes flight controller jitter. All of this onboard compute and flight stability means nothing if critical target coordinates cannot escape the disaster zone communication blackout. When commercial telecommunication towers collapse and local Wi-Fi networks go dark, standard high-bandwidth video downlinks fail completely.
```

---

### 👤 SPEAKER 5: RF Communications & Cyber Security Lead
* **Visual Track:** Semtech SX1262 LoRa module close-up, RF waterfall spectrogram, 17-byte binary bit-packing visualization.  
* **Estimated Spoken Runtime:** ~48 seconds (~145 words)  

```text
All of this onboard compute and flight stability means nothing if critical target coordinates cannot escape the disaster zone communication blackout. When commercial telecommunication towers collapse and local Wi-Fi networks go dark, standard high-bandwidth video downlinks fail completely. Grounded in the twenty-twenty-four Elsevier disaster networking research by Souli and colleagues, Phoenix X abandons vulnerable video streaming in favor of an ultra-compact seventeen-byte binary bit-packed telemetry payload. In just seventeen bytes, we bit-pack latitude, longitude, elevation, thermal confidence, victim triage severity, and timestamp. To guarantee operational integrity in hostile disaster zones, every packet is cryptographically authenticated using a Hash-based Message Authentication Code with SHA-256 to prevent spoofing. Transmitted via a Semtech SX1262 Long Range, or LoRa, point-to-point radio link on eighty-six-eight megahertz, the sub-gigahertz signal penetrates collapsed reinforced concrete and dense foliage over a five-kilometer radius. With extreme sub-gigahertz penetration, our encrypted telemetry signal punches through reinforced concrete rubble and dense forest foliage over a five-kilometer radius, instantly hitting our portable ground command terminal. Once received at the incident command post, raw telemetry is instantly converted into actionable ground triage.
```

---

### 👤 SPEAKER 6: Incident Command, GIS & Operations Lead
* **Visual Track:** Web Demo Ground Control Station map, dynamic Dijkstra safe path bypassing severed 11kV lines, team summary card.  
* **Estimated Spoken Runtime:** ~45 seconds (~135 words)  

```text
With extreme sub-gigahertz penetration, our encrypted telemetry signal punches through reinforced concrete rubble and dense forest foliage over a five-kilometer radius, instantly hitting our portable ground command terminal. Once received at the incident command post, raw telemetry is instantly converted into actionable ground triage. On our offline tactical Ground Control Station, incoming packets populate a live Geographic Information System map. Rather than allowing rescue teams to enter hazardous zones blind, our system executes a hazard-weighted Dijkstra pathfinding algorithm—automatically computing the safest pedestrian extraction corridor around severed eleven-kilovolt power lines, active fire zones, and unstable mudslides. What once required hours of agonizing, hazardous foot searches is compressed into under five minutes from drone launch to casualty extraction. Project Phoenix X delivers an end-to-end, resilient lifesaver engineered for India's most demanding disaster environments. Thank you.
```

---

## 4. Video Editor Master Assembly Timeline & Cut Sheet

| Scene & Timecode | Active Speaker | Visual B-Roll Track | Shared Audio Bridge (Cut Flexibility Window) | Audio & Visual Transition Style |
| :--- | :--- | :--- | :--- | :--- |
| **Scene 1**<br>`0:00 – 0:45` | **Speaker 1**<br>(Systems Lead) | • On-camera presenter<br>• Drone 3D render<br>• SIH26177 title overlay | *"Finding human beings trapped under collapsed debris begins with solving the perception barrier in zero-visibility environments. When conventional optical sensors fail, multi-spectral intelligence is our first line of detection."* | Fade in from black with subtle low-frequency audio bed. Transition using J-Cut into Speaker 2. |
| **Scene 2**<br>`0:42 – 1:28` | **Speaker 2**<br>(Vision Lead) | • Web Demo EO/LWIR toggle<br>• FLIR Ironbow palette<br>• 37°C bounding box lock | *"An image on a screen is completely useless to ground rescue teams unless we convert that two-dimensional camera pixel into an exact geographic coordinate on the earth's surface. Without millimeter-precise mathematical projection, responders are left searching blind in three dimensions."* | Speaker 2 voice enters underneath Speaker 1's final B-roll shot. Cut to Speaker 3 on "geographic coordinate". |
| **Scene 3**<br>`1:25 – 2:10` | **Speaker 3**<br>(Avionics Lead) | • Primary Flight Display HUD<br>• 6-DOF Tait-Bryan vector<br>• DEM surface ray-cast | *"Projecting millimeter-accurate coordinates while executing high-speed neural networks alongside sub-millisecond flight dynamics demands an uncompromising embedded hardware architecture. Traditional single-board flight controllers crash under heavy computational load, making a dedicated dual-brain partition an absolute operational necessity."* | L-Cut audio overlap. Visual cuts directly from ray-casting crosshair to the physical Arduino UNO Q board. |
| **Scene 4**<br>`2:07 – 2:50` | **Speaker 4**<br>(Embedded Lead) | • Arduino UNO Q PCB diagram<br>• QRB2210 MPU + STM32U5 split<br>• Zephyr RTOS 250 Hz badge | *"All of this onboard compute and flight stability means nothing if critical target coordinates cannot escape the disaster zone communication blackout. When commercial telecommunication towers collapse and local Wi-Fi networks go dark, standard high-bandwidth video downlinks fail completely."* | Direct cut on "blackout". Transition from hardware schematic to radio frequency antenna / LoRa hardware. |
| **Scene 5**<br>`2:47 – 3:32` | **Speaker 5**<br>(Comms Lead) | • SX1262 LoRa module<br>• RF spectrum waterfall<br>• 17-byte bit-pack diagram | *"With extreme sub-gigahertz penetration, our encrypted telemetry signal punches through reinforced concrete rubble and dense forest foliage over a five-kilometer radius, instantly hitting our portable ground command terminal. Once received at the incident command post, raw telemetry is instantly converted into actionable ground triage."* | J-Cut: Speaker 6's voice leads into the full-screen tactical map display while Speaker 5's packet animation resolves. |
| **Scene 6**<br>`3:29 – 4:15` | **Speaker 6**<br>(Command Lead) | • Offline Web GCS dashboard<br>• Dijkstra route recalculation<br>• 11kV wire hazard avoidance<br>• Closing team card & SIH logo | Final punchy delivery directly on camera, cross-cutting with the active rescue corridor visualization. | Outro music swell, fade to black on the official Smart India Hackathon and Qualcomm acknowledgment slide. |

**Total Video Duration:** **4 minutes 15 seconds** (comfortably underneath the strict 5-minute SIH submission cap, leaving generous headroom).
