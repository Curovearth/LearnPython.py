def fact(x):
    if x<0:
        return None
    elif x==0 or x==1:
        return 1
    else:
        return fact(x-1)*x

n=int(input("enter a number: "))
print('factorial of',n,'is',fact(n))