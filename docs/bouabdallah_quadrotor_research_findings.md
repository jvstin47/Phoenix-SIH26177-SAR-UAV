# Theoretical Foundations & Applied Findings for Autonomous SAR UAV Design
**Source Reference:**  
*Design and Control of Quadrotors with Application to Autonomous Flying*  
**Author:** Dr. Samir Bouabdallah  
**Institution:** École Polytechnique Fédérale de Lausanne (EPFL), Laboratory of Autonomous Systems (ASL), 2007  
**Doctoral Thesis No.:** 3727  
**Supervising Faculty:** Prof. Roland Siegwart (Advisor), Prof. Peter Corke, Dr. Philippe Müllhaupt, Prof. Jean-Daniel Nicoud  
**Project Application:** Team Phoenix — Problem Statement SIH26177 (Smart India Hackathon 2026, Qualcomm Inc.)

---

## 1. Executive Summary & Relevance

This document synthesizes core physical principles, mathematical formulations, sizing optimization algorithms, and sensor failure modes from Dr. Samir Bouabdallah's seminal doctoral dissertation at EPFL. These findings serve as the theoretical benchmark for **Team Phoenix's Autonomous Search and Rescue (SAR) UAV** project.

---

## 2. Mathematical Dynamics & Kinematics

### 2.1 Standard 12-State State-Space Representation (Section 4.2, Eq. 4.1–4.2)
The quadrotor rigid-body motion is fully captured by the 12-state vector:

```text
X = [φ,  φ_dot,  θ,  θ_dot,  ψ,  ψ_dot,  z,  z_dot,  x,  x_dot,  y,  y_dot]^T
```

* **Rotational States:**
  * Roll angle ($\phi$) and angular velocity ($\dot{\phi}$)
  * Pitch angle ($\theta$) and angular velocity ($\dot{\theta}$)
  * Yaw angle ($\psi$) and angular velocity ($\dot{\psi}$)
* **Translational States:**
  * Vertical position ($z$) and climb velocity ($\dot{z}$)
  * X position ($x$) and longitudinal velocity ($\dot{x}$)
  * Y position ($y$) and lateral velocity ($\dot{y}$)

### 2.2 Actuator Input-to-Force Mapping Matrix (Section 4.2, Eq. 4.4)
Given four rotor angular speeds $\Omega_1, \Omega_2, \Omega_3, \Omega_4$ in a cross configuration:

* **Total Vertical Thrust ($U_1$):**
  $$U_1 = b \cdot (\Omega_1^2 + \Omega_2^2 + \Omega_3^2 + \Omega_4^2)$$
* **Roll Control Torque ($U_2$):**
  $$U_2 = b \cdot (-\Omega_2^2 + \Omega_4^2)$$
* **Pitch Control Torque ($U_3$):**
  $$U_3 = b \cdot (\Omega_1^2 - \Omega_3^2)$$
* **Yaw Control Torque ($U_4$):**
  $$U_4 = d \cdot (-\Omega_1^2 + \Omega_2^2 - \Omega_3^2 + \Omega_4^2)$$

Where:
* $b$: Propeller aerodynamic thrust factor ($\text{N}\cdot\text{s}^2$)
* $d$: Propeller aerodynamic drag factor ($\text{N}\cdot\text{m}\cdot\text{s}^2$)

### 2.3 Rotational Equations with Gyroscopic Coupling (Section 2.2.4, Eq. 2.9)
Accounting for body inertia and high-speed rotor gyroscopic precession:

$$\begin{aligned}
I_{xx} \ddot{\phi} &= \dot{\theta}\dot{\psi}(I_{yy} - I_{zz}) - J_r \dot{\theta} \Omega_r + l \cdot U_2 \\
I_{yy} \ddot{\theta} &= \dot{\phi}\dot{\psi}(I_{zz} - I_{xx}) + J_r \dot{\phi} \Omega_r + l \cdot U_3 \\
I_{zz} \ddot{\psi} &= \dot{\phi}\dot{\theta}(I_{xx} - I_{yy}) + U_4
\end{aligned}$$

Where:
* $I_{xx}, I_{yy}, I_{zz}$: Principal mass moments of inertia ($\text{kg}\cdot\text{m}^2$)
* $J_r$: Rotor rotational inertia ($\text{kg}\cdot\text{m}^2$)
* $\Omega_r = -\Omega_1 + \Omega_2 - \Omega_3 + \Omega_4$: Net residual propeller angular speed
* $l$: Lever arm distance from propeller center to center of gravity (m)

### 2.4 Empirical Actuator Dynamics (Section 2.3.4, Eq. 2.22)
Motor speed response is non-instantaneous. It is accurately modeled as a first-order transfer function with time delay:

$$G(s) = \frac{\Omega_{\text{actual}}(s)}{\Omega_{\text{command}}(s)} = \frac{0.936}{0.178s + 1}$$

* **Takeaway for Team Phoenix:** Motor mechanical response time constant ($\tau \approx 0.178\text{ s}$) must be embedded into simulation controllers to prevent aggressive position-loop overshoot.

---

## 3. Optical-to-Ground Geolocation Mathematics

### 3.1 Direction Cosine Rotation Matrix (Appendix B.1, Eq. B.1–B.5)
The transformation matrix converting vectors from the body-fixed frame ($B$) to the Earth-fixed inertial frame ($E$) via Tait-Bryan angles:

$$R(\phi, \theta, \psi) = R_z(\psi) \cdot R_y(\theta) \cdot R_x(\phi)$$

Where:

```text
R_11 = cos(ψ)cos(θ)
R_12 = cos(ψ)sin(θ)sin(φ) - sin(ψ)cos(φ)
R_13 = cos(ψ)sin(θ)cos(φ) + sin(ψ)sin(φ)

R_21 = sin(ψ)cos(θ)
R_22 = sin(ψ)sin(θ)sin(φ) + cos(ψ)cos(φ)
R_23 = sin(ψ)sin(θ)cos(φ) - sin(φ)cos(ψ)

R_31 = -sin(θ)
R_32 = cos(θ)sin(φ)
R_33 = cos(θ)cos(φ)
```

### 3.2 Target Ray-Casting Algorithm for Ground Victim Geotagging
Given a detected survivor at image pixel coordinates $(u_c, v_c)$ with camera focal lengths $(f_x, f_y)$ and principal point $(c_x, c_y)$:

1. **Optical Ray in Body Frame:**
   $$\mathbf{v}_{\text{body}} = \begin{bmatrix} (u_c - c_x)/f_x \\ (v_c - c_y)/f_y \\ 1 \end{bmatrix}$$
2. **Transform to Earth Inertial Frame:**
   $$\mathbf{v}_{\text{earth}} = R \cdot \mathbf{v}_{\text{body}} = \begin{bmatrix} v_x & v_y & v_z \end{bmatrix}^T$$
3. **Ground Intersection at Known Drone Altitude $h$:**
   $$\mathbf{P}_{\text{victim}} = \mathbf{P}_{\text{drone}} + h \cdot \left(\frac{1}{v_z}\right) \begin{bmatrix} v_x \\ v_y \\ v_z \end{bmatrix}$$

* **Advantage:** Enables precise survivor geo-registration in GPS-denied or standoff reconnaissance flights without requiring direct overhead hovering.

---

## 4. Sizing Optimization Methodology & Design Indicators

### 4.1 Four Core Performance Indicators (Section 3.3.2)
1. **Propulsion Group Cost Factor ($C$):**
   $$C = \frac{P_{el}}{\frac{T}{g} - m_{pg}} \quad \left[\frac{\text{W}}{\text{g}}\right]$$
   Evaluates power expenditure per gram of net lifted payload.
2. **Propulsion Group Quality Factor ($Q_{pg}$):**
   $$Q_{pg} = \frac{BW \cdot \beta}{\Omega \cdot C} \quad \left[\frac{\text{Hz}\cdot\text{g}}{\text{rad}\cdot\text{W}}\right]$$
   Quantifies motor dynamic bandwidth ($BW$) relative to thrust-to-weight ratio ($\beta$) and electrical cost ($C$).
3. **Flight Autonomy / Endurance ($Au$):**
   $$Au = \frac{m_{bat} \cdot C_{bat}}{P_{el}} \quad [\text{hours}]$$
4. **Design Quality Index ($Q_{in}$):**
   $$Q_{in} = \frac{Au}{P_{el}} \quad \left[\frac{\text{hours}}{\text{W}}\right]$$

### 4.2 Empirical Mass Budget Benchmarks (Table 3.3, Fig. 3.8–3.10)
* **Thrust-to-Weight Ratio ($\beta$):** $\beta \ge 2.0$ provides a minimum 50% thrust reserve for high-wind disturbance rejection and emergency obstacle climb.
* **Battery Mass Fraction:** $35\% - 44\%$ of All-Up Weight (AUW). Increasing battery mass beyond 44% yields diminishing returns due to exponential motor drag scaling ($P \propto \Omega^3 D^5$).
* **Propulsion System Mass:** $25\% - 31\%$ of AUW.
* **Avionics & Edge AI Payload:** $15\% - 20\%$ of AUW.
* **Structural Airframe:** $10\% - 16\%$ of AUW.
* **Electrical Power Distribution:** Actuators consume $\approx 90\%$ of total power; flight avionics and edge compute must strictly remain within the remaining $\le 10\%$ power envelope.

---

## 5. Control Strategy Benchmark & Architecture

### 5.1 Experimental Control Technique Comparison (Chapter 4)
Bouabdallah benchmarked five controllers on the identical physical test platform:

| Control Technique | Mathematical Basis | Experimental Result on OS4 | Suitability for SAR UAV |
| :--- | :--- | :--- | :--- |
| **Lyapunov Theory** | Energy decay candidate function | Strong yaw response, but weak equilibrium stiffness | Inadequate for autonomous free flight |
| **Classical PID** | Independent SISO linear feedback | Effective in calm hover; fails under severe wind shear | Insufficient for disaster zones |
| **Linear Quadratic (LQR)** | State-space optimal Riccati optimization | Moderate results; noticeable steady-state error from unmodeled cable/wind drag | Sub-optimal under dynamic disturbance |
| **Sliding Mode (SMC)** | Variable structure switching surface | High disturbance rejection, but severe actuator chattering degraded IMU data | Unfavorable for motor wear |
| **Integral Backstepping (IB)** | Recursive Lyapunov design + Integral error tracking | **Superior:** High disturbance rejection, eliminates steady-state drift, fully stable autonomous takeoff/hover/landing | **Recommended Baseline Architecture** |

### 5.2 Cascaded Dual-Loop Spectral Separation (Section 4.10.3, Fig. 4.16)
To avoid control frequency resonance, translational and rotational loops must be decoupled across distinct execution frequencies:
* **Inner Attitude Loop (100 Hz – 250 Hz):** Dedicated to high-rate IMU attitude stabilization ($\phi, \theta, \psi$).
* **Outer Position Loop (20 Hz – 50 Hz):** Evaluates waypoint trajectories and outputs target roll and pitch angles ($\phi_d, \theta_d$) to drive horizontal translation.

### 5.3 Anti-Windup Integrator Protection (Appendix D.2, Algorithm 2)
When motors saturate during evasive maneuvers, error integration must freeze to prevent post-maneuver overshoot:
* Freeze accumulator when tracking error $|e| > \text{BandLimit}$.
* Integrate normally when actuator output is below saturation thresholds.
* Instantaneous reset when sign of control effort and integral state diverge.

---

## 6. Sensor Failure Modes & Environmental Mitigation

### 6.1 Motor Electromagnetic Interference on Magnetometers (Appendix C.1, Fig. C.4)
* **Observed Phenomenon:** Motor drive currents induce dynamic magnetic fields that distort standard electronic compasses by up to **0.25 radians in under 5 seconds**.
* **SAR Mission Consequence:** In collapsed steel-reinforced concrete rubble (heavy soft/hard-iron distortions), magnetometers are completely unreliable.
* **Mitigation Strategy:** Heading must be estimated using **Visual Inertial Odometry (VIO) / Optical Flow** fused with rate-gyro integration rather than relying on compass data.

### 6.2 Structural Vibration on IMU (Appendix C.1, Fig. C.1–C.2)
* High-frequency motor and propeller imbalances corrupt raw accelerometer readings with non-Gaussian noise.
* **Mitigation Strategy:** Mechanical silicone dampening mounts combined with a 2nd-order low-pass Butterworth filter and RPM-governed software notch filtering.

### 6.3 Ground Effect Turbulence (Section 2.3.1, Eq. 2.19)
* Within one rotor diameter ($z < 2 R_{\text{rad}}$), induced airflow velocity drops, creating an abrupt thrust increase:
  $$\frac{T_{\text{IGE}}}{T_{\text{OGE}}} = \frac{1}{1 - \frac{R_{\text{rad}}^2}{16z^2}}$$
* **Mitigation Strategy:** Implement altitude gain scheduling during takeoff and landing phases to avoid vehicle ground-rebound.

---

## 7. Formal References & Citation Details

```bibtex
@phdthesis{bouabdallah2007design,
  author       = {Bouabdallah, Samir},
  title        = {Design and Control of Quadrotors with Application to Autonomous Flying},
  school       = {École Polytechnique Fédérale de Lausanne (EPFL)},
  year         = {2007},
  number       = {3727},
  address      = {Lausanne, Switzerland},
  advisor      = {Siegwart, Roland},
  doi          = {10.5075/epfl-thesis-3727}
}

@inproceedings{bouabdallah2004pid,
  author       = {Bouabdallah, Samir and Noth, Andr{\'e} and Siegwart, Roland},
  title        = {PID vs LQ Control Techniques Applied to an Indoor Micro Quadrotor},
  booktitle    = {Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year         = {2004},
  pages        = {2451--2456},
  address      = {Sendai, Japan}
}

@inproceedings{bouabdallah2005backstepping,
  author       = {Bouabdallah, Samir and Siegwart, Roland},
  title        = {Backstepping and Sliding-Mode Techniques Applied to an Indoor Micro Quadrotor},
  booktitle    = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
  year         = {2005},
  pages        = {2247--2252},
  address      = {Barcelona, Spain}
}
```
