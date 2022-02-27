'''
@author: Swarup Tripathy
'''
def isPal(x):
    temp =x
    # temp = x[:]       # correct way - causes a copy of x to be made
    # temp.reverse()    # correct way
    temp.reverse
    if temp==x:
        return True
    else:
        return False

def silly(n):
    # result = []           # correct location
    for i in range(n):
        result = []     
        elem = input('enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('yes')
    else:
        print('no')

silly(2)