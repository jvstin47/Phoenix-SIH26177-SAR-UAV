// Project Phoenix X — Multispectral Perception Lab (Real Paired Sensor Feeds)

const PerceptionLab = {
  palette: 'ironbow', // 'ironbow', 'whitehot', 'blackhot'
  overlayMode: 'split', // 'split', 'blend', 'edge'
  splitPos: 50,
  blendOpacity: 0.7,
  showTargetMarkers: true,
  inspectTemp: null,

  assets: {},
  imagesLoaded: false,

  init() {
    this.canvasRGB = document.getElementById('canvas-rgb');
    this.ctxRGB = this.canvasRGB ? this.canvasRGB.getContext('2d') : null;

    this.canvasThermal = document.getElementById('canvas-thermal');
    this.ctxThermal = this.canvasThermal ? this.canvasThermal.getContext('2d') : null;

    this.canvasFused = document.getElementById('canvas-fused');
    this.ctxFused = this.canvasFused ? this.canvasFused.getContext('2d') : null;

    this.preloadAssets(() => {
      this.imagesLoaded = true;
      this.setupEventListeners();
      this.render();
    });

    // Subscribe to MissionState
    if (window.MissionState) {
      MissionState.subscribe((state) => {
        if (this.imagesLoaded) this.render();
      });
    }
  },

  preloadAssets(onComplete) {
    let pending = 0;
    const scenarios = Object.keys(MissionState.scenarios);

    scenarios.forEach(key => {
      const sc = MissionState.scenarios[key];

      const imgRGB = new Image();
      imgRGB.src = sc.rgbSrc;
      pending++;
      imgRGB.onload = () => { if (--pending === 0) onComplete(); };
      imgRGB.onerror = () => { if (--pending === 0) onComplete(); };
      this.assets[`${key}_rgb`] = imgRGB;

      const imgThermal = new Image();
      imgThermal.src = sc.thermalSrc;
      pending++;
      imgThermal.onload = () => { if (--pending === 0) onComplete(); };
      imgThermal.onerror = () => { if (--pending === 0) onComplete(); };
      this.assets[`${key}_thermal`] = imgThermal;
    });
  },

  setupEventListeners() {
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

    if (this.canvasFused) {
      this.canvasFused.addEventListener('mousemove', (e) => {
        const rect = this.canvasFused.getBoundingClientRect();
        const scaleX = this.canvasFused.width / rect.width;
        const scaleY = this.canvasFused.height / rect.height;
        const mouseX = (e.clientX - rect.left) * scaleX;
        const mouseY = (e.clientY - rect.top) * scaleY;

        const normX = mouseX / this.canvasFused.width;
        const normY = mouseY / this.canvasFused.height;
        this.inspectSpot(normX, normY);
      });

      this.canvasFused.addEventListener('mouseleave', () => {
        const tempEl = document.getElementById('spot-temp-readout');
        if (tempEl) tempEl.textContent = "--.- °C";
      });

      this.canvasFused.addEventListener('click', (e) => {
        const rect = this.canvasFused.getBoundingClientRect();
        const normX = ((e.clientX - rect.left) * (this.canvasFused.width / rect.width)) / this.canvasFused.width;
        const normY = ((e.clientY - rect.top) * (this.canvasFused.height / rect.height)) / this.canvasFused.height;

        const sc = MissionState.scenarios[MissionState.scenario];
        const tgt = sc.defaultTarget;
        const dist = Math.hypot(normX - tgt.normX, normY - tgt.normY);

        if (dist < 0.2) {
          this.selectCandidate(tgt);
        }
      });
    }
  },

  setScenario(scenarioKey) {
    if (window.MissionState) {
      MissionState.setScenario(scenarioKey);
    }
    this.render();
  },

  setPalette(paletteKey) {
    this.palette = paletteKey;
    document.querySelectorAll('.palette-btn').forEach(btn => {
      btn.classList.remove('border-sky-500', 'text-sky-400');
      btn.classList.add('border-slate-700', 'text-slate-400');
    });
    const active = document.getElementById(`btn-pal-${paletteKey}`);
    if (active) {
      active.classList.add('border-sky-500', 'text-sky-400');
      active.classList.remove('border-slate-700', 'text-slate-400');
    }
    this.render();
  },

  setOverlayMode(modeKey) {
    this.overlayMode = modeKey;
    document.querySelectorAll('.mode-btn').forEach(btn => {
      btn.classList.remove('bg-sky-700', 'text-white', 'border-sky-500');
      btn.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
    });
    const active = document.getElementById(`btn-mode-${modeKey}`);
    if (active) {
      active.classList.add('bg-sky-700', 'text-white', 'border-sky-500');
      active.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');
    }

    const splitP = document.getElementById('split-control-panel');
    const blendP = document.getElementById('blend-control-panel');
    if (splitP && blendP) {
      if (modeKey === 'split') {
        splitP.classList.remove('hidden');
        blendP.classList.add('hidden');
      } else {
        splitP.classList.add('hidden');
        blendP.classList.remove('hidden');
      }
    }
    this.render();
  },

  toggleTargetMarkers() {
    this.showTargetMarkers = !this.showTargetMarkers;
    const btn = document.getElementById('toggle-target-btn');
    if (btn) {
      btn.textContent = this.showTargetMarkers ? "ACTIVE" : "STANDBY";
      btn.className = this.showTargetMarkers 
        ? "tech-chip tech-chip-green cursor-pointer text-[10px]" 
        : "tech-chip cursor-pointer text-[10px]";
    }
    this.render();
  },

  inspectSpot(normX, normY) {
    const sc = MissionState.scenarios[MissionState.scenario];
    const tgt = sc.defaultTarget;
    const dist = Math.hypot(normX - tgt.normX, normY - tgt.normY);

    const tempEl = document.getElementById('spot-temp-readout');
    const classEl = document.getElementById('spot-class-readout');

    if (dist < 0.15) {
      if (tempEl) tempEl.textContent = `${tgt.spotTemp.toFixed(1)} °C`;
      if (classEl) classEl.textContent = `${tgt.label} (BIOLOGICAL LOCK)`;
    } else {
      const ambient = sc.ambientTemp + Math.sin(normX * 12) * 1.4;
      if (tempEl) tempEl.textContent = `${ambient.toFixed(1)} °C`;
      if (classEl) classEl.textContent = "AMBIENT DEBRIS";
    }
  },

  selectCandidate(target) {
    if (typeof playTargetLock === 'function') playTargetLock();
    MissionState.activeTarget = target;
    const modal = document.getElementById('candidate-modal');
    if (modal) modal.classList.remove('hidden');
    MissionState.logEvent('TARGET_SELECTED', `Selected candidate ${target.id} (${target.label}) for ground ray-casting projection.`);
  },

  render() {
    if (!this.imagesLoaded || !this.canvasFused) return;

    const w = 720;
    const h = 430;

    [this.canvasRGB, this.canvasThermal, this.canvasFused].forEach(c => {
      if (c) { c.width = w; c.height = h; }
    });

    const scenarioKey = MissionState.scenario;
    const imgRGB = this.assets[`${scenarioKey}_rgb`];
    const imgThermal = this.assets[`${scenarioKey}_thermal`];

    // 1. Render Optical
    if (this.ctxRGB && imgRGB && imgRGB.complete) {
      this.ctxRGB.drawImage(imgRGB, 0, 0, w, h);
    }

    // 2. Render Thermal with selected palette filter
    if (this.ctxThermal && imgThermal && imgThermal.complete) {
      this.ctxThermal.drawImage(imgThermal, 0, 0, w, h);
      this.applyPaletteFilter(this.ctxThermal, w, h);
    }

    // 3. Render Fused
    if (this.ctxFused && imgRGB && imgThermal) {
      const ctx = this.ctxFused;
      ctx.clearRect(0, 0, w, h);

      if (this.overlayMode === 'split') {
        const splitX = (this.splitPos / 100) * w;

        // Draw Optical on left
        ctx.save();
        ctx.beginPath();
        ctx.rect(0, 0, splitX, h);
        ctx.clip();
        ctx.drawImage(this.canvasRGB, 0, 0);
        ctx.restore();

        // Draw Thermal on right
        ctx.save();
        ctx.beginPath();
        ctx.rect(splitX, 0, w - splitX, h);
        ctx.clip();
        ctx.drawImage(this.canvasThermal, 0, 0);
        ctx.restore();

        // Divider Line
        ctx.strokeStyle = '#4DA3FF';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(splitX, 0);
        ctx.lineTo(splitX, h);
        ctx.stroke();

        // Circular Divider Handle
        ctx.fillStyle = '#101720';
        ctx.beginPath();
        ctx.arc(splitX, h / 2, 12, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#4DA3FF';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = '#EAF0F6';
        ctx.font = 'bold 9px monospace';
        ctx.textAlign = 'center';
        ctx.fillText("⮂⮃", splitX, h / 2 + 3);

      } else if (this.overlayMode === 'blend') {
        ctx.drawImage(this.canvasRGB, 0, 0);
        ctx.globalAlpha = this.blendOpacity;
        ctx.drawImage(this.canvasThermal, 0, 0);
        ctx.globalAlpha = 1.0;

      } else if (this.overlayMode === 'edge') {
        ctx.drawImage(this.canvasThermal, 0, 0);
        ctx.globalCompositeOperation = 'screen';
        ctx.globalAlpha = 0.5;
        ctx.drawImage(this.canvasRGB, 0, 0);
        ctx.globalCompositeOperation = 'source-over';
        ctx.globalAlpha = 1.0;
      }

      // 4. Render Target Markers
      if (this.showTargetMarkers) {
        const sc = MissionState.scenarios[scenarioKey];
        const tgt = sc.defaultTarget;
        const tx = tgt.normX * w;
        const ty = tgt.normY * h;
        const tw = 120;
        const th = 90;

        ctx.strokeStyle = '#FF6B35';
        ctx.lineWidth = 1.5;

        // Precision corner brackets
        const b = 10;
        ctx.beginPath(); ctx.moveTo(tx - tw/2, ty - th/2 + b); ctx.lineTo(tx - tw/2, ty - th/2); ctx.lineTo(tx - tw/2 + b, ty - th/2); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(tx + tw/2 - b, ty - th/2); ctx.lineTo(tx + tw/2, ty - th/2); ctx.lineTo(tx + tw/2, ty - th/2 + b); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(tx - tw/2, ty + th/2 - b); ctx.lineTo(tx - tw/2, ty + th/2); ctx.lineTo(tx - tw/2 + b, ty + th/2); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(tx + tw/2 - b, ty + th/2); ctx.lineTo(tx + tw/2, ty + th/2); ctx.lineTo(tx + tw/2, ty + th/2 - b); ctx.stroke();

        // Label Header
        ctx.fillStyle = 'rgba(16, 23, 32, 0.9)';
        ctx.fillRect(tx - tw/2, ty - th/2 - 18, tw, 16);
        ctx.strokeStyle = '#283544';
        ctx.strokeRect(tx - tw/2, ty - th/2 - 18, tw, 16);

        ctx.fillStyle = '#FF6B35';
        ctx.font = 'bold 9px monospace';
        ctx.textAlign = 'left';
        ctx.fillText(`${tgt.id} | ${tgt.spotTemp}°C`, tx - tw/2 + 4, ty - th/2 - 6);

        // Status Footer
        ctx.fillStyle = 'rgba(16, 23, 32, 0.9)';
        ctx.fillRect(tx - tw/2, ty + th/2 + 2, tw, 15);
        ctx.strokeStyle = '#283544';
        ctx.strokeRect(tx - tw/2, ty + th/2 + 2, tw, 15);

        ctx.fillStyle = '#6BCB9A';
        ctx.font = '8px monospace';
        ctx.fillText("CLICK TO LOCALISE ➔", tx - tw/2 + 4, ty + th/2 + 13);
      }
    }
  },

  applyPaletteFilter(ctx, w, h) {
    if (this.palette === 'ironbow') return; // Default native image

    const imgData = ctx.getImageData(0, 0, w, h);
    const data = imgData.data;

    for (let i = 0; i < data.length; i += 4) {
      // Calculate luminance
      const lum = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
      if (this.palette === 'whitehot') {
        data[i] = lum;
        data[i + 1] = lum;
        data[i + 2] = lum;
      } else if (this.palette === 'blackhot') {
        const inv = 255 - lum;
        data[i] = inv;
        data[i + 1] = inv;
        data[i + 2] = inv;
      }
    }
    ctx.putImageData(imgData, 0, 0);
  }
};

window.PerceptionLab = PerceptionLab;
