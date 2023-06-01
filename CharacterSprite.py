import pygame
import random
#if you only import the module itself without the from keyword, you have to call its methods with the class name in front of it
from random import *
#if you import all the methods from a module, you can call them without the class keyword
from pygame.locals import *

class HeroShip:

    def __init__(self, screenheight, screenwidth, imagefile):

        self.shape = pygame.image.load(imagefile)

        self.top = screenheight - self.shape.get_height()

        self.left = screenwidth/2 - self.shape.get_width()/2



    def Show(self, surface):

        surface.blit(self.shape, (self.left, self.top))



    def UpdateCoords(self, x):

        self.left = x-self.shape.get_width()/2

   