def squarerootExhaustive(x,epsilon):
    step = epsilon**2
    ans = 0.0
    while abs(ans**2-x) >= epsilon and ans*ans <= x:
        ans += step
    if ans*ans > x:
        raise ValueError
    return ans

print(squarerootExhaustive(12,0.01))

'''
* Flow of Code ---------------------------------

squarerootExhaustive(12,0.01)
- step = 0.0001
- ans = 0.0
- while abs(0.0001-12)[11.9999] >= 0.01 and 0 <= 12:
    - ans = 0 + 0.0001 = 0.0001
- while 11.99999999 >= 0.01 and 1e-08 <= 12:
    - ans = 0.0001 + 0.0001 = 0.0002
- while 11.99999996 >= 0.01 and 4e-08 <= 12:
    - ans = 0.0002 + 0.0001 = 0.0003


'''