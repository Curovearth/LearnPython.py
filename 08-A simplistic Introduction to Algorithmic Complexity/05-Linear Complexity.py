from cv2 import add


def addDigits(s):
    '''
    Assumes s is a str each character of which is a decimal digit.
    Returns an int that is the sum of the digits in s
    '''
    val = 0
    for c in s:
        val += int(c)
    return val


print(addDigits('432'))

'''
Output is 
 9

 complexity of the function is O(len(s))
'''