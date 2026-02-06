from datetime import datetime

def logs(m):
    with open("alerts.txt","a") as f:
        f.write(f"{datetime.now()} - {m}\n")
        