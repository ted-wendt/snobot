# Power System (24 V Toolhead Rail + 5 V Logic)

This guide covers a robust, reproducible power setup for Sno‑bot.

## Architecture Overview
- **Toolhead Rail:** 24–26 V (preferred: **8S LiFePO₄ 25.6 V** or **6S LiPo 22.2 V**)
- **Logic/Compute:** 5 V from a high‑quality buck converter (≥5–8 A)
- **Traction:** share the 24 V rail (separate motor drivers) _or_ keep 12 V during early tests
- **Isolation:** separate toolhead rail from logic; common ground at a star point

```
Battery (24–26 V) → Main Fuse (40–60 A) → Contactor (E‑STOP) →
    ├─ VESC (BLDC impeller/brush)
    ├─ H‑Bridge (brushed auger/actuators)
    ├─ Buck 24→5 V (Pi/servos/sensors)
    └─ Optional Buck 24→12 V (lights, relays)
```

## Sizing & Budget
Typical continuous power while clearing: **500–1200 W**.
- Drive (2 wheels): 80–200 W cruise; 400–600 W spikes on pivots
- Toolhead: 300–1200 W depending on brush/single‑stage/two‑stage
- Electronics: 10–20 W

**Runtime example** (24 V × 20 Ah LiFePO₄ ≈ 512 Wh; ~85% usable ≈ 435 Wh):
- Light: 350 W → ~1.24 h
- Moderate: 600 W → ~0.72 h
- Heavy: 1000 W → ~0.44 h

## Chemistry Choices
| Chemistry | Pros | Cons | Notes |
|---|---|---|---|
| **LiFePO₄ (8S, 25.6 V)** | Safe, long cycle life, integrated BMS | Heavier; **don’t charge <0 °C** | Best for reproducible builds |
| **LiPo (6S, 22.2 V)** | Light, high C, cheap | Touchier safety, cold sag, no BMS | Fine for prototypes & short demos |
| **Li‑ion (6–7S)** | Good energy density | Pack build complexity | Viable if you already build packs |

## Cold‑Weather Guidance
- **Don’t charge LiFePO₄ below 0 °C.** Discharge is OK with reduced capacity.
- Insulate the battery; add a **5–10 W heater pad** with a **5 °C thermostat**.
- Use **soft‑start** on toolhead motors (VESC ramp; H‑bridge PWM ramp).

## Current, Wire, Fusing
- Size for **50–60 A** bursts at 24 V.
- **Main fuse:** 40–60 A (MIDI/ANL) close to the battery.
- **Contactor/relay:** DC‑rated ≥60 A on 24 V.
- **Wire:** 10 AWG for 30–40 A runs; 8 AWG if long. Keep logic wiring separate/twisted.
- **Connectors:** **XT90‑S (anti‑spark)** or **Anderson SB50** on the toolhead rail.

## Safety Chain
- Physical **E‑STOP** in series with the **contactor coil**.
- **Guard/cover switch** in the ENABLE loop to prevent spin when open.
- **Current sensors** (INA226/ACS758) to detect jams; auto‑reverse auger.

## Using Your Existing 3S 11.1 V 5 Ah Packs
- Two in series = **6S 22.2 V 5 Ah ≈ 111 Wh** → short demos.
- For production, move to a **single 24 V LiFePO₄ pack with BMS** (20–30 Ah).

## Checklists

### Bring‑Up
- [ ] Battery secured, insulated, and strain‑relieved
- [ ] Main fuse within 10 cm of battery positive
- [ ] Contactor wired through E‑STOP and key/arm switch
- [ ] Star ground near contactor; logic return routed separately
- [ ] Buck converters mounted with airflow
- [ ] Current sensors calibrated (zero, scale)
- [ ] ESC/H‑bridge soft‑start verified; no brownouts on spin‑up

### Field Operation
- [ ] Battery at room temperature before charging
- [ ] Visual inspection for damaged chains/wires
- [ ] E‑STOP test before engaging toolhead
- [ ] Logs enabled for current, voltage, RPM (for later tuning)
