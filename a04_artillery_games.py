# file name : a04_artillery_games.py
# Student : Serra Jung
# Email : serra621@bu.edu
# description: two functions which will implement the physics/trigonometry calculations to aim a cannon at a distant target, taking into considering the angle of launch, initial velocity and the Earth’s gravitational constant

import math
import random

def calculate_projectile_distance(launch_angle, init_velocity):
    '''compute and return the distance (in meters) that a projective will travel,
    given its initial launch_angle (in degrees) and its initial_velocity in meters/second.'''
    
    #Calculating the distance from launch angle and initial velocity:
    distance = (init_velocity ** 2  / 9.8) * (math.sin(2 * math.radians(launch_angle)))
    return distance

def calculate_launch_angle(distance, init_velocity):
    '''
    compute and return the required launch angle (in degrees)to hit a target
    at a known distance (in meters) given its initial_velocity in meters/second.'''
    
    #Calculating the launch angle from distance and initial velocity: 
    l_angle = 0.5 * math.asin(9.8 * distance / int(init_velocity) ** 2)
    return math.degrees(l_angle)

#test code 
if __name__ == '__main__':
    print(calculate_projectile_distance(25, 50))
    print(calculate_launch_angle(250, 50))
