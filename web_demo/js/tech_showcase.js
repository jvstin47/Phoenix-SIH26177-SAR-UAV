// Project Phoenix X — Core Technologies: Dual-Brain, 17-Byte LoRa & Dijkstra Router

const TechShowcase = {
  // Dual-Brain Inspector State
  activeChip: 'qrb2210', // 'qrb2210' or 'stm32u5'

  chipDetails: {
    qrb2210: {
      name: "Qualcomm Dragonwing QRB2210 MPU",
      role: "Mission Computer & Edge-AI Pipeline",
      os: "Debian Linux (PREEMPT_RT Real-Time Kernel)",
      power: "< 5.0 Watts active compute envelope (Target)",
      clock: "Quad-Core ARM Cortex-A53 @ 1.3 GHz",
      tasks: [
        "INT8 Quantized YOLOv8 Object Detection (Target: ~35 FPS on NPU)",
        "Optical-to-Ground Tait-Bryan Ray-Casting Projection",
        "Multi-spectral (RGB + Thermal) Spatial Registration",
        "Souli et al. (2024) 17-byte Telemetry Serialization",
        "SX1262 LoRa 868 MHz P2P Radio Driver Stack"
      ],
      interfaces: "High-speed UART / SPI to Flight MCU; MIPI CSI-2 for dual cameras",
      timing: "Asynchronous task execution; non-blocking RPC to FMU (zero flight jitter)"
    },
    stm32u5: {
      name: "STM32U585 MCU (ARM Cortex-M33)",
      role: "Flight Management Unit & Real-Time Stabilization",
      os: "Zephyr RTOS (Deterministic Embedded OS)",
      power: "~180 mW low-power flight controller",
      clock: "ARM Cortex-M33 with TrustZone @ 160 MHz",
      tasks: [
        "250 Hz (4ms) Deterministic Inner Flight Attitude Stabilization Loop",
        "350 Hz Direct Hardware PWM Brushless Motor ESC Control",
        "MPU6050 6-Axis IMU & MS5611 Barometric Altitude Ingestion",
        "Downward ToF LiDAR Ground Altitude Measurement (MS5611 fusion)",
        "Anti-Compass Drift Visual-Inertial Odometry (Bouabdallah 2007)"
      ],
      interfaces: "Direct PWM timers to 6x ESCs; I2C for avionics sensors; UART RPC bridge",
      timing: "Hard real-time 4ms deadline; 100% immune to Linux OS user-space delays"
    }
  },

  init() {
    this.setupDualBrain();
    this.setupLoRaPacker();
    this.setupDijkstraGCS();

    if (window.MissionState) {
      MissionState.subscribe((state) => {
        this.updateLoRaDisplay();
      });
    }
  },

  setupDualBrain() {
    this.inspectChip('qrb2210');
  },

  inspectChip(chipKey) {
    this.activeChip = chipKey;
    const info = this.chipDetails[chipKey];

    document.querySelectorAll('.chip-selector').forEach(btn => {
      btn.classList.remove('border-sky-500', 'bg-sky-950/40');
      btn.classList.add('border-slate-700', 'bg-slate-900/60');
    });
    const activeBtn = document.getElementById(`btn-chip-${chipKey}`);
    if (activeBtn) {
      activeBtn.classList.add('border-sky-500', 'bg-sky-950/40');
      activeBtn.classList.remove('border-slate-700', 'bg-slate-900/60');
    }

    const panel = document.getElementById('chip-inspector-content');
    if (panel) {
      panel.innerHTML = `
        <div class="space-y-3 font-mono text-xs">
          <div class="flex justify-between items-center pb-2 border-b border-slate-800">
            <span class="text-sm font-bold text-white">${info.name}</span>
            <span class="text-[10px] px-2 py-0.5 rounded bg-sky-950 text-sky-300 border border-sky-800">${info.role}</span>
          </div>
          <div class="grid grid-cols-2 gap-2 text-[11px]">
            <div><span class="text-slate-500">ENVIRONMENT:</span> <span class="text-slate-200">${info.os}</span></div>
            <div><span class="text-slate-500">POWER DRAW:</span> <span class="text-emerald-400 font-bold">${info.power}</span></div>
            <div><span class="text-slate-500">ARCHITECTURE:</span> <span class="text-slate-200">${info.clock}</span></div>
            <div><span class="text-slate-500">INTERFACES:</span> <span class="text-slate-200">${info.interfaces}</span></div>
          </div>
          <div>
            <span class="text-slate-500 text-[10px] block mb-1">CORE RESPONSIBILITIES:</span>
            <ul class="space-y-1 text-[11px] text-slate-300">
              ${info.tasks.map(t => `<li class="flex items-start"><span class="text-sky-400 mr-1.5">•</span>${t}</li>`).join('')}
            </ul>
          </div>
          <div class="p-2 rounded bg-slate-900 border border-slate-800 text-[10px] text-slate-400">
            <span class="text-amber-400 font-bold">TIMING CONSTRAINT:</span> ${info.timing}
          </div>
        </div>
      `;
    }
  },

  setupLoRaPacker() {
    this.updateLoRaDisplay();
  },

  updateLoRaDisplay() {
    if (!MissionState || !MissionState.telemetryPacket) {
      if (MissionState) MissionState.serializeTelemetry();
    }

    const pkt = MissionState ? MissionState.telemetryPacket : null;
    if (!pkt) return;

    const hexEl = document.getElementById('lora-hex-string');
    const binContainer = document.getElementById('lora-bytes-container');
    if (hexEl) hexEl.textContent = pkt.rawHex;

    if (binContainer && pkt.buffer) {
      const byteLabels = [
        "Header ('P')",
        "Lat[0]", "Lat[1]", "Lat[2]", "Lat[3]",
        "Lon[0]", "Lon[1]", "Lon[2]", "Lon[3]",
        "Alt[0]", "Alt[1]",
        "Triage/Conf",
        "Battery%",
        "Hdg[0]", "Hdg[1]",
        "HMAC[0]", "HMAC[1]"
      ];

      let html = "";
      pkt.buffer.forEach((b, i) => {
        const hex = b.toString(16).padStart(2, '0').toUpperCase();
        const bin = b.toString(2).padStart(8, '0');
        html += `
          <div class="inline-block p-1.5 m-0.5 bg-[#101720] border border-slate-800 rounded text-center text-xs font-mono">
            <div class="text-[9px] text-sky-400 font-bold">${byteLabels[i]}</div>
            <div class="text-amber-300 font-bold my-0.5">${hex}</div>
            <div class="text-[8px] text-slate-500">${bin}</div>
          </div>
        `;
      });
      binContainer.innerHTML = html;
    }
  },

  transmitLoRaPacket() {
    if (typeof playLoraBurst === 'function') playLoraBurst();
    if (window.MissionState) {
      MissionState.simulateLoRaTransmit(() => {
        const statusEl = document.getElementById('lora-transmit-status');
        if (statusEl) {
          statusEl.textContent = "TRANSMISSION CONFIRMED [RSSI: -98 dBm, SNR: +8.5 dB]";
          statusEl.className = "text-emerald-400 text-xs font-mono font-bold";
        }
      });
    }
  },

  // Tactical Dijkstra Routing
  setupDijkstraGCS() {
    this.canvasGCS = document.getElementById('canvas-gcs');
    if (!this.canvasGCS) return;
    this.ctxGCS = this.canvasGCS.getContext('2d');

    this.gridSize = 8;
    this.cellSize = 45;
    this.startNode = { x: 0, y: 0 };
    this.targetNode = { x: 6, y: 5 };
    this.hazards = [
      { x: 3, y: 1, type: 'wire', label: '11kV CABLE' },
      { x: 3, y: 2, type: 'wire', label: '11kV CABLE' },
      { x: 2, y: 4, type: 'fire', label: 'STRUCTURAL FIRE' },
      { x: 3, y: 4, type: 'fire', label: 'STRUCTURAL FIRE' },
      { x: 4, y: 4, type: 'fire', label: 'STRUCTURAL FIRE' },
      { x: 5, y: 2, type: 'flood', label: 'DEEP WATER' }
    ];

    this.runDijkstra();
    this.drawGCS();
  },

  runDijkstra() {
    const cols = this.gridSize;
    const rows = this.gridSize;
    const isHazard = (x, y) => this.hazards.some(h => h.x === x && h.y === y);

    const queue = [[this.startNode.x, this.startNode.y]];
    const visited = new Set();
    const parent = {};
    visited.add(`${this.startNode.x},${this.startNode.y}`);

    let found = false;

    while (queue.length > 0) {
      const [cx, cy] = queue.shift();
      if (cx === this.targetNode.x && cy === this.targetNode.y) {
        found = true;
        break;
      }

      const neighbors = [
        [cx + 1, cy], [cx - 1, cy], [cx, cy + 1], [cx, cy - 1]
      ];

      for (const [nx, ny] of neighbors) {
        if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && !isHazard(nx, ny)) {
          const key = `${nx},${ny}`;
          if (!visited.has(key)) {
            visited.add(key);
            parent[key] = [cx, cy];
            queue.push([nx, ny]);
          }
        }
      }
    }

    this.path = [];
    if (found) {
      let curr = [this.targetNode.x, this.targetNode.y];
      while (curr) {
        this.path.unshift(curr);
        const pKey = `${curr[0]},${curr[1]}`;
        curr = parent[pKey];
      }
    }

    // Distance computation (each grid cell ~40m)
    const directM = Math.round(Math.hypot(this.targetNode.x - this.startNode.x, this.targetNode.y - this.startNode.y) * 40);
    const routedM = (this.path.length - 1) * 40;
    const timeMin = (routedM / 75).toFixed(1); // pedestrian SAR pace ~4.5 km/h

    const routeData = {
      path: this.path,
      directDistanceM: directM,
      distanceM: routedM,
      traverseTimeMin: timeMin
    };

    if (window.MissionState && MissionState.currentStep >= 7) {
      MissionState.setDijkstraRoute(routeData);
    }

    // Update UI elements
    const dDirect = document.getElementById('route-direct-dist');
    const dRouted = document.getElementById('route-path-dist');
    const dTime = document.getElementById('route-est-time');
    if (dDirect) dDirect.textContent = `${directM} m`;
    if (dRouted) dRouted.textContent = `${routedM} m`;
    if (dTime) dTime.textContent = `~${timeMin} min`;
  },

  drawGCS() {
    if (!this.canvasGCS || !this.ctxGCS) return;
    const ctx = this.ctxGCS;
    const w = this.canvasGCS.width;
    const h = this.canvasGCS.height;
    ctx.clearRect(0, 0, w, h);

    const cs = this.cellSize;

    // Draw Grid Cells
    for (let x = 0; x < this.gridSize; x++) {
      for (let y = 0; y < this.gridSize; y++) {
        const px = x * cs + 20;
        const py = y * cs + 20;

        ctx.fillStyle = '#101720';
        ctx.fillRect(px, py, cs - 3, cs - 3);
        ctx.strokeStyle = '#1e293b';
        ctx.strokeRect(px, py, cs - 3, cs - 3);
      }
    }

    // Draw Hazards
    this.hazards.forEach(hz => {
      const px = hz.x * cs + 20;
      const py = hz.y * cs + 20;

      if (hz.type === 'wire') {
        ctx.fillStyle = 'rgba(245, 158, 11, 0.85)';
      } else if (hz.type === 'fire') {
        ctx.fillStyle = 'rgba(239, 68, 68, 0.85)';
      } else {
        ctx.fillStyle = 'rgba(56, 189, 248, 0.85)';
      }
      ctx.fillRect(px, py, cs - 3, cs - 3);

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 8px monospace';
      ctx.fillText(hz.label.split(' ')[0], px + 3, py + 22);
    });

    // Draw Dijkstra Path
    if (this.path && this.path.length > 1) {
      ctx.strokeStyle = '#6BCB9A';
      ctx.lineWidth = 3;
      ctx.beginPath();
      this.path.forEach((pt, i) => {
        const px = pt[0] * cs + 20 + (cs / 2);
        const py = pt[1] * cs + 20 + (cs / 2);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Waypoint dots
      ctx.fillStyle = '#6BCB9A';
      this.path.forEach(pt => {
        const px = pt[0] * cs + 20 + (cs / 2);
        const py = pt[1] * cs + 20 + (cs / 2);
        ctx.beginPath();
        ctx.arc(px, py, 3.5, 0, Math.PI * 2);
        ctx.fill();
      });
    }

    // Start Node (Base Camp)
    const bx = this.startNode.x * cs + 20 + (cs / 2);
    const by = this.startNode.y * cs + 20 + (cs / 2);
    ctx.fillStyle = '#4DA3FF';
    ctx.beginPath();
    ctx.arc(bx, by, 7, 0, Math.PI * 2);
    ctx.fill();

    // Target Node (Survivor)
    const vx = this.targetNode.x * cs + 20 + (cs / 2);
    const vy = this.targetNode.y * cs + 20 + (cs / 2);
    ctx.fillStyle = '#FF4D4F';
    ctx.beginPath();
    ctx.arc(vx, vy, 8, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }
};

window.TechShowcase = TechShowcase;
