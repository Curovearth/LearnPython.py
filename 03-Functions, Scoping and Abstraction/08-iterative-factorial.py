
def factorial(x):
    ans=1
    if(x<0):
        return None
    elif (x==0 or x==1):
        return 1
    else:
        for i in range(1,x+1):
            ans = ans*i
        return ans


n = int(input("enter a number:"))
print('factorial of',n,'is',factorial(n))