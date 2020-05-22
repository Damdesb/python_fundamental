'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

#get user investment amount (invest)
invest = float(input("how much would you like to invest?"))

#define interest rate (int_rate)
int_rate = float(input("interest rate"))

#get number of year to invest (years)
years = int(input("how many years would you like to invest?"))

#print the future value (fw)
fw = (invest * (int_rate / 100) * years)
print("after", years, "years, the return will be : ", fw,"$")
