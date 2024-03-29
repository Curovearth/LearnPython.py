# NEWTON RAPHSON method for square root
# Find x such that x**2-24 is within epsilon of 0.01

epsilon = 0.01
k = 24
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2)-k)/(2*guess))
    print(guess)
print('Square root of',k,'is about',guess)