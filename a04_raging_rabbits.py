# file name: a04_raging_rabbits.py
# Student: Serra Jung
# email: serra621@bu.edu
# description: A family of rabbits is tired of being attacked by larger predators. Being slightly more clever than birds, they have managed to obtain a cannon and ammunition for it. But being rabbits, they are completely unable to handle any math besides multiplication. They are relying on you to help them aim the cannon and select the launch velocity to predict where the shot will fall on the field.

from a04_artillery_games import calculate_projectile_distance
from a04_artillery_games import calculate_launch_angle
import random

def raging_rabbits():
    '''implement an input-process-output program for this interactive game.'''
    
    #welcome message
    print('Welcome to Raging Rabbits!')

    #prompt the user to enter the velocity 
    launch_velocity = int(input("Enter the desired launch velocity (in m/s): "))
    
    #calculate the minimum and maximum distance that the projectile could travel.
    minimum_dist = float(calculate_projectile_distance(10, int(launch_velocity)))
    maximum_dist = float(calculate_projectile_distance(45, int(launch_velocity)))

    # Pick a random distance to the target that is within this range and display to game's player
    random_dist = random.randint(int(minimum_dist), int(maximum_dist))

    #print the output 
    print("At an initial launch velocity of %.2f" % launch_velocity ,"meters/second, your cannon can hit a target between %.2f and %.2f" % (minimum_dist,maximum_dist),"meters.")
    print()
    print("Your target is located at " + str(random_dist) + " meters.")

    print()
    print()
    #Enter the launch angle in degrees 
    launch_angle = int(input("Enter your launch angle (in degrees): "))

    # calculate the actual distance the projectile will travel at this angle and initial velocity, and calculate the “error”, i.e., how far off target was the shot
    traveled = float(calculate_projectile_distance(launch_angle, launch_velocity))
    from_the_target =  random_dist - traveled

    #print the output 
    print("Your projectile traveled " + str("%.2f" % traveled) + " meters.")
    print("Your shot was " + str("%.2f" % from_the_target) + " meters from the target.")




# test code:
if __name__ == '__main__':

    raging_rabbits()

