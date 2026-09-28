with open('README.md', 'r') as f:
    text = f.read()

text = text.replace(
'''| Ref | Paper & Authors | Venue | Phoenix X Application |
|:--|:----------------|:------|:----------------------|
|  | **SwarmSAR-FW** — Siotia et al. (IIT Jodhpur & Manipal) | *IEEE Access*, Sept 2026 | Hazard-aware safe ingress/egress Dijkstra routing; 98.7% triage accuracy |
|  | **BLE Detection via Drone LoRa Relays** — Pérez-Díaz-de-Cerio et al. (UPC Spain) | *IEEE Access*, Sept 2026 | 868 MHz LoRa off-grid data bridge (<15g, <50 mW, 500m slant range) in canyons |
|  | **17-Byte LoRa Binary Telemetry** — Souli et al. | *Elsevier Computer Comms*, 2024 | Binary bit-packing serialization schema for resilient telemetry over raw LoRa |
|  | **RIS-Based Collaborative Swarm Computing** — Rahbari et al. (TalTech Estonia) | *IEEE Access*, July 2023 | Decentralized edge computing without cloud (-32% energy, -18% latency) |
|  | **SARDO** — Albanese et al. | *IEEE TMC*, 2022 | RF-based victim localization baseline; Phoenix X achieves equivalent triage at 1/8th weight |
|  | **Aerial CNN Survivor Detection** — Mishra et al. (BITS Pilani & Bennett Univ.) | *Elsevier Computer Comms*, 2020 | Quantized INT8 aerial human detection dataset (2000+ unique aerial images) |
|  | **First Drones in SAR** — Van Tilburg | *Wilderness & Environmental Medicine*, 2017 | Foundational field evidence for portable drone SAR and rapid unboxing protocols |''',
'''| Ref | Paper & Authors | Venue | Phoenix X Application |
|:--|:----------------|:------|:----------------------|
| `[1]` | **SwarmSAR-FW** — Siotia et al. (IIT Jodhpur & Manipal) | *IEEE Access*, Sept 2026 | Hazard-aware safe ingress/egress Dijkstra routing; 98.7% triage accuracy |
| `[2]` | **BLE Detection via Drone LoRa Relays** — Pérez-Díaz-de-Cerio et al. (UPC Spain) | *IEEE Access*, Sept 2026 | 868 MHz LoRa off-grid data bridge (<15g, <50 mW, 500m slant range) in canyons |
| `[3]` | **17-Byte LoRa Binary Telemetry** — Souli et al. | *Elsevier Computer Comms*, 2024 | Binary bit-packing serialization schema for resilient telemetry over raw LoRa |
| `[4]` | **RIS-Based Collaborative Swarm Computing** — Rahbari et al. (TalTech Estonia) | *IEEE Access*, July 2023 | Decentralized edge computing without cloud (-32% energy, -18% latency) |
| `[5]` | **SARDO** — Albanese et al. | *IEEE TMC*, 2022 | RF-based victim localization baseline; Phoenix X achieves equivalent triage at 1/8th weight |
| `[6]` | **Aerial CNN Survivor Detection** — Mishra et al. (BITS Pilani & Bennett Univ.) | *Elsevier Computer Comms*, 2020 | Quantized INT8 aerial human detection dataset (2000+ unique aerial images) |
| `[7]` | **First Drones in SAR** — Van Tilburg | *Wilderness & Environmental Medicine*, 2017 | Foundational field evidence for portable drone SAR and rapid unboxing protocols |'''
)

text = text.replace('indexed in [](research_papers/):', 'indexed in [`research_papers/`](research_papers/):')

with open('README.md', 'w') as f:
    f.write(text)

print('README.md fixed cleanly')
