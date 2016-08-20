#!/usr/bin/env python3
"""
graphics_test.py basic graphics set up for AT Robots clone
@author Marios Richards
@version 19-08-2016
"""

from graphics import *
import numpy as np
import time


class CPU:
    
    # registers
    
    def __init__(self, tank):
        self.physical_tank = tank
    
    def run_cpu(self):
        self.physical_tank.change_facing(self.physical_tank.facing + (np.random.rand()-.5)*50 )
        
        
    # 


class Tank:
   #'Tank class'
    # standard points for tank facing up (x,y)
    # (-2, -3), (2,-3), (0,3)
   tank_points = np.array( [ [-3,2], [-3,-2], [3,0] ] )/np.sqrt(2*2 + 3*3)
   
   #tank_points = np.array( [ [-2,-3], [2,-3], [0,3] ] )/np.sqrt(2*2 + 3*3)   
   #tank_points = -tank_points
   max_turn = 10
   
   
   def __init__(self, xpos, ypos, radius, facing, window, speed):
      self.xpos = xpos
      self.ypos = ypos
      self.speed = 20
     
      self.radius = radius
      self.facing = facing
      facing_radians = (facing/128) * np.pi
      
      rot_facing = [ [np.cos(facing_radians), np.sin(facing_radians)], [-np.sin(facing_radians), np.cos(facing_radians)] ]
      
      rot_tank = self.radius*np.dot(self.tank_points,rot_facing)
    
      self.tank_image = Polygon( Point(self.xpos + rot_tank[0,0],
                                            self.ypos + rot_tank[0,1]),
                    Point(self.xpos + rot_tank[1,0],
                        self.ypos + rot_tank[1,1]),
                    Point(self.xpos + rot_tank[2,0],
                        self.ypos + rot_tank[2,1]), )      
    
      self.tank_image.setFill("red")     # color it
      self.tank_image.draw(window)       # place ball on window
      
      self.xvel = self.speed*np.cos(facing_radians)
      self.yvel = self.speed*np.sin(facing_radians)         
      
      self.cpu = CPU(self)
    
   def change_facing(self, desired_facing):
        desired_turn = ( ( desired_facing - self.facing +128) % 256 ) -128
        if desired_turn > self.max_turn:
            desired_turn = self.max_turn
        elif desired_turn < -self.max_turn:
            desired_turn = -self.max_turn
        self.facing = (self.facing + desired_turn) % 256
        
        print(self.facing)
    
   def update(self, delta_t, width, height, window):
   
        self.cpu.run_cpu()
   
        # 
        facing_radians = (self.facing/128) * np.pi
        self.xvel = self.speed*np.cos(facing_radians)
        self.yvel = self.speed*np.sin(facing_radians)          
   
        xmov = self.xvel * delta_t           # identify new x
        ymov = self.yvel * delta_t           # and y positions

        if (xmov + self.xpos + self.radius) > width:
            xmov = width - self.radius - self.xpos

        elif (xmov + self.xpos - self.radius) < 0 :
            xmov = self.radius - self.xpos
        
        if (ymov + self.ypos + self.radius) > height:
            ymov = height - self.radius - self.ypos

        elif (ymov + self.ypos - self.radius) < 0 :
            ymov = self.radius - self.ypos

        #self.tank_image.move(xmov, ymov)    

        self.xpos += xmov     # reset x_i and y_i values so that
        self.ypos += ymov     # we can use loop to move it agai
        
        self.tank_image.undraw()
        

        rot_facing = [ [np.cos(facing_radians), np.sin(facing_radians)], [-np.sin(facing_radians), np.cos(facing_radians)] ]

        rot_tank = self.radius*np.dot(self.tank_points,rot_facing)

        self.tank_image = Polygon( Point(self.xpos + rot_tank[0,0],
                                            self.ypos + rot_tank[0,1]),
                    Point(self.xpos + rot_tank[1,0],
                        self.ypos + rot_tank[1,1]),
                    Point(self.xpos + rot_tank[2,0],
                        self.ypos + rot_tank[2,1]), )      

        self.tank_image.setFill("red")     # color it
        self.tank_image.draw(window)       # place ball on window

            
def main():
    width = 500                         # set up window
    height = 500
    w = GraphWin("AT robots clone",width,height)
    w.setCoords(0,0,width,height)       # Reset coords to more friendly usage
    
    
    
    
    radius = 20            # establish initial values
    x_i = width/2 + radius
    y_i = height/2 + radius
    facing = 0 # 
    speed = 1
 
    object_list = []
    
    initial_tank = Tank(x_i, y_i, radius, facing, w, speed)
    
    second_tank = Tank(x_i+100, y_i+100, radius, facing, w, speed)
    object_list.append(initial_tank)
    object_list.append(second_tank)

    


    
    
    delta_t = 1                        # establish time interval
    # start timer loop   
    game_cycle = 0
    while (True):
        game_cycle += 1

        print("STATUS: ",game_cycle)    # report values in Terminal window
        for obj in object_list:
            obj.update(delta_t, width, height, w)
    

        time.sleep(1/30)


if __name__ == "__main__":
    main()