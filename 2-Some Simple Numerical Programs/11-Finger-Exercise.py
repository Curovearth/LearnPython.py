# Finding cube root of both positive and negative numbers using Bisection algorithm 

n=27
x=abs(n)
low = 0
high = max(0,x)
epsilon = 0.01
numGuess = 0
ans = (high+low)/2

while abs(ans**3-x) >= epsilon:
    numGuess += 1
    if ans**3 >= x:
        high = ans
    else:
        low = ans
    ans = (high+low)/2

print('number of guesses =',numGuess)
print(ans,'is the closest cube root of',n)
    