import win32api, win32gui, win32con, pyHook, pythoncom, os
from PIL import Image, ImageGrab, ImageOps
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#In clockwise order
red_rgb = [226, 27, 60]
blue_rgb = [16, 88, 175]
green_rgb = [41, 143, 13]
yellow_rgb = [216, 158, 0]
red = [364, 299]
blue = [1071, 245]
green = [1266, 685]
yellow = [303, 614]
x_pad = 0
y_pad = 0
class kahootObj(object):
    def __init__(self, red, blue, green, yellow):
        self.red = red
        self.blue = blue
        self.green = green
        self.yellow = yellow
        self.order = []
        self.current = 0
    def click(self, position):
        if(str(position).lower() == 'red'):
            position = self.red
        elif(str(position).lower() == 'blue'):
            position = self.blue
        elif(str(position).lower() == 'green'):
            position = self.green
        elif(str(position).lower() == 'yellow'):
            position = self.yellow
        x = position[0]
        y = position[1]
        win32api.SetCursorPos(position)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        return True
    def screenGrab(self):
        im = ImageGrab.grab()
        ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
        return im
    def find_rgb(self, r_query, g_query, b_query):
        img = kahoot.screenGrab()
        rgb = img.convert('RGB')
        for x in range(img.size[0]):
           for y in range(img.size[1]):
               r, g, b, = rgb.getpixel((x, y))
               if r == r_query and g == g_query and b == b_query:
                   return (x,y)
    def start(self):
        while 1:
            track = True    
            if self.find_rgb(yellow_rgb[0], yellow_rgb[1], yellow_rgb[2]) != None and track:
                self.click(self.order[self.current])
                self.current += 1
                print(self.current)
                track = not track
            if self.find_rgb(yellow_rgb[0], yellow_rgb[1], yellow_rgb[2]) == None and not track:
                track = not track
def listen(event):
    if event.Key == 'F1':
        kahoot.click(kahoot.order[kahoot.current])
        kahoot.current += 1
        if(kahoot.current > len(kahoot.order)):
            os._exit(1)
"""def start():
    hm = pyHook.HookManager()
    hm.KeyDown = listen
    hm.HookKeyboard()
    pythoncom.PumpMessages()
"""


kahoot = kahootObj(red, blue, green, yellow)