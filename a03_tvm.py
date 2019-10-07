# file : a03_tvm.py
# student : Serra Jung
# BU email: serra621@bu.edu
# description: function fv_lump_sum(r, n, pv) to calculate and return the future value of a lump sump pv invested at the periodic rate r for n periods.

def future_value(r, n, pv):
    '''to calculate and return the future value of a lump sunmp pv invested at the periodic rate r for n periods.'''

    #get future value
    fv = pv*((1+r)**n)

    #return the future value
    return fv


    
def present_value(r, n, fv):
    ''' to calculate and return the present value of a lump sum fv to be received in the future, discounted at the periodic rate r for n periods.'''

    #get present value
    pv = fv / ((1+r)**n)

    #return the present value
    return pv


def present_value_of_annuity(r, n, pmt):
    '''calculate and return the present value of an annuity of pmt to be received each period for n periods, discounted at the rate r.'''

    #get present value
    bpmt = (1 - (1+r)**(-n)) / r
    pv = pmt * bpmt

    #return the presetn value of annuity
    return pv


def annuity_payment(r, n, pv):
    '''calculates the amortizing annuity payment for a present value of pv to be repaid at a periodic interest rate of r for n periods.'''

    #calculate the amortizing annuity
    bpmt = 1 - (1 + r)**(-n)
    pmt = (r * pv)/bpmt

    #return the annuity_payment
    return pmt


def dollar_format(amount):
    '''create a formatted string representatino of a numeric amount.'''

    #convert
    amount = int(amount)
    amount = '$' + str(amount)

    #return amount
    return amount
    
