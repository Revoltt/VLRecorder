import win32api
import win32con
from sys import exit
from time import sleep
from PIL import ImageGrab

sleep(10)
end_1 =  False # lecture finish flag
end_2 = False
# check every 2 minutes if the lecture is over
while True:
    img = ImageGrab.grab()
    #check certain image pixels
          
    x = 100
    y = 100
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
      
    x = 1300
    y = 650
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = end_3 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
          
    x = 1300
    y = 600
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = end_3 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    
    x = 1050
    y = 50
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = end_3 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    
    x = 700
    y = 10
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = end_3 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    
    x = 700
    y = 50
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = end_3 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
      
    x = 240
    y = 170
    pixel = img.getpixel((x, y))
    print pixel
    end_1 = end_1 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    end_2 = end_2 & (pixel[0] <= 5) & (pixel[1] <= 5) & (pixel[2] <= 5)
    end_3 = end_3 & (pixel[0] >= 240) & (pixel[1] >= 95) & (pixel[2] >= 30)
    
    if end_1 | end_2 | end_3:
        print "done"
        break
    else:
        print "not yet"
        sleep(10)
    