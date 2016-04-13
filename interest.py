# Prompt the user for an Initial Balance (and save to a variable)
# use the float() function to convert the input into a number.
# ibal = input("What is your initial balance? ")
# ibalf = float(ibal)
balance = float(input("Initial balance: "))

# Prompt the user for an Annual Interest % (and save to a variable)
# use the float() function to convert the input into a number
# aint = input("What is your Annual Interest %? ")
# prct = float(aint)
interest = float(input("Annual Interest %: "))

# change the percentage number into a decimal (e.g. 6 turns into .06, 5 turns into .05, etc).
# remember to save your new value to a variable!
# dec = prct / 100
interest = interest/100

# Prompt the user for a Number of years (and save to a variable)
# use the int() function to convert the input into an integer
# num = input("Number of years? ")
# inum = int(num)
years = int(input("Years: "))

# Calculate the total value following the formula.
# You can use multiple steps and variables if necessary.
# Note that n = 12
# totval = round(ibalf * (1 + (dec/12))**(12*inum),2)
new_balance = round((balance*(1+(interest/12))**(12*years)),2)

# Calculate the interest earned based on the above value and the initial balance
# intear = round((totval-ibalf),2)
interest_earned = round((new_balance - balance),2)

# Output the interest earned
# print(intear)
output = "Interest earned in "+str(years)+" years: $"+str(interest_earned)
print(output)

# Output the total value
# print(totval)
print("Total value after "+str(years)+" years: $"+str(new_balance))