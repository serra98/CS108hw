#
# File: a02_stats.py
# your name: Serra Jung
# your email: serra621@bu.edu
# 
#


#functions 
def calc_sum(a, b, c, d, e):
    """ calculate and return the sum of the 5 parameters """
    return a + b + c + d + e

def calc_mean(a, b, c, d, e):
    """ calculate and return the mean of the 5 parameters """ 
    sum = calc_sum(a, b, c, d, e)
    return sum / 5 

def calc_variance(a, b, c, d, e):
    """ calculate and return the variance of the 5 parameters. """
    mean = calc_mean(a, b, c, d, e)
    sq_result = (a - mean)**2 + (b - mean)**2 + (c - mean)**2 + (d - mean)**2 + (e - mean)**2
    result = sq_result / 5 
    return result

def calc_stdev(a, b, c, d, e): 
    """ calculate and return the std of the 5 parameters. """
    result = calc_variance(a, b, c, d, e) ** (1/2)
    return result 

 # unit test code:
if __name__ == '__main__':
    
    # declare variables with which to test the functions
    a = 8
    b = 9
    c = 10
    d = 9
    e = 8
    # call the function to calculate the sum:
    sum_of_obs = calc_sum(a, b, c, d, e)
    mean_of_obs = calc_mean(a, b, c, d, e)
    variance_of_obs = calc_variance(a, b, c, d, e)
    stdev_of_obs = calc_stdev(a, b, c, d, e)

    # print the result
    print("The sum of observations is:", sum_of_obs)
    print("The mean of observations is:", mean_of_obs)
    print("The variance of observations is:", variance_of_obs)
    print("The standard deviation of observations is:", stdev_of_obs)