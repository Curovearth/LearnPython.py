#Squaring integer, the hard way

n = int(input("Give a number please: "))
ans = 0
iterations_left = n
while(iterations_left!=0):
    ans = ans + abs(n)
    iterations_left = abs(iterations_left) - 1

print('Square of a number the hard way is ',ans)

'''
n = 3
ans = 0 | iterations_left = 3
ans = 3 | iterations_left = 2
ans = 6 | iterations_left = 1
ans = 9 | iterations_left = 0
while loop ends
print ans i.e., 9
'''