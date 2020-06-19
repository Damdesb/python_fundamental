'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def lyrics():
    print('frere jaques')
    print('dormez vous?')

def repeat_lyrics():
    print(lyrics())
    print(lyrics())

def full_song():
    print(repeat_lyrics())
    print('sonnez les matines. Ding, dung dong')

full_song()
