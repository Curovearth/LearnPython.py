def getBinaryRep(n,numDigits):
    '''
    Assumes n and numDigits are non negative ints
    Returns a str of length numDigits that is a binary representation of n
    '''
    result = ''
    while n>0:
        result = str(n%2)+result
        n = n//2
        
    if len(result)>numDigits:
        # return len(result)
        raise ValueError('not enough digits')
    for i in range(numDigits-len(result)):
        result = '0'+result
    return result

