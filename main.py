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



# Set the background scrolling speed

bg_speed = 100

# Load the background image here. Make sure the file exists!

#bg = pygame.image.load(os.path.join("./backgrounds", "blue.png"))
bg_img = pygame.image.load('./backgrounds/blue.png')
bg_img = pygame.transform.scale(bg_img,(screenwidth, screenheight))

#counter, text = 0, '0'.rjust(3)

pygame.mouse.set_visible(0)

pygame.display.set_caption('March for Macragge')
Generate = False
Switch = False

# fix indentation
font = pygame.font.SysFont('Consolas', 30)
start_ticks=pygame.time.get_ticks() #starter tick
while True:

   
    clock.tick(60)

    #screen.blit(bg, (0, 0))
 

    x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    screen.blit(bg_img, (0, 0))
       
    #time = clock.tick(framerate)/1000.0
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    timer = str(seconds)
    Timer = font.render(timer, True, (0, 0, 0))
    screen.blit(Timer, (1300, 48))

    if (int(seconds) % 5 == 0 and TimeBetweenDrop > 1):
        if Switch == False:
            Difficulty += 1
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




