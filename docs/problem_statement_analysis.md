# Problem Statement Analysis: SIH26177 (Qualcomm Inc.)

**Problem Title**: Autonomous AI-Powered Search and Rescue (SAR) UAV for Disaster Reconnaissance  
**Sponsoring Organization**: Qualcomm Inc.  
**Category**: Hardware | **Theme**: Robotics and Drones  
**Author**: Team Phoenix (Systems Engineering & Pitch Strategy)  

---

## 1. Official Problem Background & Description

### 1.1 Official Background
> *"India is highly vulnerable to natural disasters including floods, cyclones, earthquakes, landslides, and flash floods, which often result in damaged infrastructure, inaccessible terrain, and delayed rescue operations. During the first few critical hours after a disaster, responders need rapid situational awareness to locate survivors, assess hazards, and prioritize rescue efforts. Traditional ground-based assessments can be slow, dangerous, and resource-intensive, particularly in remote or heavily damaged areas. Autonomous drones equipped with on-device AI can provide real-time aerial intelligence while operating in environments with limited connectivity."*

### 1.2 Official Description
> *"Develop an autonomous drone system capable of navigating disaster-affected areas and performing real-time detection of survivors and hazards using on-device AI. The drone should use RGB and thermal cameras to identify stranded individuals, detect signs of human presence, and recognize environmental hazards such as fire, floodwaters, damaged structures, exposed electrical lines, debris, landslides, or chemical leaks. The solution must process data locally on the drone to ensure low latency and continued operation even when network connectivity is unavailable. The drone should autonomously map affected regions, generate situational reports, and transmit actionable insights to emergency response teams. This concept aligns with existing edge-AI drone approaches for incident response and disaster assessment."*

---

## 2. The 8 Expected Solution Pillars: Architectural Mapping

The official problem statement mandates 8 explicit technical capabilities. Below is Team Phoenix's direct systems engineering response for each pillar:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        PROJECT PHOENIX: 8-PILLAR SOLUTION MAPPING                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Autonomous Navigation       │ GPS + VIO SLAM + Forward/Downward ToF Obstacle Avoid  │
│ 2. On-Device AI Inference      │ Qualcomm Flight™ RB5 (Hexagon 698 NPU, INT8 SNPE)     │
│ 3. Multi-Sensor Fusion         │ Hardware-Synced 4K RGB + Radiometric LWIR + IMU/LiDAR │
│ 4. Hazard Classification       │ Multi-Head Neural Segmentation (Fires, Floods, Lines) │
│ 5. Geo-Tagged Mapping          │ 3D Ray-Casting Projection + Safe Responder Corridors  │
│ 6. Emergency Alerting          │ Dynamic Triage Engine + 64-Byte LoRa Mesh Alerts      │
│ 7. Offline Resilience          │ Non-Volatile Flash Store-and-Forward + Dual-Tier Comms│
│ 8. Command Center Dashboard    │ Tactical GIS Web Dashboard (Offline QGIS / Mapbox)    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Pillar 1: Autonomous Navigation (GPS-Enabled & GPS-Denied SLAM)
* **GPS-Enabled Mode**: Standard waypoint navigation and boustrophedon search sweeps via PX4 Autopilot over multi-constellation GNSS (NavIC, GPS, GLONASS).
* **GPS-Denied Mode (Urban Canyons / Collapsed Bridges)**: When GNSS drops (multipath or jamming), the platform automatically engages **Visual-Inertial Odometry (VIO)** and optical flow processed through the **Qualcomm Spectra™ 480 ISP** paired with a downward ToF LiDAR.
* **Obstacle Avoidance**: 3D spatial voxel grid generated in real time from forward and downward stereo vision / solid-state LiDAR, autonomously dodging dangling high-voltage electrical wires, collapsed rebar, and tree canopies.

### Pillar 2: On-Device AI Inference (Zero-Cloud Autonomy)
* **Compute Heart**: **Qualcomm Flight™ RB5 (Snapdragon® QRB5165 SoC)**.
* **Inference Engine**: **Qualcomm Snapdragon Neural Processing Engine (SNPE) SDK** running quantized INT8 neural backbones.
* **Throughput & Power**: Sustained **35 FPS** across dual video streams at just **8.4W active NPU power**, operating within an ultra-tight total compute budget of $<12\text{W}$ (saving 20W+ compared to NVIDIA Jetson or desktop-class GPU boards).

### Pillar 3: Multi-Sensor Fusion (RGB + Radiometric LWIR + IMU + GPS)
* **Hardware Ingestion**: Pixel-synchronized dual-stream ingest (Sony IMX586 4K RGB + InfiRay/FLIR $640 \times 512$ Radiometric LWIR).
* **Spatial Alignment**: Homographic projective warping aligning wide-angle RGB FOV with thermal FOV.
* **False-Alarm Mitigation**: Fused confidence metric cross-referencing apparent temperature ($32^\circ\text{C} - 38.5^\circ\text{C}$) against optical human limb/contour signatures, preventing false alarms from solar-baked asphalt or hot metal debris.

### Pillar 4: Hazard Classification (Dual-Task Perception Pipeline)
The edge neural network features a **Dual-Head Architecture**:
* **Head A (Survivor & Victim Detection)**: Detects standing, prone, gesturing, or partially rubble-trapped individuals.
* **Head B (Disaster Hazard Semantic Segmentation)**:
  * **Class 1 (Hydrological)**: Rising floodwaters, breached embankments.
  * **Class 2 (Thermal / Fire)**: Active flames, structural hot-spots, smoke plumes.
  * **Class 3 (Structural & Debris)**: Collapsed structures, impassable rubble piles, landslide scarps.
  * **Class 4 (Infrastructure Threats)**: Snapped/exposed high-voltage electrical lines, hazardous industrial/chemical leak plumes.

### Pillar 5: Geo-Tagged Mapping & Safe Access Routes
* **Exact Ground Geolocation**: Trigonometric 3D ray-casting projects image detection centroids through the UAV's 6-DoF state estimate (roll, pitch, yaw, altitude AGL, gimbal pan/tilt) directly to WGS-84 coordinates ($\pm 2.5\text{m}$).
* **Dynamic Safe Corridor Generation**: Using an $A^*$ / Dijkstra graph-search algorithm on the local occupancy grid, the system identifies ground obstacles and hazard zones (fires, live wires, deep floodwaters) and computes **Safe Ingress & Egress Corridors** for NDRF rescue teams.

### Pillar 6: Emergency Alerting & Prioritized Rescue Recommendations
* **Dynamic Triage Scoring Formula**:
  $$\text{Triage Priority} = w_1 \cdot \text{Vitality}(\Delta T) + w_2 \cdot \text{Movement} + w_3 \cdot \text{Hazard Proximity}$$
  * **Critical (Code Red)**: Living human detected adjacent to rising floodwaters or active fire.
  * **Urgent (Code Yellow)**: Trapped survivor detected under stable void without immediate external threats.
  * **Non-Urgent (Code Green)**: Ambulatory individuals in safe clear zones.
* **Alert Transmission**: Generates compact 64-byte structured triage packets broadcast immediately across the tactical mesh.

### Pillar 7: Offline Resilience & Communication Hierarchy
* **Tier 1 (High Bandwidth / Local)**: Wi-Fi 6 / 5G sub-6 for real-time video streaming to mobile incident command trucks within line-of-sight.
* **Tier 2 (Long-Range Resilient Fallback)**: SX1262 LoRa (868 MHz) mesh network transmitting encrypted micro-telemetry up to 10–15 km with zero dependence on commercial cellular towers.
* **Store-and-Forward**: If complete RF silence occurs, all geotagged detections, metadata, and high-res thumbnails are cryptographically signed (Ed25519) and logged in onboard NVMe flash, bursting to ground control immediately upon link reconnection.

### Pillar 8: Tactical Command Center Dashboard
* **Offline-First Architecture**: Runs on ruggedized laptops or tablets with cached vector maps (OpenStreetMap / QGIS).
* **Live GIS Visualizations**:
  * Real-time UAV flight trajectory, battery reserve, and sensor FOV footprint.
  * Color-coded casualty pins with photo thumbnails, estimated depth, and medical triage priority.
  * Hazard overlay polygons (fire zones in red, floodwater in blue, downed wires in yellow).
  * Auto-generated Safe Access Path overlaid directly for boots-on-the-ground rescue teams.

---

## 3. Indian Regulatory & Operational Alignment
* **National Disaster Management Authority (NDMA)**: Directly matches the Incident Response System (IRS) protocols for rapid damage assessment and search teams.
* **DGCA Drone Rules 2021 / 2023 Amendments**: 
  * Full NPNT (No Permission, No Takeoff) digital sky architecture.
  * Fail-safe autonomous Return-To-Home (RTH) upon battery reaching critical 20% reserve.
  * RF link loss contingency routines compliant with Indian civil airspace guidelines.
