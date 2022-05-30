from o08_Exponential_Complexity1 import getBinaryRep

def genPowerSet(l):
    '''
    Assumes L is a list
    Returns a list of lists that contains all possible combinations of the elements of L. Eg. if L is [1,2] it will return a list with elements [],[1],[2],[1,2] 
    '''
    powerSet = []
    for i in range(2**len(l)):
        subset = []
        binStr = getBinaryRep(i,len(l))
        for j in range(len(binStr)):
            if binStr[j]=='1':
                subset.append(l[j])
        powerSet.append(subset)
        
    return powerSet


print(genPowerSet([1,2,3]))