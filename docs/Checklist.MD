# Capstone Checklist — What Should Work By End of Each Week

Use this to self-check progress. Each week lists what should actually build, run, or pass — not just "worked on."

---

**Week 1 — Setup + Synthetic Data**
- [ ] Repo initialized, `.gitignore` in place, first commit pushed
- [ ] `CMakeLists.txt` builds an empty `main.cpp` successfully
- [ ] Python venv created, `requirements.txt` installs cleanly
- [ ] Synthetic IMU+GPS data generator runs and outputs a CSV/log for a simple straight-line path

**Week 2 — Sensor Pipeline + Fusion Core**
- [ ] C++ code reads and parses the synthetic IMU+GPS data (from file or stdin)
- [ ] Fusion filter (complementary or Kalman) implemented and compiling
- [ ] Fused output tracks ground-truth position closely on clean (no-noise) data — sanity check first, tune later

**Week 3 — Baseline Nav + Detection Logic**
- [ ] Simulated vehicle can navigate to a single waypoint using fused position, no attacks
- [ ] Spoof-detection function exists and correctly flags an obviously bad GPS reading (e.g. teleporting 500m) in a unit test

**Week 4 — Fallback Nav + Parts List**
- [ ] Fallback (dead-reckoning) navigation runs when detection flags GPS as untrusted
- [ ] A run where GPS "drops out" mid-route still reaches the waypoint using fallback alone
- [ ] Finalized hardware parts list with exact part numbers/links saved in `docs/`

**Week 5 — Harden the Sim Case**
- [ ] At least 3 distinct attack scenarios implemented (full spoof, intermittent, gradual drift)
- [ ] All 3 pass: detection triggers, fallback engages, vehicle still reaches the goal
- [ ] This is your "proof it works" checkpoint — if this isn't solid, don't move to hardware yet

**Week 6 — Order Hardware**
- [ ] Hardware ordered
- [ ] Driver/interface stub code written for each sensor based on its datasheet (won't run yet, just compiles)

**Week 7 — Assembly + Sanity Checks**
- [ ] Chassis assembled, wiring complete
- [ ] Motors respond to a basic test command
- [ ] Each sensor (IMU, GPS, ultrasonic) returns real, non-garbage data when read directly

**Week 8 — Port Fusion to Hardware**
- [ ] Fusion algorithm runs on real sensor data (not synthetic) and produces a stable position estimate
- [ ] Noise/calibration differences from sim documented and accounted for

**Week 9 — Port Detection + Fallback — CHECKPOINT WEEK**
- [ ] Detection logic correctly flags a faked/recorded spoofed GPS signal on real hardware
- [ ] Fallback navigation engages on hardware, not just in sim
- [ ] **Decision point:** if this isn't working reliably, switch to the sim-only fallback plan rather than continuing to debug hardware

**Week 10 — Autonomy Layer**
- [ ] Path planning + obstacle avoidance running in Python
- [ ] Vehicle (real or sim) completes a simple course with at least one obstacle, no attack yet

**Week 11 — Full Integration**
- [ ] End-to-end run: navigate a course, get spoofed mid-route, detect, fall back, recover, finish
- [ ] This should work at least once, reliably, even if not every run is clean

**Week 12 — Buffer / Stress Testing**
- [ ] Multiple attack types tested against the full integrated system
- [ ] Known failure modes documented (even if not fixed)

**Week 13 — Demo + Documentation**
- [ ] Demo video recorded showing a spoofing event and recovery
- [ ] README complete: architecture, design decisions, limitations, future work

**Week 14 — Final Prep**
- [ ] Final bug fixes done
- [ ] Interview talking points written: fusion choices, detection thresholds, tradeoffs made
- [ ] Ready to submit/present

---

### Red flags to watch for
- Still debugging the fusion core in Week 5+ → the detection/fallback logic has nothing solid to build on
- Hardware not responding at all by end of Week 7 → order a backup/replacement part immediately, don't wait
- Week 9 checkpoint not met → trigger the sim-only fallback plan without hesitation