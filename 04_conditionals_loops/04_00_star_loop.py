'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''
n = 5
row = 0
while row < n:
    star = row + 1
    while star > 0:
        print("*", end=" ")
        star = star - 1
    row = row + 1
    print()




