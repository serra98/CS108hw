# file: tree_height.py
# author: Aaron Stevens (azs@bu.edu)
# description: demonstrate use of math library

import math

def calculate_tree_height(distance, angle):
    ''' 
    Calculate the height of a tree, by using the distance (in meters)
    to the bottom of the tree and the angle (in degrees) to the top. 

    The height of the tree is given by: height = tan(angle) * distance.
    '''
    #convert the angle from degrees to radians:
    theta = math.radians(angle)

    height = math.tan(theta) * distance 
    return height

if __name__ == '__main__': 

    #test code: 
    print('calculate_tree_height(100,30)', calculate_tree_height(100,30))   
    print('calculate_tree_height(100,45)', calculate_tree_height(100,45))
    print('The height of the tree is %.2f' % calculate_tree_height(100,45))
