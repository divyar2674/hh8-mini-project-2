from datetime import datetime

def logs(m):
    with open("alerts.txt","a",encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {m}\n")
        