import pstuil
# code to detect all process running in the system
def getprocesslist():
    proc_list=[]
    for a in pstuil.process_iter(['pid', 'name','exe']):
        try:
            proc_list.append(a.info)
        except:
            pass
    return proc_list
