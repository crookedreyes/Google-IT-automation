#REPLACE THIS STARTER CODE WITH YOUR FUNCTION

june_days = 30
print("June has " + str(june_days) + " days.")

july_days = 31
print("July has " + str(july_days) + " days.")

# Refactored code
def month_days(month,days):
    print(month + " has " + str(days)+" days.")

month_days("June",30)
month_days("January",31)
month_days("February",28)
