def squarerootBi(x,epsilon):
    low = 0
    high = max(1.0,x)
    ans = (high+low)/2.0
    while abs(ans**2-x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans

        ans = (high+low)/2
    return ans

print(squarerootBi(12,0.01))

# 3.462890625