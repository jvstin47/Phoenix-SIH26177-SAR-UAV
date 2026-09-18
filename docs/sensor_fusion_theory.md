# Mathematical Formulations & Theoretical Models

**Project**: Phoenix-SIH26177-SAR-UAV  
**Subsystem**: Multi-Spectral Perception & Geolocation Mathematics  

---

## 1. 3D Ray-Casting Target Geolocation Model

To resolve a detected survivor's real-world geographical coordinates (WGS-84 Latitude $\phi$, Longitude $\lambda$, Altitude $h$) from camera pixel coordinates $(u, v)$ without relying on external cloud compute or stereoscopic depth cameras at high altitudes, we formulate a 3D ray-casting pinhole camera projection model.

### 1.1 Coordinate Frame Definitions
1. **Camera Frame $\{C\}$**: Origin at camera optical center; $+Z_C$ forward along optical axis, $+X_C$ right, $+Y_C$ down.
2. **Gimbal Frame $\{G\}$**: Orientation relative to UAV body defined by pan (yaw $\psi_g$) and tilt (pitch $\theta_g$) angles.
3. **Body Frame $\{B\}$**: UAV reference frame (Forward-Right-Down).
4. **Local Tangent Plane / NED Frame $\{W\}$**: North-East-Down coordinate system centered at UAV takeoff or initial reference point.
5. **Geodetic Frame**: WGS-84 reference ellipsoid $(\phi, \lambda, h)$.

### 1.2 Normalized Ray in Camera Frame
Given camera intrinsic calibration matrix $\mathbf{K}$:
$$\mathbf{K} = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix}$$

For a bounding box detection centroid $(u, v)$, the unprojected ray vector $\vec{r}_C$ in camera coordinates is:
$$\vec{r}_C = \begin{bmatrix} \frac{u - c_x}{f_x} \\ \frac{v - c_y}{f_y} \\ 1 \end{bmatrix}$$
Normalized directional unit vector:
$$\hat{r}_C = \frac{\vec{r}_C}{\|\vec{r}_C\|}$$

### 1.3 Transformation to World NED Frame
The ray direction in the world frame $\hat{r}_W$ is obtained by successive rotation transformations:
$$\hat{r}_W = \mathbf{R}_{B}^{W}(\phi_b, \theta_b, \psi_b) \cdot \mathbf{R}_{G}^{B}(\psi_g, \theta_g) \cdot \hat{r}_C$$

Where:
* $\mathbf{R}_{B}^{W}$ is the rotation matrix derived from the UAV's onboard AHRS/IMU attitude (Euler angles: roll $\phi_b$, pitch $\theta_b$, yaw $\psi_b$).
* $\mathbf{R}_{G}^{B}$ is the gimbal rotation matrix measured from high-resolution optical encoders.

### 1.4 Ray-Ground Intersection
Let the current UAV position in the world NED frame be $\vec{P}_{\text{UAV}} = [x_{\text{UAV}}, y_{\text{UAV}}, z_{\text{UAV}}]^T$ where $z_{\text{UAV}} = -H_{\text{AGL}}$ (Above Ground Level, measured by down-facing LiDAR/barometric fusion).

Assuming local ground terrain elevation plane at $z = z_{\text{ground}} = 0$:
$$z_{\text{target}} = z_{\text{UAV}} + s \cdot \hat{r}_{W, z} = 0$$
Solving for scaling parameter $s$:
$$s = \frac{-z_{\text{UAV}}}{\hat{r}_{W, z}} = \frac{H_{\text{AGL}}}{\hat{r}_{W, z}}$$

The target position in world NED coordinates:
$$\vec{P}_{\text{target}} = \vec{P}_{\text{UAV}} + s \cdot \hat{r}_W$$

### 1.5 Geodetic Conversion (NED to WGS-84)
Using reference latitude $\phi_0$ and longitude $\lambda_0$ of the UAV:
$$\Delta \phi = \frac{x_{\text{target}}}{R_M + h}, \quad \Delta \lambda = \frac{y_{\text{target}}}{(R_N + h) \cos \phi_0}$$
Where $R_M$ is the meridian radius of curvature and $R_N$ is the prime vertical radius of curvature of Earth.

---

## 2. Multi-Spectral Radiometric Fusion & False-Positive Mitigation

Disaster environments are saturated with thermal false-positives: solar-baked metal sheeting, hot rocks, and machinery exhaust. A naive infrared threshold will trigger hundreds of false alarms.

### 2.1 Radiometric Calibration & Temperature Thresholding
Long-Wave Infrared (LWIR $8 - 14\,\mu\text{m}$) radiometric sensor records per-pixel absolute temperature $T(x, y)$ in Kelvin:
$$T_{\text{Celsius}}(x, y) = \frac{\text{Digital Count}(x, y)}{100} - 273.15$$

Human body core temperature is regulated at $37^\circ\text{C}$ ($310.15\text{ K}$), with exposed skin emitting an apparent thermal signature between:
$$\Omega_{\text{human}} = [32.0^\circ\text{C}, 38.5^\circ\text{C}]$$

### 2.2 Dual-Stream Spatio-Temporal Confidence Fusion
Let:
* $C_{\text{RGB}} \in [0, 1]$: Confidence score from the INT8 YOLO RGB model (trained on partial human body parts, limb contours, head profiles).
* $C_{\text{Thermal}} \in [0, 1]$: Confidence score from the thermal YOLO model.
* $\Phi(T)$: Radiometric gating function based on the temperature distribution inside the candidate bounding box:
$$\Phi(T) = \exp\left(-\frac{(T_{\text{mean}} - 36.5)^2}{2\sigma_T^2}\right)$$
where $\sigma_T \approx 2.5^\circ\text{C}$.

The fused triage score $S_{\text{fused}}$ is computed as:
$$S_{\text{fused}} = \alpha \cdot C_{\text{RGB}} + \beta \cdot C_{\text{Thermal}} \cdot \Phi(T)$$
Subject to dynamic weighting:
* Under daylight clear conditions: $\alpha = 0.6, \beta = 0.4$.
* Under night/smoke conditions (RGB brightness metric $I_{\text{mean}} < \tau_{\text{dark}}$): $\alpha = 0.1, \beta = 0.9$.

A target is registered as a confirmed casualty only when:
$$S_{\text{fused}} \ge \Theta_{\text{threshold}} \quad (\text{default: } 0.68)$$
This mathematical formulation virtually eliminates false positives from static solar-heated asphalt ($T > 45^\circ\text{C}$ or $\Phi(T) \to 0$) and cold mannequin debris.
