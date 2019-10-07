# file name: a05_find_min.py
# Student: Serra Jung
# email: serra621@bu.edu
# Instructor: Aaron Stevens
# Description: A warm-up exercise to using decision logic in your program, you will write a function to evaluate parameters and return a value


def my_min(a,b):
    '''takes 2 parameters and returns the minimum of these two. Inside your function, use decision logic to identify and return the minimum value among the parameters.'''
    if a < b:
        return a
    else:
        return b

def find_min(a,b,c):
    ''' takes 3 parameters and returns the minimum of these three. Inside your function, use decision logic to identify and return the minimum value among the parameters'''
    if a < b:
        if a < c:
            return a
        else:
            return c 
    else: 
        if b < c:
            return b
        else:
            return c 
        



#test code 
if __name__ == '__main__':
    print('my_min(1,2)', my_min(1,2))
    print('my_min(2,1)', my_min(2,1))
    print('my_min(2,2)', my_min(2,2))
    print('find_min(1,2,3)', find_min(1,2,3))
    print('find_min(2,1,3)', find_min(2,1,3))
    print('find_min(3,2,1)', find_min(3,2,1))
    print('find_min(3,3,3)', find_min(3,3,3))
