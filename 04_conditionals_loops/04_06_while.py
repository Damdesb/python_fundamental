'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
#printing multiplication table of 5 up to 1000
a = 0
c = 1000
while c <= 1000:
    a += 1
    c = a*5
    if c == 1000:
        break
    print(c)


