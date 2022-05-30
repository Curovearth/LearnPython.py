'''
-------------- swarup tripathy's APPROACH ---------------------

Binary search is similar to the bisection search algorithm

Here we rely on the assumption that the list is ordered

- Pick an index i, that divides the list l roughly in half
- ask if l[i] == e
- if not, ask whether l[i] is larger or smaller than e
- depending upon the answer, search either left or right half of l for e.
'''

def binarySearch(l,e):
    # print('l=',l)
    length = len(l)
    # print('len=',length)
    half = length//2
    # print('half=',half)

    max_index = length - 1 

    if l[max_index] < e or l[0] > e or length==0:
        return False

    if l[half] > e:
        new_llist = l[:half]
        # print('low list=',new_llist)
        return binarySearch(new_llist,e)

    if l[half] < e:
        new_hlist = l[half:]
        # print('high list=',new_hlist)
        return binarySearch(new_hlist,e)
    
    if l[half] == e:
        return True
    
    return False


print(binarySearch([1,2,3,4,5],7))  #false
print(binarySearch([1,2,3,4,5],3))  #true
print(binarySearch([1,2,3,4,5],1))  #true
print(binarySearch([1,2,3,4,5],0))  #false