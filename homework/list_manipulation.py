'''
Write a program to prompt you for a comma separated list of values 
(like 'a,b,3,c') and print that list reversed. Then print it with the last value
first, but the rest in the order they were entered.
'''

in_str = raw_input("enter a comma separated list: ")
in_list = in_str.split(',')
print list(reversed(in_list))
print [in_list[-1]] + in_list[0:-1]