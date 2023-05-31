import pygame
import sys 
import os 
import time
from pygame.locals import * 

xCoorPlayer = 0 


total = 0 
gameRunning = true
scalefactor = 200

class calc: 
  def refreshScore(): 
    while gameRunning: 
    time.sleep(.1)
    total += yCoorPlayer/scalefactor
    
 
  

