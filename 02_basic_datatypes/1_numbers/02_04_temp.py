'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
#get users input (f)
user_input_fahrenheit = int(input("temp in Fahrenheit is :"))
#convert fahrenheit to celsius
celsius = (user_input_fahrenheit - 32) * (5 / 9)

print(user_input_fahrenheit, ("degrees fahrenheit ="),(celsius), ("degrees celcius"))
