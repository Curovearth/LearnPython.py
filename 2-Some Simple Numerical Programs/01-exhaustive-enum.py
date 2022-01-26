#Find the cube root of a perfect cube

x = int(input('enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1


if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x<0:
        ans = -ans
    print('Cube root of',x,'is',ans)

'''
understanding the above code

-x=27
-ans=0
-while loop:
    -0**3=0<27
    -1**3=1<27
    -2**3=8<27
    -3**3=27 break
-ans=3
-if 3^3 != 27
    -false
-else
    -if 3<0
        -false
    -finally prints the value

'''