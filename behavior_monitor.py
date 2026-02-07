import os

suspicious= ["temp", "appdata", "downloads"]
trusted= ["windows", "program files"]

def suspiciouspath(path):
    if not path:
        return False

    path = path.lower()

    if any(tp in path for tp in trusted):
        return False

    return any(sp in path for sp in suspicious)

def risk_measure(proc):
    risk = 0

    try:
        exe = proc.exe()
        name = proc.name().lower()

        if suspiciouspath(exe):
            risk += 2

        if len(name) <= 4 or name.count(".") > 1:
            risk += 1
        if proc.cpu_percent(interval=0.1) > 15:
            risk += 1

        print(f"Process: {name}, Path: {exe}, Risk Score: {risk}")
    except Exception:
        pass
    return risk

