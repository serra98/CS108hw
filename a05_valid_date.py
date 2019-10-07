#file name: a05_valid_date.py
#Student: Serra Jung
#email: serra621@bu.edu
#description: use decision statements to validate some parameter data, to determine whether the parameters can be interpreted as a valid calendar date.

#function1

def is_valid_month(month):
    '''n integer parameter. The function returns True if the month is valid, and False otherwise.'''
    if(month < 0):
        return False
    elif(month > 12):
        return False
    else:
        return True

#function2

def is_leap_year(year):
    '''year is an integer parameter. The function returns True if the year is a leap year, and False otherwise.'''
    if(year % 4 != 0):
        return False
    elif(year % 400 != 0 and year % 100 == 0):
        return False
    else:
        return True

#function3

def is_valid_day_in_month(month, day, year):
    '''where month, day, and year and integer parameters. The function returns True if the day number is valid within the month, and False otherwise.'''
    #see if month is valid/true 
    if(is_valid_month == False):
        return False
    #see if days are valid in general / can't be negative number
    elif(day <= 0):
        return False
    #if everything else is true, now compare the months 
    else:
        if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            if(day <= 31):
                return True
            else:
                return False
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            if (day <= 30):
                return True
            else:
                return False
        else:
        #february has a weird dates 
            if(is_leap_year == True):
                if(day <= 28):
                    return True
                else:
                    return False
            else:
                if(day <= 29):
                    return True
                else:
                    return False

#function 4       
def get_month_name(month):
    ''' takes an integer parameter month and must return the name of the month as a string.'''
    if (month == 1):
        return 'January'
    elif (month == 2):
        return 'February'
    elif (month == 3):
        return 'March'
    elif (month == 4):
        return 'April'
    elif (month == 5):
        return 'May'
    elif (month == 6):
        return 'June'
    elif (month == 7):
        return 'July'
    elif (month == 8):
        return 'August'
    elif (month == 9):
        return 'September'
    elif (month == 10):
        return 'October'
    elif (month == 11):
        return 'November'
    elif (month == 12):
        return 'December'
    else:
        return 'Invalid Month!'
#function5
def is_valid_date(month, day, year):
    ''' takes integer parameters for the month, day, and year, and then returns True if this is a valid date and False if it is not a valid date.'''
    #check with is_valid_day_in_month
    if(is_valid_day_in_month(month, day, year) == False):
        month_name = get_month_name(month)
        print(str(month) + "/" + str(day) + "/" + str(year) + " is not a valid date, because day " + str(day) + " is not a valid date for " + month_name + ", " + str(year) + ".")
        return False
    #check if month is false or true (nonnegative/ less than or equal to 12) 
    elif(is_valid_month(month) == False):
        print(str(month) + "/" + str(day) + "/" + str(year) + " is not a valid date because " + str(month) + " is not a valid month")
        return False
    else:
        print(str(month) + "/" + str(day) + "/" + str(year) + " is a valid date.")
        return True
#test code
__name__ == '__main__'
print(is_valid_month(12))
print(is_valid_month(-1))
print(is_valid_month(31))
print(is_leap_year(2012))
print(is_leap_year(2020))
print(is_valid_day_in_month(3,33,2016))
print(is_valid_day_in_month(2,29,2016))
print(get_month_name(9))
print(get_month_name(13))
print(is_valid_date(2,29,2016))
print(is_valid_date(2,29,2017))
print(is_valid_date(2,29,2012))
#print(is_valid_date(2,29,2018))
#print(is_valid_date(1,32,2018))
#print(is_valid_date(13,7,2018))
#print(is_valid_date(9,24,2018))
#print(is_valid_date(2,29,2012))
