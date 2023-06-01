import pygame
import sys 
import os 
import time
from pygame.locals import * 

xCoorPlayer = 0 


totalVolume = 0 
gameRunning = true
scalefactor = 200

class calc: 
  def refreshScoreVolume(): 
    while gameRunning: 
        time.sleep(.1)
        totalVolume += yCoorPlayer/scalefactor

  def arcLengthRefresh(): 
    while gameRunning: 
      initXCoorPlayer = xCoorPlayer
      
      initXCoorPlayer = yCoorPlayer
  
 
  

