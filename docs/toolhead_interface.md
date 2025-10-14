# Toolhead Interface (Electrical + Software)

## Electrical Connector (example)
- Power: **+V_tool**, **GND**
- Safety: **ENABLE loop** (series with E‑stop + guard switch)
- Bus: **I²C** (SDA/SCL) *or* **CAN** (H/L)
- Aux: 2–4 pins for PWM/DIR/servo if needed
- ID: analog ID pin *or* I²C EEPROM (24LC02) with JSON blob

## Toolhead MCU Responsibilities
- Drive local motors (VESC over UART/CAN; H‑bridge PWM/DIR)
- Servo control for chute/deflector
- Read sensors (current, RPM, temp, lid)
- Implement **state machine**: IDLE → SPINUP → RUN → JAM_CLEAR → FAULT
- Expose uniform API to Pi

## Uniform API (I²C example)
- `0x01 SET_ENABLE {0|1}`
- `0x02 SET_THROTTLE {-100..100}` (or `SET_RPM` for BLDC)
- `0x03 SET_DIR {FWD|REV}`
- `0x04 SET_CHUTE_DEG {0..360}`
- `0x05 SET_DEFLECT_PCT {0..100}`
- `0x10 GET_STATUS` → currents, rpm, temp, faults, type

See `firmware/toolhead_mcu/examples/i2c_api_sketch.ino`.
