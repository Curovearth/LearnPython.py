def selSort(l):
    '''
    Assumes that L is a list of elements that can be compared using >.
    Sorts L in ascending order.
    '''

    suffixStart = 0
    while suffixStart != len(l):
        # Look at each element in suffix
        for i in range(suffixStart, len(l)):
            print(f'i{l[i]} < ss{l[suffixStart]}')
            if l[i] < l[suffixStart]:
                # Swap position of elements
                l[suffixStart], l[i] = l[i], l[suffixStart]
                print('updated list =',l)

        suffixStart += 1
        print('suffixStart =',suffixStart)

    return l

print(selSort([4,2,6,1]))

'''
Working of the above code: assume l is [4,2,6,3]

suffixStart = 0
while 0!=4:
    for i in range(0,4)
    i=0:
        if 4<4:
            NA
    i=1:
        if 2<4:
            l[suffixStart], l[i] = 4,2
            l = [2,4,6,3]
    i=2:
        if 6<2:
            NA
    i=3:
        if 3<2:
            NA
suffixStart = 1
while 1!=4:
    i=1:
        if 4<4:

'''

'''
the complexity of the inner loop is O(len(L)). 
the complexity of the outer loop is O(len(L)). 
the complexity of the entire function is O(len(L)^2). 


'''