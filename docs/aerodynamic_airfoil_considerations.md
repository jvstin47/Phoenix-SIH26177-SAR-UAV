# Aerodynamic Airfoil & Rotor Selection Considerations
**Source Reference:**  
*Computer Program To Obtain Ordinates for NACA Airfoils*  
**Authors:** Charles L. Ladson, Cuyler W. Brooks, Jr., Acquilla S. Hill, Darrell W. Sproles  
**Institution:** NASA Langley Research Center (December 1996)  
**Document ID:** NASA Technical Memorandum 4741 (NASA TM-4741)  
**Project Application:** Team Phoenix — Problem Statement SIH26177 (Smart India Hackathon 2026, Qualcomm Inc.)

---

## 1. Context & Relevance to Team Phoenix

While Team Phoenix does not manufacture custom propeller geometries from raw composite molds, understanding airfoil behavior is essential for **Commercial-Off-The-Shelf (COTS) propeller selection**, **vibration mitigation**, and **aerodynamic parameter identification** in simulation models.

This document summarizes the aerodynamic principles from NASA TM-4741 directly applicable to multirotor propeller efficiency and flight controller stability.

---

## 2. Key Theoretical Insights for Rotorcraft

### 2.1 Reflexed Camber & Zero Pitching Moment ($C_{m, c/4} = 0$)
In Section *Camber-Line Equations (3-digit reflex, Page 8/11)*, the report highlights an important rotorcraft aerodynamic design rule:

> *"For some applications, for example, rotorcraft main rotors, to produce an airfoil with a quarter-chord pitching-moment coefficient of zero may be desirable. The 3-digit-reflexed camber line was thus designed to have a theoretical zero pitching moment..."*

#### **Operational Consequence for SAR UAV:**
* Standard asymmetric cambered airfoils generate a pitching moment that varies dynamically with rotational velocity ($\Omega$), inducing torsional twisting along the propeller blade.
* At high throttle or under turbulent disaster-zone gusts, this aerodynamic twist causes **blade flutter** and injects high-frequency mechanical vibration into the drone frame.
* **Selection Strategy:** For our SAR UAV, propellers utilizing reflexed camber lines or balanced semi-symmetric profiles are selected to keep aerodynamic pitching moments near zero, reducing stress on motor bearings and preventing sensor noise in the flight controller's IMU.

---

### 2.2 Airfoil Lift Slope ($a$) in Blade Element Momentum Theory (BEMT)
In foundational quadrotor dynamics (Bouabdallah, 2007; Leishman, 2006), the non-dimensional thrust coefficient ($C_T$) is parameterized by the lift-curve slope $a$:

$$C_T = \sigma a \left[\left(\frac{1}{6} + \frac{1}{4}\mu^2\right)\theta_0 - \frac{1}{4}\lambda\right]$$

Where:
* $\sigma$: Rotor solidity ratio ($N_{\text{blades}} \cdot c / \pi R$)
* $\theta_0$: Blade pitch angle at root
* $\mu$: Advance ratio in horizontal flight
* $\lambda$: Rotor inflow ratio

NASA TM-4741 establishes that for low-thickness, moderate-camber profiles operating at low-to-moderate Mach numbers, the section lift-curve slope asymptotically approaches the theoretical thin-airfoil limit:

$$a = \frac{dC_l}{d\alpha} \approx 2\pi \approx 5.73\text{ rad}^{-1} \text{ (to } 6.0\text{ rad}^{-1}\text{)}$$

* **Simulation Application:** When parameterizing propeller thrust in our PX4/Gazebo simulation environment, this lift slope value forms the baseline for thrust scaling.

---

## 3. Scope Justification for SIH26177 Evaluators

When addressing hardware selection during evaluation rounds, Team Phoenix presents the following engineering justification:

| Dimension | Approach Taken by Team Phoenix | Engineering Rationale |
| :--- | :--- | :--- |
| **Blade Manufacturing** | Commercial-Off-The-Shelf (COTS) Carbon/Nylon Propellers (e.g., T-Motor / Gemfan) | Re-inventing custom airfoil injection molds is cost-ineffective and diverts resources from Edge AI and search autonomy. |
| **Airfoil Profile Selection** | Stiff, low-pitching-moment profiles optimized for low Reynolds numbers ($Re \approx 50,000 - 150,000$) | Minimizes blade torsional flex, reducing IMU vibration and maximizing aerodynamic battery efficiency. |
| **Simulation Rigor** | Grounded in NASA & NACA aerodynamic lift/drag characteristics | Ensures physics-based simulation in Gazebo/SITL matches real-world thrust curves. |

---

## 4. Formal Citation

```bibtex
@techreport{ladson1996naca,
  author       = {Ladson, Charles L. and Brooks, Cuyler W., Jr. and Hill, Acquilla S. and Sproles, Darrell W.},
  title        = {Computer Program To Obtain Ordinates for NACA Airfoils},
  institution  = {NASA Langley Research Center},
  year         = {1996},
  number       = {NASA TM-4741},
  address      = {Hampton, VA, USA}
}
```
