from toolhead_manager import ToolheadManager
import time

th = ToolheadManager()
print("Arming…")
th.enable(True)
th.set_dir(True)
th.set_chute_deg(270)
th.set_deflector(30)
print("Spin up 20% for 2s")
th.set_throttle(20); time.sleep(2)
print("Jam clear pulse")
th.set_dir(False); th.set_throttle(40); time.sleep(0.3)
th.set_throttle(0); th.set_dir(True)
print("Run 35% for 3s")
th.set_throttle(35); time.sleep(3)
print("Disarm")
th.set_throttle(0); th.enable(False)
