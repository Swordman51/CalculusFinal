import pygame

import sys

import os

from pygame.locals import *

from movmentMethods import *

pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screenwidth, screenheight = (1200, 960)

screen = pygame.display.set_mode((screenwidth, screenheight))




# Set the framerate

framerate = 100



# Set the background scrolling speed

bg_speed = 100

# Load the background image here. Make sure the file exists!

#bg = pygame.image.load(os.path.join("./backgrounds", "blue.png"))

StarField = ScrollingBackground(screenheight/2, "./backgrounds/warhammer.jpg")

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')


# fix indentation


while True:

    clock.tick(60)

    #screen.blit(bg, (0, 0))
    
    time = clock.tick(framerate)/1000.0

    x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    StarField.UpdateCoords(bg_speed, time)

    StarField.Show(screen)

  
    pygame.display.update()




