# Hardware Trade-Off Studies & Component Selection Matrix

**Project**: Project Phoenix X — Phoenix-SIH26177-SAR-UAV  
**Problem Statement ID**: SIH26177 (Qualcomm Inc.)  
**Team**: Phoenix X (ID: 141943)  
**Last Updated**: September 2026

---

## 1. Edge Compute Architecture — Comparative Trade-Off

A central criterion for Qualcomm evaluators in SIH26177 is why and how the platform leverages Qualcomm edge silicon over generic compute boards. Phoenix X uses the **Arduino UNO Q**, which integrates the **Qualcomm Dragonwing™ QRB2210** (Linux SoC + Qualcomm NPU) alongside an **STM32U585** (Zephyr RTOS flight controller) on a single board.

| Feature / Metric | **Qualcomm Dragonwing QRB2210** *(Arduino UNO Q)* ✅ | NVIDIA Jetson Orin Nano (8 GB) | Raspberry Pi 5 + Hailo-8 Hat |
|:----------------|:------------------------------------------------------|:-------------------------------|:-----------------------------|
| **Dedicated AI Acceleration** | **Qualcomm NPU — INT8 inference (YOLOv8n)** | Ampere GPU Tensor Cores (40 TOPS) | Hailo-8 M.2 Module (26 TOPS) |
| **Flight Controller Integration** | **Dual-brain: QRB2210 + STM32U585 on same board** | Companion board only — requires separate FC | Companion board only — no RT guarantees |
| **Operating System** | **Linux (Yocto/Ubuntu) on QRB2210; Zephyr RTOS on STM32U585** | JetPack Linux | Raspberry Pi OS |
| **AI Inference Latency** | **< 30 ms for INT8 YOLOv8n on Qualcomm NPU** | ~25 ms (higher power cost) | ~50 ms (Hailo + CPU overhead) |
| **Active Power Consumption** | **~8 W typical (highly efficient mobile SoC)** | 15 W – 25 W (high thermal dissipation) | 12 W – 18 W (combined SBC + NPU) |
| **Board-Level Integration** | **Single Arduino UNO Q board (compute + FC)** | Two separate boards required | Two separate boards required |
| **Sponsor Alignment** | **Direct match: Qualcomm SIH26177 sponsor hardware** | Non-sponsor silicon — evaluator penalty | Low compute tier for dual thermal/RGB |
| **Flight Battery Impact** | **+28% to +35% longer flight duration** | ~8–12 min endurance reduction | Moderate penalty |
| **DGCA AUW Impact** | **Minimal — compact form factor stays under 2 kg** | Heavier — risks DGCA Micro limit breach | Moderate weight |

> **Decision**: Qualcomm Dragonwing QRB2210 (Arduino UNO Q) selected — directly mandated by Qualcomm Inc. as SIH26177 sponsor hardware, and provides the only integrated dual-brain (AI + flight control) solution in a sub-2 kg airframe.

---

## 2. Airframe Architecture — Quadcopter Selection

Phoenix X is a **custom carbon-fibre quadcopter** (4-rotor) designed to achieve the **DGCA Micro-UAV classification** (AUW < 2 kg) while meeting SAR mission payload requirements.

| Parameter | **Custom Carbon-Fibre Quadcopter** ✅ | Alternative: Hexacopter |
|:----------|:--------------------------------------|:------------------------|
| **Rotor Count** | 4 | 6 |
| **AUW (Phoenix X)** | **1.58 kg** | ~2.2–2.8 kg (heavier frame + 2 extra motors/ESCs) |
| **DGCA Category** | **Micro (<2 kg) — UAS Rules 2021** | Small (2–25 kg) — higher regulatory burden |
| **Payload Budget** | Optimised for QRB2210 + STM32U585 + LWIR + LoRa | Excess payload capacity not needed |
| **Wind Resistance** | Up to 10 m/s operational | Up to 14 m/s |
| **Regulatory Burden** | **Lowest — no DGCA operator permit for Green Zones** | Remote Pilot Certificate required |
| **Frame Material** | Carbon-fibre composite | Carbon-fibre composite |
| **ESC Count** | 4 ESCs | 6 ESCs |
| **Cost** | Lower (4 motors, 4 ESCs) | Higher (6 motors, 6 ESCs) |
| **Decision** | **✅ Selected** | ❌ Rejected — exceeds Micro AUW limit |

> **Decision**: Quadcopter selected. The critical design constraint is the **DGCA Micro (<2 kg) AUW limit**. At 1.58 kg, Phoenix X achieves the lightest regulatory category while meeting all sensor and compute payload requirements. A hexacopter would breach the 2 kg limit with standard components.

---

## 3. Communication Link Trade-Off

| Link Type | Frequency / Standard | Max Range (Urban Rubble) | Bandwidth | Power | Role in Phoenix X |
|:----------|:---------------------|:-------------------------|:----------|:------|:------------------|
| **Primary LoRa Triage** | **SX1262 LoRa 868 MHz** | **3.5 km – 12 km (NLoS/LoS)** | **1.2 – 5.4 kbps** | **~150 mW** | **Mission-critical 17-byte survivor geotag broadcast** |
| **RC Manual Override** | ExpressLRS (ELRS 2.4 GHz) | 5 km – 10 km | 250 Hz telemetry | ~250 mW | Manual pilot safety takeover |
| **Local Video** | Wi-Fi 5 GHz (when available) | 200 m – 800 m | 20–100 Mbps | ~3 W | Base-camp live video streaming (optional / non-mission-critical) |

> **LoRa Decision**: 868 MHz SX1262 selected as the primary mission-critical link — India WPC unlicensed band, infrastructure-free, covers 3.5–12 km through rubble and terrain. 17-byte binary packet format validated by Souli et al. (*Elsevier Computer Communications*, 2024).

---

## 4. Thermal Sensor Trade-Off

| Parameter | **LWIR Radiometric Sensor** ✅ | Near-IR (NIR) Camera | Standard RGB Night Vision |
|:----------|:-------------------------------|:---------------------|:--------------------------|
| **Spectral Band** | **8–14 µm (long-wave IR)** | 0.7–1.4 µm | 0.4–0.7 µm |
| **Smoke / Dust Penetration** | **✅ Yes — thermal wavelengths pass through** | Partial | ❌ No — obscured by smoke |
| **Darkness Operation** | **✅ Yes — passive thermal emission** | Requires IR illuminator | Requires illumination |
| **Survivor Detection** | **✅ 37°C body-heat lock** | Not reliable | Not reliable |
| **NETD** | **< 50 mK** | N/A | N/A |
| **Decision** | **✅ Selected** | ❌ Insufficient | ❌ Insufficient |

---

## 5. BOM Summary

### Phase 1 — Functional Prototype

| Category | Key Components | Approx. Cost (₹) |
|:---------|:---------------|:----------------|
| Compute | Arduino UNO Q (QRB2210 + STM32U585 — 4GB/32GB) | 8,800 |
| Airframe | Carbon-fibre frame, 4× motors, 4× ESCs, propellers | 9,200 |
| Sensors | LWIR thermal camera module + 1080p RGB camera | 8,400 |
| Communications | Semtech SX1262 LoRa module + 868 MHz antenna | 1,800 |
| Power | LiPo battery pack + BMS + charger | 4,200 |
| Miscellaneous | Wiring, connectors, 2-axis gimbal, fasteners, standoffs | 5,000 |
| **Phase 1 Total** | **Fully flying functional prototype** | **₹ 37,400** |

### Phase 2 — Production Unit

| Configuration | Per-Unit Cost | Notes |
|:--------------|:-------------|:------|
| Standard (India, domestic sourcing) | **₹ 85,000** | Volume pricing, domestic supply chain |
| Advanced (ruggedised / export) | **₹ 1,20,000** | IP65 enclosure, enhanced thermal, extended battery |

> Full itemised BOM with unit prices and vendors: [`docs/prototype_bom_and_financial_viability.md`](../docs/prototype_bom_and_financial_viability.md)

---

## 6. Compliance Summary

| Regulation | Requirement | Phoenix X Status |
|:-----------|:------------|:----------------|
| DGCA UAS Rules 2021 | AUW < 2 kg for Micro category | ✅ 1.58 kg AUW |
| WPC (India) | 868 MHz unlicensed ISM band (GSR 564(E)) | ✅ SX1262 868 MHz |
| IEEE Control Standards | Anti-windup cascaded PID for quadrotors | ✅ STM32U585 + Zephyr RTOS |
| Souli et al. (2024) [3] | 17-byte binary LoRa packet format | ✅ Implemented in QRB2210 pipeline |
