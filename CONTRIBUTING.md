# Contributing to Project Phoenix X

**Project Phoenix X** (SIH26177) is a Qualcomm-sponsored autonomous AI search-and-rescue UAV system built for Smart India Hackathon 2026. Thank you for your interest in contributing!

---

## About the Project

Phoenix X is a **DGCA Micro-UAV** (<2 kg AUW) powered by:
- **Qualcomm Dragonwing™ QRB2210** (Linux + Qualcomm NPU) for AI inference (INT8 YOLOv8n)
- **STM32U585** running **Zephyr RTOS** at 250 Hz for hard real-time flight control
- **SX1262 LoRa 868 MHz** for off-grid 17-byte binary telemetry up to 12 km
- **LWIR thermal + RGB dual-spectral** vision for 37°C survivor detection through smoke

**Live Demo:** [phoenix-sar-uav.vercel.app](https://phoenix-sar-uav.vercel.app)  
**GitHub:** [github.com/jvstin47/Phoenix-SIH26177-SAR-UAV](https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV)

---

## Running the Web Demo Locally

The interactive mission control demo requires **no build step** — it's pure HTML, CSS, and JavaScript.

```bash
# 1. Clone the repository
git clone https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV.git
cd Phoenix-SIH26177-SAR-UAV

# 2. Serve the web demo
python3 -m http.server 8080 --directory web_demo

# 3. Open in your browser
open http://localhost:8080
```

---

## Repository Structure

```
Phoenix-SIH26177-SAR-UAV/
├── README.md                          # Main project README
├── CONTRIBUTING.md                    # This file
├── web_demo/                          # Interactive mission control demo (HTML/JS/CSS)
├── docs/                              # Research & system design documentation
│   ├── system_architecture.md         # Hardware block diagrams & data flows
│   ├── prototype_bom_and_financial_viability.md
│   └── references.bib                 # All 8 IEEE/Elsevier citations (BibTeX)
├── hardware_bom/
│   └── component_selection_matrix.md  # Trade-off tables & BOM summary
└── presentation/                      # SIH 2026 presentation decks & scripts
```

---

## Documentation Conventions

- All hardware specs must reference the **Qualcomm Dragonwing QRB2210 + STM32U585** (Arduino UNO Q) — **not** QRB5165 or Pixhawk.
- Airframe is a **quadcopter at 1.58 kg AUW** — **not** a hexacopter.
- LoRa frequency is **868 MHz** (India WPC unlicensed band).
- All 8 IEEE/Elsevier papers listed in [`docs/references.bib`](docs/references.bib) and the README should be cited where relevant.
- Costs must reference the **₹35,800 prototype** and **₹85,000–₹1,20,000 production** figures.

---

## Contribution Guidelines

1. **Fork** the repository and create a feature branch: `git checkout -b feat/your-feature`
2. Ensure all documentation is internally consistent with the hardware specs above.
3. Run a quick sanity check: does the web demo still serve correctly after your changes?  
   `python3 -m http.server 8080 --directory web_demo`
4. **Commit** with a clear message: `git commit -m 'docs: describe what changed'`
5. Open a **Pull Request** against `main`.

---

## Contact

- **Team Phoenix X** — SIH26177 — Team ID 141943
- GitHub Issues: [github.com/jvstin47/Phoenix-SIH26177-SAR-UAV/issues](https://github.com/jvstin47/Phoenix-SIH26177-SAR-UAV/issues)
