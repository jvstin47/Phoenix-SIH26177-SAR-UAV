// Project Phoenix X - Drone Operator FPV HUD & Tait-Bryan Ray-Caster Engine (Clean Defense OSD)

const OperatorHUD = {
  pitch: -2.5, // degrees
  roll: 1.8,   // degrees
  yaw: 124.0,  // degrees heading
  altitudeAGL: 28.4, // meters from Downward LiDAR (MS5611 + ToF)
  uavLat: 11.58124, // Wayanad reference coords
  uavLon: 76.12845,
  focalLength: 520, // camera intrinsic fx, fy (pixels)
  
  lockedTarget: null,
  bgImage: null,

  init() {
    this.canvas = document.getElementById('canvas-hud');
    this.ctx = this.canvas.getContext('2d');
    
    // Load real disaster camera feed for FPV cockpit background
    this.bgImage = new Image();
    this.bgImage.src = 'images/earthquake_rgb.jpg';
    this.bgImage.onload = () => {
      this.drawHUD();
    };

    this.setupListeners();
    this.startLoop();
  },

  setupListeners() {
    this.canvas.addEventListener('click', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const scaleX = this.canvas.width / rect.width;
      const scaleY = this.canvas.height / rect.height;
      const clickX = (e.clientX - rect.left) * scaleX;
      const clickY = (e.clientY - rect.top) * scaleY;

      this.executeRayCast(clickX, clickY);
    });

    const pitchSlider = document.getElementById('hud-pitch-slider');
    if (pitchSlider) {
      pitchSlider.addEventListener('input', (e) => {
        this.pitch = parseFloat(e.target.value);
        document.getElementById('hud-pitch-val').textContent = `${this.pitch.toFixed(1)}°`;
      });
    }

    const rollSlider = document.getElementById('hud-roll-slider');
    if (rollSlider) {
      rollSlider.addEventListener('input', (e) => {
        this.roll = parseFloat(e.target.value);
        document.getElementById('hud-roll-val').textContent = `${this.roll.toFixed(1)}°`;
      });
    }

    const altSlider = document.getElementById('hud-alt-slider');
    if (altSlider) {
      altSlider.addEventListener('input', (e) => {
        this.altitudeAGL = parseFloat(e.target.value);
        document.getElementById('hud-alt-val').textContent = `${this.altitudeAGL.toFixed(1)}m`;
      });
    }
  },

  executeRayCast(u, v) {
    const w = this.canvas.width;
    const h = this.canvas.height;
    const cx = w / 2;
    const cy = h / 2;

    // Step 1: Pinhole Ray Unprojection
    const fx = this.focalLength;
    const fy = this.focalLength;
    const rCx = (u - cx) / fx;
    const rCy = (v - cy) / fy;
    const rCz = 1.0;

    // Step 2: Tait-Bryan Rotation Transformation (Pitch theta, Yaw psi)
    const theta = (this.pitch * Math.PI) / 180;
    const psi = (this.yaw * Math.PI) / 180;

    const groundDistanceZ = this.altitudeAGL;
    const offsetX = (rCx / rCz) * groundDistanceZ + (Math.tan(theta) * groundDistanceZ);
    const offsetY = (rCy / rCz) * groundDistanceZ;

    // Step 3: WGS-84 Geodetic Coordinate Conversion
    const deltaLat = (offsetX * Math.cos(psi) - offsetY * Math.sin(psi)) / 111320;
    const deltaLon = (offsetX * Math.sin(psi) + offsetY * Math.cos(psi)) / (111320 * Math.cos((this.uavLat * Math.PI) / 180));

    const targetLat = this.uavLat + deltaLat;
    const targetLon = this.uavLon + deltaLon;

    this.lockedTarget = {
      u, v,
      lat: targetLat,
      lon: targetLon,
      distance: Math.sqrt(offsetX * offsetX + offsetY * offsetY + groundDistanceZ * groundDistanceZ),
      errorMargin: (0.075 * groundDistanceZ).toFixed(1)
    };

    document.getElementById('raycast-pixel').textContent = `[u: ${Math.round(u)}, v: ${Math.round(v)}]`;
    document.getElementById('raycast-coords').textContent = `${targetLat.toFixed(6)}° N, ${targetLon.toFixed(6)}° E`;
    document.getElementById('raycast-dist').textContent = `${this.lockedTarget.distance.toFixed(1)} m`;
    document.getElementById('raycast-err').textContent = `± ${this.lockedTarget.errorMargin} m (SEP 95%)`;

    if (typeof playRaycastLaser === 'function') playRaycastLaser();
    if (typeof playLoraBurst === 'function') setTimeout(playLoraBurst, 250);

    if (typeof LoRaPacker !== 'undefined' && LoRaPacker.updateFromRayCast) {
      LoRaPacker.updateFromRayCast(targetLat, targetLon, 1);
    }
  },

  drawHUD() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const cx = w / 2;
    const cy = h / 2;

    ctx.clearRect(0, 0, w, h);

    // 1. Draw Real Drone Camera Background
    if (this.bgImage && this.bgImage.complete) {
      ctx.drawImage(this.bgImage, 0, 0, w, h);
      ctx.fillStyle = 'rgba(10, 14, 20, 0.25)';
      ctx.fillRect(0, 0, w, h);
    } else {
      ctx.fillStyle = '#0a0e14';
      ctx.fillRect(0, 0, w, h);
    }

    // 2. Artificial Horizon Ladder (Clean White/Muted Cyan Aviation Standard)
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate((-this.roll * Math.PI) / 180);

    const pitchOffset = this.pitch * 3.5;

    ctx.strokeStyle = 'rgba(241, 245, 249, 0.75)';
    ctx.lineWidth = 1.2;

    // Horizon line with central gap
    ctx.beginPath();
    ctx.moveTo(-90, pitchOffset);
    ctx.lineTo(-25, pitchOffset);
    ctx.moveTo(25, pitchOffset);
    ctx.lineTo(90, pitchOffset);
    ctx.stroke();

    // Pitch rungs (+10, -10)
    [-20, -10, 10, 20].forEach(deg => {
      const yPos = pitchOffset - (deg * 3.5);
      const isNeg = deg < 0;
      if (isNeg) ctx.setLineDash([4, 4]);
      else ctx.setLineDash([]);

      ctx.beginPath();
      ctx.moveTo(-35, yPos);
      ctx.lineTo(-15, yPos);
      ctx.moveTo(15, yPos);
      ctx.lineTo(35, yPos);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = 'rgba(241, 245, 249, 0.75)';
      ctx.font = '8px monospace';
      ctx.textAlign = 'right';
      ctx.fillText(`${deg}°`, -40, yPos + 3);
      ctx.textAlign = 'left';
      ctx.fillText(`${deg}°`, 40, yPos + 3);
    });

    ctx.restore();

    // 3. Center Aircraft Reticle (Clean Military Gun Crosshair)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.arc(cx, cy, 5, 0, Math.PI * 2);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(cx - 16, cy); ctx.lineTo(cx - 8, cy);
    ctx.moveTo(cx + 8, cy); ctx.lineTo(cx + 16, cy);
    ctx.moveTo(cx, cy - 16); ctx.lineTo(cx, cy - 8);
    ctx.moveTo(cx, cy + 8); ctx.lineTo(cx, cy + 16);
    ctx.stroke();

    // 4. Heading Tape (Top Bar)
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.fillRect(cx - 140, 8, 280, 24);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.strokeRect(cx - 140, 8, 280, 24);

    ctx.fillStyle = '#f8fafc';
    ctx.font = '10px monospace';
    ctx.textAlign = 'center';
    ctx.fillText(`HDG: ${Math.round(this.yaw)}°  |  VIO-HEADING: STABLE`, cx, 24);

    // 5. Left Tape: Ground Speed (12.4 m/s)
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.fillRect(12, cy - 65, 45, 130);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.strokeRect(12, cy - 65, 45, 130);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '9px monospace';
    ctx.textAlign = 'center';
    ctx.fillText("GND SPD", 34, cy - 45);
    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 12px monospace';
    ctx.fillText("12.4", 34, cy);
    ctx.font = '8px monospace';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText("m/s", 34, cy + 14);

    // Right Tape: LiDAR Altitude AGL
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.fillRect(w - 57, cy - 65, 45, 130);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.strokeRect(w - 57, cy - 65, 45, 130);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '9px monospace';
    ctx.textAlign = 'center';
    ctx.fillText("ALT AGL", w - 34, cy - 45);
    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 12px monospace';
    ctx.fillText(`${this.altitudeAGL.toFixed(1)}`, w - 34, cy);
    ctx.font = '8px monospace';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText("m", w - 34, cy + 14);

    // 6. Draw Target Lock Reticle if Selected
    if (this.lockedTarget) {
      const tx = this.lockedTarget.u;
      const ty = this.lockedTarget.v;

      // Clean military target box
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.arc(tx, ty, 14, 0, Math.PI * 2);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(tx - 20, ty); ctx.lineTo(tx + 20, ty);
      ctx.moveTo(tx, ty - 20); ctx.lineTo(tx, ty + 20);
      ctx.stroke();

      // Slant line
      ctx.strokeStyle = 'rgba(16, 185, 129, 0.6)';
      ctx.lineWidth = 1;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(tx, ty);
      ctx.stroke();
      ctx.setLineDash([]);

      // Coordinate Tag
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.strokeStyle = '#10b981';
      ctx.fillRect(tx + 18, ty - 20, 165, 42);
      ctx.strokeRect(tx + 18, ty - 20, 165, 42);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '9px monospace';
      ctx.textAlign = 'left';
      ctx.fillText(`GEO-LOCK: WGS-84`, tx + 24, ty - 8);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`${this.lockedTarget.lat.toFixed(6)}° N, ${this.lockedTarget.lon.toFixed(6)}° E`, tx + 24, ty + 6);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`SEP (95%): ±${this.lockedTarget.errorMargin}m`, tx + 24, ty + 18);
    }
  },

  startLoop() {
    const loop = () => {
      this.pitch += Math.sin(Date.now() / 700) * 0.015;
      this.roll += Math.cos(Date.now() / 900) * 0.01;
      this.drawHUD();
      requestAnimationFrame(loop);
    };
    loop();
  }
};
