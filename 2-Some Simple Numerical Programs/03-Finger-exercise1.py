# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0< pwr<6 and 
# root ** pwr is equal to the integer entered by the user, If no such pair of integers exist it should print a message to that effect

'''
Writing a Pseudocode for the same

what the question is asking
    -input from user
    -prints out 2 integers i.e., it's root and pwr
    -0 < pwr < 6 
    -root**pwr = intput integer
    -if no such pair exists print something

'''

import math

a = int(input("enter an integer: "))
pwr = math.pow(a,2)
root = math.sqrt(a)
print("pwr of",a,"is",pwr)
print("root of",a,"is",root)


if 0 < pwr < 6:
    if root**pwr == a:
        print("pair exists")
    else: 
        print("No such pair exists")
else:
    print("No such pair will exist")