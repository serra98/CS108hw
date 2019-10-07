from a03_tvm import present_value_of_annuity
from a03_tvm import annuity_payment
from a03_tvm import dollar_format

def life_cycle_model():
    ''' '''
    rate = float(input('Enter the current inflation-indexed risk-free rate of return: '))
    age = int(input('Enter your age now: ')
    re_age = int(input('Enter your expected retirement age: ')
    annual_income = int(input('Enter your current annual income: ')

    remaining = r_age - age

    print('You have ' + str(remaining) + ' remaining working years with an income of ' + dollar_format(annual_income) + ' per year.'


        if__name__ == '__main__':
          life_cycle_model()
