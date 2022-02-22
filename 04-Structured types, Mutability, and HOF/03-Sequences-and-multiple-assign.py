from listprime import listPrime

def findExtremeDivisors(n1,n2):
    '''
    Assumes that n1 and n2 are postiive ints
    Returns a tuple containing the smallest common divisor > 1 and the largest common divisor of n1 and n2.
    '''
    minVal, maxVal = None, None
    result = []
    for i in range(2,min(n1,n2)):
        if n1%i==0 and n2%i==0:
            result.append(i)
    print(result)
    
    primeDivisors = []
    
    for j in result:
        if j in listPrime(max(n1,n2)):
            primeDivisors.append(j)
        else:
            continue
    minVal = min(primeDivisors)
    maxVal = max(primeDivisors)
    print('min value',minVal,'max value',maxVal)


print(findExtremeDivisors(48,30))
