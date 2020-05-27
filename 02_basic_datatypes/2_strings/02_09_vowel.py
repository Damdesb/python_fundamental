'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
#get a sentence from user (sentence)
sentence = set(input("write a sentence : "))
vowels = set('aeiou')
numb_vowels = (vowels & sentence)
print((len(numb_vowels)), ("vowels in this sentence"))
print(numb_vowels)

for vowels in sentence:
    enumerate(vowels)
    print(vowels)




