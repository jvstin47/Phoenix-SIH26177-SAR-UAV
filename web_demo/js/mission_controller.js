// Project Phoenix X — End-to-End Mission Simulator & Event Timeline Controller

const MissionController = {
  isReplaying: false,

  init() {
    this.renderTimeline();

    // Subscribe to MissionState updates
    if (window.MissionState) {
      MissionState.subscribe((state) => {
        this.updateWorkflowUI(state);
        this.renderTimeline();
      });
    }
  },

  updateWorkflowUI(state) {
    const step = state.currentStep;

    // Update Step Indicators
    for (let i = 1; i <= 9; i++) {
      const node = document.getElementById(`sim-step-node-${i}`);
      const card = document.getElementById(`sim-step-card-${i}`);
      if (node) {
        node.classList.remove('active', 'completed', 'border-sky-500', 'border-emerald-500', 'bg-sky-950/40', 'bg-emerald-950/40');
        if (i < step) {
          node.classList.add('completed', 'border-emerald-500', 'bg-emerald-950/40', 'text-emerald-400');
        } else if (i === step) {
          node.classList.add('active', 'border-sky-500', 'bg-sky-950/40', 'text-sky-300');
        } else {
          node.classList.add('border-slate-800', 'text-slate-500');
        }
      }
      if (card) {
        if (i === step) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      }
    }

    // Step-specific dynamic UI bindings
    // Step 1: Sector
    const secEl = document.getElementById('step1-active-sector');
    if (secEl && state.selectedSector) {
      secEl.textContent = `${state.selectedSector.id} (${state.selectedSector.name}) — Area: ${state.selectedSector.areaKm2} km²`;
    }

    // Step 2: Sweep Progress
    const sweepBar = document.getElementById('step2-sweep-bar');
    const sweepText = document.getElementById('step2-sweep-text');
    if (sweepBar && sweepText) {
      sweepBar.style.width = `${state.sweepProgress}%`;
      sweepText.textContent = `${state.sweepProgress}% SWEEP COVERAGE`;
    }

    // Step 3: Detection Details
    const tgt = state.activeTarget;
    if (tgt) {
      const dLabel = document.getElementById('step3-target-label');
      const dVis = document.getElementById('step3-target-vis');
      const dTemp = document.getElementById('step3-target-temp');
      if (dLabel) dLabel.textContent = `${tgt.id}: ${tgt.label}`;
      if (dVis) dVis.textContent = tgt.opticalVisibility;
      if (dTemp) dTemp.textContent = tgt.thermalDelta;
    }

    // Step 4: Raycast Output
    const rc = state.raycastResult;
    if (rc) {
      const rcCoords = document.getElementById('step4-target-coords');
      const rcErr = document.getElementById('step4-target-err');
      if (rcCoords) rcCoords.textContent = `${rc.targetLat.toFixed(6)}° N, ${rc.targetLon.toFixed(6)}° E`;
      if (rcErr) rcErr.textContent = `± ${rc.sepErrorMargin} m (Simulation Estimate)`;
    }

    // Step 5: LoRa Packet
    const pkt = state.telemetryPacket;
    if (pkt) {
      const pBytes = document.getElementById('step5-packet-hex');
      if (pBytes) pBytes.textContent = pkt.rawHex;
    }

    // Step 7: GCS Triage
    const triCoords = document.getElementById('step7-triage-coords');
    if (triCoords && tgt) {
      triCoords.textContent = `${tgt.lat.toFixed(6)}° N, ${tgt.lon.toFixed(6)}° E`;
    }

    // Step 8: Routing stats
    const r = state.dijkstraRoute;
    if (r) {
      const rDist = document.getElementById('step8-route-dist');
      const rTime = document.getElementById('step8-route-time');
      if (rDist) rDist.textContent = `${r.distanceM} m (Direct LOS: ${r.directDistanceM} m)`;
      if (rTime) rTime.textContent = `~${r.traverseTimeMin} min estimated responder transit`;
    }
  },

  jumpToStep(stepNumber) {
    if (window.MissionState) {
      MissionState.setStep(stepNumber);
    }
  },

  executeStepAction(action) {
    if (!window.MissionState) return;

    if (action === 'start_sweep') {
      MissionState.startReconSweep(() => {
        // Callback after sweep completes
      });
    } else if (action === 'confirm_detection') {
      MissionState.confirmCandidate();
    } else if (action === 'execute_raycast') {
      // Simulate click at target norm coords
      const u = 350;
      const v = 210;
      if (window.OperatorHUD) OperatorHUD.executeRayCast(u, v);
    } else if (action === 'transmit_lora') {
      MissionState.simulateLoRaTransmit();
    } else if (action === 'calculate_route') {
      if (window.TechShowcase) TechShowcase.runDijkstra();
      MissionState.setStep(8);
    } else if (action === 'complete_mission') {
      MissionState.completeMission();
    } else if (action === 'reset_mission') {
      MissionState.setScenario(MissionState.scenario);
    }
  },

  renderTimeline() {
    const container = document.getElementById('mission-timeline-container');
    if (!container || !window.MissionState) return;

    const events = MissionState.timelineEvents;
    if (events.length === 0) {
      container.innerHTML = `<div class="text-xs text-slate-500 font-mono">No operational events recorded yet.</div>`;
      return;
    }

    let html = "";
    events.slice(0, 15).forEach(e => {
      html += `
        <div class="flex items-start space-x-2.5 py-1.5 border-b border-slate-800/80 font-mono text-[11px]">
          <span class="text-slate-500 text-[10px] whitespace-nowrap">${e.timestamp}</span>
          <span class="px-1.5 py-0.2 rounded bg-slate-800 text-sky-400 text-[9px] font-bold border border-slate-700">${e.type}</span>
          <span class="text-slate-300 flex-1 leading-tight">${e.message}</span>
        </div>
      `;
    });
    container.innerHTML = html;
  },

  replayMission() {
    if (this.isReplaying) return;
    this.isReplaying = true;
    MissionState.setStep(1);

    const steps = [
      () => this.executeStepAction('start_sweep'),
      () => this.executeStepAction('confirm_detection'),
      () => this.executeStepAction('execute_raycast'),
      () => this.executeStepAction('transmit_lora'),
      () => this.executeStepAction('calculate_route'),
      () => this.executeStepAction('complete_mission')
    ];

    let current = 0;
    const interval = setInterval(() => {
      if (current < steps.length) {
        steps[current]();
        current++;
      } else {
        clearInterval(interval);
        this.isReplaying = false;
      }
    }, 2200);
  }
};

window.MissionController = MissionController;
