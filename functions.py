#file : functios.py
#author: Aaron Stevens (azs@bu.edu)
#student name: Serra Jung
#description: introduction to functions
# syntax, calling function, writing test cases

def triple(x):
    """ this function returns the triple of the parameter x."""
    return 3*x

def calc_perimeter(w,l):
    """ returns the perimeter of a rectangle."""

    return 2 * w + 2 * l

def calc_area_circle(diameter):
    """ returns the area of a circle with diameter d. """

    radius = diameter / 2
    area = radius * radius * 3.14159
    return area

def mystery(a, b, c,):
    """ We don't know what this function does. """
    x = a * 2 + b - c
    y = 3 * b - 4 * c // 2
    return x - y

## our test code
print('triple(14)',triple(14))
print('triple(-4)',triple(-4))
print('calc_perimeter(4,3)',calc_perimeter(4,3))
print('calc_area_circle(10)',calc_area_circle(10))
print('mystery(3,4,5)',mystery(3,4,5))

print(help(triple))




