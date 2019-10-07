#
# file: a01_change.py
# author: Serra Jung
# CS108

# To make the autograder script work, you will need to follow these constraints:
# * You must have variables named price, change, quarters, dimes, nickels,
#   and pennies. You may include any additional variables you choose.
# * In your finished code, the only place in your file that may contain print( )
#   statements is inside the if __name__ == '__main__': section at the bottom of
#   the file (see starter code) – otherwise the autograder script will fail.
#   You may use print statements elsewhere in your code while you are developing
#   and testing, but you must comment out those print statements before submission. 
#   The reason for this will be explained further next class.

# once you have a working solution, you should change this line to test other 
# starting values, e.g., 68 cents, 69 cents, etc. to ensure that your calculations 
# work for each value.

def change():
    price = int(input('Inpur your price: '))
    change = 100 - price
    pennies = 1
    nickels = 5
    dimes = 10
    quarters = 25
    

    # do all of your computations here:

    qua_num = change // quarters
    afterQuarter = change - (quarters * qua_num)
    di_num = afterQuarter // dimes
    afterDimes = afterQuarter - (dimes * di_num)
    nick_num = afterDimes // nickels
    afterNickels = afterDimes - (nickels * nick_num)
    penn_num = afterNickels // pennies
    
    print('The price is ', price,'cents, and Your change is ', change,' cents. ' )
    print("Here's the change that uses the fewest coins: ")
    print('pennies:',penn_num)
    print('nickels:',nick_num)
    print('dimes:',di_num)
    print('quarters:',qua_num)




if __name__ == '__main__':

    # put all print statements in this section, indented by one tab, e.g., :
          
    
    
    change()
