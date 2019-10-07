# file: decisions.py
# author: Aaron Stevens (azs@bu.edu)
# student name: Serra Jung
# demonstrate decision-making with if/else logic

def print_letter_grade(grade):
    '''Print out a letter grade (A, B, C,...) based on a numeric grade.'''

    if grade > 93:
        print("You get an A!")
        
    elif grade > 90:
        print("You get an A-.")

    elif grade > 88:
        print("You get a B+.")

    elif grade > 83:
        print("You get a B.")
    else:
        print("You get an F. Better luck next time.") 
    
    
