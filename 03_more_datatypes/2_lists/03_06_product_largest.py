'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''


numbers_string = input("enter 10 numbers :")
user_numbers = numbers_string.split()
numbers = []
for user_number in user_numbers:
    number_int = int(user_number)
    numbers.append(number_int)
total = sum(numbers)
print(total)

#
#print(total)
#print(user_numbers)
# m = max(user_numbers)
# print(m)




