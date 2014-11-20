'''
Make a version of the game Mastermind. Use your random string generator to make
a secret string, print the length of the string, then prompt the user for a
guess of what the string is. Compare their guess to the secret string and print
how many characters the guesser got correct. Keep prompting for another guess
until they get it right or they enter "quit".

(random string generator assignment: 
    Make a function that returns a random string. Use random.randint() from the
    random library to create a list between 5 and 15 elements long, populated
    with random integers between 0 and 25. Then use that list to make a random
    string, with 0 = a, 1 = b, ... 25 = z.)
'''
import random

def random_string(length):
    # I modified the function to take a length parameter.
    # Long words were hard to guess.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rand_num_list = []
    for length in range(length):
        rand_num_list.append(random.randint(0,25))
    random_string = ''
    for num in rand_num_list:
        random_string += letters[num]
    return random_string

secret_string = random_string(5)

print "Word length is " + str(len(secret_string))

cmd = None
while cmd != 'quit':
    cmd = raw_input('Guess the word (or quit): ')
    if cmd != 'quit':
        if cmd == secret_string:
            print "You got it!"
            cmd = 'quit'
        else:
            num_correct = 0
            for i in range(len(secret_string)):
                if secret_string[i] == cmd[i]:
                    num_correct += 1
            print "You guessed " + str(num_correct) + " letters correctly."

print "Thanks for playing!"


