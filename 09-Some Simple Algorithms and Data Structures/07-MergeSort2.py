# Reference Video = https://www.youtube.com/watch?v=cVZMah9kEjI by FelixTechTips
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


test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 8]
print(mergeSort2(test))

'''
Output [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8]
'''