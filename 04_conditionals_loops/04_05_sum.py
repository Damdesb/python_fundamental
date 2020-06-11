'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
first_numb = int(input("enter your first number: "))
second_numb = int(input("enter your second number"))

new_list = []
for i in range(first_numb, second_numb+1):
    new_list.append(i)
print("the sum is: ", sum(new_list))





