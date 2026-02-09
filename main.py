import time
import psutil
from processmonitor import getprocesslist
from behavior_monitor import risk_measure
from logger import logs

print("start")
risk_thres = 2

while True:
    for proc in getprocesslist():

        # Skip System Idle Process
        if proc.pid == 0:
            continue

        try:
            name = proc.name()
            pid = proc.pid
            path = proc.exe()

            risk = risk_measure(proc)
            print(f"Process: {name}, Path: {path}, Risk Score: {risk}")
            if risk >= risk_thres:
                msg = (
                    f"Suspicious process detected: {name} "
                    f"(PID: {pid}) with risk score: {risk}"
                )
                print(msg)
                logs(msg)

        except (psutil.AccessDenied, psutil.NoSuchProcess):
                  continue

        except Exception as e:
            print(f"Unexpected error (PID {proc.pid}): {e}")

    time.sleep(5)
