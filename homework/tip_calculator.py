'''
Write a program that splits a restaurant bill and calculates the tip. Write a
prompt to enter the bill total, the tip percentage, and the number of people
who will be splitting the bill, and output the bill and tip amounts for each
person.

requires: input, variables, math
'''

bill_total = int(raw_input('Bill total: '))
tip_percentage = int(raw_input('Tip percentage: '))
num_payers = int(raw_input('Number of payers: '))

tip_total = bill_total * (tip_percentage / 100.0)

# optional: use the math library to limit your total to two decimal digits
import math
tip_total = math.floor(tip_total * 100) / 100

grand_total = bill_total + tip_total

bill_per_person = bill_total / num_payers
tip_per_person = tip_total / num_payers
total_per_person = bill_per_person + tip_per_person

print
print "Bill amount per person: " + str(bill_per_person)
print "Tip amount per person: " + str(tip_per_person)
print "Total per person: " + str(total_per_person)
