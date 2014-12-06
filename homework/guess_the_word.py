'''
Rewrite the previous program to be a game where the user has to guess the word that the computer came up with.

(Previous: Write a program that asks a user for a word and outputs a list with the letters from the word in a random order. Hint: use the list() function to convert a string to a list (myList = list(myString)) and ''.join(myList) to convert a list back to a string.)

Requires: lists, libraries, loops, conditionals
'''
import random

words = ['open','ten','seem','simple','together','several','next','vowel','whit','toward','children','war','begin','lay','got','against','walk','pattern','example','slow','ease','center','paper','love','often','person','always','money','music','serve','those','appear','both','road','mark','map','book','science','letter','rule','until','govern','mile','pull','river','cold','car','notice','feet','voice','care','fall','second','power','group','town','carry','fine','took','certain','rain','fly','eat','unit','room','lead','friend','cry','began','dark','idea','machine','fish','note','mountain','wait','north','plan','once','figure','base','star','hear','box','horse','noun','cut','field','sure','rest','watch','correct','color','able','face','pound','wood','done','main','beauty','enough','drive','plain','stood','girl','contain','usual','front','young','teach','ready','week','above','final','ever','gave','red','green','list','oh','though','quick','feel','develop','talk','sleep','bird','warm','soon','free','body','minute','dog','strong','family','special','direct','mind','pose','behind','leave','clear','song','tail','measure','produce','state','fact','product','street','black','inch','short','lot','numeral','nothing','class','course','wind','stay','question','wheel','happen','full','complete','force','ship','blue','area','object','half','decide','rock','surface','order','deep','fire','moon','south','island','problem','foot','piece','yet','told','busy','knew','test','pass','record','farm','boat','top','common','whole','gold','king','possible','size','plane','heard','age','best','dry','hour','wonder','better','laugh','true','thousand','during','ago','hundred','ran','am','check','remember','game','step','shape','early','yes','hold','hot','west','miss','ground','brought','interest','heat','reach','snow','fast','bed','five','bring','sing','sit','listen','perhaps','six','fill','table','east','travel','weight','less','language','morning','among']

word = random.choice(words)
wlist = list(word)
for i in range(random.randint(20,50)):
    idx = random.randint(0, len(word)-1)
    wlist.append(wlist.pop(idx))
scrambled = ''.join(wlist)

print "The scrambled word is " + scrambled

guess = None
while guess not in (word, 'quit'):
    guess = raw_input('Your guess: ').lower()
    if guess == word:
        print 'You got it!'
    elif guess != 'quit':
        print 'Try again'
print 'Goodbye'

