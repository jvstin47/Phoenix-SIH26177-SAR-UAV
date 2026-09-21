# Project Phoenix X — 6-Speaker Video Presentation Master Script
**Problem Statement ID:** SIH26177 | **Sponsoring Organization:** Qualcomm Inc.  
**Team Name:** Team Phoenix | **Category:** Hardware | **Theme:** Robotics & Drones  
**Associated Presentation Deck:** [`Team_Phoenix_SIH26177_Deck_v2.pptx`](Team_Phoenix_SIH26177_Deck_v2.pptx)  
**Slide-by-Slide Content Spec:** [`slide_by_slide_presentation_content_doc.md`](slide_by_slide_presentation_content_doc.md)

---

## 1. Alignment Matrix: Video Script vs. Official SIH PPT

Each speaker's script is mapped 1:1 with the verified presentation deck (`Team_Phoenix_SIH26177_Deck_v2.pptx`):

| Speaker | Role | Corresponding PPT Slide & Focus | Core Engineering Specs Mentioned |
| :--- | :--- | :--- | :--- |
| **Speaker 1** | **Mission Architect & Systems Lead** | **Slide 1 & Slide 2:** Title, Problem Statement & The Golden 72h | SIH26177, Qualcomm Inc., Zero-connectivity disaster reconnaissance, Golden 72h window. |
| **Speaker 2** | **Computer Vision & Edge AI Lead** | **Slide 2 & Slide 3:** Multi-Spectral Sensor Fusion & Perception | Dual-spectral EO + Radiometric LWIR 8–14μm, NETD <50mK, 37.0°C biological emissivity lock. |
| **Speaker 3** | **Navigation, Avionics & Geolocation Lead** | **Slide 2 & Slide 3:** Oblique Ray-Casting & Coordinate Projection | Oblique standoff angle, 6-DOF Tait-Bryan intrinsic rotation matrix, DEM projection, WGS-84 ±2.1m SEP. |
| **Speaker 4** | **Embedded Systems & Flight Dynamics Lead** | **Slide 3 & Slide 4:** Dual-Brain Compute Partition & Sizing Laws | Arduino UNO Q, Qualcomm QRB2210 Linux MPU (<5W) + STM32U585 Zephyr RTOS @ 250Hz, non-blocking RPC. |
| **Speaker 5** | **RF Communications & Cyber Security Lead** | **Slide 3, 4 & 6:** Off-Grid Comms & Telemetry Serialization | Elsevier 2024 Souli et al., 17-byte binary bit-packing, HMAC-SHA256 anti-spoof, Semtech SX1262 LoRa 868MHz. |
| **Speaker 6** | **Incident Command, GIS & Operations Lead** | **Slide 5 & Slide 6:** Tactical Triage, Safe Routing & Impact Closing | Offline React/Leaflet GCS, Dijkstra hazard-aware rescue routing (11kV lines, mudslides), sub-5 min triage. |

---

## 2. Recording Guidelines for the 6 Speakers

To ensure seamless editing and a broadcast-quality submission:
1. **Audio Recording:** 
   - Use a smartphone voice recorder or lapel mic held **6–8 inches** from your mouth.
   - Keep the mic at a **45-degree angle** to your mouth to eliminate plosive "pops" on words starting with P, T, and B.
   - Record in a quiet room with minimal echo (carpets, curtains, or sofas help absorb reverb).
2. **Tempo & Pacing:** 
   - Read at an authoritative, steady pace (~**130 words per minute**).
   - Do **not** rush technical terms or model numbers.
3. **Pronunciation Guide:**
   - **QRB2210:** *"Q-R-B twenty-two ten"*
   - **STM32U585:** *"S-T-M thirty-two U five-eighty-five"*
   - **Tait-Bryan:** *"Tate Bryan"*
   - **SX1262:** *"S-X twelve sixty-two"*
   - **WGS-84:** *"W-G-S eighty-four"*
   - **LoRa:** *"Low-Rah"*
   - **Zephyr RTOS:** *"Zeff-er R-TOSS"*
   - **Dijkstra:** *"Dike-stra"*
4. **The Overlap System (In-Handle & Out-Handle):**
   - Each script starts with an **[In-Handle]** that repeats the exact ending idea of the previous speaker, and ends with an **[Out-Handle]** that sets up the next speaker.
   - **Read the entire block continuously without stopping.**
   - The video editor will choose the cleanest take and cut between speakers smoothly (using audio crossfades / J-cuts / L-cuts).

---

## 3. Individual Copyable Scripts for Team Distribution

---

### 👤 SPEAKER 1: Mission Architect & Systems Lead
* **Visual Cue:** On-camera medium close-up, cutting to drone 3D model and disaster footage.
* **Duration:** ~40 seconds (~110 words)

```text
In the golden seventy-two hours following an earthquake, landslide, or flash flood, the single biggest killer isn't just the disaster—it's the complete breakdown of situational awareness. Cellular towers collapse, roads are wiped out, and ground rescue teams are forced to search blind across square kilometers of treacherous debris. That is the challenge we solved with Project Phoenix X for Qualcomm Smart India Hackathon problem statement SIH26177. Instead of relying on vulnerable cloud infrastructure, we engineered an autonomous tactical UAV designed to deploy instantly into total blackouts, detect human life through smoke and rubble, and relay actionable casualty locations back to incident command without needing cell service or internet. But finding human beings trapped under debris begins with solving the perception barrier in zero-visibility environments.
```

---

### 👤 SPEAKER 2: Computer Vision & Edge AI Lead
* **Visual Cue:** Screen recording of Dual-Stream EO/IR toggle, Ironbow colormap, and 37°C bounding box lock.
* **Duration:** ~45 seconds (~130 words)

```text
Finding human beings trapped under debris begins with solving the perception barrier in zero-visibility environments. Standard RGB cameras are completely blinded by nightfall, dust, and heavy smoke plumes. To overcome this, Phoenix X utilizes a dual-spectral optical and long-wave infrared payload operating across the eight to fourteen micrometer band with thermal sensitivity under fifty millikelvins. We don't just run raw object detection—we fuse visual edge features with radiometric temperature analysis. When solar reflection creates false positives on hot tin roofs or rocks, our edge-AI model cross-verifies against human biological emissivity around thirty-seven degrees Celsius. The moment a viable heat plume is isolated through a crevice, the model locks a high-confidence bounding box. But an image on a screen is useless to rescue teams unless we convert that 2D camera pixel into an exact GPS coordinate on the earth's surface.
```

---

### 👤 SPEAKER 3: Navigation, Avionics & Geolocation Lead
* **Visual Cue:** Primary Flight Display (PFD) HUD with attitude ladder, DEM elevation grid, and ±2.1m SEP target crosshair.
* **Duration:** ~45 seconds (~130 words)

```text
An image on a screen is useless to rescue teams unless we convert that 2D camera pixel into an exact GPS coordinate on the earth's surface. Hovering directly above a disaster site puts the drone at risk and destabilizes debris piles. Instead, Phoenix X operates in an oblique standoff mode. Our avionics software ingests real-time telemetry from the onboard dual-antenna RTK-GPS, barometric altimeter, and three-axis IMU. By applying a full six-degree-of-freedom Tait-Bryan intrinsic rotation matrix, the drone projects an optical line-of-sight vector from the camera's optical center straight down to a local Digital Elevation Model. Within sixty milliseconds, that pixel is translated into a WGS-84 coordinate with a spherical error probable under two point one meters. But executing heavy neural networks alongside millisecond-level flight dynamics requires an uncompromising embedded architecture.
```

---

### 👤 SPEAKER 4: Embedded Systems & Flight Dynamics Lead
* **Visual Cue:** Close-up of Arduino UNO Q / flight controller PCB hardware diagram showing dual-brain split.
* **Duration:** ~40 seconds (~120 words)

```text
Executing heavy neural networks alongside millisecond-level flight dynamics requires an uncompromising embedded architecture. Running vision pipelines on a traditional flight controller causes latency spikes that can crash the drone. To guarantee deterministic stability, Phoenix X uses a dual-brain hardware partition. High-level compute is handled by a Qualcomm QRB2210 quad-core Linux MPU running lightweight neural inference within a strict five-watt thermal envelope. Simultaneously, mission-critical flight stabilization, motor mixing, and fail-safe return-to-home are isolated on a dedicated STM32U585 microcontroller running Zephyr RTOS at two hundred and fifty hertz. The two chips communicate over a non-blocking inter-process bridge. If Linux ever restarts or hits peak load, flight safety is never compromised. But all this onboard intelligence means nothing if the target coordinates cannot escape the communication blackout.
```

---

### 👤 SPEAKER 5: RF Communications & Cyber Security Lead
* **Visual Cue:** Semtech SX1262 LoRa module, spectrum waterfall, and 17-byte hex packet breakdown graphic.
* **Duration:** ~45 seconds (~135 words)

```text
All this onboard intelligence means nothing if the target coordinates cannot escape the communication blackout. When 4G towers and Wi-Fi networks go dark, standard video downlinks fail completely. Inspired by the twenty-twenty-four Souli et al. disaster networking framework, Phoenix X abandons heavy video streaming and condenses the entire detection payload into an ultra-compact seventeen-byte binary packet. In just seventeen bytes, we bit-pack latitude, longitude, elevation, thermal confidence, victim status, and timestamp. This packet is encrypted with HMAC-SHA256 to prevent spoofing and transmitted over an eighty-six-eight megahertz SX1262 LoRa point-to-point link. With extreme sub-gigahertz penetration, the signal punches through collapsed concrete and dense foliage over a five-kilometer radius, instantly hitting our portable ground command terminal.
```

---

### 👤 SPEAKER 6: Incident Command, GIS & Operations Lead
* **Visual Cue:** Ground Station Web UI live map, Dijkstra safe corridor avoiding hazard zones, and closing team slide.
* **Duration:** ~45 seconds (~130 words)

```text
With extreme sub-gigahertz penetration, the signal punches through collapsed concrete and dense foliage over a five-kilometer radius, instantly hitting our portable ground command terminal. On our lightweight web dashboard, the seventeen-byte packet immediately instantiates a live tactical pin. Rather than sending NDRF rescue teams blindly across dangerous terrain, our GIS engine runs a hazard-aware Dijkstra routing algorithm—automatically charting the safest walking path around severed eleven-kilovolt power lines, active fire zones, and secondary landslide hazards. What used to take hours of manual scouting is compressed into under five minutes from drone launch to boots on the ground. Project Phoenix X isn't just another drone prototype—it is an end-to-end, resilient lifesaver engineered for the harshest disaster zones in India. Thank you.
```

---

## 4. Video Editor Cut & B-Roll Master Sheet

| Sequence | Speaker | On-Screen Video Track (B-Roll) | Audio Crossfade In | Audio Crossfade Out |
| :--- | :--- | :--- | :--- | :--- |
| **01 (0:00–0:40)** | Speaker 1 | Medium close-up ➔ Drone 3D render ➔ Disaster zone title slide. | Fade from black / Title sting. | J-Cut: Speaker 2 audio starts over Speaker 1's final drone shot. |
| **02 (0:40–1:25)** | Speaker 2 | Speaker 2 webcam in corner ➔ Screen capture of Web Demo RGB vs. Thermal Ironbow toggle ➔ 37°C box lock. | L-Cut from Speaker 1. | J-Cut into Speaker 3's geolocation HUD. |
| **03 (1:25–2:10)** | Speaker 3 | Speaker 3 webcam ➔ Synthetic HUD overlay with pitch/roll ladder and ground ray intersection onto elevation map. | Cut on "ground coordinates". | J-Cut into hardware compute PCB. |
| **04 (2:10–2:50)** | Speaker 4 | Speaker 4 webcam ➔ Architectural diagram of Qualcomm QRB2210 + STM32U585 Zephyr bridge ➔ Sub-5W callout. | Smooth crossfade. | Cut on "communication blackout". |
| **05 (2:50–3:35)** | Speaker 5 | Speaker 5 webcam ➔ SX1262 LoRa module photo ➔ 17-byte bit-packing breakdown graphic. | Cut on "escape blackout". | J-Cut into GCS tactical dashboard. |
| **06 (3:35–4:20)** | Speaker 6 | Fullscreen Web Demo Ground Station ➔ Dijkstra route recalculation around 11kV wire ➔ Closing team card with SIH logo. | Cut on "ground terminal". | Fade to black / Outro music swell. |

Total Estimated Video Runtime: **4 minutes 15 seconds** to **4 minutes 30 seconds** (comfortably within the 5-minute SIH video presentation limit).
