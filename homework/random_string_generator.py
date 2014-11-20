'''
Make a function that returns a random string. Use random.randint() from the
random library to create a list between 5 and 15 elements long, populated with
random integers between 0 and 25. Then use that list to make a random string,
with 0 = a, 1 = b, ... 25 = z.
'''
import random


def random_string():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rand_num_list = []
    for length in range(random.randint(5, 15)):
        rand_num_list.append(random.randint(0,25))
    random_string = ''
    for num in rand_num_list:
        random_string += letters[num]
    return random_string


print random_string()
