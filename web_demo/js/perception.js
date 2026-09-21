// Project Phoenix X - Multi-Spectral Perception & Thermal Fusion Engine

const PerceptionLab = {
  currentScenario: 'wayanad', // 'wayanad', 'earthquake', 'night_smoke'
  overlayMode: 'split', // 'split', 'blend', 'edge'
  splitPos: 50, // percentage (0 - 100)
  blendOpacity: 0.7,
  showBoundingBoxes: true,
  hoverTemp: null,

  // Scenario definitions
  scenarios: {
    wayanad: {
      title: "Wayanad Landslide & Mud Slush",
      ambientTemp: 16.5,
      description: "Severe mud deposits and torrential rain. In RGB, the trapped survivor is camouflaged by brown clay and debris (visibility ~15%). LWIR Thermal (8–14μm) instantly isolates the 36.8°C living body heat.",
      targets: [
        { id: 1, type: 'human', label: 'TRAPPED SURVIVOR', x: 0.46, y: 0.52, w: 0.14, h: 0.22, temp: 36.8, confidence: 96, status: 'CRITICAL (MUD ENTRAPMENT)' },
        { id: 2, type: 'hazard', label: 'UNSTABLE MUD SLIP', x: 0.18, y: 0.35, w: 0.26, h: 0.32, temp: 15.2, confidence: 88, status: 'ACTIVE HAZARD' }
      ]
    },
    earthquake: {
      title: "Earthquake Concrete Slab Collapse",
      ambientTemp: 21.0,
      description: "Structural pancake collapse. Dense shadow under shattered concrete completely blinds standard optical cameras. Radiometric thermal penetration detects trapped casualty emitting 37.1°C radiation.",
      targets: [
        { id: 1, type: 'human', label: 'SURVIVOR IN VOID', x: 0.52, y: 0.48, w: 0.16, h: 0.24, temp: 37.1, confidence: 94, status: 'CONFINED SPACE VOID' },
        { id: 2, type: 'hazard', label: 'STRUCTURAL FAULT', x: 0.72, y: 0.28, w: 0.22, h: 0.45, temp: 22.4, confidence: 91, status: 'SECONDARY COLLAPSE RISK' }
      ]
    },
    night_smoke: {
      title: "Night Smoke & Live 11kV Power Cable",
      ambientTemp: 18.0,
      description: "Zero-lux night conditions with dense billowing smoke from industrial fire. Downed live electrical cable poses fatal risk to ground rescuers. Multi-spectral fusion detects both arcing line (82°C) and casualty.",
      targets: [
        { id: 1, type: 'hazard', label: 'LIVE 11kV WIRE', x: 0.28, y: 0.38, w: 0.32, h: 0.14, temp: 82.5, confidence: 98, status: 'ELECTROCUTION HAZARD' },
        { id: 2, type: 'human', label: 'INJURED CASUALTY', x: 0.68, y: 0.56, w: 0.15, h: 0.24, temp: 36.4, confidence: 92, status: 'CODE RED PRIORITY' }
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

    this.setupListeners();
    this.render();
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

    // Canvas mouse move for pixel temperature inspection
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
    
    // Update scenario button UI
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

  // Ironbow false color converter from Temperature (10°C - 90°C)
  tempToIronbow(temp, minT = 12, maxT = 42) {
    if (temp > 70) minT = 15, maxT = 85; // adapt for high-heat wire
    const t = Math.max(0, Math.min(1, (temp - minT) / (maxT - minT)));

    let r = 0, g = 0, b = 0;
    if (t < 0.2) {
      // Dark to deep violet
      const sub = t / 0.2;
      r = Math.floor(20 * sub);
      g = Math.floor(10 * sub);
      b = Math.floor(75 * sub);
    } else if (t < 0.45) {
      // Violet to magenta/purple
      const sub = (t - 0.2) / 0.25;
      r = Math.floor(20 + 140 * sub);
      g = Math.floor(10 + 20 * sub);
      b = Math.floor(75 + 110 * sub);
    } else if (t < 0.7) {
      // Magenta to fire orange
      const sub = (t - 0.45) / 0.25;
      r = Math.floor(160 + 85 * sub);
      g = Math.floor(30 + 80 * sub);
      b = Math.floor(185 * (1 - sub));
    } else if (t < 0.9) {
      // Fire orange to radiant yellow
      const sub = (t - 0.7) / 0.2;
      r = Math.floor(245 + 10 * sub);
      g = Math.floor(110 + 120 * sub);
      b = Math.floor(20 * sub);
    } else {
      // Yellow to blinding white-hot
      const sub = (t - 0.9) / 0.1;
      r = 255;
      g = Math.floor(230 + 25 * sub);
      b = Math.floor(20 + 235 * sub);
    }
    return `rgb(${r}, ${g}, ${b})`;
  },

  renderRGB(w, h) {
    const ctx = this.ctxRGB;
    ctx.clearRect(0, 0, w, h);

    if (this.currentScenario === 'wayanad') {
      // Wet Mud Slush & Heavy Rains
      const grad = ctx.createLinearGradient(0, 0, w, h);
      grad.addColorStop(0, '#38281f');
      grad.addColorStop(0.5, '#4a3525');
      grad.addColorStop(1, '#2c1e17');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, w, h);

      // Mud flows & boulders
      ctx.fillStyle = '#261b14';
      for (let i = 0; i < 15; i++) {
        ctx.beginPath();
        ctx.arc(60 + (i * 48), 110 + (Math.sin(i) * 60), 22 + (i % 4) * 8, 0, Math.PI * 2);
        ctx.fill();
      }

      // Trapped casualty partially submerged in mud (heavily camouflaged)
      const target = this.scenarios.wayanad.targets[0];
      const tx = target.x * w, ty = target.y * h, tw = target.w * w, th = target.h * h;
      ctx.fillStyle = '#423227'; // Barely distinguishable from mud!
      ctx.beginPath();
      ctx.ellipse(tx + tw/2, ty + th/2, tw/2.2, th/2.4, 0.2, 0, Math.PI * 2);
      ctx.fill();

      // Torrential rain/fog streaks
      ctx.strokeStyle = 'rgba(200, 220, 240, 0.12)';
      ctx.lineWidth = 1.2;
      for (let x = 0; x < w; x += 18) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x - 30, h);
        ctx.stroke();
      }

    } else if (this.currentScenario === 'earthquake') {
      // Shattered concrete slabs and deep dark voids
      ctx.fillStyle = '#1e242d';
      ctx.fillRect(0, 0, w, h);

      // Concrete slabs
      ctx.fillStyle = '#475569';
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 2;
      ctx.fillRect(40, 30, 280, 110);
      ctx.strokeRect(40, 30, 280, 110);

      ctx.fillRect(260, 120, 380, 130);
      ctx.strokeRect(260, 120, 380, 130);

      // Deep dark void (pitch black crevice)
      ctx.fillStyle = '#05070a';
      ctx.beginPath();
      ctx.moveTo(250, 150);
      ctx.lineTo(440, 150);
      ctx.lineTo(400, 270);
      ctx.lineTo(230, 270);
      ctx.closePath();
      ctx.fill();

      // Survivor in deep shadow (imperceptible to RGB camera)
      const target = this.scenarios.earthquake.targets[0];
      ctx.fillStyle = '#11151c'; // Inky dark shadow
      ctx.beginPath();
      ctx.ellipse(target.x * w + (target.w * w)/2, target.y * h + (target.h * h)/2, 28, 35, 0.4, 0, Math.PI * 2);
      ctx.fill();

    } else if (this.currentScenario === 'night_smoke') {
      // Zero-Lux Night with Billowing Smoke & Arcing Wire
      ctx.fillStyle = '#06090e';
      ctx.fillRect(0, 0, w, h);

      // Billowing smoke clouds
      for (let i = 0; i < 12; i++) {
        const radGrad = ctx.createRadialGradient(
          120 + i * 50, 80 + (Math.sin(i) * 70), 10,
          120 + i * 50, 80 + (Math.sin(i) * 70), 75
        );
        radGrad.addColorStop(0, 'rgba(80, 85, 95, 0.55)');
        radGrad.addColorStop(1, 'rgba(10, 12, 16, 0)');
        ctx.fillStyle = radGrad;
        ctx.beginPath();
        ctx.arc(120 + i * 50, 80 + (Math.sin(i) * 70), 75, 0, Math.PI * 2);
        ctx.fill();
      }

      // Downed electrical line (thin black line on dark background)
      ctx.strokeStyle = '#222';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(100, 70);
      ctx.quadraticCurveTo(220, 220, 360, 140);
      ctx.stroke();

      // Casual electric spark in optical
      ctx.fillStyle = '#bae6fd';
      ctx.beginPath();
      ctx.arc(220, 180, 2.5, 0, Math.PI * 2);
      ctx.fill();
    }
  },

  renderThermal(w, h) {
    const ctx = this.ctxThermal;
    ctx.clearRect(0, 0, w, h);

    const sc = this.scenarios[this.currentScenario];

    // Background thermal gradient (ambient cold terrain: 14°C - 20°C in deep purple/blue)
    const bgGrad = ctx.createLinearGradient(0, 0, w, h);
    bgGrad.addColorStop(0, this.tempToIronbow(sc.ambientTemp));
    bgGrad.addColorStop(1, this.tempToIronbow(sc.ambientTemp + 2.5));
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, w, h);

    // Render thermal targets
    sc.targets.forEach(t => {
      const tx = t.x * w;
      const ty = t.y * h;
      const tw = t.w * w;
      const th = t.h * h;

      if (t.type === 'human') {
        // Human Body Heat Gradient (36.8°C white-hot core fading to yellow/orange limbs)
        const rad = ctx.createRadialGradient(tx + tw/2, ty + th/2, 4, tx + tw/2, ty + th/2, Math.max(tw, th)/1.5);
        rad.addColorStop(0, this.tempToIronbow(t.temp)); // 37°C white-hot
        rad.addColorStop(0.4, this.tempToIronbow(t.temp - 1.2)); // 35.6°C yellow
        rad.addColorStop(0.7, this.tempToIronbow(t.temp - 4.5)); // 32.3°C magenta
        rad.addColorStop(1, 'rgba(30, 27, 75, 0)'); // blend to background

        ctx.fillStyle = rad;
        ctx.beginPath();
        ctx.ellipse(tx + tw/2, ty + th/2, tw/1.8, th/1.7, 0.2, 0, Math.PI * 2);
        ctx.fill();

      } else if (t.type === 'hazard') {
        if (t.temp > 50) {
          // Blazing high-temperature electrical arc / fire (82°C+)
          const rad = ctx.createRadialGradient(tx + tw/2, ty + th/2, 2, tx + tw/2, ty + th/2, tw/1.2);
          rad.addColorStop(0, '#ffffff'); // Pure white hot
          rad.addColorStop(0.3, '#fef08a');
          rad.addColorStop(0.6, '#ea580c');
          rad.addColorStop(1, 'rgba(0,0,0,0)');

          ctx.fillStyle = rad;
          ctx.beginPath();
          ctx.arc(tx + tw/2, ty + th/2, tw/1.4, 0, Math.PI * 2);
          ctx.fill();
        } else {
          // Cold mud slip hazard
          ctx.fillStyle = this.tempToIronbow(t.temp);
          ctx.fillRect(tx, ty, tw, th);
        }
      }
    });
  },

  renderFused(w, h) {
    const ctx = this.ctxFused;
    ctx.clearRect(0, 0, w, h);

    if (this.overlayMode === 'split') {
      // Split-Screen Interactive Slider
      const splitX = (this.splitPos / 100) * w;

      // Draw RGB on left slice
      ctx.save();
      ctx.beginPath();
      ctx.rect(0, 0, splitX, h);
      ctx.clip();
      ctx.drawImage(this.canvasRGB, 0, 0);
      ctx.restore();

      // Draw Thermal on right slice
      ctx.save();
      ctx.beginPath();
      ctx.rect(splitX, 0, w - splitX, h);
      ctx.clip();
      ctx.drawImage(this.canvasThermal, 0, 0);
      ctx.restore();

      // Vertical Split Divider Bar
      ctx.strokeStyle = '#ff6b00';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(splitX, 0);
      ctx.lineTo(splitX, h);
      ctx.stroke();

      // Split Knob Icon
      ctx.fillStyle = '#ff6b00';
      ctx.beginPath();
      ctx.arc(splitX, h / 2, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px monospace';
      ctx.fillText("⮂⮃", splitX - 8, h / 2 + 3);

    } else if (this.overlayMode === 'blend') {
      // Alpha-Blend Overlay
      ctx.drawImage(this.canvasRGB, 0, 0);
      ctx.globalAlpha = this.blendOpacity;
      ctx.drawImage(this.canvasThermal, 0, 0);
      ctx.globalAlpha = 1.0;

    } else if (this.overlayMode === 'edge') {
      // Edge High-Pass Fusion (Optical texture + thermal heat signature glow)
      ctx.drawImage(this.canvasThermal, 0, 0);
      ctx.globalCompositeOperation = 'screen';
      ctx.globalAlpha = 0.55;
      ctx.drawImage(this.canvasRGB, 0, 0);
      ctx.globalCompositeOperation = 'source-over';
      ctx.globalAlpha = 1.0;
    }

    // Render Bounding Boxes & Geotags if toggled
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
        const bLen = 8;
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
        ctx.fillRect(tx, ty - 22, tw > 160 ? tw : 160, 20);

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px monospace';
        ctx.fillText(`${t.label} [${t.confidence}%]`, tx + 4, ty - 8);

        // Temperature Badge
        ctx.fillStyle = 'rgba(0, 0, 0, 0.75)';
        ctx.fillRect(tx, ty + th + 4, 90, 16);
        ctx.fillStyle = isHuman ? '#34d399' : '#fbbf24';
        ctx.font = '9px monospace';
        ctx.fillText(`${t.temp}°C | ${t.status.slice(0, 12)}`, tx + 4, ty + th + 15);
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
      const estimatedTemp = sc.ambientTemp + (Math.sin(normX * 10) * 1.5);
      tempValEl.textContent = `${estimatedTemp.toFixed(1)} °C`;
      tempValEl.className = "text-slate-300 font-medium";
      classValEl.textContent = "AMBIENT DEBRIS";
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
