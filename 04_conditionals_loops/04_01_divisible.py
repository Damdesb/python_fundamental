'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num = int(input("enter an number between 1 to 1, 000, 000, 000 : "))
if num % 3 == 0:
    print(num, "is divisible by 3")
else:
    print(num, "is not divisible by 3")

