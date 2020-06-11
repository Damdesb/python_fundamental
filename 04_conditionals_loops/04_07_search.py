'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
user_input = int(input("enter a number between 0 to 1 000 000 000: "))
guessing = True

while guessing:
    user_guess = int(input("guess the number:"))
    if user_guess == user_input:
        print("this is right!!")
        #this causes the while loop to stop
        guessing = False
    elif user_guess < user_input:
        print("this is too low")

    else:
        print("this is too high")

else:
    print("the search is over")
