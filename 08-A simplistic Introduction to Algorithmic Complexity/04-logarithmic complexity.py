def intToStr(i):
    '''
    Assumes i is a non negative int
    returns a decimal string representation of i
    '''

    digits = '0123456789'
    if i==0:
        return '0'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i//10
    return result

print(intToStr(5765), 'type is',type(intToStr(5765)))

'''
Output is

5765 type is <class 'str'>

Overall complexity is O(log(n))
'''