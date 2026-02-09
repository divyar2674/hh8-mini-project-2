import psutil
# code to detect all process running in the system
def getprocesslist():
    proc_list=[]
    for a in psutil.process_iter():
        try:
            proc_list.append(a)
        except(psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return proc_list
