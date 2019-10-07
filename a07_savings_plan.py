#file name: a07_savings_plan.py
#student name: Serra Jung 
#email: serra621@bu.edu 
#description: Accumulating interest on your savings 

def print_monthly_savings_accumulation(rm,amount_saved,initial_balance = 0):
    '''produce a table of outputs as well as returning a numeric value.'''
    savings = 0
    interestEarned = 0

    print("Month\tInterest\tAmount\t\tBalance")
    for month in range(1,13):
        
        #getting the interest 
        interest = initial_balance * rm

        #add interests  
        interestEarned += interest
      

        #balance goes up so you keep adding  
        initial_balance += amount_saved + interest 
        

        #update savings 
        savings += amount_saved

        #for the format of table 10.2f works the best 
        print(str(month) + "\t$%10.2f" %  (interest) + "\t$%10.2f" % (amount_saved) + "\t$%10.2f" % (initial_balance))
    print()
    print("Total amount saved:    $ %0.2f" % savings)
    print("Total interest earned: $ %0.2f" % interestEarned)
    print("End of year balance:   $ %0.2f" % initial_balance)
    print() 
    return initial_balance 

def interactive_savings_plan():
    ''' create an interactive program which should prompt the user for inputs, and then delegate work to the print_monthly_savings_accumulation function from above.'''
    #put user inputs for goals, interest_rate, how many years 
    saving_goals = int(input("Enter your savings goal in dollars: "))
    interest_rate = float(input("Enter the expected annual rate of return (i.e. 0.03): "))
    time = int(input("Enter time until goal in years: "))

    #get monthly rate by dividing by 12 
    monthly_rate = interest_rate / 12
    #calculating amount using the formula provided 
    amount = (monthly_rate * saving_goals)/ (((1 + monthly_rate)**(12 * time)) - 1)

    #print how much you have to save every month 
    print("To reach your goal in 2 years, you will need to save" , "$%.2f" % (amount),"per month")
    
    print()

    #start with balance 0 (intial balance = 0) 
    balance = 0
    for yr in range(1,time + 1):
        print("Summary for year",yr,": ")

        #update balance for other years not to start from 0 
        balance = print_monthly_savings_accumulation(monthly_rate, amount, balance)
    
        print()

if __name__ == '__main__':
    print_monthly_savings_accumulation(0.04/12, 500)
    interactive_savings_plan() 
