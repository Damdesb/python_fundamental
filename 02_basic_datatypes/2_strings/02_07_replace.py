'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

#get sentence from user (sentence)
sentence = input("write a sentence")
#get symbol from user (symbol)
symbol = input("write a symbol")
#get first letter (first_letter)
first_letter = sentence[0]
print(first_letter)
#replace all occurences of the first letter with symbol
print(sentence.replace(first_letter, symbol))
