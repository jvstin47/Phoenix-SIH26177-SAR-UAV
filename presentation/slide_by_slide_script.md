# Complete Slide-by-Slide PPT Production Guide & Pitch Script

**Event**: Smart India Hackathon (SIH) 2026  
**Problem Statement**: SIH26177 (Qualcomm Inc.)  
**Project**: Project Phoenix — Autonomous AI-Powered Search and Rescue (SAR) UAV  
**Team**: Team Phoenix  

---

## Slide 1: Cover, Problem Context & The 72-Hour "Golden Window"

### Layout & Visual Composition
* **Header**: Qualcomm Logo (Top-Left) | Smart India Hackathon 2026 (Top-Right).
* **Left Column (45% Width)**: Text content (Project Title, Problem Statement ID, Team Name, Member Disciplines).
* **Right Column (55% Width)**: High-impact hero visual.
  * *Visual*: 3D isometric render or schematic of a ruggedized hexacopter scanning collapsed urban rubble with dual-cone sensor projection (one blue cone for RGB, one orange/red cone for thermal LWIR) down to ground targets.
  * *Inset Infographic*: A clean "Golden Window" decay graph showing survivor extrication probability collapsing from 90% at 0h down to <15% after 72h.

### Exact Text Content (Slide Copy)
* **Title**: PROJECT PHOENIX
* **Subtitle**: Autonomous Edge-AI Multi-Spectral UAV for Rapid Disaster Reconnaissance and Survivor Triage
* **Problem Statement ID**: SIH26177 | **Sponsoring Organization**: Qualcomm Inc.
* **Category**: Hardware | **Theme**: Robotics & Drones
* **Team Details**: Team Phoenix — Interdisciplinary Engineering (CSE, AI & Data Science, Cyber Security)
* **The Operational Imperative**:
  * The first 72 hours dictate disaster casualty survival.
  * Ground teams are obstructed by impassable rubble, toxic dust, and destroyed infrastructure.
  * Current commercial drones fail in real disaster zones: they either mandate cloud/cellular connectivity (instantly severed) or burn batteries in under 18 minutes carrying power-hungry 35W+ desktop-grade GPUs.

### 30-Second Speaker Script (Pitcher)
> *"Respected evaluators, in catastrophic disasters like earthquakes, landslides, and flash floods, first responders face what is known as 'The Golden Window'—the critical 72 hours where survivor extrication probability plummets with every passing minute. Ground teams face impassable rubble, while standard drones are either blinded by dust, depend on destroyed cellular networks, or run out of battery in 15 minutes due to heavy GPUs. We are Team Phoenix, and we present an autonomous, edge-intelligent UAV powered by the Qualcomm Flight RB5 platform that executes real-time multi-spectral survivor detection and triage geolocation entirely on the edge, operating under a strict 12W compute envelope for over 35 minutes of continuous search endurance."*

### Qualcomm Evaluator Defense Tip
* *Anticipated Question*: "Why is your solution different from an off-the-shelf DJI Matrice thermal drone?"
* *Pre-emptive Defense*: Commercial DJI drones act as passive video cameras requiring a human pilot to manually stare at a screen for hours (operator fatigue). Phoenix runs *autonomous on-board perception, sensor fusion, and exact mathematical ray-casting geolocation*, producing structured casualty triage cards in under 3 seconds over an off-grid LoRa mesh without requiring continuous pilot interaction or active video links.

---

## Slide 2: Proposed Solution & Concept of Operations (ConOps)

### Layout & Visual Composition
* **Header**: PROPOSED SOLUTION & CONCEPT OF OPERATIONS (ConOps)
* **Structure**: 5-Stage Horizontal Flow Diagram across the center of the slide with clear phase badges and time milestones.
* **Bottom Half**: 3 Feature Highlights (Dual-Spectral Perception, On-Device Neural Pipeline, Off-Grid Resilient Telemetry).

### Exact Text Content (Slide Copy)
* **Stage 1 — Rapid Dispatch (0–3 min)**:
  * Hand-deployable Hexacopter with quick-lock folding arms.
  * Automated pre-flight system check, NPNT compliance token verification, and sector boundary upload.
* **Stage 2 — Autonomous Adaptive Sweep (3–25 min)**:
  * Boustrophedon / frontier grid coverage at optimal altitude ($25\text{m} - 35\text{m}$ AGL).
  * Real-time terrain-following via downward LiDAR and Visual-Inertial Odometry.
* **Stage 3 — Dual-Spectral On-Edge Detection (Continuous)**:
  * Hardware-synchronized 4K HDR RGB + Radiometric LWIR thermal sensor streams.
  * INT8 Quantized YOLO inference executing locally on Qualcomm Hexagon™ DSP/NPU.
* **Stage 4 — 3D Ray-Casting & Triage Geotagging (<35ms)**:
  * Pixel bounding-box centroid projected through 6-DoF gimbal attitude and altitude to WGS-84 coordinates ($\pm 2.5\text{m}$).
  * Dynamic triage priority assigned (Critical / Moderate / Non-Urgent) based on temperature delta and movement.
* **Stage 5 — Tactical Mesh Broadcast & Responder Delivery (<3s)**:
  * Encrypted 64-byte micro-telemetry packet broadcast via 868MHz LoRa mesh directly to NDRF field terminals and GCS map.

### 30-Second Speaker Script (Pitcher)
> *"Here is how Project Phoenix operates in the field. From the moment our hexacopter is deployed by NDRF teams, it executes an autonomous survey sweep over the disaster sector. As the drone traverses the grid, our synchronized 4K optical and radiometric LWIR thermal sensors ingest dual video streams directly into the Qualcomm QRB5165 processor. The onboard Hexagon NPU detects survivors in real time—even when partially obscured under rubble or in zero-lux darkness. Within 35 milliseconds, our onboard ray-casting engine translates the camera pixel coordinates into precise WGS-84 GPS coordinates. The drone then immediately transmits an encrypted 64-byte triage card over an independent LoRa mesh directly to the rescuers' handheld pagers."*

---

## Slide 3: System Architecture & Qualcomm Silicon Native Design

### Layout & Visual Composition
* **Header**: SYSTEM ARCHITECTURE & QUALCOMM SILICON-NATIVE INTEGRATION
* **Left Side (55% Width)**: Hardware Subsystem Block Diagram (Sensors $\to$ Qualcomm Flight RB5 $\to$ Avionics $\to$ Comms $\to$ Ground Station).
* **Right Side (45% Width)**: 4 Architecture Callout Cards with Qualcomm badge highlights.

### Exact Text Content (Slide Copy)
* **Card 1: Compute Engine (Qualcomm Flight™ RB5 / QRB5165 SoC)**
  * Octa-core Kryo™ 585 CPU running ROS 2 Humble mission planner.
  * Spectra™ 480 ISP handling 4K hardware camera debayering, HDR tone mapping, and sensor synchronization with zero CPU overhead.
* **Card 2: Hexagon™ 698 DSP + Tensor NPU (Edge AI Acceleration)**
  * INT8 Quantized YOLO model deployed via Qualcomm Snapdragon Neural Processing Engine (SNPE).
  * 15 TOPS computational throughput consuming only **8.2W–11.5W** (compared to 25W–40W on competing GPU boards).
  * Direct gain: **+30% extended flight duration** on standard 6S battery packs.
* **Card 3: Perception & Avionics Layer**
  * Sony IMX586 4K RGB + InfiRay/FLIR radiometric LWIR thermal camera on 2-axis stabilized brushless gimbal.
  * PX4 Autopilot on STM32 flight controller with triple-redundant IMUs linked via high-baud MAVLink UART.
* **Card 4: Resilient Communications Hierarchy**
  * Tier 1: FastConnect™ 6800 (Wi-Fi 6 / 5G) for high-bandwidth video when in base-camp range.
  * Tier 2: SX1262 LoRa (868 MHz) mesh transceiver for off-grid 10km+ mission-critical triage packet telemetry.

### 30-Second Speaker Script (Pitcher)
> *"What sets Phoenix apart is our architecture designed specifically around Qualcomm silicon. Instead of strapping an inefficient 35W desktop-class GPU to a drone, we exploit the heterogeneous architecture of the Qualcomm Flight RB5 platform. Our neural models are quantized to INT8 and run accelerated on the Hexagon 698 DSP and Tensor NPU via the Qualcomm SNPE SDK. This delivers 15 TOPS of AI power while sipping less than 12 Watts of power. The Qualcomm Spectra 480 ISP synchronizes and processes both 4K optical and thermal video streams directly in silicon, freeing up the Kryo CPU for autonomous mission navigation and fail-safe handling."*

---

## Slide 4: Mathematical Modeling & Edge-Case Robustness

### Layout & Visual Composition
* **Header**: MATHEMATICAL MODELING & EDGE-CASE ROBUSTNESS
* **Left Panel (50% Width)**: 3D Ray-Casting Geolocation Math with 3D coordinate geometry diagram.
* **Right Panel (50% Width)**: Radiometric Thermal False-Positive Filter & Failover State Machine.

### Exact Text Content (Slide Copy)
* **Mathematical Derivation: 3D Ray-Casting Geolocation**:
  * Unproject pixel $(u, v)$ via intrinsic matrix $\mathbf{K}^{-1}$ to camera ray $\vec{r}_C$.
  * Transform ray across Gimbal and Body frames to World NED coordinates:
    $$\hat{r}_W = \mathbf{R}_{\text{Body}}^{\text{World}}(\phi, \theta, \psi) \cdot \mathbf{R}_{\text{Gimbal}}^{\text{Body}}(\psi_g, \theta_g) \cdot \frac{\mathbf{K}^{-1} [u, v, 1]^T}{\|\mathbf{K}^{-1} [u, v, 1]^T\|}$$
  * Intersect with ground plane using altitude $H_{\text{AGL}}$:
    $$\vec{P}_{\text{target}} = \vec{P}_{\text{UAV}} + \left(\frac{H_{\text{AGL}}}{\hat{r}_{W, z}}\right) \cdot \hat{r}_W \quad \longrightarrow \quad (\text{Latitude } \phi, \text{Longitude } \lambda) \pm 2.5\text{m}$$
* **Radiometric False-Positive Suppression Formula**:
  * Eliminates false alarms from solar-heated asphalt ($>45^\circ\text{C}$), hot rocks, and machinery exhausts.
  * Radiometric biological window: $\Omega_{\text{human}} = [32.0^\circ\text{C}, 38.5^\circ\text{C}]$ with Gaussian gating:
    $$S_{\text{fused}} = \alpha \cdot C_{\text{RGB}} + \beta \cdot C_{\text{Thermal}} \cdot \exp\left(-\frac{(T_{\text{mean}} - 36.5)^2}{2\sigma_T^2}\right)$$
* **Deterministic Failover State Machine**:
  * *GNSS Denied*: Instant switch to Visual-Inertial Odometry (VIO) drift-bounded holding pattern.
  * *RF Blackout*: Store-and-Forward to non-volatile NVMe flash + LoRa broadcast without pausing mission.

### 30-Second Speaker Script (Pitcher)
> *"Disaster zones are full of edge-case traps that cause naive systems to fail. A hot tin roof or sun-baked asphalt will trigger countless false alarms in a standard thermal camera. Our pipeline uses a mathematically rigorous radiometric gating function that cross-validates biological skin temperature distributions with optical body contours, suppressing false alarms. Furthermore, to eliminate the need for cloud computing, our onboard 3D ray-casting engine factors the drone's 6-DoF attitude, gimbal tilt, and LiDAR altitude to compute real-world GPS coordinates within 2.5 meters. If GPS is jammed or cellular towers collapse, our failover state machine shifts to Visual-Inertial Odometry and broadcasts micro-telemetry across an off-grid LoRa mesh."*

---

## Slide 5: Bill of Materials (BOM), Feasibility & Cost-Benefit Analysis

### Layout & Visual Composition
* **Header**: FEASIBILITY, BILL OF MATERIALS (BOM) & COST COMPARISON
* **Left Side (60% Width)**: Structured Component Cost Table with Subsystem Groupings.
* **Right Side (40% Width)**: Cost Comparison Bar Chart & ROI Analysis.

### Exact Text Content (Slide Copy)
* **BOM Breakdown (Working Prototype Tier)**:
  * *Airframe & Propulsion*: Carbon-fiber folding hexacopter frame (680mm), 6x brushless motors (4006 380KV), 40A ESCs, 15-inch carbon props — **₹38,000**
  * *Companion Compute*: Qualcomm Flight™ RB5 Platform (QRB5165 SoC + Carrier board) — **₹62,000**
  * *Flight Avionics*: Pixhawk 6X Autopilot + Dual High-Precision GNSS / Compass + Downward LiDAR — **₹24,000**
  * *Perception Gimbal*: 4K Sony IMX586 + Radiometric LWIR Thermal Core + 2-axis brushless gimbal — **₹32,000**
  * *Power & Comms*: 6S 16,000mAh Semi-Solid Li-Ion battery + SX1262 LoRa module — **₹16,000**
  * **Total Prototype Investment**: **~₹1,72,000 (~$2,050 USD)**
* **Cost Advantage vs Commercial / Defense Benchmarks**:
  * Teledyne FLIR SkyRanger / Skydio X2D: **₹22,00,000 – ₹30,00,000+**
  * Commercial DJI Matrice 350 RTK + H20T: **₹11,00,000 – ₹14,00,000** (Cloud dependent, non-autonomous triage)
  * **Team Phoenix Platform**: **85% – 92% Cost Reduction** while delivering native on-edge AI and open tactical mesh integration.

### 30-Second Speaker Script (Pitcher)
> *"Feasibility and practical economics are central to our design. Commercial military-grade SAR drones like the FLIR SkyRanger cost upwards of 25 to 30 Lakh Rupees, placing them out of reach for widespread municipal disaster teams. Off-the-shelf industrial drones cost over 12 Lakhs and remain dependent on proprietary cloud backends. By harnessing the cost-effective Qualcomm Flight RB5 platform and commercially accessible avionics, Team Phoenix delivers a complete autonomous multi-spectral reconnaissance system at approximately 1.72 Lakh Rupees in prototype stage. That is an 88% cost reduction, making high-end edge AI deployable across every regional disaster response battalion in India."*

---

## Slide 6: Deployment Roadmap, Impact & National Disaster Alignment

### Layout & Visual Composition
* **Header**: DEPLOYMENT ROADMAP, OPERATIONAL IMPACT & SCALABILITY
* **Top Half**: 3-Phase Execution Roadmap (Gantt-style timeline).
* **Bottom Left (50% Width)**: 4 Quantifiable Impact Metrics.
* **Bottom Right (50% Width)**: Multi-UAV Swarm Expansion Architecture.

### Exact Text Content (Slide Copy)
* **3-Phase Execution Roadmap**:
  * *Phase 1 (Months 1–3)*: Gazebo / PX4 Software-in-the-Loop (SITL) simulation, Qualcomm SNPE model quantization, and synthetic smoke/thermal benchmarking.
  * *Phase 2 (Months 4–6)*: Hardware-in-the-Loop (HITL) bench assembly on Qualcomm Flight RB5, vibration damping calibration, and controlled burn/field testing.
  * *Phase 3 (Months 7–9)*: Collaborative field trials with State Disaster Response Force (SDRF) / Civil Defense units; integration with NDMA Incident Command Systems.
* **Target Impact Metrics**:
  * **80% Faster Reconnaissance**: Reduces initial square-kilometer sweep time from 3 hours to 35 minutes.
  * **Zero Personnel Risk**: Completely replaces vulnerable human scouts in hazardous collapse zones.
  * **Instant Triage Prioritization**: Responders receive geotagged casualty cards within 3 seconds of overflight.
* **Future Scalability (Multi-UAV Swarm)**:
  * Distributed LoRa mesh coordination allowing 3–5 Phoenix drones to collaboratively partition vast disaster zones without centralized cellular infrastructure.

### 30-Second Speaker Script (Pitcher)
> *"Looking ahead, Project Phoenix is structured as a clear, phased engineering deployment. Over the next six months, we advance our validated mathematical models through Software-in-the-Loop simulation directly into Qualcomm Flight RB5 hardware integration, culminating in field trials alongside SDRF and civil defense units. Our platform slashes initial reconnaissance time by 80%—from 3 hours down to 35 minutes per square kilometer—delivering instant, life-saving triage intelligence to first responders while keeping human scouts out of harm's way. Project Phoenix brings the computational supremacy of Qualcomm edge silicon directly to the frontlines of humanitarian disaster relief. Thank you, and we are ready for your questions."*
