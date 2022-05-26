def isSubset(l1,l2):
    '''
    Assumes l1 and l2 are lists
    returns true if each element in l1 is also in l2 and false otherwise
    '''
    for e in l1:
        matched = False
        for f in l2:
            if e == f:
                matched = True
                break
        if not matched:
            return False
    return True

print(isSubset([2,3,4,5,6],[4,5,6,7,8]))

'''
e = 2
    matched = false
    f = 4
    f = 5
    f = 6
    f = 7
    f = 8
    return False

Complexity of the function is O(len(l1)*len(l2))
'''