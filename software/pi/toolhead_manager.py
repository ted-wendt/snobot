"""Toolhead Manager: uniform API to any attachment via I2C.
Switches seamlessly between TELEOP and AUTO command sources.
"""
import time
from smbus2 import SMBus

I2C_ADDR = 0x2A
CMD_SET_ENABLE = 0x01
CMD_SET_THROTTLE= 0x02
CMD_SET_DIR     = 0x03
CMD_SET_CHUTE   = 0x04
CMD_SET_DEFLECT = 0x05
CMD_GET_STATUS  = 0x10

class ToolheadManager:
    def __init__(self, busnum=1, addr=I2C_ADDR):
        self.bus = SMBus(busnum)
        self.addr = addr
        self.enabled = False

    def _write(self, data: bytes):
        self.bus.write_i2c_block_data(self.addr, data[0], list(data[1:]))

    def enable(self, on: bool):
        self._write(bytes([CMD_SET_ENABLE, 1 if on else 0]))
        self.enabled = on

    def set_throttle(self, pct: int):
        pct = max(-100, min(100, int(pct)))
        self._write(bytes([CMD_SET_THROTTLE, (pct & 0xFF)]))

    def set_dir(self, fwd=True):
        self._write(bytes([CMD_SET_DIR, 1 if fwd else 0]))

    def set_chute_deg(self, deg: int):
        deg = max(0, min(360, int(deg)))
        self._write(bytes([CMD_SET_CHUTE, (deg>>8)&0xFF, deg&0xFF]))

    def set_deflector(self, pct: int):
        pct = max(0, min(100, int(pct)))
        self._write(bytes([CMD_SET_DEFLECT, pct]))

    def get_status(self):
        try:
            self.bus.write_byte(self.addr, CMD_GET_STATUS)
            data = self.bus.read_i2c_block_data(self.addr, 0, 8)
        except Exception as e:
            return {"ok": False, "err": str(e)}
        typ = data[0]; faults = data[1]
        curr = (data[2]<<8) | data[3]
        rpm  = (data[4]<<8) | data[5]
        temp = data[6]
        return {"ok": True, "type": typ, "faults": faults, "current": curr, "rpm": rpm, "tempC": temp}

if __name__ == "__main__":
    th = ToolheadManager()
    th.enable(True)
    th.set_dir(True)
    th.set_throttle(20)
    for _ in range(5):
        print(th.get_status())
        time.sleep(0.5)
    th.set_throttle(0)
    th.enable(False)
