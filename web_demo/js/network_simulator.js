// Project Phoenix X — Network-Denial Simulator & Zero-Infrastructure Resilience

const NetworkSimulator = {
  internetOnline: false,
  cellularOnline: false,
  loraOnline: true,

  init() {
    this.updateTopology();
  },

  toggleNetwork(type) {
    if (type === 'internet') {
      this.internetOnline = !this.internetOnline;
      if (window.MissionState) MissionState.setNetworkState('internet', this.internetOnline);
    } else if (type === 'cellular') {
      this.cellularOnline = !this.cellularOnline;
      if (window.MissionState) MissionState.setNetworkState('cellular', this.cellularOnline);
    } else if (type === 'lora') {
      this.loraOnline = !this.loraOnline;
      if (window.MissionState) MissionState.setNetworkState('loraLink', this.loraOnline);
    }
    this.updateTopology();
  },

  updateTopology() {
    // Update Button styles
    const btnNet = document.getElementById('net-toggle-internet');
    const btnCell = document.getElementById('net-toggle-cellular');
    const btnLora = document.getElementById('net-toggle-lora');

    if (btnNet) {
      btnNet.textContent = this.internetOnline ? "INTERNET: ONLINE" : "INTERNET: SEVERED (DISASTER)";
      btnNet.className = this.internetOnline 
        ? "tech-chip tech-chip-green cursor-pointer text-xs" 
        : "tech-chip cursor-pointer text-xs text-rose-400 border-rose-900/60";
    }

    if (btnCell) {
      btnCell.textContent = this.cellularOnline ? "4G/5G CELLULAR: ACTIVE" : "CELLULAR: DOWN (TOWERS DESTROYED)";
      btnCell.className = this.cellularOnline 
        ? "tech-chip tech-chip-green cursor-pointer text-xs" 
        : "tech-chip cursor-pointer text-xs text-rose-400 border-rose-900/60";
    }

    if (btnLora) {
      btnLora.textContent = this.loraOnline ? "LoRa 868MHz P2P: ACTIVE (3-5 km)" : "LoRa RADIO: DISABLED";
      btnLora.className = this.loraOnline 
        ? "tech-chip tech-chip-green cursor-pointer text-xs" 
        : "tech-chip cursor-pointer text-xs text-rose-400 border-rose-900/60";
    }

    // Update Topology Status Text
    const statusBox = document.getElementById('network-resilience-status');
    if (statusBox) {
      if (!this.internetOnline && !this.cellularOnline && this.loraOnline) {
        statusBox.innerHTML = `
          <div class="p-3 rounded bg-slate-900 border border-slate-800 space-y-1 font-mono text-xs">
            <div class="text-emerald-400 font-bold flex items-center space-x-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
              <span>NOMINAL DISASTER OPERATIONAL MODE (100% AIR-GAPPED)</span>
            </div>
            <p class="text-slate-400 text-[11px] leading-relaxed">
              • All neural inference runs on Qualcomm QRB2210 NPU (zero cloud latency).<br>
              • Mission-critical casualty triage packets broadcast via SX1262 LoRa direct to NDRF handheld terminals.<br>
              • High-resolution raw images logged to onboard NVMe flash (store-and-forward architecture).
            </p>
          </div>
        `;
      } else if (!this.loraOnline) {
        statusBox.innerHTML = `
          <div class="p-3 rounded bg-rose-950/40 border border-rose-800 space-y-1 font-mono text-xs">
            <div class="text-rose-400 font-bold flex items-center space-x-1.5">
              <span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>
              <span>COMPLETE RF SILENCE DETECTED (STORE-AND-FORWARD FALLBACK)</span>
            </div>
            <p class="text-slate-400 text-[11px] leading-relaxed">
              • Autonomous survey continues under PX4 autopilot dead reckoning.<br>
              • Geotagged detections cryptographically signed (HMAC-SHA256) and held in flash memory until landing or link restoration.
            </p>
          </div>
        `;
      } else {
        statusBox.innerHTML = `
          <div class="p-3 rounded bg-slate-900 border border-slate-800 space-y-1 font-mono text-xs">
            <div class="text-sky-400 font-bold">HYBRID CONNECTIVITY ACTIVE</div>
            <p class="text-slate-400 text-[11px] leading-relaxed">
              Live high-bandwidth video stream available to base camp via 5G/Wi-Fi link alongside LoRa tactical mesh telemetry.
            </p>
          </div>
        `;
      }
    }
  }
};

window.NetworkSimulator = NetworkSimulator;
