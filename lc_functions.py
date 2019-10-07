#file: lc_functions.py
#author: Aaron Stevens (azs@bu.edu)
#description: demonstrate using a list as an accumulator

def doubles(elements):
    '''processes a list of elements and returns a list of the doubles of each element.'''

    lc = [ x * 2 for x in elements ]
    return lc

    # set up accumulator variable

    #result = [] #empty list

    # process the sequence using a loop
    # for x in elements:

    # result.append(x * 2)
    # result += [x * 2]

    #return the accumulated result
    #return result 



def string_length(words):
    '''Processes a list of words and returns a list of the lengths of each word.'''

    lc = [len(w) for w in words]
    return [len(w) for w in words] 
    return lc 

    # set up accumulator variable
    # lengths = [] # empty list

    # process the sequene using a loop
    # for word in words:

    # lengths += [len(word)]

def longest_word(words):
    '''returns the longest word in a list of words.'''

    lc = [[len(w),w] for w in words]
    longest = max(lc) #produces a pair of [length, word]
    return longest[1] # use indexing to return just the word 


    
