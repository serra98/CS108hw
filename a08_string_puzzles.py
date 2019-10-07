# file name: a08_string_puzzles.py
# Student name: Serra Jung 
# email: serra621@bu.edu 
# description: None of these problems requires if/else logic, and none requires nested loops.

def reverse(s): 
    ''' takes a string s and returns  a version of that string in reverse order. '''
    #we reverse the string 
    s = s[::-1]
    return s

def every_other(s):
    ''' takes a string s and returns a version of that string with every other character removed.'''
    #we print every other character 
    s = s[0::2]
    return s

def outside_chars(s, n):
    '''takes a string s and a number n and returns a version of s with only the first n characters from the beginning and the end of the string.'''
    #adding first n characters from the beginning (first) and the end (last) of the string
    first = s[0:n]
    last = s[-n::1]
    result = first + last
    return result

def triple_outsides(s):
    '''takes a string s, and returns a version of that string with only the first 3 characters from the beginning and end of s tripled, and the rest of the characters in the middle.'''
    #double the first letter 
    first = s[0] * 2
    #double the second letter 
    last = s[-1] * 2
    #add them (then it will be triple because the original already has the letter in it) 
    result = first + s + last
    return result

def swap_halves(s):
    '''takes a string s and returns a new string in which the two halves of the string have been swapped.'''
    #to swap 
    first = int(len(s)/2)
    second = int(len(s)/2 - 1)

    #if length of s is even 
    if len(s) % 2 == 0:
        result = s[first:] + s[:second]
        return result
    #when it's odd 
    else:
        result = s[first:] + s[:second:]
        return result
                                          
def slice_middle(s):
    '''takes a string s and returns a substring which is the middle half of the string.'''

    #get the first quarter 
    first_quarter = int(round(len(s)/4))

    #get rid of last quarter 
    drop_last_quarter = len(s) - first_quarter

    #add those strings 
    result = s[first_quarter:drop_last_quarter]
    return result
    




if __name__ == '__main__':
     print('reverse("blackbird")', reverse("blackbird"))
     print('every_other("across the universe")',every_other("across the universe"))
     print('outside_chars("yesterday", 2)',outside_chars("yesterday", 2))
     print('triple_outsides("cayenne")', triple_outsides("cayenne"))
     print('swap_halves("good day sunshine ")',swap_halves("good day sunshine ") )
     print('swap_halves("good day")',swap_halves("good day") )
     print('slice_middle("all together now")',slice_middle("all together now"))
     print('slice_middle("she came in through the bathroom window!")',slice_middle("she came in through the bathroom window!"))
