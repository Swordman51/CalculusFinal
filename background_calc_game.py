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

#from main import *
from fractions import Fraction




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
        totalVolume += Character.Y/scalefactor
  
  def f(dydx): 
    return math.sqrt(1+(dydx ** 2))

  def arcLengthRefresh(): 
    while gameRunning: 
      initYCoorPlayer = Character.Y # initial y value
      time.sleep(updateMathTime)
      finalYCoorPlayer = Character.Y # final y value
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
    screen.blit(Timer, (1100, 45))
    screen.blit(Ang, (1100, 65))
    screen.blit(Radians, (1100, 85))

  
  def DisplayVectorFunction(screen, Character, font):
    PositionFunction = "▲X = " + str((int)(Character.X)) +"i + " + str((int)(780 - Character.Y)) +"j"
    VelocityFunction = "V = " +str((int)(Character.x_change)) + " dx/dt + " + str((int)(Character.y_change)) + " dy/dt"
    AccelerationFunction = "a = " + str((int)(Character.accel_x)) + " d^2x/dt^2 + "+ str((int)(Character.accel_y)) + "d^2y/dt^2"
    Pos = font.render(PositionFunction, True, (0, 0, 0))
    Vel = font.render(VelocityFunction, True, (0, 0, 0))
    Acel = font.render(AccelerationFunction, True, (0, 0, 0))
    screen.blit(Pos, (1100, 125))
    screen.blit(Vel, (1100, 145))
    screen.blit(Acel, (1100, 165))

  
 
  

