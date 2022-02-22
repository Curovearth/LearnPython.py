def removeDups(L1,L2):
    '''Removes any list from L1 that also occurs in L2'''
    for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)
    print('L1 =',L1,'and L2=',L2)
L1=[1,2,3,4]
L2=[1,2,5,6]
removeDups(L1,L2)

'''
The output in the case if it had been for e1 in l1[] in 3rd line comes out to be
[2,3,4]
since python keeps a tracks of where it is in the list using an internal counter that is incremented at the end of each iteration.
when l1[0] first gets removed then the counter reaches to 1 so at that time the length of list becomes 3 and l1[1] is 3 but not 2
'''