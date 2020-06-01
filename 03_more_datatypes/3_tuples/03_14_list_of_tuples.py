'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

num = str(input("enter a script"))
x = num.split()
print(x)
all_tuple = []
for t in x:
    if t not in all_tuple:
        all_tuple.append(t)
        print(all_tuple)


t = tuple(x[0])
tr = tuple(x[1])
print((t)+(tr))







