# file name: a06_raging_rabbits2.py
# Student: Serra Jung
# email: serra621@bu.edu
# description: another version of what we worked on in assignment 4. function does not take any parameters or return any value. Instead, it will be an interactive program that takes input from the keyboard calculates some values, and prints output to the console.


from a04_raging_rabbits import *
import random


#function1
def raging_rabbits2():
    '''does not take any parameters or return any value. Instead, it will be an interactive program that takes input from the keyboard calculates some values, and prints output to the console.'''
    #welcome message
    print('Welcome to Raging Rabbits!')

    #prompt the user to enter the velocity
    random_launch_velocity = random.randint(100,200)
    print("Your cannon has been calibrated with an initial launch velocity of " + str(random_launch_velocity) + " meters/second.")

    #calculate the minimum and maximum distance that the projectile could travel.
    minimum_dist = float(calculate_projectile_distance(10,random_launch_velocity))
    maximum_dist = float(calculate_projectile_distance(45,random_launch_velocity))
    
    #print min distance and max distance and get the five percent of range of possible distances. 
    print("At this velocity, you can hit a target between " + str(int(minimum_dist)) + " and " + str(int(maximum_dist)) + " meters.")
    five_percent = int((maximum_dist - minimum_dist) * 0.05)
    print("To succeed, you must land your bomb within " + str(five_percent) + " meters.")

    print()
    #get random distance 
    random_dist = random.randint(int(minimum_dist), int(maximum_dist))
    print("Your target is located at " + str(int(random_dist)) + " meters.")
    print("You get 5 tries to hit your target.") 
    
    for x in range(5):
        print("Attempt " + str(x + 1) + ":")
        print()
        
        #Enter the launch angle in degrees 
        launch_angle = int(input("Enter your launch angle (in degrees): "))

        # calculate the actual distance the projectile will travel at this angle and initial velocity, and calculate the “error”, i.e., how far off target was the shot
        traveled = float(calculate_projectile_distance(launch_angle, random_launch_velocity))
        from_the_target =  random_dist - traveled

        #from raging_rabbits.py 
        print("Your projectile traveled " + str(int(traveled)) + " meters.")
        print("Your shot was " + str(int(from_the_target)) + " meters from the target.")

        #to compare positive/negative value make it an absolute value 
        abs_value_fp = abs(five_percent)
        abs_ftp = abs(from_the_target) 

        #to see if we hit the target or have to continue 
        if int(abs_ftp) <= abs_value_fp:
            print()
            print("You hit your target!")
            break; 
        if x == 4:
            print()
            print("You were not close enough to the target. :(") 
        print()
        print()
    
    






#test code
if __name__ == '__main__':
    raging_rabbits2()
