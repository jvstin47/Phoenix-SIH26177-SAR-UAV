// Project Phoenix X - Multi-Spectral Perception & Thermal Fusion Engine (REAL IMAGERY)

const PerceptionLab = {
  currentScenario: 'wayanad', // 'wayanad', 'earthquake', 'night_smoke'
  overlayMode: 'split', // 'split', 'blend', 'edge'
  splitPos: 50, // percentage (0 - 100)
  blendOpacity: 0.7,
  showBoundingBoxes: true,
  imagesLoaded: false,

  // Cache loaded Image objects
  assets: {},

  // Scenario definitions with real image paths and target ground truth coordinates
  scenarios: {
    wayanad: {
      title: "Wayanad Landslide & Mud Slush (Western Ghats, India)",
      ambientTemp: 15.0,
      description: "Severe torrential mudflow and clay deposits. In 4K Optical RGB, the mud-soaked survivor is virtually camouflaged in the reddish-brown clay. Radiometric LWIR Thermal (8–14μm) penetrates the moisture layer and isolates the living 37.0°C body heat.",
      rgbSrc: "images/wayanad_rgb.jpg",
      thermalSrc: "images/wayanad_thermal.jpg",
      targets: [
        { id: 1, type: 'human', label: 'MUD-COVERED CASUALTY', x: 0.45, y: 0.50, w: 0.22, h: 0.35, temp: 37.0, confidence: 96, status: 'SURVIVOR ALIVE' },
        { id: 2, type: 'hazard', label: 'UNSTABLE MUD ESCARPMENT', x: 0.15, y: 0.20, w: 0.35, h: 0.30, temp: 14.8, confidence: 89, status: 'SLIP RISK' }
      ]
    },
    earthquake: {
      title: "Earthquake Structural Pancake Collapse",
      ambientTemp: 16.0,
      description: "Massive concrete slab collapse in urban disaster zone. Deep shadow and fractured masonry create total optical blindness. Long-Wave Infrared detects the survivor pinned beneath the slab emitting 36.8°C thermal radiation.",
      rgbSrc: "images/earthquake_rgb.jpg",
      thermalSrc: "images/earthquake_thermal.jpg",
      targets: [
        { id: 1, type: 'human', label: 'TRAPPED SURVIVOR', x: 0.28, y: 0.52, w: 0.28, h: 0.28, temp: 36.8, confidence: 94, status: 'ALIVE / CONFINED VOID' }
      ]
    },
    night_smoke: {
      title: "Zero-Lux Night Smoke & Live 11kV Power Line",
      ambientTemp: 16.0,
      description: "Post-disaster structural collapse at night with dense particulate smoke plumes. Standard cameras are completely blinded. LWIR thermal cuts through the smoke, detecting both an arcing high-voltage cable (85°C) and an injured victim (36.8°C).",
      rgbSrc: "images/night_smoke_rgb.jpg",
      thermalSrc: "images/night_smoke_thermal.jpg",
      targets: [
        { id: 1, type: 'hazard', label: 'ARCING 11kV CABLE', x: 0.22, y: 0.22, w: 0.65, h: 0.30, temp: 85.0, confidence: 98, status: 'ELECTROCUTION HAZARD' },
        { id: 2, type: 'human', label: 'COLLAPSED SURVIVOR', x: 0.35, y: 0.70, w: 0.45, h: 0.22, temp: 36.8, confidence: 92, status: 'CODE RED INJURED' }
      ]
    }
  },

  init() {
    this.canvasRGB = document.getElementById('canvas-rgb');
    this.ctxRGB = this.canvasRGB.getContext('2d');
    
    this.canvasThermal = document.getElementById('canvas-thermal');
    this.ctxThermal = this.canvasThermal.getContext('2d');
    
    this.canvasFused = document.getElementById('canvas-fused');
    this.ctxFused = this.canvasFused.getContext('2d');

    this.preloadAllImages(() => {
      this.setupListeners();
      this.render();
    });
  },

  preloadAllImages(onComplete) {
    let pending = 0;
    const scenarios = Object.keys(this.scenarios);

    scenarios.forEach(key => {
      const sc = this.scenarios[key];
      
      const imgRGB = new Image();
      imgRGB.src = sc.rgbSrc;
      pending++;
      imgRGB.onload = () => { if (--pending === 0) onComplete(); };
      this.assets[`${key}_rgb`] = imgRGB;

      const imgThermal = new Image();
      imgThermal.src = sc.thermalSrc;
      pending++;
      imgThermal.onload = () => { if (--pending === 0) onComplete(); };
      this.assets[`${key}_thermal`] = imgThermal;
    });
  },

  setupListeners() {
    const slider = document.getElementById('split-slider');
    if (slider) {
      slider.addEventListener('input', (e) => {
        this.splitPos = parseFloat(e.target.value);
        this.render();
      });
    }

    const blendSlider = document.getElementById('blend-slider');
    if (blendSlider) {
      blendSlider.addEventListener('input', (e) => {
        this.blendOpacity = parseFloat(e.target.value) / 100;
        this.render();
      });
    }

    // Mouse move for pixel temperature inspection
    this.canvasFused.addEventListener('mousemove', (e) => {
      const rect = this.canvasFused.getBoundingClientRect();
      const scaleX = this.canvasFused.width / rect.width;
      const scaleY = this.canvasFused.height / rect.height;
      const mouseX = (e.clientX - rect.left) * scaleX;
      const mouseY = (e.clientY - rect.top) * scaleY;
      
      const normX = mouseX / this.canvasFused.width;
      const normY = mouseY / this.canvasFused.height;

      this.inspectPixel(normX, normY);
    });

    this.canvasFused.addEventListener('mouseleave', () => {
      document.getElementById('hover-temp-val').textContent = "--.- °C";
      document.getElementById('hover-class-val').textContent = "STANDBY";
    });
  },

  setScenario(name) {
    this.currentScenario = name;
    
    document.querySelectorAll('.scenario-btn').forEach(b => {
      b.classList.remove('bg-cyan-600', 'text-white', 'border-cyan-400');
      b.classList.add('bg-slate-800', 'text-slate-300');
    });
    const activeBtn = document.getElementById(`btn-scen-${name}`);
    if (activeBtn) {
      activeBtn.classList.add('bg-cyan-600', 'text-white', 'border-cyan-400');
      activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
    }

    const sc = this.scenarios[name];
    document.getElementById('scenario-desc-title').textContent = sc.title;
    document.getElementById('scenario-desc-text').textContent = sc.description;
    
    if (typeof playTargetLock === 'function') playTargetLock();
    this.render();
  },

  setOverlayMode(mode) {
    this.overlayMode = mode;
    document.querySelectorAll('.mode-btn').forEach(b => {
      b.classList.remove('bg-orange-600', 'text-white', 'border-orange-400');
      b.classList.add('bg-slate-800', 'text-slate-300');
    });
    const activeBtn = document.getElementById(`btn-mode-${mode}`);
    if (activeBtn) {
      activeBtn.classList.add('bg-orange-600', 'text-white', 'border-orange-400');
      activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
    }

    const splitControl = document.getElementById('split-control-panel');
    const blendControl = document.getElementById('blend-control-panel');
    if (mode === 'split') {
      splitControl.classList.remove('hidden');
      blendControl.classList.add('hidden');
    } else {
      splitControl.classList.add('hidden');
      blendControl.classList.remove('hidden');
    }

    this.render();
  },

  toggleBoundingBoxes() {
    this.showBoundingBoxes = !this.showBoundingBoxes;
    const btn = document.getElementById('toggle-bbox-btn');
    if (this.showBoundingBoxes) {
      btn.textContent = "AI BOUNDING BOXES: ON";
      btn.classList.add('text-emerald-400', 'border-emerald-500');
    } else {
      btn.textContent = "AI BOUNDING BOXES: OFF";
      btn.classList.remove('text-emerald-400', 'border-emerald-500');
    }
    this.render();
  },

  renderRGB(w, h) {
    const ctx = this.ctxRGB;
    ctx.clearRect(0, 0, w, h);
    const img = this.assets[`${this.currentScenario}_rgb`];
    if (img && img.complete) {
      ctx.drawImage(img, 0, 0, w, h);
    }
  },

  renderThermal(w, h) {
    const ctx = this.ctxThermal;
    ctx.clearRect(0, 0, w, h);
    const img = this.assets[`${this.currentScenario}_thermal`];
    if (img && img.complete) {
      ctx.drawImage(img, 0, 0, w, h);
    }
  },

  renderFused(w, h) {
    const ctx = this.ctxFused;
    ctx.clearRect(0, 0, w, h);

    const imgRGB = this.assets[`${this.currentScenario}_rgb`];
    const imgThermal = this.assets[`${this.currentScenario}_thermal`];

    if (!imgRGB || !imgThermal) return;

    if (this.overlayMode === 'split') {
      // Split-Screen Interactive Slider
      const splitX = (this.splitPos / 100) * w;

      // Draw RGB on left slice
      ctx.save();
      ctx.beginPath();
      ctx.rect(0, 0, splitX, h);
      ctx.clip();
      ctx.drawImage(imgRGB, 0, 0, w, h);
      ctx.restore();

      // Draw Thermal on right slice
      ctx.save();
      ctx.beginPath();
      ctx.rect(splitX, 0, w - splitX, h);
      ctx.clip();
      ctx.drawImage(imgThermal, 0, 0, w, h);
      ctx.restore();

      // Divider Line & Knob
      ctx.strokeStyle = '#ff6b00';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(splitX, 0);
      ctx.lineTo(splitX, h);
      ctx.stroke();

      ctx.fillStyle = '#ff6b00';
      ctx.beginPath();
      ctx.arc(splitX, h / 2, 16, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px monospace';
      ctx.fillText("⮂⮃", splitX - 9, h / 2 + 4);

    } else if (this.overlayMode === 'blend') {
      // Alpha-Blend Overlay
      ctx.drawImage(imgRGB, 0, 0, w, h);
      ctx.globalAlpha = this.blendOpacity;
      ctx.drawImage(imgThermal, 0, 0, w, h);
      ctx.globalAlpha = 1.0;

    } else if (this.overlayMode === 'edge') {
      // Edge High-Pass Fusion (Contour superimposition)
      ctx.drawImage(imgThermal, 0, 0, w, h);
      ctx.globalCompositeOperation = 'screen';
      ctx.globalAlpha = 0.55;
      ctx.drawImage(imgRGB, 0, 0, w, h);
      ctx.globalCompositeOperation = 'source-over';
      ctx.globalAlpha = 1.0;
    }

    // Render Bounding Boxes & Geotags if enabled
    if (this.showBoundingBoxes) {
      const sc = this.scenarios[this.currentScenario];
      sc.targets.forEach(t => {
        const tx = t.x * w;
        const ty = t.y * h;
        const tw = t.w * w;
        const th = t.h * h;

        const isHuman = t.type === 'human';
        const color = isHuman ? '#10b981' : '#f59e0b'; // Emerald for survivor, Amber for hazard

        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.strokeRect(tx, ty, tw, th);

        // Corner brackets
        const bLen = 10;
        ctx.lineWidth = 3;
        // Top-left
        ctx.beginPath(); ctx.moveTo(tx, ty + bLen); ctx.lineTo(tx, ty); ctx.lineTo(tx + bLen, ty); ctx.stroke();
        // Top-right
        ctx.beginPath(); ctx.moveTo(tx + tw - bLen, ty); ctx.lineTo(tx + tw, ty); ctx.lineTo(tx + tw, ty + bLen); ctx.stroke();
        // Bottom-left
        ctx.beginPath(); ctx.moveTo(tx, ty + th - bLen); ctx.lineTo(tx, ty + th); ctx.lineTo(tx + bLen, ty + th); ctx.stroke();
        // Bottom-right
        ctx.beginPath(); ctx.moveTo(tx + tw - bLen, ty + th); ctx.lineTo(tx + tw, ty + th); ctx.lineTo(tx + tw, ty + th - bLen); ctx.stroke();

        // Label Tag Box
        ctx.fillStyle = isHuman ? 'rgba(16, 185, 129, 0.9)' : 'rgba(245, 158, 11, 0.9)';
        const labelW = Math.max(tw, 160);
        ctx.fillRect(tx, ty - 22, labelW, 20);

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px monospace';
        ctx.fillText(`${t.label} [${t.confidence}%]`, tx + 4, ty - 8);

        // Temperature Badge
        ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
        ctx.fillRect(tx, ty + th + 4, 110, 16);
        ctx.fillStyle = isHuman ? '#34d399' : '#fbbf24';
        ctx.font = '9px monospace';
        ctx.fillText(`${t.temp}°C | ${t.status.slice(0, 14)}`, tx + 4, ty + th + 15);
      });
    }
  },

  inspectPixel(normX, normY) {
    const sc = this.scenarios[this.currentScenario];
    let detectedTarget = null;

    sc.targets.forEach(t => {
      if (normX >= t.x && normX <= (t.x + t.w) && normY >= t.y && normY <= (t.y + t.h)) {
        detectedTarget = t;
      }
    });

    const tempValEl = document.getElementById('hover-temp-val');
    const classValEl = document.getElementById('hover-class-val');

    if (detectedTarget) {
      tempValEl.textContent = `${detectedTarget.temp.toFixed(1)} °C`;
      tempValEl.className = detectedTarget.type === 'human' ? "text-emerald-400 font-bold" : "text-amber-400 font-bold";
      classValEl.textContent = `${detectedTarget.label} (${detectedTarget.confidence}%)`;
    } else {
      const estimatedTemp = sc.ambientTemp + (Math.sin(normX * 8) * 1.2);
      tempValEl.textContent = `${estimatedTemp.toFixed(1)} °C`;
      tempValEl.className = "text-slate-300 font-medium";
      classValEl.textContent = "AMBIENT TERRAIN";
    }
  },

  render() {
    const w = 700;
    const h = 420;

    [this.canvasRGB, this.canvasThermal, this.canvasFused].forEach(c => {
      c.width = w;
      c.height = h;
    });

    this.renderRGB(w, h);
    this.renderThermal(w, h);
    this.renderFused(w, h);
  }
};
