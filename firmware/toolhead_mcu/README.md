# Toolhead MCU

Provide a uniform API to the Pi regardless of attachment (brush/thrower/plow).

- Enforce local safety (overcurrent → FAULT)
- Jam clear routine (reverse X ms, retry N)
- Servo control for chute/deflector
- Report: type, currents, rpm, temp, faults
