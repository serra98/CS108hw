# file: string_accumulator.py
# author: Aaron Stevens (azs@bu.edu)
# description: demonstrate the accumulator pattern with string result

def spaced_out(s):
    '''Process a string one character at a time to produce a result where each character is separated by a space.'''

    # set up accumulator variable
    result = '' #an empty string

    #process sequence with a loop to build result
    for ch in s:

        result += ch + ''

    #return result
    return result

def backwards(s):
    '''process a string one character at a time to produce a result which contains the string in reverse order.'''

    # set up accumnulator variable
    result = '' #empty string

    # process sequence with a loop to build result
    for ch in s:

        result = ch + result #prepend the new character ch

    # return result
    return result
