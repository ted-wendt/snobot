"""Teleop controller example.
Map a Bluetooth gamepad to toolhead commands; priority over AUTO.
"""
import time
from toolhead_manager import ToolheadManager

# TODO: integrate evdev / inputs library for your controller mapping.
def read_gamepad():
    # placeholder: return dict with keys active, throttle, dir, chute, deflect
    return {"active": False}

def main():
    th = ToolheadManager()
    armed = False
    while True:
        gp = read_gamepad()
        if gp.get("active"):
            if not armed:
                th.enable(True); armed = True
            th.set_throttle(gp.get("throttle", 0))
            th.set_dir(gp.get("dir", True))
            th.set_chute_deg(gp.get("chute", 180))
            th.set_deflector(gp.get("deflect", 30))
        else:
            if armed:
                th.set_throttle(0); th.enable(False); armed = False
        time.sleep(0.02)

if __name__ == "__main__":
    main()
