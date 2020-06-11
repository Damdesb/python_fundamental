'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
user_input = int(input("enter a month number: "))
month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
for month, numb in month_dict.items():
    if user_input == numb:
        print('this is:', month)
    elif user_input > 12:
        print("there is no such month")
else:
    print("done")
