# When the implementation of fib is used to compute fib(5), how many times does it compute the value of 
# fib(2) on the way to computing fib(5)


def fib(n):
    if n==0 or n==1:
        return 1
    else:

        ans = fib(n-1) + fib(n-2)
        if n==2:
            return ans
        else:
            return ans
        

def testFib(n):
    for i in range(n+1):
        
        print('fib of',i,'=',fib(i))
        


testFib(5)


# The fib(k - n + 1) will give number of times fib(n) called when calculating fib(k) recursively, where k > n and this works for n = 0 as well.