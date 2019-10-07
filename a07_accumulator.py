# file name : a07_accumulator.py
# Student: Serra Jung
# email : serra621@bu.edu
# description: few functinos to practice with accumulator pattern

def sum_of_range(start,stop,skip):
    ''' must calculate and return the sum of the numbers produced by the range function. You will use the parameters start, stop, skip as the inputs to the range function. '''
    #declare sum = 0 
    sum = 0
    for x in range(start,stop,skip):
        #add the loop 
        sum += x
    return sum
        
def replace(s, old_ch, new_ch):
    ''' process the string s and replace all occurrences of character old_ch with the character new_ch. '''
    #start with empty string
    result = ''

    for ch in s:
        if (ch == old_ch):
            #change old character to new character
            ch = new_ch
            result = result + ch
        else:
            #if it doesnt have old character, just print the original 
            result += ch
    return result 
        

            
def calculate_average():
    '''calculate the collect inputs from the keyboard, calculate and print out the average of those inputs. '''
    
    #telling what we are going to do 
    print("This program will compute the average of numerical observation.")
    
    num = int(input("How many observations do you have? "))
    
    #declare 0 for the sum 
    sum = 0
    for val in range(num):
        val = int(input("Enter next value: "))
        #add the values to make it a sum 
        sum += val
    #getting the average 
    average = sum / num
    
    #blank space 
    print()
    #return the average 

    print("The average is " + "%.2f" % average + ".")
    return average
    
            
if __name__ == '__main__':
    print('sum_of_range(1,5,1)', sum_of_range(1,5,1))
    print('sum_of_range(5,15,2)', sum_of_range(5,15,2))
    print(calculate_average())
