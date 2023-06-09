import pygame
import sys
import ObstacleSprite
from RandomGeneration import *
from ObstacleSprite import *
from pygame.locals import *
from Variables import *
from CharacterSprite import *
from FunctionLine import* 


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

    def MakeNewPixel(character): 
        pix = pixel(character.X - 9, character.Y)

        Pixels.append(pix)
        
     
        for pix in Pixels: #condition that the pixel is going out of the screen
            if(pix.x <=0):
                Pixels.remove(pix)
      
        
    def DropOb(surface):
      
        for ob in Obstacles:
            ob.Show(surface)

        for obstacle in Obstacles:
            left = obstacle.left
            #top -= 40
            obstacle.UpdateCoords(left-bg_speed)
            #the screen is generated with the top left corner being 0, 0, so you need to add to the y coordinate to make the
            #object go downward

        for pix in Pixels:
            #pix.drawPixel(surface)
            pix.drawRect(surface)

        for pix in Pixels:
            initXPixelValue = pix.x
            #top -= 40
            pix.updateCoord(initXPixelValue-10)
            #the screen is generated with the top left corner being 0, 0, so you need to add to the y coordinate to make the
            #object go downward
            
        for pix in Pixels: #condition that the pixel is going out of the screen
            if(pix.x <=0):
                Pixels.remove(pix)

    def UpdateObPos(Character):
        Character.X -= 5
        if(Character.X <= 109):
            Character.X = 109
    

    def CheckCollisions(Character, Obstacles):
        #if (len(Obstacles) > 0):
            for obstacle in Obstacles:
                if (Character.Y - 9 > obstacle.top and Character.Y + 9 < obstacle.top + obstacle.height):
                    if (Character.X + 9 < obstacle.left + obstacle.length and Character.X - 9 > obstacle.left):
                        return True

    
        
