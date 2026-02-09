import time
import psutil
import os

print("Fake keylogger simulator started (SAFE)")

process = psutil.Process(os.getpid())

while True:
    cpu = process.cpu_percent(interval=0.1)
    time.sleep(0.01)
