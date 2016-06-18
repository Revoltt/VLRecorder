import win32api
import win32con
from sys import exit
from time import sleep
from PIL import ImageGrab

sleep(10)
end = False
while True:
    img = ImageGrab.grab()
    #check certain image pixels
    
    x = 100
    y = 100
    pixel = img.getpixel((x, y))
    #print pixel
    end = (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
    
    x = 1300
    y = 650
    pixel = img.getpixel((x, y))
    #print pixel
    end = end & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
    
    x = 1300
    y = 600
    pixel = img.getpixel((x, y))
    #print pixel
    end = end & (pixel[0] == 244) & (pixel[1] == 99) & (pixel[2] == 33)
    
    if end:
        print "done"
        break
    else:
        print "not yet"
        sleep(10)
