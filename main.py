import pygame
#use Crtl + Shift + P to open the command palette, and from there you can select the python interpretor that you want to use
import sys

import Pygame_Lights
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

obstacle = Obstacle(GenRandomXOb(ObstacleXFloor, ObstacleXCeiling), GenRandomYOb(ObstacleXFloor, ObstacleXCeiling), "./backgrounds/EVIL.png")
character = Character(HeroX, HeroY)
# Set the framerate
framerate = 100 



font = pygame.font.SysFont('Consolas', 18) #you need to initalize pygame to initalize these fonts
font1 = pygame.font.SysFont('Comic Sans MS', 30)
font2 = pygame.font.SysFont('Jokerman', 25)
font3 = pygame.font.SysFont('Stencil', 25)


pygame.display.set_caption('March for Macragge')
Generate = False
Switch = False

# fix indentation

start_ticks=pygame.time.get_ticks() #starter tick
Beginning = True
while True:
    

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN: #means that the key is pressed down
            if event.key == pygame.K_UP or event.key == pygame.K_w: #it'll only change when the key is hit once
                    character.accel_y = -0.5
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    character.accel_y = 0.5
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    character.accel_x = 0.5
            elif event.key == pygame.K_u:
                    Beginning = False
                    Gaming = False
                    Dead = True
            elif event.key == pygame.K_b:
                    if (Beginning == True):
                        Beginning = False
                        Gaming = True
                        Dead = False
                        pygame.event.clear()
                        start_ticks = pygame.time.get_ticks()
            elif event.key == pygame.K_r:
                    if (Dead == True):
                        Beginning = True
                        Gaming = False
                        Dead = False
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_s):
                    character.accel_y = 0
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                    character.accel_x = 0

    if (Beginning == True):
        bg_img = pygame.image.load('./backgrounds/orange.png')
        bg_img = pygame.transform.scale(bg_img,(screenwidth, screenheight))
        #bg_img = pygame.image.load('./backgrounds/orange.png')
        #bg_img = pygame.transform.scale(bg_img,(screenwidth, screenheight))
        text = font.render("Press B to begin (get it????)", True, (GREEN))
        screen.blit(bg_img, (0, 0))
        screen.blit(text, (700, 350))
        
        
    #screen.blit(bg, (0, 0))
    #x, y = pygame.mouse.get_pos()
    
    elif (Gaming == True):
        #screen = pygame.display.set_mode((screenwidth, screenheight))
        bg_img = pygame.image.load('./backgrounds/blue.png')
        bg_img = pygame.transform.scale(bg_img,(screenwidth, screenheight))
   
        character.y_change += character.accel_y
        character.x_change += character.accel_x

        if abs(character.y_change) >= max_speed_V:  # If max_speed is exceeded.
        # Normalize the x_change and multiply it with the max_speed.
        # Essentially just set it to max speed
            character.y_change = character.y_change/abs(character.y_change) * max_speed_V
        
        if abs(character.x_change) >= max_speed_H:  
            character.x_change = character.x_change/abs(character.x_change) * max_speed_H
        
            # Decelerate if no key is pressed.
        if character.accel_y == 0:
            character.y_change *= 0.92

        if character.accel_x == 0:
            character.x_change *= 0.92

        if character.Y < 20:
            character.y_change = 20
        character.Y += character.y_change  # Move the object.
        character.X += character.x_change

        if (character.Y > 771):
            character.Y = 771
    
        if (character.Y < 9):
            character.Y = 9

        if (character.X > 1391):
            character.X = 1391
    
        if (character.X < 109):
            character.X = 109


        screen.blit(bg_img, (0, 0))
        ScrollingBackground.MakeNewPixel(character)
       
        #time = clock.tick(framerate)/1000.0
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        timer = "Time = " + str(round(seconds, 2))
        Timer = font.render(timer, True, (0, 0, 0))
        screen.blit(Timer, (1050, 23))
        calc.DisplayPolarFunction(screen, character, font)
        calc.DisplayVectorFunction(screen, character, font)

        if (int(seconds) % 5 == 0 and TimeBetweenDrop > 1):
            if Switch == False:
                TimeBetweenDrop -= 1
                Switch = True
        else:
            Switch = False
        x, y = pygame.mouse.get_pos()

        obstacle.UpdateCoords(y)
        if((int)(seconds) < 5):
         
            taunt = "Are you ready for what is coming?"
            Taunt = font1.render(taunt, True, (0, 0, 0))
            screen.blit(Taunt, (700, 350))
        elif((int)(seconds) < 17):
         
            taunt = "Avoid them all"
            Taunt = font.render(taunt, True, (0, 0, 0))
            screen.blit(Taunt, (700, 350))
        elif((int)(seconds) < 18):
            taunt = "3"
            Taunt = font3.render(taunt, True, (0, 0, 0))
            screen.blit(Taunt, (700, 350))
        elif((int)(seconds) < 19):
            taunt = "2" 
            Taunt = font3.render(taunt, True, (0, 0, 0))
            screen.blit(Taunt, (700, 350))
        elif((int)(seconds) < 20):
            taunt = "1"  
            Taunt = font3.render(taunt, True, (0, 0, 0))
            screen.blit(Taunt, (700, 350))
        elif int(seconds) % TimeBetweenDrop <= 0:
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
        if ScrollingBackground.CheckCollisions(character, Obstacles) == True:
            time.sleep(1.0)
            Beginning = False
            Gaming = False
            Dead = True
            pygame.event.clear()
        
      

        character.drawCircle(screen)
        ScrollingBackground.MakeNewPixel(character)
        ScrollingBackground.UpdateObPos(character)
        #TODO WRITE NOT SO EASY NOW IS IT WHEN THE ONE SECOND STUFF STARTS
        ScrollingBackground.DropOb(screen)
        calc.refreshScoreVolume(character)
        calc.arcLengthRefresh(character)
        calc.DisplayScore(screen, font)
        

       

    elif(Dead == True):
        bg_img = pygame.image.load('./backgrounds/black.jpg')
        bg_img = pygame.transform.scale(bg_img,(screenwidth, screenheight))
        screen.blit(bg_img, (0, 0))
        DM = font.render(DeathMessage, True, (255, 0, 0))
        screen.blit(DM, (600, 350))
        Obstacles.clear()
        y_change = 0
        accel_y = 0
        max_speed_V = 30

        x_change = 0
        accel_x = 0
        max_speed_H = 30
        


    pygame.display.update()


