def fib(x):
    global numFibCalls
    numFibCalls += 1
    if x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print('fib',i,'=',fib(i))
        print('fib called',numFibCalls,'times')

testFib(4)