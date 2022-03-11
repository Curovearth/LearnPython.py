# Finger Exercise: Implement a function that satisfies the specifications of
'''
def findAnEven(L):
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number
'''

def findAnEven(L):
    for i in L:
        if i%2==0:
            print(i)
            break
        else: 
            raise Exception(i,'not allowed')

list = [2,3,4]
findAnEven(list)