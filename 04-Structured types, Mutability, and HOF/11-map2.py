list1 = [1,28,36]
list2 = [2,57,9]

for i in map(min,list1,list2):
    print(i,end=" ")

'''
What exactly is happening here?

we map l1 and l2 simultaneously by applying inbuilt 'min' function over it since it requires two arguments
'''