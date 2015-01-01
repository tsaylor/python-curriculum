'''
Given two words, test to see if one is an anagram of the other.

Requires: lists, conditionals, maybe loops
'''

first_word = raw_input('First word: ')
second_word = raw_input('Second word: ')

if ''.join(sorted(first_word)) == ''.join(sorted(second_word)):
    print 'These words are anagrams.'
else:
    print 'These words are not anagrams.'

