import win32api

def keyboard_action():
    count=0
    for i in range(8,256):
        if win32api.GetAsyncKeyState(i):
            count+=1
    return count
