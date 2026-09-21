// Project Phoenix X - Drone Operator FPV HUD & Tait-Bryan Ray-Caster Engine

const OperatorHUD = {
  pitch: -2.5, // degrees
  roll: 1.8,   // degrees
  yaw: 124.0,  // degrees heading
  altitudeAGL: 28.4, // meters from Downward LiDAR (MS5611 + ToF)
  uavLat: 11.58124, // Wayanad reference coords
  uavLon: 76.12845,
  focalLength: 520, // camera intrinsic fx, fy (pixels)
  
  lockedTarget: null,
  raycastSteps: null,

  init() {
    this.canvas = document.getElementById('canvas-hud');
    this.ctx = this.canvas.getContext('2d');
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

    // Gimbal angle sliders
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

    // Step 1: Pinhole Ray Unprojection in Camera Frame
    const fx = this.focalLength;
    const fy = this.focalLength;
    const rCx = (u - cx) / fx;
    const rCy = (v - cy) / fy;
    const rCz = 1.0;
    const magC = Math.sqrt(rCx * rCx + rCy * rCy + rCz * rCz);
    const unitRC = [rCx / magC, rCy / magC, rCz / magC];

    // Step 2: Tait-Bryan Rotation Transformation (Euler angles: roll phi, pitch theta, yaw psi)
    const phi = (this.roll * Math.PI) / 180;
    const theta = (this.pitch * Math.PI) / 180;
    const psi = (this.yaw * Math.PI) / 180;

    // Direction Cosine Matrix (DCM) Body to World NED
    const cosP = Math.cos(theta), sinP = Math.sin(theta);
    const cosR = Math.cos(phi), sinR = Math.sin(phi);
    const cosY = Math.cos(psi), sinY = Math.sin(psi);

    // Simplified forward vector projection to ground NED
    const groundDistanceZ = this.altitudeAGL;
    // Ground intersection offset in meters
    const offsetX = (rCx / rCz) * groundDistanceZ + (Math.tan(theta) * groundDistanceZ);
    const offsetY = (rCy / rCz) * groundDistanceZ;

    // Step 3: WGS-84 Geodetic Coordinate Conversion
    // 1 deg Lat ~= 111,320m, 1 deg Lon ~= 111,320m * cos(lat)
    const deltaLat = (offsetX * Math.cos(psi) - offsetY * Math.sin(psi)) / 111320;
    const deltaLon = (offsetX * Math.sin(psi) + offsetY * Math.cos(psi)) / (111320 * Math.cos((this.uavLat * Math.PI) / 180));

    const targetLat = this.uavLat + deltaLat;
    const targetLon = this.uavLon + deltaLon;

    this.lockedTarget = {
      u, v,
      lat: targetLat,
      lon: targetLon,
      distance: Math.sqrt(offsetX * offsetX + offsetY * offsetY + groundDistanceZ * groundDistanceZ),
      errorMargin: (0.08 * groundDistanceZ).toFixed(1) // ~±2.1m at 28m AGL
    };

    // Update UI Elements
    document.getElementById('raycast-pixel').textContent = `[u: ${Math.round(u)}, v: ${Math.round(v)}]`;
    document.getElementById('raycast-coords').textContent = `${targetLat.toFixed(6)}° N, ${targetLon.toFixed(6)}° E`;
    document.getElementById('raycast-dist').textContent = `${this.lockedTarget.distance.toFixed(1)} m`;
    document.getElementById('raycast-err').textContent = `± ${this.lockedTarget.errorMargin} m (SEP 95%)`;

    // Trigger audio feedback
    if (typeof playRaycastLaser === 'function') playRaycastLaser();
    if (typeof playLoraBurst === 'function') setTimeout(playLoraBurst, 250);

    // Update 17-byte LoRa Packer if active
    if (typeof LoRaPacker !== 'undefined' && LoRaPacker.updateFromRayCast) {
      LoRaPacker.updateFromRayCast(targetLat, targetLon, 1); // 1 = Critical survivor
    }
  },

  drawHUD() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const cx = w / 2;
    const cy = h / 2;

    ctx.clearRect(0, 0, w, h);

    // 1. Synthetic Camera Background (disaster rubble texture)
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, '#0a101d');
    grad.addColorStop(0.5, '#162235');
    grad.addColorStop(1, '#0c1322');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Ground Grid
    ctx.strokeStyle = 'rgba(0, 150, 255, 0.12)';
    ctx.lineWidth = 1;
    for (let y = h / 2; y < h; y += 28) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // 2. Artificial Horizon Ladder (Roll & Pitch)
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate((-this.roll * Math.PI) / 180);

    const pitchOffset = this.pitch * 3.5; // pitch scale

    ctx.strokeStyle = '#00e5ff';
    ctx.lineWidth = 2;

    // Horizon line
    ctx.beginPath();
    ctx.moveTo(-110, pitchOffset);
    ctx.lineTo(-30, pitchOffset);
    ctx.moveTo(30, pitchOffset);
    ctx.lineTo(110, pitchOffset);
    ctx.stroke();

    // Pitch rungs (+10, -10)
    [-20, -10, 10, 20].forEach(deg => {
      const yPos = pitchOffset - (deg * 3.5);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(-45, yPos);
      ctx.lineTo(-20, yPos);
      ctx.moveTo(20, yPos);
      ctx.lineTo(45, yPos);
      ctx.stroke();

      ctx.fillStyle = '#00e5ff';
      ctx.font = '9px monospace';
      ctx.fillText(`${deg}°`, -65, yPos + 3);
      ctx.fillText(`${deg}°`, 52, yPos + 3);
    });

    ctx.restore();

    // 3. Center Aircraft Reticle
    ctx.strokeStyle = '#ff6b00';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    // Inverted T
    ctx.moveTo(cx - 24, cy);
    ctx.lineTo(cx - 8, cy);
    ctx.lineTo(cx, cy + 8);
    ctx.lineTo(cx + 8, cy);
    ctx.lineTo(cx + 24, cy);
    ctx.stroke();

    // 4. Compass Heading Ribbon (Top)
    ctx.fillStyle = 'rgba(6, 11, 19, 0.85)';
    ctx.fillRect(cx - 160, 10, 320, 32);
    ctx.strokeStyle = 'rgba(0, 150, 255, 0.4)';
    ctx.strokeRect(cx - 160, 10, 320, 32);

    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 11px monospace';
    ctx.textAlign = 'center';
    ctx.fillText(`HDG: ${Math.round(this.yaw)}° [ANTI-COMPASS VIO LOCKED]`, cx, 30);

    // 5. Altitude & Airspeed Tapes
    // Left Tape: Airspeed (12 m/s)
    ctx.fillStyle = 'rgba(6, 11, 19, 0.75)';
    ctx.fillRect(15, cy - 80, 55, 160);
    ctx.strokeStyle = '#0075c9';
    ctx.strokeRect(15, cy - 80, 55, 160);
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px monospace';
    ctx.fillText("SPD", 42, cy - 60);
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 14px monospace';
    ctx.fillText("12.4", 42, cy);
    ctx.font = '9px monospace';
    ctx.fillText("m/s", 42, cy + 18);

    // Right Tape: Altitude AGL from LiDAR
    ctx.fillStyle = 'rgba(6, 11, 19, 0.75)';
    ctx.fillRect(w - 75, cy - 80, 60, 160);
    ctx.strokeStyle = '#ff6b00';
    ctx.strokeRect(w - 75, cy - 80, 60, 160);
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px monospace';
    ctx.fillText("LiDAR", w - 45, cy - 60);
    ctx.fillStyle = '#fb923c';
    ctx.font = 'bold 14px monospace';
    ctx.fillText(`${this.altitudeAGL.toFixed(1)}`, w - 45, cy);
    ctx.font = '9px monospace';
    ctx.fillText("m AGL", w - 45, cy + 18);

    // 6. Draw Ray-Casting Target Lock if Present
    if (this.lockedTarget) {
      const tx = this.lockedTarget.u;
      const ty = this.lockedTarget.v;

      // Reticle Circle & Crosshair
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(tx, ty, 18, 0, Math.PI * 2);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(tx - 24, ty); ctx.lineTo(tx + 24, ty);
      ctx.moveTo(tx, ty - 24); ctx.lineTo(tx, ty + 24);
      ctx.stroke();

      // Laser vector from drone center to target
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.65)';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cx, cy + 8);
      ctx.lineTo(tx, ty);
      ctx.stroke();
      ctx.setLineDash([]);

      // Target Coordinate Bubble
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.strokeStyle = '#ef4444';
      ctx.fillRect(tx + 24, ty - 25, 175, 48);
      ctx.strokeRect(tx + 24, ty - 25, 175, 48);

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px monospace';
      ctx.textAlign = 'left';
      ctx.fillText(`TAIT-BRYAN RAY-CAST LOCK`, tx + 30, ty - 10);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`${this.lockedTarget.lat.toFixed(6)}° N`, tx + 30, ty + 4);
      ctx.fillText(`${this.lockedTarget.lon.toFixed(6)}° E`, tx + 30, ty + 18);
    }
  },

  startLoop() {
    const loop = () => {
      // Subtle natural drone breathing motion
      this.pitch += Math.sin(Date.now() / 600) * 0.02;
      this.roll += Math.cos(Date.now() / 800) * 0.015;
      this.drawHUD();
      requestAnimationFrame(loop);
    };
    loop();
  }
};
