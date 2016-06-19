import win32api
import win32con
from time import sleep
from PIL import ImageGrab

print "All coordinates for mouse clicks are set for screen size 1366x768 pixels"
print "Automatic recording starts in 7 seconds. Please switch to the window you want to record"
    
# keyboard codes
start = 0xBB # =
close_1 = 0xA2 # left Ctrl
close_2 = 0x57 # w
sleep(7)
# variable for correct lecture switching after lecture 25
k = 0
    
# main lecture loop
while True:
    # left click on the lecture
    x = 640
    y = 385
    win32api.SetCursorPos((x,y))
    sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    sleep(7.5)
           
    # the player can be placed not in the usual spot. then we need to press one more button
    # This check is BAD
    x = 480
    y = 100
    img = ImageGrab.grab()
    pixel = img.getpixel((x, y))
    if pixel == (43, 187, 134):
        x = 905
        y = 125
        win32api.SetCursorPos((x,y))
        sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
         
    # press play button in the player
    x = 440
    y = 400
    win32api.SetCursorPos((x,y))
    sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    sleep(2.5)
    # second time? not quite understood why it is needed
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        
    # make sure the recording starts from the beginning of the lecture
    # for some reason this pauses the player
    x = 3
    y = 665
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    sleep(1.5)
        
    # full screen
    x = 870
    y = 680
    win32api.SetCursorPos((x,y))
    sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
    # start recording
    sleep(0.5)
    win32api.keybd_event(start,0,0,0) # holds the "=" key down
    win32api.keybd_event(start,0,win32con.KEYEVENTF_KEYUP,0)
    sleep(0.5)
    
    # start the player again
    x = 440
    y = 400
    win32api.SetCursorPos((x,y))
    sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        
    # wait till the lecture is nearly over
    sleep(5400) # average lecture length - 1.5 hours
    end_1 =  False # lecture finish flag
    end_2 = False
    # check every 2 minutes if the lecture is over
    while True:
        img = ImageGrab.grab()
        #check certain image pixels
          
        x = 100
        y = 100
        pixel = img.getpixel((x, y))
        #print pixel
        end_1 = (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
        end_2 = (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
          
        x = 1300
        y = 650
        pixel = img.getpixel((x, y))
        #print pixel
        end_1 = end_1 & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
        end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
              
        x = 1300
        y = 600
        pixel = img.getpixel((x, y))
        #print pixel
        end_1 = end_1 & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
        end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
        
        x = 1050
        y = 50
        pixel = img.getpixel((x, y))
        #print pixel
        end_1 = end_1 & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
        end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
        
        x = 700
        y = 50
        pixel = img.getpixel((x, y))
        #print pixel
        end_1 = end_1 & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
        end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
          
        x = 240
        y = 170
        pixel = img.getpixel((x, y))
        #print pixel
        end_1 = end_1 & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
        end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
        
        if end_1 | end_2:
            print "done"
            break
        else:
            print "not yet"
            sleep(180)
    # stop the recording
    sleep(0.5)
    win32api.keybd_event(start,0,0,0) # holds the "=" key down
    win32api.keybd_event(start,0,win32con.KEYEVENTF_KEYUP,0)
    sleep(0.5)
     
    # close the tab (for google chrome)
    win32api.keybd_event(close_1,0,0,0) # holds the "left-Ctrl" key down
    win32api.keybd_event(close_2,0,0,0) # holds the "w" key down
    sleep(0.05)
    win32api.keybd_event(close_1,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(close_2,0,win32con.KEYEVENTF_KEYUP,0)
    sleep(2)
    #switch to the next lecture
    x = 420
    y = 300
    img = ImageGrab.grab()
    if img.getpixel((x, y)) == (231, 238, 241):
        #option 1 - lectures up to 24
        y = y + 70
        win32api.SetCursorPos((x,y))
        sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    else:
        #option 2 - lectures 25-30
        k = k + 1
        y = y + 65 * (k + 1) - 15
        win32api.SetCursorPos((x,y))
        sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)