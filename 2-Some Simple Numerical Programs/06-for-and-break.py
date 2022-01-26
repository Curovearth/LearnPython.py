#Find the cube root of a perfect cube

x = int(input("Enter an integer: "))
for ans in range(0,abs(x)+1):
    if ans**3 >= abs(x):
        break

print(ans)
if ans**3 != abs(x):
    print(x,"is not a perfect cube")
else:
    if x<0:
        ans = -ans
    print("Cube root of",x,"is",ans)

'''
What is actually happening in the code - An example of exhaustive enumeration algorithm

x=8
ans in range(0,8+1)
    -0^3 >= 8 is false
    -1^3 >= 8 is false
    -2^3 >= 8 is true
        -break and ans=2
    
if 2^3 != 8
    -false
else:
    -if 8<0
        -false
    -finally prints

'''