# a01_four_fours.py - Assignment 1
# your name: Serra Jung
# your email:serra621@bu.edu
# Computes the integers 0 through 4 using exactly 4 fours, and a creative combination 
# of arithmetic operators.
#

# this statement creates a variable called 'zero' which is the result of the expression 4 + 4 - 4 - 4
zero = 4 + 4 - 4 - 4

# continue to create variables 'one', 'two', 'three', and 'four' below.

one = 4 // 4 + 4 - 4
two = 4 * 4 // (4 + 4)
three = (4 + 4 + 4) // 4
four = 4 * (4 - 4) + 4





# test code below, do not modify!
if __name__ == '__main__':
    
    # this statement prints out the value of each variable, if they have been defined:

    for x in ['zero', 'one', 'two', 'three', 'four']:
        if x in dir():
            print(x + ' = ', eval(x))

