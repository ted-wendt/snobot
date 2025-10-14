# CAN API Sketch
If you choose CANbus, mirror the same commands with 11-bit IDs:
- 0x100: SET_ENABLE, payload 1 byte
- 0x101: SET_THROTTLE, payload 1 byte (signed)
- 0x102: SET_DIR, payload 1 byte
- 0x103: SET_CHUTE, payload 2 bytes (deg)
- 0x104: SET_DEFLECT, payload 1 byte
- 0x180: GET_STATUS → periodic 10 Hz frame (currents, rpm, temp, faults)
