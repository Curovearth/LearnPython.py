def mergeSort2(l):

    if len(l) > 1:
        left_arr = l[:len(l)//2]    # beginning to middle
        right_arr = l[len(l)//2:]   # middle to end 
        # print('left =',left_arr)                                                     
        # print('right =',right_arr)

        # recursion 
        mergeSort2(left_arr)
        mergeSort2(right_arr)
        # after recursion both left and right arr are in sorted order.
        # after two arr are in sorted order you need to merge them

        # merge
        i,j=0,0 # array idx for left and right array
        k = 0   # merged array idx

        while i < len(left_arr) and j < len(right_arr):
            # Performing comparisons

            if left_arr[i] < right_arr[j]:  # left arr smaller than right arr
                l[k] = left_arr[i]
                i += 1
            else:                           # right arr smaller than left arr
                l[k] = right_arr[j]
                j += 1
            k += 1
        print('l1 =',l)

        # Now imagine if we looked at each element from the right array and transferred the element from the right array to the merged array, there is nothing to compare the left over elements of the left array
        # considering the case where we want to transfer elements from the left array to the merged array without considering the right array.
        
        while i < len(left_arr):
            l[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            l[k] = right_arr[j]
            j += 1
            k += 1
        # print('l2 =',l)
    return l


def lastNameFirstName(name1,name2):
    arg1 = name1.split(' ')
    print('arg1 =',arg1)
    arg2 = name2.split(' ')
    print('arg2 =',arg2)
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:                           # last names the same sort by first name
        return arg1[0] < arg2[0]


def firstNameLastName(name1,name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else:
        return arg1[1] < arg2[1]

# print(lastNameFirstName('swarup tripathy','yatharth agarwal'))

L = ['Tom Brady','Eric Grimson','Gisele Bundchan']
newL = mergeSort2(L)
print('Sorted by last name:',newL)
newL = mergeSort2(L)
print('Sorted by first name:',newL)
