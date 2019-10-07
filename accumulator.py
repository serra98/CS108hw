#File: accumulator.py
#Author: Aaron Stevens (azs@bu.edu)
#Student name: Serra Jung
#Description: Demonstrate the accumulator design pattern

# set up accumulator variable
total = 0 #intial value is 0
num_items = int(input("How many items in the cart?"))

# go through n steps in the loop, and accumulate the result:
for i in range(num_items):

    #collect the price
    price = float(input("Enter the price of this item: "))

    #add the price into the total (the accumulation)
    #total = total + price
    total += price

#use the accumulated result after the loop
print("Your total is %.2f" % total)
