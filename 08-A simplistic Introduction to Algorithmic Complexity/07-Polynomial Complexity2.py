def intersect(l1,l2):
    '''
    Assumes: l1 and l2 are lists
    returns a list without duplicates that is the intersection of l1 and l2
    '''
    # Build a list containing common elements
    common = []
    for e in l1:
        for f in l2:
            if e == f:
                common.append(e)
                break
    
    # Build a list without duplicates
    result = [] 
    for l in l1:
        if l not in common:
            result.append(l)
    for c in l2:
        if c not in common:
            result.append(c)
    return (common,result)

print(intersect([1,2,3],[2,3,4]))
    

'''
Output is 

([2, 3], [1, 4])

complexity of the function is O(len(l1),len(l2))
'''