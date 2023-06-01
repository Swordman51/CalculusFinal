import pygame
from RandomGeneration import *
from pygame.locals import *

class Obstacle:

    def __init__(self, screenheight, screenwidth, imagefile):

        self.shape = pygame.image.load(imagefile)
        self.shape = pygame.transform.scale(self.shape, (GenRandomXOb(10, 100), GenRandomYOb(50, 150)))
        #self.top = screenheight - self.shape.get_height()
        self.top = screenheight
        #self.left = screenwidth/2 - self.shape.get_width()/2
        self.left = screenheight


    def Show(self, surface):

        surface.blit(self.shape, (self.left, self.top))


    #the first parameter is always the instance the method is called on (self)
    def UpdateCoords(self, y):

        self.top = y-self.shape.get_width()/2

