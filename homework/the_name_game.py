'''
Use the [:] technique for finding bits of a string to write a program that sings
"The Name Game" song (http://en.wikipedia.org/wiki/The_Name_Game) You can assume
for now that the name given is one word and begins with a consonant.
'''

name = 'Jefferson'
partial_name = name[1:]

print (name + ', ') * 2  + 'bo-b' + partial_name
print 'Banana-fana fo-f' + partial_name
print 'Fee-fi-mo-m' + partial_name
print name + '!'