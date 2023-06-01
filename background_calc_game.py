import pygame
import sys 
import os 
import time
from pygame.locals import * 
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy





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
      initYCoorPlayer = yCoorPlayer
      time.sleep(.1)
      finalYCoorPlayer = yCoorPlayer
      

  
 
  

