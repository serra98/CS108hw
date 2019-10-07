#file: list_accumulator.py
#author: Aaron Stevens (azs@bu.edu)
#description: demonstrate using a list as an accumulator

def doubles(elements):
    '''processes a list of elements and returns a list of the doubles of each element.'''

    # set up accumulator variable

    result = [] #empty list

    # process the sequence using the loop

    # about choosing loop index variable
    # i -- processing a sequence of numbers (i.e., range function)
    # ch -- processing characters from a string
    # x -- processing elements from a list

    for x in elements:

        result.append(x * 2)
        # result += [x * 2]

    # return the accumulated result
    return result

def string_length(words):
    '''Processes a list of words and returns a list of the lengths of each word.'''

    # set up accumulator variable
    lengths = [] # empty list

    # process the sequence using a loop
    for word in words:

        lengths += [len(word)]


    # return the accumulated result
    return lengths
