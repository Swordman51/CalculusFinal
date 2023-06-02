import pygame
import sys 
import os 
import time
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

  def arcLengthRefresh(): 
    while gameRunning: 
      initYCoorPlayer = yCoorPlayer # initial y value
      time.sleep(updateMathTime)
      finalYCoorPlayer = yCoorPlayer # final y value
      changeX = bg_speed * updateMathTime #change in x over the time interval
      changeY = finalYCoorPlayer - initYCoorPlayer # change in y over the time interval
      dydx = changeY/changeX

      def f(x): 
      	return sqrt(1+dydx)

      x = sy.Symbol("x")
      totalArcLength += (sy.integrate(f(x), (x, 0, changeX)))

      

  
 
  

