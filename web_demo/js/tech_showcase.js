// Project Phoenix X - Core Technologies Showcase: Dual-Brain, 17-Byte LoRa Packer & Dijkstra GCS

const LoRaPacker = {
  lat: 11.581240,
  lon: 76.128450,
  alt: 28.4,
  triage: 1, // 0: Green, 1: Red (Critical), 2: Yellow
  confidence: 94,
  battery: 78,
  heading: 124,

  init() {
    this.updateDisplay();
  },

  updateFromRayCast(lat, lon, triage = 1) {
    this.lat = lat;
    this.lon = lon;
    this.triage = triage;
    this.updateDisplay();
  },

  // Packs fields into exact 17-byte buffer as per Souli et al. (2024)
  serialize() {
    const buffer = new ArrayBuffer(17);
    const view = new DataView(buffer);

    // Byte 0: Protocol Header (0x50 = 'P' for Phoenix)
    view.setUint8(0, 0x50);

    // Bytes 1-4: Latitude (Float32)
    view.setFloat32(1, this.lat, false); // Big endian

    // Bytes 5-8: Longitude (Float32)
    view.setFloat32(5, this.lon, false);

    // Bytes 9-10: Altitude in decimeters (Int16)
    view.setInt16(9, Math.round(this.alt * 10), false);

    // Byte 11: Bit-packed Triage (2 bits) + TargetType (2 bits) + Conf (4 bits)
    const triageBits = (this.triage & 0x03) << 6;
    const typeBits = (0 & 0x03) << 4; // 0 = human
    const confBits = Math.min(15, Math.floor(this.confidence / 6.66)) & 0x0F;
    view.setUint8(11, triageBits | typeBits | confBits);

    // Byte 12: Battery percentage (Uint8)
    view.setUint8(12, Math.round(this.battery));

    // Bytes 13-14: Heading in centidegrees (Uint16)
    view.setUint16(13, Math.round(this.heading * 100), false);

    // Bytes 15-16: HMAC Checksum (Uint16)
    const dummyChecksum = ((Math.round(this.lat * 1000) ^ Math.round(this.lon * 1000)) & 0xFFFF);
    view.setUint16(15, dummyChecksum, false);

    return new Uint8Array(buffer);
  },

  updateDisplay() {
    const bytes = this.serialize();
    let hexString = "";
    let binaryHtml = "";

    const byteLabels = [
      "Header (0x50)",
      "Lat[0]", "Lat[1]", "Lat[2]", "Lat[3]",
      "Lon[0]", "Lon[1]", "Lon[2]", "Lon[3]",
      "Alt[0]", "Alt[1]",
      "Triage/Conf",
      "Battery%",
      "Hdg[0]", "Hdg[1]",
      "HMAC[0]", "HMAC[1]"
    ];

    bytes.forEach((b, i) => {
      const hex = b.toString(16).padStart(2, '0').toUpperCase();
      hexString += hex + " ";
      
      const bin = b.toString(2).padStart(8, '0');
      binaryHtml += `
        <div class="inline-block p-1 m-1 bg-slate-900 border border-slate-700 rounded text-center text-xs">
          <div class="text-[9px] text-cyan-400 font-bold">${byteLabels[i]}</div>
          <div class="text-amber-300 font-mono font-bold">${hex}</div>
          <div class="text-[8px] text-slate-400 font-mono">${bin}</div>
        </div>
      `;
    });

    const hexEl = document.getElementById('lora-hex-string');
    const binContainer = document.getElementById('lora-bytes-container');
    if (hexEl) hexEl.textContent = hexString.trim();
    if (binContainer) binContainer.innerHTML = binaryHtml;
  }
};

// --- Tactical GCS & Dijkstra Safe Route Planner ---
const TacticalGCS = {
  canvas: null,
  ctx: null,

  gridSize: 8,
  cellSize: 45,
  start: { x: 0, y: 0, label: "BASE CAMP (NDRF)" },
  victim: { x: 6, y: 5, label: "SURVIVOR #1 [RED]" },
  
  hazards: [
    { x: 3, y: 1, type: 'wire', label: 'LIVE 11kV CABLE' },
    { x: 3, y: 2, type: 'wire', label: 'LIVE 11kV CABLE' },
    { x: 2, y: 4, type: 'fire', label: 'STRUCTURAL FIRE' },
    { x: 3, y: 4, type: 'fire', label: 'STRUCTURAL FIRE' },
    { x: 4, y: 4, type: 'fire', label: 'STRUCTURAL FIRE' },
    { x: 5, y: 2, type: 'flood', label: 'DEEP WATER' }
  ],

  path: [],

  init() {
    this.canvas = document.getElementById('canvas-gcs');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.calculateDijkstra();
    this.draw();
  },

  calculateDijkstra() {
    // Dijkstra / BFS grid pathfinding avoiding hazards
    const cols = this.gridSize;
    const rows = this.gridSize;
    const isHazard = (x, y) => this.hazards.some(h => h.x === x && h.y === y);

    const queue = [[this.start.x, this.start.y]];
    const visited = new Set();
    const parent = {};
    visited.add(`${this.start.x},${this.start.y}`);

    let found = false;

    while (queue.length > 0) {
      const [cx, cy] = queue.shift();
      if (cx === this.victim.x && cy === this.victim.y) {
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

    // Reconstruct path
    this.path = [];
    if (found) {
      let curr = [this.victim.x, this.victim.y];
      while (curr) {
        this.path.unshift(curr);
        const pKey = `${curr[0]},${curr[1]}`;
        curr = parent[pKey];
      }
    }
  },

  draw() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    ctx.clearRect(0, 0, w, h);

    const cs = this.cellSize;

    // Draw Grid Cells
    for (let x = 0; x < this.gridSize; x++) {
      for (let y = 0; y < this.gridSize; y++) {
        const px = x * cs + 20;
        const py = y * cs + 20;

        ctx.fillStyle = '#0f172a';
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
        ctx.fillStyle = 'rgba(234, 88, 12, 0.8)'; // Amber
      } else if (hz.type === 'fire') {
        ctx.fillStyle = 'rgba(239, 68, 68, 0.85)'; // Red
      } else {
        ctx.fillStyle = 'rgba(59, 130, 246, 0.85)'; // Blue
      }
      ctx.fillRect(px, py, cs - 3, cs - 3);

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 8px monospace';
      ctx.fillText(hz.type.toUpperCase(), px + 4, py + 24);
    });

    // Draw Dijkstra Path
    if (this.path.length > 1) {
      ctx.strokeStyle = '#10b981'; // Emerald route
      ctx.lineWidth = 4;
      ctx.beginPath();
      this.path.forEach((pt, i) => {
        const px = pt[0] * cs + 20 + (cs / 2);
        const py = pt[1] * cs + 20 + (cs / 2);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      });
      ctx.stroke();

      // Waypoint dots
      ctx.fillStyle = '#34d399';
      this.path.forEach(pt => {
        const px = pt[0] * cs + 20 + (cs / 2);
        const py = pt[1] * cs + 20 + (cs / 2);
        ctx.beginPath();
        ctx.arc(px, py, 4, 0, Math.PI * 2);
        ctx.fill();
      });
    }

    // Base Camp marker
    const bx = this.start.x * cs + 20 + (cs / 2);
    const by = this.start.y * cs + 20 + (cs / 2);
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(bx, by, 8, 0, Math.PI * 2);
    ctx.fill();

    // Victim marker
    const vx = this.victim.x * cs + 20 + (cs / 2);
    const vy = this.victim.y * cs + 20 + (cs / 2);
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(vx, vy, 9, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }
};
