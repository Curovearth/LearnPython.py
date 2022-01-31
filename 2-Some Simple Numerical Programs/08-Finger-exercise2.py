# let s be a string that contains a sequence of decimal numbers separated by commas
# e.g., s='1.23,2.4,3.123'. Write a program that prints the sum of numbers in s


s = '1.23,2.4,3.123'
t=0
elem = ''
total=0
t=0     #acts as a flag - no use in particular
for i in s+' ':
    elem = elem + i
    # print(elem)
    if(i==',' or i==' '):       #checks for ',' or ' ' present in the string
        total = total + float(elem[:-1])
        # print(a)
        elem = ''
        continue
    else:
        t+=1
        # print(a)
        
print("final sum is", total)

'''
Algorithm

-take the string
-to look for each element
-join the elements
-if found a ',' or ' '
    -convert to float till the -1 element
    -reset the join
-else
    -just increase the flag
'''