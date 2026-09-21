// Project Phoenix X — Central Mission State Architecture
// Source of truth for connected end-to-end mission workflow

const MissionState = {
  // Current Active Mission Workflow Step (1 to 9)
  currentStep: 1,

  // Scenario Selection (Generic disaster archetypes)
  scenario: 'landslide', // 'landslide', 'collapse', 'smoke_wire'

  // Predefined Disaster Scenarios with ground truth values
  scenarios: {
    landslide: {
      id: 'landslide',
      name: 'Tropical Mudflow & Slope Escarpment',
      category: 'Geological / Hydrological Disaster',
      ambientTemp: 15.0,
      description: 'Torrential rains and deep clay mudflow. Visible spectrum camera is obstructed by low-contrast mud camouflage. Radiometric LWIR thermal isolates 37.0°C body heat through moisture fissure.',
      rgbSrc: 'images/wayanad_rgb.jpg',
      thermalSrc: 'images/wayanad_thermal.jpg',
      sectors: [
        { id: 'SEC-01A', name: 'Valley Inundation Zone', areaKm2: 1.8, terrain: 'Wet Clay Slush', risk: 'HIGH' },
        { id: 'SEC-01B', name: 'Upper Slope Failure', areaKm2: 2.0, terrain: 'Debris Flow & Timber', risk: 'CRITICAL', default: true },
        { id: 'SEC-01C', name: 'Roadway Inundation Cutoff', areaKm2: 1.5, terrain: 'Unstable Asphalt Edge', risk: 'MODERATE' }
      ],
      defaultTarget: {
        id: 'CAND-01',
        type: 'human',
        label: 'MUD-COVERED CASUALTY',
        normX: 0.45,
        normY: 0.50,
        spotTemp: 37.0,
        opticalVisibility: '~15% (Mud Camouflage)',
        thermalDelta: '+22.0°C (37.0°C vs 15.0°C Ambient)',
        status: 'CRITICAL (MUD ENTRAPMENT)',
        lat: 11.581240,
        lon: 76.128450
      },
      hazards: [
        { id: 'HAZ-01', label: 'ACTIVE MUD SLIP', normX: 0.15, normY: 0.20, temp: 14.8, type: 'geological' }
      ]
    },
    collapse: {
      id: 'collapse',
      name: 'Structural Concrete Pancake Collapse',
      category: 'Urban Seismic Event',
      ambientTemp: 16.0,
      description: 'Pancake failure of multi-story reinforced concrete structures. Deep shadows in rubble crevices create optical blindness. Emitted LWIR radiation detects trapped casualty emitting 36.8°C.',
      rgbSrc: 'images/earthquake_rgb.jpg',
      thermalSrc: 'images/earthquake_thermal.jpg',
      sectors: [
        { id: 'SEC-02A', name: 'Residential Block Rubble', areaKm2: 1.4, terrain: 'Shattered Masonry', risk: 'CRITICAL' },
        { id: 'SEC-02B', name: 'Commercial Plaza Voids', areaKm2: 2.0, terrain: 'Reinforced Concrete Slabs', risk: 'HIGH', default: true }
      ],
      defaultTarget: {
        id: 'CAND-02',
        type: 'human',
        label: 'TRAPPED SURVIVOR IN VOID',
        normX: 0.28,
        normY: 0.52,
        spotTemp: 36.8,
        opticalVisibility: '~5% (Shadow Occlusion)',
        thermalDelta: '+20.8°C (36.8°C vs 16.0°C Ambient)',
        status: 'CONFINED SPACE VOID',
        lat: 34.053210,
        lon: -118.244820
      },
      hazards: [
        { id: 'HAZ-02', label: 'UNSTABLE OVERHANG', normX: 0.72, normY: 0.28, temp: 16.5, type: 'structural' }
      ]
    },
    smoke_wire: {
      id: 'smoke_wire',
      name: 'Zero-Lux Night Smoke & High-Voltage Hazard',
      category: 'Industrial Collapse / Fire Hazard',
      ambientTemp: 16.0,
      description: 'Post-blast structural damage at night with dense toxic particulate smoke plumes. Daylight camera is blinded. Thermal sensor pierces smoke to identify both an arcing 11kV cable (85°C) and an injured victim (36.8°C).',
      rgbSrc: 'images/night_smoke_rgb.jpg',
      thermalSrc: 'images/night_smoke_thermal.jpg',
      sectors: [
        { id: 'SEC-03A', name: 'Industrial Yard Sector', areaKm2: 2.0, terrain: 'Twisted Rebar & Smoke', risk: 'EXTREME', default: true }
      ],
      defaultTarget: {
        id: 'CAND-03',
        type: 'human',
        label: 'COLLAPSED SURVIVOR',
        normX: 0.35,
        normY: 0.70,
        spotTemp: 36.8,
        opticalVisibility: '~2% (Particulate Smoke Blindness)',
        thermalDelta: '+20.8°C (36.8°C vs 16.0°C Ambient)',
        status: 'CODE RED INJURED',
        lat: 28.613939,
        lon: 77.209021
      },
      hazards: [
        { id: 'HAZ-03', label: 'ARCING 11kV TRANSMISSION CABLE', normX: 0.22, normY: 0.22, temp: 85.0, type: 'electrical' }
      ]
    }
  },

  // Active Mission State Variables
  selectedSector: null,
  sweepProgress: 0,
  activeTarget: null,
  raycastResult: null,
  telemetryPacket: null,
  isTransmitting: false,
  transmitConfirmed: false,
  dijkstraRoute: null,

  // Network Denial Simulation State
  networkState: {
    internet: false,   // Disabled (Disaster blackout)
    cellular: false,   // Disabled (Towers severed)
    loraLink: true     // Enabled (868MHz P2P Tactical Mesh)
  },

  // Persistent Mission Event Timeline
  timelineEvents: [],

  // Subscribers for reactive UI updates
  subscribers: [],

  init() {
    // Initialize with default scenario
    this.setScenario('landslide', false);
    this.logEvent('MISSION_INIT', 'System initialized. Ready for search sector assignment.');
  },

  subscribe(callback) {
    this.subscribers.push(callback);
    callback(this);
  },

  notify() {
    this.subscribers.forEach(cb => cb(this));
  },

  setScenario(scenarioKey, shouldNotify = true) {
    if (!this.scenarios[scenarioKey]) return;
    this.scenario = scenarioKey;
    const sc = this.scenarios[scenarioKey];
    
    // Select default sector
    this.selectedSector = sc.sectors.find(s => s.default) || sc.sectors[0];
    this.activeTarget = Object.assign({}, sc.defaultTarget);
    
    // Reset progression
    this.currentStep = 1;
    this.sweepProgress = 0;
    this.raycastResult = null;
    this.telemetryPacket = null;
    this.transmitConfirmed = false;
    this.dijkstraRoute = null;

    this.logEvent('SCENARIO_LOADED', `Loaded scenario: ${sc.name} (${sc.category})`);
    if (shouldNotify) this.notify();
  },

  setStep(stepNumber) {
    this.currentStep = Math.max(1, Math.min(9, stepNumber));
    this.logEvent('STEP_TRANSITION', `Advanced to Mission Step ${this.currentStep}`);
    this.notify();
  },

  selectSector(sectorId) {
    const sc = this.scenarios[this.scenario];
    const s = sc.sectors.find(item => item.id === sectorId);
    if (s) {
      this.selectedSector = s;
      this.logEvent('SECTOR_ASSIGNED', `Assigned search polygon ${s.id} (${s.name}) — Target area: ${s.areaKm2} km²`);
      this.notify();
    }
  },

  startReconSweep(onComplete) {
    this.setStep(2);
    this.sweepProgress = 0;
    this.logEvent('RECON_SWEEP_START', `Autonomous boustrophedon lawnmower sweep initiated on sector ${this.selectedSector.id}.`);
    
    const interval = setInterval(() => {
      this.sweepProgress += 10;
      if (this.sweepProgress >= 100) {
        clearInterval(interval);
        this.logEvent('ANOMALY_TRIGGERED', `Thermal anomaly detected in sector ${this.selectedSector.id}. High contrast detected.`);
        this.setStep(3); // Advance to Candidate Detection
        if (onComplete) onComplete();
      }
      this.notify();
    }, 200);
  },

  confirmCandidate() {
    this.setStep(4); // Advance to Ray-Cast localization
    this.logEvent('CANDIDATE_CONFIRMED', `Target ${this.activeTarget.id} confirmed for ground ray-casting projection.`);
    this.notify();
  },

  setRaycastResult(result) {
    this.raycastResult = result;
    this.activeTarget.lat = result.targetLat;
    this.activeTarget.lon = result.targetLon;
    this.logEvent('RAYCAST_RESOLVED', `Ray-casting locked WGS-84 coordinates: ${result.targetLat.toFixed(6)}° N, ${result.targetLon.toFixed(6)}° E (±${result.sepErrorMargin}m)`);
    
    // Automatically serialize into 17-byte LoRa packet
    this.serializeTelemetry();
    this.setStep(5);
    this.notify();
  },

  serializeTelemetry() {
    // 17-byte serialization matching Souli et al. (2024)
    const lat = this.activeTarget.lat;
    const lon = this.activeTarget.lon;
    const alt = this.raycastResult ? this.raycastResult.altitudeAGL : 28.4;
    const buffer = new ArrayBuffer(17);
    const view = new DataView(buffer);

    view.setUint8(0, 0x50); // Header 'P'
    view.setFloat32(1, lat, false); // Big endian
    view.setFloat32(5, lon, false);
    view.setInt16(9, Math.round(alt * 10), false); // Decimeters
    view.setUint8(11, (1 << 6) | (0 << 4) | (14 & 0x0F)); // Triage Red | Human | 93% Conf
    view.setUint8(12, 78); // Battery 78%
    view.setUint16(13, 12400, false); // 124.00 deg heading
    view.setUint16(15, 0xA412, false); // HMAC Checksum

    const bytes = new Uint8Array(buffer);
    let hexStr = "";
    bytes.forEach(b => hexStr += b.toString(16).padStart(2, '0').toUpperCase() + " ");

    this.telemetryPacket = {
      buffer: bytes,
      rawHex: hexStr.trim(),
      byteCount: 17,
      lat: lat,
      lon: lon,
      alt: alt,
      status: 'ENCODED'
    };

    this.logEvent('LORA_PACKET_ENCODED', `Serialized 17-byte binary telemetry packet: ${this.telemetryPacket.rawHex}`);
  },

  simulateLoRaTransmit(onComplete) {
    this.isTransmitting = true;
    this.logEvent('LORA_TRANSMIT_BURST', `Broadcasting 17-byte P2P packet over 868 MHz (SX1262 LoRa link)...`);
    this.notify();

    setTimeout(() => {
      this.isTransmitting = false;
      this.transmitConfirmed = true;
      this.logEvent('LORA_BURST_ACK', `Ground Control Station received 17-byte packet. RSSI: -98 dBm | SNR: +8.5 dB.`);
      this.setStep(7); // Advance to GCS Triage
      if (onComplete) onComplete();
      this.notify();
    }, 1200);
  },

  setDijkstraRoute(routeData) {
    this.dijkstraRoute = routeData;
    this.logEvent('ROUTE_COMPUTED', `Dijkstra obstacle-free ingress route computed: ${routeData.distanceM}m (~${routeData.traverseTimeMin} min traverse).`);
    this.setStep(8);
    this.notify();
  },

  completeMission() {
    this.setStep(9);
    this.logEvent('MISSION_COMPLETED', `End-to-End reconnaissance and triage workflow completed successfully.`);
    this.notify();
  },

  setNetworkState(networkKey, isAvailable) {
    this.networkState[networkKey] = isAvailable;
    this.logEvent('NETWORK_CHANGE', `Network state changed: ${networkKey.toUpperCase()} = ${isAvailable ? 'ONLINE' : 'SEVERED'}`);
    this.notify();
  },

  logEvent(type, message) {
    const timestamp = new Date().toISOString().substring(11, 19);
    this.timelineEvents.unshift({
      timestamp,
      type,
      message,
      step: this.currentStep
    });
    // Keep max 50 events
    if (this.timelineEvents.length > 50) this.timelineEvents.pop();
  }
};

window.MissionState = MissionState;
