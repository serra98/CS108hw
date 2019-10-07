#
# File: a02_functions.py
# your name: Serra Jung
# your email:serra621@bu.edu
# 
#

# function 0: an example of funciton definition
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x


# put your definitions for the remaining functions below

def cube(x):
    """ returns the cube of its input """
    return x**3 

def slope(x1, y1, x2, y2): 
    """ takes four numeric inputs that specify the coordinates of two points (x1 , y1) and (x2, y2) 
    in the Cartesian plane, and that returns the slope of the line formed by two points."""
    return (y2 - y1)/(x2 - x1)

def cylinder_volume(diameter, length):
    """ calculates and returns the volume of a cylinder of a given diameter and length """
    radius = diameter/2 
    volume = 3.14159 * radius * radius * length
    return volume

# use this section for any test code:
if __name__ == '__main__':

    # Replace this line with your test code!
    print(cube(-5))
    print(slope(7, 2, 3, 4))
    print(slope(2, 3, 5, 3))
    print(cylinder_volume(10,10))
