'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
numbers_string = input("enter a list of numbers : ")
numbers_list = numbers_string.split()

list_of_numbers = []

for number in numbers_list:
    number_int = int(number)
    list_of_numbers.append(number_int)
    print(list_of_numbers)

#sort the list of numbers
list_of_numbers.sort()
print(list_of_numbers)

#sort the numbers in tuples of 2 in a list


size_list = len(list_of_numbers)

first_num = 0
second_num = first_num + 1

new_number_list = []

for i in range(size_list):
    if i < size_list and second_num < size_list:
        new_tuple = (list_of_numbers(first_num), list_of_numbers(second_num))
        new_number_list.append(new_tuple)
        first_num = first_num + 2
        second_num = first_num + 1
    elif second_num == size_list:
        new_tuple = (list_of_numbers(-1, 0))
        new_number_list.append(new_tuple)
        break

print(new_number_list)