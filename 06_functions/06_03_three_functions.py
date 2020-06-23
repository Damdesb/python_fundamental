'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def lyrics():
    return 'frere jaques', 'dormez vous?'



def repeat_lyrics():
    return lyrics(), lyrics()


def full_song():
    print(repeat_lyrics())
    print('sonnez les matines. Ding, dung dong')


full_song()
