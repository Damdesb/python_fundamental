'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
numb_a = 10
numb_b = 50
list_b = []

for i in range(numb_a):
    print(i, end=' ')
for j in range(10, numb_b):
    list_b.append(j)
    stop = len(list_b)
    for k in range(10,numb_b,10):
        for m in range(10,20):
            this_elm = m+k
            if this_elm < stop:
                slice = str(list_b[this_elm])
                print(slice.ljust(10)),
print()





'''numb = 50
row = 0
new_list = []
end_list = len(new_list)
for j in range(0, 10):
    print(j, end=" ")
print()
for h in range(10, numb):
    new_list.append(h)
for k in range(end_list):
        print(k, end=" ")
print(end_list)'''
