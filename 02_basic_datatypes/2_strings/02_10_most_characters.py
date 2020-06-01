'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
#get user input
words_of_user = input("write 3 words separated by a comma")
words = words_of_user.split(",")
for word in words:
    lenght = len(word)
    result = str(lenght) + ", " + word
    print(result)












