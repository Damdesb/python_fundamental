'''

Write a script that completes the following tasks.

'''


def message_result(is_divisible):
    if is_divisible:
        print('the number is divisible by 4 or 7')
    else:
        print('the number is not divisible by 4 or 7')


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

def numb_divisible(divisible):
    x = 4
    y = 7
    divisible = int(divisible)
    if divisible % x == 0 or divisible % y == 0:
        return True
    else:
        return False


# take in a number from the user between 1 and 1,000,000,000

numb = (input("enter a number between 1 to 1,000,000,000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables
is_divisible_by_7_or_4 = numb_divisible(numb)

# print your new variables to display the results
# print(is_divisible_by_7_or_4)


message_result(is_divisible_by_7_or_4)
