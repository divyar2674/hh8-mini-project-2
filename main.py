import time
from processmonitor import getprocesslist
from Keyboard_action_monitor import keyboard_action
from behavior_monitor import risk_measure
from logger import logs

print("start")

while True:
    keyscore=keyboard_action()

    for proc in getprocesslist():
        try:
            risk=risk_measure(proc,keyscore)
            if risk>=3:
                print(f"High risk process detected: {proc['name']} (PID: {proc['pid']}) with risk score {risk}")
                logs(f"High risk process detected: {proc['name']} (PID: {proc['pid']}) with risk score {risk}")
        except:
            pass

    time.sleep(5)

