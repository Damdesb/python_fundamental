'''

Write a script that completes the following tasks.

'''
# take in a number from the user between 1 and 1,000,000,000

numb = int(input("enter a number between 1 to 1,000,000,000: "))


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean


def numb_divisible(divisible):
    x = 4
    y = 7
    if numb % x == 0 or numb % y == 0:
        print(True, '- the numb is divisible by 4 or 7')
    else:
        print('The number is not divisible by 4 or 7')


# call your functions, passing in the user input as the arguments, and set their output equal to new variables


# print your new variables to display the results

numb_divisible(numb)
