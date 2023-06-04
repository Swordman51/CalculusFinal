import pygame
import ObstacleSprite
from RandomGeneration import *
from ObstacleSprite import *
from pygame.locals import *
from Variables import *

class ScrollingBackground:

    def __init__(self, screenheight, imagefile):

        self.img = pygame.image.load(imagefile)

        self.coord = [0, 0]

        self.coord2 = [0, -screenheight]

        self.y_original = self.coord[1]

        self.y2_original = self.coord2[1]

    def MakeNewOb():
        pos = GenRandomXOb(1, 780)
        if (len(Obstacles) < 12):
            ob = Obstacle(pos, 1400, ObstacleImg)
            Obstacles.append(ob)
        else:
            for obstacle in Obstacles:
                if (obstacle.left <= -100):
                    Obstacles.remove(obstacle)
            

    def DropOb(surface):
      
        for ob in Obstacles:
            ob.Show(surface)

        for obstacle in Obstacles:
            left = obstacle.left
            #top -= 40
            obstacle.UpdateCoords(left-10)
            #the screen is generated with the top left corner being 0, 0, so you need to add to the y coordinate to make the
            #object go downward

    
        