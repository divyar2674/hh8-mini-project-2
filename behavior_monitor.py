def suspicious(path):
    if not path:
        return False
    path=path.lower()
    return "temp" in path or "appdata" in path

def risk_measure(proc,key_count):
    risk=0
    try:
        if suspicious(proc.exe()):
            risk+=1
        if proc.cpu_percent()>30:
            risk+=1
        if key_count>20:
            risk+=2
    except:
        pass
    return risk

