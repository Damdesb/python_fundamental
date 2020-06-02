'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

my_dict = {}
n = range(1, 11)
for i in n:
    my_dict[i] = i*i
    print(("result = "), my_dict)