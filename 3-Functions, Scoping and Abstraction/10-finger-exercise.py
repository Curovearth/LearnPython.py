# When the implementation of fib is used to compute fib(5), how many times does it compute the value of 
# fib(2) on the way to computing fib(5)

def fib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def testFib(number,toCall):
    if number==toCall or number-toCall==2:
        ans=1
    elif number>toCall:
        for i in range(number+1):
            print('fib of',i,'=',fib(i))
        ans = fib(number-toCall+1)
    else:
        ans = 'Not Valid'
    print("number of times",toCall,"is called =",ans)

x = int(input("Fibonacci of= "))
k = int(input("to call= "))

testFib(x,k)


# The fib(k - n + 1) will give number of times fib(n) called when calculating fib(k) recursively, where k > n and this works for n = 0 as well.