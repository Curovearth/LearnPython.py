'''
Program 1
'''

l = [x**2 for x in range(4)]
print(l)

'''
Program 2
'''

mixed = [1,2,'a',3,4.0]
p = [x**2 for x in mixed if type(x)==int]
print(p)