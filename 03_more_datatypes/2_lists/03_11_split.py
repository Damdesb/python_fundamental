'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

users_input = input("write a sentence")
method_split = users_input.split(" ")
print(method_split)
most_word = []
for most_word in method_split:
    count = users_input.count(most_word)
    if count > 1:
        print(most_word)





