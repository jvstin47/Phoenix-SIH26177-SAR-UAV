// Project Phoenix X - Tactical Web Audio Synthesizer
let audioCtx = null;
let soundEnabled = false;

function initAudio() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    audioCtx = new AudioContext();
  }
}

function toggleAudio() {
  initAudio();
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  soundEnabled = !soundEnabled;
  const audioBtn = document.getElementById('audio-toggle-btn');
  const audioIcon = document.getElementById('audio-icon');
  const audioLabel = document.getElementById('audio-label');
  
  if (soundEnabled) {
    audioBtn.classList.remove('bg-slate-800', 'text-slate-400');
    audioBtn.classList.add('bg-cyan-600/30', 'text-cyan-300', 'border-cyan-500');
    audioIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path>`;
    audioLabel.textContent = "AUDIO: ON";
    playTargetLock();
  } else {
    audioBtn.classList.add('bg-slate-800', 'text-slate-400');
    audioBtn.classList.remove('bg-cyan-600/30', 'text-cyan-300', 'border-cyan-500');
    audioIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2"></path>`;
    audioLabel.textContent = "AUDIO: MUTED";
  }
}

function playTargetLock() {
  if (!soundEnabled || !audioCtx) return;
  const now = audioCtx.currentTime;
  
  // High tactical double-beep
  const osc1 = audioCtx.createOscillator();
  const gain1 = audioCtx.createGain();
  osc1.type = 'sine';
  osc1.frequency.setValueAtTime(880, now);
  osc1.frequency.setValueAtTime(1200, now + 0.08);
  
  gain1.gain.setValueAtTime(0.12, now);
  gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.22);
  
  osc1.connect(gain1);
  gain1.connect(audioCtx.destination);
  osc1.start(now);
  osc1.stop(now + 0.23);
}

function playRaycastLaser() {
  if (!soundEnabled || !audioCtx) return;
  const now = audioCtx.currentTime;
  
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(1400, now);
  osc.frequency.exponentialRampToValueAtTime(320, now + 0.18);
  
  gain.gain.setValueAtTime(0.1, now);
  gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
  
  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(now);
  osc.stop(now + 0.21);
}

function playLoraBurst() {
  if (!soundEnabled || !audioCtx) return;
  const now = audioCtx.currentTime;
  
  // Rapid 17-byte data chirp
  for (let i = 0; i < 4; i++) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'square';
    osc.frequency.setValueAtTime(2200 + (i * 300), now + (i * 0.03));
    gain.gain.setValueAtTime(0.04, now + (i * 0.03));
    gain.gain.exponentialRampToValueAtTime(0.001, now + (i * 0.03) + 0.025);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now + (i * 0.03));
    osc.stop(now + (i * 0.03) + 0.028);
  }
}
