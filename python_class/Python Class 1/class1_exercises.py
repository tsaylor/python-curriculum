####
# Class 1 Exercises 
###

# Exercise 1
print("Exercise 1")
print 39482*243

# Exercise 2
print("\nExercise 2")
print 5/2
print 5.0/2

# Exercise 3
print("\nExercise 3")
print("Hello Francesca! Hello Molly!")

# Exercise 4
print("\nExercise 4")
print("Your mother was a hamster and your father smelt of elderberries!")

# Exercise 5
print("\n Exercise 5")
print (("de" + "ed" + " ") *5)

#Exercise 6
print("\nExercise 7")
print("Here's Some Text".islower())
print("Here's Some Text".swapcase())
print(len("Here's Some Text"))

# Exercise 7
print("\nExercise 6")
"A".isupper()
"a".isupper()
"Aa".isupper()

#Exercise  8
print("\nExercise 8")
# print("THIS WILL NEVER SHOW UP! It's commented out.)


#Excercise 9
print("\nExercise 9")
#nothing to see here. 

#Exercise 10
print("\nExercise9")
# print("forgot to close the string)
print("The above line would cause an error if it wasn't commented out")

#Exercise 10
print("\nExercise 10")
print("ABCDEFG"[2])

#Exercise 11
print("\nExercise 11")
print("Hello World"[0:-1:3])

#Exercise 12
print("\nExercise 12")
print("mystery string!"[0:0])

#Exercise 13
print("\nExercise 13")
print("Do Re Mi"[0:])
print("Do Re Mi"[:])
print("Do Re Mi"[::-1])

#Exercise 14
print("\nExercise 14")
print("HEIRDTDGEXN   MQESSPSXAZGAEM"[0:-1:2])

#Exercise 15
print("\nExercise 15")
name = "Molly"


#Exercise 16
print("\nExercise 16")
print("Hello " + name + "!")

#Exercise 17
print("\nExercise 17")
age = 115
year = 2013
print(year - age)

#Exercise 18
print("\nExercise 18")
print(name.swapcase())

#Excercise 19
print("\nExcercise 19")

#Ask some questions
bestAnimals = raw_input("What is your favorite animal? (Please answer with a plural!)")
noise = raw_input("What noise does this animal make?")

#Sing a song
print("")
print("Old McDonald had a farm")
print("Ee i ee i oh")
print("And on his farm he had some " + bestAnimals)
print("Ee i ee i oh")
print("With a " + noise + " here")
print("And a " + noise + " there")
print("Old McDonald had a farm")
print("Ee i ee i oh")

print("\nExercise 20")

#This version works!
#Ask some questions
fauna = raw_input("What is your favorite animal? (Please answer with a plural!)")
noise = raw_input("What noise does this animal make?")


#Sing a song
print("")
print("Old McDonald had a farm")
print("Ee i ee i oh")
print("And on his farm he had some " + fauna)
print("Ee i ee i oh")
print("With a " + noise + " here")
print("And a " + noise + " there")
print("Old McDonald had a farm")
print("Ee i ee i oh")

#This version would break if it wasn't commented out.
#Ask some questions
##fauna = raw_input("What is your favorite animal? (Please answer with a plural!)")
##noise = raw_input("What noise does this animal make?")
##
##
###Sing a song
##print("")
##print("Old McDonald had a farm")
##print("Ee i ee i oh")
##print("And on his farm he had some " + bestAnimals)
##print("Ee i ee i oh")
##print("With a " + noise + " here")
##print("And a " + noise + " there")
##print("Old McDonald had a farm")
##print("Ee i ee i oh")

#Exercise 21
print("\nExcercise 21")

#Ask some questions
bestAnimals = raw_input("What is your favorite animal? (Please answer with a plural!)")
noise = raw_input("What noise does this animal make?")
refrain = "Ee i ee i oh"
farmOwner = "McDonald"
age = "Old"


#Sing a song
print("\n")
print(age + farmOwner + "had a farm")
print(refrain)
print("And on his farm he had some " + bestAnimals)
print(refrain)
print("With a " + noise + " here")
print("And a " + noise + " there")
print(age + farmOwner + "had a farm")
print(refrain)

#Exercise 22
print("\nExcercise 22")
list1 = [1,2,3,4]
list2 = ['a','b','c','d','e']
list3 = []
listOfLists = [list1, list2, list3]
print(len(listOfLists))

#Exercise 23
print("\nExcercise 23")
print(len(listOfLists[0]))
