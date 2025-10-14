# Wiring Overview

## Power Domains
- Pi 5 V (isolated, buck converter)
- Toolhead rail (24–36 V) → **Main fuse** → **Contactor** → Drivers/ESC

## Safety Chain
`E‑STOP` + `Guard switch` in series with **ENABLE** to toolhead MCU/contactor coil.

## Signals
- Pi ↔ Toolhead MCU: I²C (or CAN)
- MCU ↔ VESC: UART (or CAN)
- MCU ↔ H‑bridge: PWM + DIR + EN
- Pi ↔ PCA9685: I²C (if servos not on MCU)

## Telemetry
- Current sensors to MCU (I²C or analog ADC)
- Optional INA219/226 on battery rail for logging
