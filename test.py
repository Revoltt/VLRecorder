import win32api
import win32con
import time
#win32api.keybd_event(win32con.VK_CAPITAL, 0)
#win32api.keybd_event(0x58, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)

#the following operations should emulate mouse left click
time.sleep(2)
x = 500
y = 500
win32api.SetCursorPos((x,y))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

f = 0x46 
#following code kinda emulates continuously pressed key
for i in range(10):
    win32api.keybd_event(f,0,0,0) # holds the "F" key down
    time.sleep(0.001)
time.sleep(2) # waits 2 seconds
#single key pressing
win32api.keybd_event(f,0,0,0) # holds the "F" key down
#this operation should emulate unpressing the key, but it does not 
win32api.keybd_event(f,0,win32con.KEYEVENTF_KEYUP,0)

#
#