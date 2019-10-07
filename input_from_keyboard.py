#file : input_from_keyboard.py
#author: Aaron Stevens (azs@bu.edu)
#student: Serra Jung
#description: demonstrate taking inputs from keyboard

def do_greeting():
    '''Take some inputs from the user, and display a welcome message.'''

    # prompt the user to enter their name
    name = input("What is your name? ")

    # display a welcome message with the name
    # print ("Hello, ", name) #note: 2 spaces in output
    # print ("hello,", name, ".")
    print("Hello, " + name + ".") # + operator does concatenation (joining strings together)

    # prompt the user to enter a number
    age = int(input("What is your age? "))

    # user the number in a calculation
    next_age = age + 1

    # display the result of the calculation
    print("On your next birthday, you wil be" + str(next_age) + "years old.")

