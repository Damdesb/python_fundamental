'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
'''unique_list = list(set(list_))
print(unique_list)

new_list = []
for x in list_:
    if x not in new_list :
        new_list.append(x)
print(new_list)'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
new_list = []
for number in list_:
    count = list_.count(number)
    if count == 1:
        print(number)



'''for x in list_:
    if x not in new_list:
        new_list.append(x)
print(new_list)'''








'''list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
for x in list_:
    if x not in unique_list:
        unique_list.append(x)
    if x in list_
         and in unique_list:
        unique_list.remove(x)
print(unique_list)'''
