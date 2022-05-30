def search(l,e):

    def bsearch(l,e,low,high):
        if high == low:
            return l[low] == e
        mid  = (low+high)//2
        if l[mid] == e:
            return True
        elif l[mid] > e:
            if low == mid:
                return False
            else:
                return bsearch(l,e,low,mid-1)
        else:
            return bsearch(l,e, mid+1,high)

    if len(l)==0:
        return False
    else:
        return bsearch(l,e,0,len(l)-1)


'''
The complexity of bSearch depends only upon the number of recursive calls.
'''