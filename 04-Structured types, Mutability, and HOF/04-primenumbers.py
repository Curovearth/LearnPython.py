# To check if the number is prime or not

def isPrime(n):
    result =()  # initiating a tuple
    if n==1 or n<=0:    # if the input is either 1 or 0 or less than 0, they aren't prime
        None
    else:
        for i in range(1,n+1):  # range is set from 1 to number itself
            if n%i==0:  # here, we find what all is the input divisible by
                result += (i,)
            else:
                0
    length = len(result)
    if length==2:
        print(i,'is Prime')


def test(): # defined a test code for the same
    for i in range(20):
        print(isPrime(i))
            
test()