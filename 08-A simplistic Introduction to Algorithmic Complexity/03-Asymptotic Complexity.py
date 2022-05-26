def f(x):
    # assume x is an int > 0
    ans = 0
    # loop that takes constant time
    for i in range(1000):
        ans += 1
    print('Number of additions so far: ',ans)

    # loop that takes time x
    for i in range(x):
        ans += 1
    print('Number of additions so far: ',ans)

    # nested for loops take time x**2
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print('Number of additions so far: ',ans)
    return ans

print(f(10))

'''
Output

Number of additions so far:  1000
Number of additions so far:  1010
Number of additions so far:  1210
1210
'''