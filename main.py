import time
from processmonitor import getprocesslist
from behavior_monitor import risk_measure
from logger import logs

print("start")
risk_thres=1
while True:
    for proc in getprocesslist():
        try:
            risk = risk_measure(proc)
            if risk >= risk_thres:
                logs(f"Suspicious process detected: {proc['name']} (PID: {proc['pid']}) with risk score: {risk}")
                print(f"Suspicious process detected: {proc['name']} (PID: {proc['pid']}) with risk score: {risk}")
        except Exception as e:
            print(f"Error processing {proc['name']} (PID: {proc['pid']}): {e}")
        
        time.sleep(2)