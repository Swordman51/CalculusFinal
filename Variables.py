from ObstacleSprite import *

ObstacleXFloor = 1
ObstacleXCeiling = 15
HeroX = 100
HeroY = 500
Speed = 100
TimeBetweenDrop = 6
ObstacleImg = "./backgrounds/EVIL.png"
Obstacles = [] #you don't need to define the type of list, because you were providing an iterable when you weren't supposed to
#you are supposed to put iterables in the brackets, and Obstacles aren't an iterable
RED = (255, 0, 0)

y_change = 0
accel_y = 0
max_speed_up = 30



