# file name: a06_pringting_shapes.py
# student : Serra Jung
# email: serra621@bu.edu
# description:  to get comfortable working with the for loop and the range function.

#function1
def print_rect(ch, width, height):
    '''  that prints out the character ch in the shape of a rectangle. The rectangle should have the dimensions width * height.'''
    for x in range(0, int(height)):
        print(ch * width)

#function2
def print_upper_left_triangle(ch, height):
    ''' prints out the character ch in the shape of an upper left triangle of size height.'''
    for x in range(0, height):
        print(ch * height)
        height = height - 1

#function3 
def print_upper_right_triangle(ch, height):
    ''' prints out the character ch in the shape of an upper right triangle of size height.'''
    empty_str = ' '
    for x in range(0, height):
        other_height = height - x
        print(empty_str * x + ch * int(other_height))

#function4
def print_lower_left_triangle(ch, height):
    '''prints out the character ch in the shape of a lower left triangle of size height.'''
    for x in range(1, height + 1):
        print(ch * x)


#function5
def print_lower_right_triangle(ch, height):
    '''prints out the character ch in the shape of a lower right triangle of size height. '''
    other_height = height - 1
    empty_str = ' '
    for x in range(1, height + 1):
        print(empty_str * other_height + ch * x)
        other_height = other_height - 1 #arrange so that we can change number of empty strings for later calculation

#function6
def print_pyramid(ch, height):
    '''prints out the character ch in the shape of a pyramid of size height. '''
    empty_str = ' '
    stars = (height - 1) * 2 
    count = 1
    for x in range(0, height):
        num_empty_str = (stars - count) // 2
        print(empty_str * int(num_empty_str + 1) + ch * int(count))
        count = count + 2 #increases two more each 

#function7
def print_diamond(ch, height):
    '''prints out the character ch in the shape of a diamond of size height.'''
    diamond_height = height // 2
    print_pyramid(ch,diamond_height)
    #use above function of print_pyramid to get print_diamond (structure is very similar) 
    empty_str = ' '
    stars = (height/2 - 1) * 2
    count = stars - 1
    for x in range(1, height):
        num_empty_str = (stars - count) // 2
        print(empty_str * int(num_empty_str + 1) + ch * int(count))
        count = count - 2 #opposite of pyramid (going down/ counts get smaller) 


#test code 
if __name__ == '__main__':
    print('print_rect(*, 7, 5):')
    print_rect('*', 7, 5)
    print('print_upper_left_triangle(*,5)')
    print_upper_left_triangle('*', 5)
    print('print_upper_right_triangle(*,5)')
    print_upper_right_triangle('*', 5)
    print('print_lower_left_triangle(*, 5)')
    print_lower_left_triangle('*', 5)
    print('print_lower_right_triangle(*, 5)')
    print_lower_right_triangle('*', 5)
    print('print_pyramid(*,5)')
    print_pyramid('*', 5) 
    print('print_diamond(*,10)')
    print_diamond('*', 10)
    print()
    
