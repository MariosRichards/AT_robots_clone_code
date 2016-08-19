#!/usr/bin/env python3
"""
graphics_test.py basic graphics set up for AT Robots clone
@author Marios Richards
@version 19-08-2016
"""

from graphics import *
import numpy as np
import time

def main():
    width = 500                         # set up window
    height = 500
    w = GraphWin("AT robots clone",width,height)
    w.setCoords(0,0,width,height)       # Reset coords to more friendly usage
    radius = 20                         # establish initial values
    x_i = width/2 + radius
    y_i = height/2 + radius
    
# Polygon(point1, point2, point3, ...) Constructs a polygon having the g    
    
    # standard points for tank facing up (x,y)
    # (-2, -3), (2,-3), (0,3)
    
    size = radius
    facing = 128 # 
    facing_radians = (facing/128) * np.pi
    tank_points = np.array( [ [-2,-3], [2,-3], [0,3] ] )/np.sqrt(2*2 + 3*3)
    rot_facing = [ [np.cos(facing_radians), -np.sin(facing_radians)], [np.sin(facing_radians), np.cos(facing_radians)] ]
    
    rot_tank = size*np.dot(tank_points,rot_facing)
    
    tank = Polygon( Point(x_i + rot_tank[0,0],
                        y_i + rot_tank[0,1]),
                    Point(x_i + rot_tank[1,0],
                        y_i + rot_tank[1,1]),
                    Point(x_i + rot_tank[2,0],
                        y_i + rot_tank[2,1]), )
   # ball = Circle(Point(x_i,y_i), radius)   # establish ball as a circle
    tank.setFill("red")                 # color it
    tank.draw(w)                        # place ball on window
    v_x = 10                            # set up x and y velocities
    v_y = 0
    delta_t = 1                        # establish time interval
    # start timer loop
    while (True):
        x_f = x_i + v_x * delta_t           # identify new x
        y_f = y_i + v_y * delta_t           # and y positions
    
        print("STATUS:",x_f," // ", y_f)    # report values in Terminal window
    
    
        tank.move(x_f - x_i, y_f - y_i)     # move the ball the required amount
        
        x_i = x_f                           # reset x_i and y_i values so that
        y_i = y_f                           # we can use loop to move it agai
        time.sleep(1/30)
        if (x_f + radius) > width or (x_f - radius) < 0 :
            v_x = v_x * -1  # reverse direction of velocity        

if __name__ == "__main__":
    main()