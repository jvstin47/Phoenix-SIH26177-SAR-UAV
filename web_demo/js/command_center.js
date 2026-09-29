/**
 * Project Phoenix X — Disaster Management Agency Command Center
 * National Disaster Response Force (NDRF) / State Emergency Operations Center (SEOC)
 * 
 * Implements SIH26177 Requirement #8:
 * "Command Center Dashboard: Visualization of drone feeds, detected survivors, 
 *  hazard markers, and mission status to support disaster management agencies."
 */

const CommandCenter = {
  // Operational State
  activeScenario: 'wayanad',
  feedMode: 'fusion', // 'rgb', 'thermal', 'fusion'
  selectedVictimId: 'VIC-01',
  squadDispatched: false,
  squadProgress: 0,
  squadAnimTimer: null,
  metSeconds: 8468, // T+ 02:21:08 initial
  goldenHoursRemaining: 69.4, // out of 72 hrs
  
  // Scenarios with real assets
  scenarios: {
    wayanad: {
      name: "Sector-4 Wayanad Landslide Ingress",
      rgbImg: "images/wayanad_rgb.jpg",
      thermalImg: "images/wayanad_thermal.jpg",
      hazards: [
        { x: 3, y: 1, type: 'wire', label: '11kV Live Conductor' },
        { x: 3, y: 2, type: 'wire', label: '11kV Live Conductor' },
        { x: 2, y: 4, type: 'mudslide', label: 'Unstable Slip Plane' },
        { x: 3, y: 4, type: 'mudslide', label: 'Unstable Slip Plane' },
        { x: 5, y: 2, type: 'flood', label: 'Deep Water Depression' }
      ]
    },
    earthquake: {
      name: "Zone-B Collapsed Structure Void",
      rgbImg: "images/earthquake_rgb.jpg",
      thermalImg: "images/earthquake_thermal.jpg",
      hazards: [
        { x: 2, y: 2, type: 'fire', label: 'Smoldering Gas Pocket' },
        { x: 2, y: 3, type: 'fire', label: 'Smoldering Gas Pocket' },
        { x: 4, y: 2, type: 'wire', label: 'Severed Power Grid' },
        { x: 4, y: 4, type: 'mudslide', label: 'Secondary Collapse Wall' }
      ]
    },
    night_smoke: {
      name: "Night Ingress // Zero-Visibility Rubble",
      rgbImg: "images/night_smoke_rgb.jpg",
      thermalImg: "images/night_smoke_thermal.jpg",
      hazards: [
        { x: 1, y: 3, type: 'fire', label: 'Active Rubble Blaze' },
        { x: 3, y: 3, type: 'wire', label: 'Exposed 11kV Grid' },
        { x: 5, y: 3, type: 'mudslide', label: 'Steep Landslip Face' }
      ]
    }
  },

  // Casualties Manifest
  victims: [
    {
      id: 'VIC-01',
      status: 'CODE RED',
      statusClass: 'bg-rose-950/80 text-rose-400 border-rose-600',
      urgency: 'IMMEDIATE',
      coords: '11.581240° N, 76.128450° E',
      node: { x: 6, y: 5 },
      temp: '37.1°C',
      confidence: '98.4%',
      posture: 'Trapped under concrete roof void',
      assignedSquad: 'NDRF Team Alpha (Dispatched)',
      eta: '4.8 min',
      notes: 'Weak respiratory movement detected via thermal NetD'
    },
    {
      id: 'VIC-02',
      status: 'CODE YELLOW',
      statusClass: 'bg-amber-950/80 text-amber-400 border-amber-600',
      urgency: 'DELAYED',
      coords: '11.583190° N, 76.126120° E',
      node: { x: 5, y: 1 },
      temp: '36.8°C',
      confidence: '94.1%',
      posture: 'Surface debris entrapment; responsive',
      assignedSquad: 'SDRF Squad Bravo (Standby)',
      eta: '11.2 min',
      notes: 'Lower extremity pinned; non-critical'
    },
    {
      id: 'VIC-03',
      status: 'CODE GREEN',
      statusClass: 'bg-emerald-950/80 text-emerald-400 border-emerald-600',
      urgency: 'MINIMAL',
      coords: '11.584100° N, 76.124500° E',
      node: { x: 1, y: 6 },
      temp: '36.5°C',
      confidence: '89.6%',
      posture: 'Walking wounded near perimeter',
      assignedSquad: 'Local Responders (Self-Evac)',
      eta: 'En Route',
      notes: 'Superficial contusions; ambulatory'
    }
  ],

  // Layer Visibility
  layers: {
    droneTrack: true,
    hazards: true,
    dijkstra: true,
    elevation: true
  },

  // Map Grid
  gridSize: 8,
  cellSize: 46,
  baseNode: { x: 0, y: 0 },
  currentPath: [],

  // Telemetry Log History
  logs: [
    { time: "08:14:02", tag: "SYS", msg: "Incident Command Post GCS operational on 868.1 MHz LoRa link." },
    { time: "08:14:15", tag: "UAV", msg: "Phoenix-01 airborne AGL 42.5m; INT8 YOLOv8n inference stable @ 31.2ms." },
    { time: "08:14:32", tag: "AI", msg: "Multi-Spectral Bio-Lock confirmed on target VIC-01 (37.1°C, 98.4%)." },
    { time: "08:14:35", tag: "LORA", msg: "17-byte telemetry frame verified with HMAC-SHA256 signature." },
    { time: "08:14:48", tag: "ROUTER", msg: "Dijkstra safe corridor calculated around severed 11kV conductor." }
  ],

  init() {
    this.canvasFeed = document.getElementById('cmd-canvas-feed');
    this.canvasMap = document.getElementById('cmd-canvas-map');
    
    if (this.canvasFeed) this.ctxFeed = this.canvasFeed.getContext('2d');
    if (this.canvasMap) this.ctxMap = this.canvasMap.getContext('2d');

    this.loadImages();
    this.startMETTimer();
    this.recomputeRoute();
    this.render();

    // Responsive redraw
    window.addEventListener('resize', () => {
      this.render();
    });
  },

  loadImages() {
    this.loadedImages = {};
    const toLoad = [
      ['wayanad_rgb', 'images/wayanad_rgb.jpg'],
      ['wayanad_thermal', 'images/wayanad_thermal.jpg'],
      ['earthquake_rgb', 'images/earthquake_rgb.jpg'],
      ['earthquake_thermal', 'images/earthquake_thermal.jpg'],
      ['night_smoke_rgb', 'images/night_smoke_rgb.jpg'],
      ['night_smoke_thermal', 'images/night_smoke_thermal.jpg']
    ];

    toLoad.forEach(([key, src]) => {
      const img = new Image();
      img.src = src;
      img.onload = () => {
        this.loadedImages[key] = img;
        this.renderFeed();
      };
    });
  },

  startMETTimer() {
    setInterval(() => {
      this.metSeconds++;
      this.updateMETDisplay();
    }, 1000);
  },

  updateMETDisplay() {
    const hours = Math.floor(this.metSeconds / 3600);
    const mins = Math.floor((this.metSeconds % 3600) / 60);
    const secs = this.metSeconds % 60;
    const str = `T+ ${String(hours).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    
    const el = document.getElementById('cmd-met-timer');
    if (el) el.textContent = str;

    // Remaining Golden 72h countdown
    const remHours = (72 - (this.metSeconds / 3600)).toFixed(1);
    const remEl = document.getElementById('cmd-golden-hours');
    const barEl = document.getElementById('cmd-golden-bar');
    if (remEl) remEl.textContent = `${remHours}h REMAINING`;
    if (barEl) {
      const pct = Math.max(0, Math.min(100, (remHours / 72) * 100));
      barEl.style.width = `${pct}%`;
    }
  },

  setFeedMode(mode) {
    this.feedMode = mode;
    ['rgb', 'thermal', 'fusion'].forEach(m => {
      const btn = document.getElementById(`btn-mode-${m}`);
      if (btn) {
        if (m === mode) {
          btn.className = "px-3 py-1.5 rounded bg-sky-600 text-white font-mono font-bold text-xs shadow-sm transition";
        } else {
          btn.className = "px-3 py-1.5 rounded bg-[#101720] hover:bg-slate-800 text-slate-400 font-mono text-xs transition border border-slate-800";
        }
      }
    });
    this.renderFeed();
    this.log("STREAM", `Sensor view mode switched to ${mode.toUpperCase()}`);
  },

  setScenario(scenKey) {
    this.activeScenario = scenKey;
    const scen = this.scenarios[scenKey];
    const labelEl = document.getElementById('cmd-incident-name');
    if (labelEl) labelEl.textContent = scen.name;

    // Reset hazards to scenario default
    this.recomputeRoute();
    this.renderFeed();
    this.renderMap();
    this.log("SECTOR", `Command theater shifted to: ${scen.name}`);
  },

  selectVictim(vId) {
    this.selectedVictimId = vId;
    this.recomputeRoute();
    this.render();
    this.log("TARGET", `Active incident extraction target locked on: ${vId}`);
  },

  toggleLayer(layerKey) {
    this.layers[layerKey] = !this.layers[layerKey];
    this.renderMap();
  },

  recomputeRoute() {
    const scen = this.scenarios[this.activeScenario];
    const victim = this.victims.find(v => v.id === this.selectedVictimId) || this.victims[0];
    const targetNode = victim.node;

    const cols = this.gridSize;
    const rows = this.gridSize;
    const hazards = scen.hazards;

    const isHazard = (x, y) => hazards.some(h => h.x === x && h.y === y);

    // Dijkstra / BFS search
    const queue = [[this.baseNode.x, this.baseNode.y]];
    const visited = new Set();
    const parent = {};
    visited.add(`${this.baseNode.x},${this.baseNode.y}`);

    let found = false;

    while (queue.length > 0) {
      const [cx, cy] = queue.shift();
      if (cx === targetNode.x && cy === targetNode.y) {
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

    this.currentPath = [];
    if (found) {
      let curr = [targetNode.x, targetNode.y];
      while (curr) {
        this.currentPath.unshift(curr);
        const pKey = `${curr[0]},${curr[1]}`;
        curr = parent[pKey];
      }
    }

    // Update UI numbers
    const directM = Math.round(Math.hypot(targetNode.x - this.baseNode.x, targetNode.y - this.baseNode.y) * 40);
    const routedM = Math.max(1, (this.currentPath.length - 1)) * 40;
    const timeMin = (routedM / 75).toFixed(1);

    const dDirect = document.getElementById('cmd-route-direct');
    const dRouted = document.getElementById('cmd-route-routed');
    const dTime = document.getElementById('cmd-route-eta');
    if (dDirect) dDirect.textContent = `${directM} m`;
    if (dRouted) dRouted.textContent = `${routedM} m`;
    if (dTime) dTime.textContent = `~${timeMin} min`;
  },

  injectDynamicHazard() {
    const scen = this.scenarios[this.activeScenario];
    // Pick an empty cell on the current path or near it
    let candidate = null;
    if (this.currentPath.length > 3) {
      const mid = this.currentPath[Math.floor(this.currentPath.length / 2)];
      candidate = { x: mid[0], y: mid[1] };
    } else {
      candidate = { x: 4, y: 3 };
    }

    scen.hazards.push({
      x: candidate.x,
      y: candidate.y,
      type: 'wire',
      label: 'Secondary 11kV Grid Rupture'
    });

    if (typeof playWarningChime === 'function') playWarningChime();
    this.log("HAZARD_ALERT", `NEW OBSTACLE: 11kV Wire Collapse at Grid [${candidate.x}, ${candidate.y}]! Recalculating safe corridor...`);
    this.recomputeRoute();
    this.renderMap();
  },

  dispatchSquad() {
    this.squadDispatched = true;
    this.squadProgress = 0;
    if (typeof playLoraBurst === 'function') playLoraBurst();

    this.log("DISPATCH", `NDRF Rescue Squad Alpha deployed along Dijkstra extraction corridor.`);

    if (this.squadAnimTimer) clearInterval(this.squadAnimTimer);
    this.squadAnimTimer = setInterval(() => {
      this.squadProgress += 0.04;
      if (this.squadProgress >= 1) {
        this.squadProgress = 1;
        clearInterval(this.squadAnimTimer);
        this.log("ARRIVED", `NDRF Squad Alpha reached ${this.selectedVictimId}. Beginning physical casualty extraction.`);
      }
      this.renderMap();
    }, 120);
  },

  broadcastLoRa() {
    if (typeof playLoraBurst === 'function') playLoraBurst();
    this.log("LORA_TX", `Broadcasting 17-byte encrypted triage payload over 868.1 MHz LoRa [SF10, BW 125kHz]`);
    const status = document.getElementById('cmd-lora-flash');
    if (status) {
      status.classList.remove('hidden');
      setTimeout(() => status.classList.add('hidden'), 2500);
    }
  },

  exportICSReport() {
    const incidentData = {
      agency: "National Disaster Response Force (NDRF)",
      incidentName: this.scenarios[this.activeScenario].name,
      metTimestamp: document.getElementById('cmd-met-timer')?.textContent || "T+02:21:08",
      uavPlatform: "Phoenix X Dual-Brain Micro-UAV (SIH26177)",
      telemetryLink: "Semtech SX1262 LoRa @ 868 MHz (P2P Mesh)",
      detectedCasualties: this.victims,
      activeHazards: this.scenarios[this.activeScenario].hazards,
      computedEvacuationCorridor: {
        waypoints: this.currentPath,
        lengthMeters: document.getElementById('cmd-route-routed')?.textContent || "480 m",
        estimatedTransitTime: document.getElementById('cmd-route-eta')?.textContent || "6.5 min"
      },
      auditLogSummary: this.logs.slice(-10)
    };

    const blob = new Blob([JSON.stringify(incidentData, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ICS-201_Phoenix_${this.activeScenario}_${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);

    this.log("EXPORT", `ICS-201 Tactical Incident Manifest successfully generated and exported.`);
  },

  log(tag, msg) {
    const now = new Date();
    const timeStr = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
    this.logs.push({ time: timeStr, tag, msg });
    if (this.logs.length > 30) this.logs.shift();

    const container = document.getElementById('cmd-log-stream');
    if (container) {
      const row = document.createElement('div');
      row.className = "flex space-x-2 text-[11px] font-mono leading-tight py-0.5 border-b border-slate-900";
      row.innerHTML = `<span class="text-slate-500">${timeStr}</span><span class="text-sky-400 font-bold">[${tag}]</span><span class="text-slate-300">${msg}</span>`;
      container.appendChild(row);
      container.scrollTop = container.scrollHeight;
    }
  },

  render() {
    this.renderFeed();
    this.renderMap();
  },

  renderFeed() {
    if (!this.canvasFeed || !this.ctxFeed) return;
    const ctx = this.ctxFeed;
    const w = this.canvasFeed.width;
    const h = this.canvasFeed.height;

    ctx.clearRect(0, 0, w, h);

    const scenKey = this.activeScenario;
    const rgbImg = this.loadedImages[`${scenKey}_rgb`];
    const thImg = this.loadedImages[`${scenKey}_thermal`];

    // Background video simulation
    if (this.feedMode === 'rgb' && rgbImg) {
      ctx.drawImage(rgbImg, 0, 0, w, h);
    } else if (this.feedMode === 'thermal' && thImg) {
      ctx.drawImage(thImg, 0, 0, w, h);
    } else if (this.feedMode === 'fusion' && rgbImg && thImg) {
      ctx.drawImage(rgbImg, 0, 0, w, h);
      ctx.globalAlpha = 0.55;
      ctx.drawImage(thImg, 0, 0, w, h);
      ctx.globalAlpha = 1.0;
    } else {
      // Fallback procedural visualizer
      ctx.fillStyle = '#090D12';
      ctx.fillRect(0, 0, w, h);
    }

    // Overlay Tactical Crosshairs & HUD Elements
    ctx.strokeStyle = '#00F0FF';
    ctx.lineWidth = 1.5;

    // Artificial Horizon Pitch Ladder
    const cx = w / 2;
    const cy = h / 2;

    ctx.beginPath();
    ctx.moveTo(cx - 50, cy);
    ctx.lineTo(cx - 15, cy);
    ctx.moveTo(cx + 15, cy);
    ctx.lineTo(cx + 50, cy);
    ctx.moveTo(cx, cy - 8);
    ctx.lineTo(cx, cy + 8);
    ctx.stroke();

    // Compass Tape at top
    ctx.fillStyle = 'rgba(9, 13, 18, 0.75)';
    ctx.fillRect(0, 0, w, 28);
    ctx.fillStyle = '#00F0FF';
    ctx.font = '10px monospace';
    ctx.textAlign = 'center';
    ctx.fillText('030° · · · · 042° NE · · · · 060° · · · · 075°', cx, 18);

    // Target Bounding Box on Survivor
    const boxX = cx - 45;
    const boxY = cy - 25;
    const boxW = 90;
    const boxH = 50;

    ctx.strokeStyle = '#FF3366';
    ctx.lineWidth = 2;
    ctx.strokeRect(boxX, boxY, boxW, boxH);

    // Target Label Pill
    ctx.fillStyle = 'rgba(255, 51, 102, 0.85)';
    ctx.fillRect(boxX, boxY - 18, boxW, 18);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 9px monospace';
    ctx.textAlign = 'left';
    ctx.fillText('VIC-01: 37.1°C', boxX + 4, boxY - 5);

    // Corner brackets
    const bLen = 8;
    ctx.strokeStyle = '#00F0FF';
    ctx.lineWidth = 2;
    // Top-left
    ctx.beginPath();
    ctx.moveTo(15, 45 + bLen); ctx.lineTo(15, 45); ctx.lineTo(15 + bLen, 45);
    // Bottom-right
    ctx.moveTo(w - 15 - bLen, h - 25); ctx.lineTo(w - 15, h - 25); ctx.lineTo(w - 15, h - 25 - bLen);
    ctx.stroke();

    // Flight Telemetry Bar at bottom
    ctx.fillStyle = 'rgba(9, 13, 18, 0.85)';
    ctx.fillRect(0, h - 26, w, 26);
    ctx.fillStyle = '#64748B';
    ctx.font = '10px monospace';
    ctx.textAlign = 'left';
    ctx.fillText('ALT: 42.5m AGL', 12, h - 9);
    ctx.fillText('SPD: 8.2 m/s', 110, h - 9);
    ctx.fillStyle = '#10B981';
    ctx.fillText('NPU: 31.2ms [INT8]', 200, h - 9);
    ctx.fillStyle = '#F59E0B';
    ctx.textAlign = 'right';
    ctx.fillText('BATT: 15.1V [76%]', w - 12, h - 9);
  },

  renderMap() {
    if (!this.canvasMap || !this.ctxMap) return;
    const ctx = this.ctxMap;
    const w = this.canvasMap.width;
    const h = this.canvasMap.height;

    ctx.clearRect(0, 0, w, h);

    const cs = this.cellSize;
    const isLight = document.documentElement.classList.contains('light');

    // Base background
    ctx.fillStyle = isLight ? '#F1F5F9' : '#0B1118';
    ctx.fillRect(0, 0, w, h);

    // Draw Grid Cells
    for (let x = 0; x < this.gridSize; x++) {
      for (let y = 0; y < this.gridSize; y++) {
        const px = x * cs + 14;
        const py = y * cs + 14;

        ctx.fillStyle = isLight ? '#FFFFFF' : '#101720';
        ctx.fillRect(px, py, cs - 3, cs - 3);

        ctx.strokeStyle = isLight ? '#CBD5E1' : '#1e293b';
        ctx.lineWidth = 1;
        ctx.strokeRect(px, py, cs - 3, cs - 3);
      }
    }

    const scen = this.scenarios[this.activeScenario];

    // 1. Draw Hazards
    if (this.layers.hazards) {
      scen.hazards.forEach(hz => {
        const px = hz.x * cs + 14;
        const py = hz.y * cs + 14;

        if (hz.type === 'wire') {
          ctx.fillStyle = 'rgba(245, 158, 11, 0.25)';
          ctx.fillRect(px, py, cs - 3, cs - 3);
          ctx.strokeStyle = '#F59E0B';
          ctx.lineWidth = 2;
          ctx.strokeRect(px, py, cs - 3, cs - 3);

          // Diagonal strike
          ctx.beginPath();
          ctx.moveTo(px + 4, py + 4);
          ctx.lineTo(px + cs - 7, py + cs - 7);
          ctx.stroke();

          ctx.fillStyle = '#F59E0B';
          ctx.font = 'bold 8px monospace';
          ctx.textAlign = 'center';
          ctx.fillText('11kV', px + (cs - 3)/2, py + (cs - 3)/2 + 3);
        } else if (hz.type === 'fire') {
          ctx.fillStyle = 'rgba(239, 68, 68, 0.35)';
          ctx.fillRect(px, py, cs - 3, cs - 3);
          ctx.strokeStyle = '#EF4444';
          ctx.lineWidth = 2;
          ctx.strokeRect(px, py, cs - 3, cs - 3);

          ctx.fillStyle = '#EF4444';
          ctx.font = 'bold 8px monospace';
          ctx.textAlign = 'center';
          ctx.fillText('FIRE', px + (cs - 3)/2, py + (cs - 3)/2 + 3);
        } else {
          ctx.fillStyle = 'rgba(56, 189, 248, 0.25)';
          ctx.fillRect(px, py, cs - 3, cs - 3);
          ctx.strokeStyle = '#38BDF8';
          ctx.lineWidth = 2;
          ctx.strokeRect(px, py, cs - 3, cs - 3);

          ctx.fillStyle = '#38BDF8';
          ctx.font = 'bold 8px monospace';
          ctx.textAlign = 'center';
          ctx.fillText('SLIP', px + (cs - 3)/2, py + (cs - 3)/2 + 3);
        }
      });
    }

    // 2. Draw Dijkstra Corridor
    if (this.layers.dijkstra && this.currentPath.length > 1) {
      ctx.beginPath();
      this.currentPath.forEach(([x, y], idx) => {
        const cx = x * cs + 14 + (cs - 3)/2;
        const cy = y * cs + 14 + (cs - 3)/2;
        if (idx === 0) ctx.moveTo(cx, cy);
        else ctx.lineTo(cx, cy);
      });
      ctx.strokeStyle = '#10B981';
      ctx.lineWidth = 4;
      ctx.setLineDash([6, 3]);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Squad Position along path if dispatched
      if (this.squadDispatched && this.currentPath.length > 1) {
        const totalSegments = this.currentPath.length - 1;
        const currentSegment = Math.min(totalSegments - 1, Math.floor(this.squadProgress * totalSegments));
        const segT = (this.squadProgress * totalSegments) - currentSegment;

        const pA = this.currentPath[currentSegment];
        const pB = this.currentPath[currentSegment + 1];

        const sqX = (pA[0] + (pB[0] - pA[0]) * segT) * cs + 14 + (cs - 3)/2;
        const sqY = (pA[1] + (pB[1] - pA[1]) * segT) * cs + 14 + (cs - 3)/2;

        ctx.fillStyle = '#3B82F6';
        ctx.beginPath();
        ctx.arc(sqX, sqY, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#FFFFFF';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#FFFFFF';
        ctx.font = 'bold 8px monospace';
        ctx.textAlign = 'center';
        ctx.fillText('ALPHA', sqX, sqY - 11);
      }
    }

    // 3. Draw Base Camp (Start Node)
    const bx = this.baseNode.x * cs + 14 + (cs - 3)/2;
    const by = this.baseNode.y * cs + 14 + (cs - 3)/2;

    ctx.fillStyle = '#3B82F6';
    ctx.beginPath();
    ctx.arc(bx, by, 9, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = isLight ? '#1E293B' : '#FFFFFF';
    ctx.font = 'bold 9px monospace';
    ctx.textAlign = 'left';
    ctx.fillText('NDRF BASE', bx + 12, by + 3);

    // 4. Draw Survivor Pins
    this.victims.forEach(v => {
      const vx = v.node.x * cs + 14 + (cs - 3)/2;
      const vy = v.node.y * cs + 14 + (cs - 3)/2;
      const isTarget = v.id === this.selectedVictimId;

      ctx.fillStyle = v.status === 'CODE RED' ? '#EF4444' : (v.status === 'CODE YELLOW' ? '#F59E0B' : '#10B981');
      ctx.beginPath();
      ctx.arc(vx, vy, isTarget ? 10 : 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#FFFFFF';
      ctx.lineWidth = isTarget ? 2.5 : 1.5;
      ctx.stroke();

      if (isTarget) {
        // Glowing target beacon
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(vx, vy, 16, 0, Math.PI * 2);
        ctx.stroke();
      }

      ctx.fillStyle = isLight ? '#0F172A' : '#F8FAFC';
      ctx.font = 'bold 9px monospace';
      ctx.textAlign = 'center';
      ctx.fillText(v.id, vx, vy + 20);
    });

    // 5. Draw Drone Location (Hovering)
    if (this.layers.droneTrack) {
      const dx = 4 * cs + 14 + (cs - 3)/2;
      const dy = 3 * cs + 14 + (cs - 3)/2;

      ctx.fillStyle = '#00F0FF';
      ctx.beginPath();
      ctx.arc(dx, dy, 6, 0, Math.PI * 2);
      ctx.fill();

      // Rotor blades
      ctx.strokeStyle = '#00F0FF';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(dx - 10, dy - 10); ctx.lineTo(dx + 10, dy + 10);
      ctx.moveTo(dx - 10, dy + 10); ctx.lineTo(dx + 10, dy - 10);
      ctx.stroke();

      ctx.fillStyle = '#00F0FF';
      ctx.font = 'bold 8px monospace';
      ctx.textAlign = 'left';
      ctx.fillText('PHOENIX-01', dx + 12, dy - 2);
    }
  }
};

// Global accessor
window.CommandCenter = CommandCenter;
