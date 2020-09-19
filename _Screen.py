import ctypes
import os
#Create object Screen
class Screen(object):
    '''Screen info'''
    def __init__(self, surface):
        self.x = ctypes.windll.user32.GetSystemMetrics(0)
        self.y = ctypes.windll.user32.GetSystemMetrics(1)
        self.size = (self.x, self.y)
        self.center = (self.x//2, self.y//2)
    def Max(self):
        os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" %(0,0)
        surface = pygame.display.set_mode(self.size, 0, 32)
    def Mid(self):
        os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" %(self.center)
        surface = pygame.display.set_mode(self.center, 0, 32)
    def Min(self):
        os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" %(0,0)
        surface = pygame.display.set_mode((0, 0), NOFRAME, 32)
    def Info(self):
        print("Screen Information:\nSize:",self.x,"x",self.y)
