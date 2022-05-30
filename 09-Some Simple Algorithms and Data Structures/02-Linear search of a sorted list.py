def search(l,e):
    '''
    Assumes L is a list, the elements of which are in ascending order.
    Returns true if e is in l and false otherwise
    '''
    for i in range(len(l)):
        if l[i] == e:
            return True
        if l[i] > e:
            return False
    
    return False


print(search([1,2,3,4,5],4))

'''
Here we already know that the list has been given in ascending order
'''