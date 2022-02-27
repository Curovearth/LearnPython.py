'''
@author: Swarup Tripathy
'''

# To implement a function that meets the specification below, Use a try-except block.
# Using try-except block


def sumDigits():
    s = input('Enter a string: ')
    # Assumes s is a string 
    #         Returns the sum of the decimal digits in s
    #             For eg , if s is 'a2b3c' it returns 5
    
    sum = 0
    for i in s:
        try:
            sum = sum + int(i)

        except ValueError:
            print(i,'throwing exception')
    print(sum)

sumDigits()