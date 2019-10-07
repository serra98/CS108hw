# file:  a03_lcm.py
# email: serra621@bu.edu
# student : Serra Jung
# description: life_cycle_model of a person income and etc 

from a03_tvm import present_value_of_annuity
from a03_tvm import annuity_payment
from a03_tvm import dollar_format

def life_cycle_model():
    ''' will interact with the user to collect inputs and display outputs, and will not have a return value.'''

    rate = float(input("Enter the current inflation-indexed risk-free rate of return: "))
    age = int(input("Enter your age now: "))
    r_age = int(input("Enter your expected retirement age now: "))
    income = int(input("Enter your current annual income: "))
    print()

    w_year = r_age - age
    print('You have ' + str(w_year) + ' remaining working years with an income of ' + dollar_format(income) + ' per year.')

    human_cap = present_value_of_annuity(rate, w_year, income)
    print('The present value of your human capital is about ' + dollar_format(human_cap) + '.')
    print()
    
    assets = int(input('Enter the value of your financial assets: '))

    econet_worth = human_cap + assets
    print('Your economic net worth is: ' + dollar_format(econet_worth))
    print()

    l_standard = annuity_payment(rate, 100 - age, econet_worth)

    print('Your sustainable standard of living is about ' + dollar_format(l_standard)+ ' per year')
    saving = income - l_standard
    print('To achieve this standard of living to age 100, you must save ' + dollar_format(saving) +' per year.')
    



    
    
    
