#!/usr/bin/env python3
"""
graphics_test.py basic graphics set up for AT Robots clone
@author Marios Richards
@version 19-08-2016
"""

from graphics import *
import numpy as np
import time


class Tank:
   #'Tank class'

   tank_points = np.array( [ [-2,-3], [2,-3], [0,3] ] )/np.sqrt(2*2 + 3*3)
   
   def __init__(self, xpos, ypos, radius, facing, window, xvel, yvel):
      self.xpos = xpos
      self.ypos = ypos
      self.xvel = xvel
      self.yvel = yvel      
      self.radius = radius
      self.facing = facing
      facing_radians = (facing/128) * np.pi
      rot_facing = [ [np.cos(facing_radians), -np.sin(facing_radians)], [np.sin(facing_radians), np.cos(facing_radians)] ]
      rot_tank = self.radius*np.dot(self.tank_points,rot_facing)
      
      self.tank_image = Polygon( Point(self.xpos + rot_tank[0,0],
                                            self.ypos + rot_tank[0,1]),
                    Point(self.xpos + rot_tank[1,0],
                        self.ypos + rot_tank[1,1]),
                    Point(self.xpos + rot_tank[2,0],
                        self.ypos + rot_tank[2,1]), )      
    
      self.tank_image.setFill("red")                 # color it
      self.tank_image.draw(window)                        # place ball on window    
    
   def update(self, delta_t, width, height):
        xmov = self.xvel * delta_t           # identify new x
        ymov = self.yvel * delta_t           # and y positions
        self.tank_image.move(xmov , ymov)     # move the ball the required amount
        self.xpos += xmov     # reset x_i and y_i values so that
        self.ypos += ymov     # we can use loop to move it agai

        if (self.xpos + self.radius) > width  or (self.xpos - self.radius) < 0 :
            self.xvel = -self.xvel  # reverse direction of velocity        
        
        if (self.ypos + self.radius) > height or (self.ypos - self.radius) < 0 :
            self.yvel = -self.yvel  # reverse direction of velocity           
        
def main():
    width = 500                         # set up window
    height = 500
    w = GraphWin("AT robots clone",width,height)
    w.setCoords(0,0,width,height)       # Reset coords to more friendly usage
    
    
    
    
    radius = 20            # establish initial values
    x_i = width/2 + radius
    y_i = height/2 + radius
    facing = 128 # 
    v_x = 10    # set up x and y velocities
    v_y = 0    
    
    initial_tank = Tank(x_i, y_i, radius, facing, w, v_x, v_y)
    # standard points for tank facing up (x,y)
    # (-2, -3), (2,-3), (0,3)
    

    # facing_radians = (facing/128) * np.pi
    # tank_points = np.array( [ [-2,-3], [2,-3], [0,3] ] )/np.sqrt(2*2 + 3*3)
    # rot_facing = [ [np.cos(facing_radians), -np.sin(facing_radians)], [np.sin(facing_radians), np.cos(facing_radians)] ]
    
    # rot_tank = size*np.dot(tank_points,rot_facing)
    
    # tank = Polygon( Point(x_i + rot_tank[0,0],
                        # y_i + rot_tank[0,1]),
                    # Point(x_i + rot_tank[1,0],
                        # y_i + rot_tank[1,1]),
                    # Point(x_i + rot_tank[2,0],
                        # y_i + rot_tank[2,1]), )
   # ball = Circle(Point(x_i,y_i), radius)   # establish ball as a circle

    
    
    delta_t = 1                        # establish time interval
    # start timer loop   

    while (True):

        # x_f = x_i + v_x * delta_t           # identify new x
        # y_f = y_i + v_y * delta_t           # and y positions
    
        print("STATUS:XXXX")    # report values in Terminal window
        initial_tank.update(delta_t, width, height)
    
        # tank.move(x_f - x_i, y_f - y_i)     # move the ball the required amount
        
        # x_i = x_f                           # reset x_i and y_i values so that
        # y_i = y_f                           # we can use loop to move it agai
        time.sleep(1/30)
        # if (x_f + radius) > width or (x_f - radius) < 0 :
            # v_x = v_x * -1  # reverse direction of velocity        

if __name__ == "__main__":
    main()