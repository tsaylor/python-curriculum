'''
Write a program that asks a user for a word and outputs a list with the letters from the word in a random order. Hint: use the list() function to convert a string to a list (myList = list(myString)) and ''.join(myList) to convert a list back to a string.

Requires: lists, libraries, loops
'''
import random

word = raw_input('Word: ')
wlist = list(word)

# random.shuffle() would do exactly what we want, but that's too easy.
for i in range(random.randint(20,50)):
    idx = random.randint(0, len(word)-1)
    wlist.append(wlist.pop(idx))

print wlist
