from Variables import *
class pixel: 

    black = (0,0,0)

    def __init__(self, x, y):
        self.x  = x
        self.y = y

    def drawPixel(self, surface):
        surface.set_at(((int)(self.x), (int)(self.y)), BLACK)  

    def updateCoords(self, y):
        self.y = y
