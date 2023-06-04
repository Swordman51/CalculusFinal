import pygame
import sys 
import os 
import math
import time
import CharacterSprite
from pygame.locals import * 
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy





xCoorPlayer = 0 

totalArcLength = 0
totalVolume = 0 
gameRunning = True
scalefactor = 200
updateMathTime = .1 # time inerval used to calculate the integral and the arc length 



class calc: 
  def refreshScoreVolume(): 
    while gameRunning: 
        time.sleep(updateMathTime)
        totalVolume += yCoorPlayer/scalefactor
  
  def f(dydx): 
    return math.sqrt(1+(dydx ** 2))

  def arcLengthRefresh(): 
    while gameRunning: 
      initYCoorPlayer = yCoorPlayer # initial y value
      time.sleep(updateMathTime)
      finalYCoorPlayer = yCoorPlayer # final y value
      changeX = bg_speed * updateMathTime #change in x over the time interval
      changeY = finalYCoorPlayer - initYCoorPlayer # change in y over the time interval
      dydx = changeY/changeX

 

      x = sy.Symbol("x")
      totalArcLength += (sy.integrate(calc.f(dydx), (x, 0, changeX)))

  
  def DisplayPolarFunction(screen, Character, font):
    Magnitude = math.sqrt( ((Character.X - 0)**2) + ((Character.Y - 780)**2))
    Rad = np.arctan((780 - Character.Y)/(Character.X - 0))
    Angle = np.rad2deg(np.arctan((780 - Character.Y)/(Character.X - 0)))
    MEquation = "R = " + str(round(Magnitude, 2))
    Timer = font.render(MEquation, True, (0, 0, 0))
    AExpression = "Θ = " + str(round(Angle, 2))+"°"
    RExpression = "Radians = " + str(round(Rad, 2))
    Ang = font.render(AExpression, True, (0, 0, 0))
    Radians = font.render(RExpression, True, (0, 0, 0))
    screen.blit(Timer, (1200, 70))
    screen.blit(Ang, (1200, 90))
    screen.blit(Radians, (1200, 110))

  
  #def DisplayParametricFunction(screen, Character, font):
    #PositionFunction = 

  
 
  

