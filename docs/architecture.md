# System Architecture

## Goals
- Helena snowbanks: must **lift/throw** snow (not just push)
- **Modular toolhead** with uniform electrical + software interface
- **Teleop now, autonomy later** without electronics redo

## High-Level Diagram
- **Compute**: Raspberry Pi (teleop + autonomy)
- **Traction**: Pololu motor HAT (left/right)
- **Toolhead**: Swappable module with its own MCU + drivers
  - BLDC impeller via **VESC** (UART/CAN)
  - Brushed DC auger/actuators via **H-bridge**
  - Servos (chute/deflector) via PCA9685 or MCU PWM
- **Safety**: E‑stop → DC contactor; guard/cover interlock; current sensing
- **Perception**: mono camera → segmentation (Fast‑SCNN/ENet) → drivable ribbon
- **Localization**: wheel odom + IMU (optional LiDAR later)
- **Planner**: centerline follow + “no‑throw” map → chute angles

## Operating Modes
- **DISARMED** → **ARMED** → **TELEOP** or **AUTO** → **FAULT**/E‑STOP
- Teleop has priority; MCU enforces current limits + jam clear.
