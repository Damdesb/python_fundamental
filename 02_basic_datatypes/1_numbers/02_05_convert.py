'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#convert an int to a float
a = 2
b = float(a)
print(b)

#convert float to int
c = 3.2
d = int(c)
print(d)

#floor division ising float and int
print(c//a)

#use two users inputted values to perform multiplication
user_1 = int(input("please enter a value :"))
user_2 = int(input("please enter a value :"))

total = (user_1 * user_2)
print(total)
