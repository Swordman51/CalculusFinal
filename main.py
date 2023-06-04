import pygame
#use Crtl + Shift + P to open the command palette, and from there you can select the python interpretor that you want to use
import sys

from Variables import *
from RandomGeneration import *
from CharacterSprite import *
from ObstacleSprite import *
from pygame.locals import *
from movmentMethods import *
from background_calc_game import *

pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screenwidth, screenheight = (1400, 780)

screen = pygame.display.set_mode((screenwidth, screenheight))

#Hero = HeroShip(screenheight, screenwidth, "./backgrounds/ship.png")
obstacle = Obstacle(GenRandomXOb(ObstacleXFloor, ObstacleXCeiling), GenRandomYOb(ObstacleXFloor, ObstacleXCeiling), "./backgrounds/EVIL.png")
character = Character(HeroX, HeroY)
# Set the framerate
framerate = 100 





# Load the background image here. Make sure the file exists!

bg_img = pygame.image.load('./backgrounds/blue.png')
bg_img = pygame.transform.scale(bg_img,(screenwidth, screenheight))

pygame.mouse.set_visible(0)

pygame.display.set_caption('March for Macragge')
Generate = False
Switch = False

# fix indentation
font = pygame.font.SysFont('Consolas', 20)
start_ticks=pygame.time.get_ticks() #starter tick
while True:

   
    clock.tick(60)

    #screen.blit(bg, (0, 0))
 

    #x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #means that the key is pressed down
            if event.key == pygame.K_UP: #it'll only change when the key is hit once
                accel_y = -5
            elif event.key == pygame.K_DOWN:
                accel_y = 5
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                accel_y = 0

        y_change += accel_y

        if abs(y_change) >= max_speed_up:  # If max_speed is exceeded.
        # Normalize the x_change and multiply it with the max_speed.
        # Essentially just set it to max speed
            y_change = y_change/abs(y_change) * max_speed_up
        
        

        # Decelerate if no key is pressed.
    if accel_y == 0:
        y_change *= 0.92

    character.Y += y_change  # Move the object.

    if (character.Y > 771):
        character.Y = 771
    
    if (character.Y < 9):
        character.Y = 9







    screen.blit(bg_img, (0, 0))
       
    #time = clock.tick(framerate)/1000.0
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    timer = "Time = " + str(round(seconds, 2))
    Timer = font.render(timer, True, (0, 0, 0))
    screen.blit(Timer, (1200, 48))
    calc.DisplayPolarFunction(screen, character, font)

    if (int(seconds) % 5 == 0 and TimeBetweenDrop > 1):
        if Switch == False:
            TimeBetweenDrop -= 1
            Switch = True
    else:
         Switch = False
    x, y = pygame.mouse.get_pos()

    obstacle.UpdateCoords(y)

    if int(seconds) % TimeBetweenDrop <= 0:
        if Generate == False:
            ScrollingBackground.MakeNewOb()
            if (TimeBetweenDrop != 1):
                Generate = True
    else:
        Generate = False
    #if you call the method with the name of the object created in front, you don't need to provide the self argument
    #however, if you call the class method, you need to provide the name of the object created.
    #Hero.Show(screen)

    #real
    character.drawCircle(screen)

#TODO WRITE NOT SO EASY NOW IS IT WHEN THE ONE SECOND STUFF STARTS
    ScrollingBackground.DropOb(screen)
    pygame.display.update()




