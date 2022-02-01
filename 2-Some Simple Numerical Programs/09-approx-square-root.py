# Finding approximation of square root
# EXHAUSTIVE ENUMERATION
x = 4
epsilon = 1 #original value = 0.01
step = epsilon ** 2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1

print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of ',x)
else:
    print(ans, 'is close square root of',x)

'''
ALGORITHM when epsilion was 0.001

-initialising variables
-x=4
-epsilon=0.01
-ans=0

-while abs(0^2-4) >= 0.01 and 0 <= 4
    -true
    -ans = 0 + 0.01^2 = 0.0001
    -numguesses = 0 + 1 = 1

-while abs(0.0001^2-4) >= 0.01 and 0.0001 <= 4
    -true
    -ans = 0.0001 + 0.0001 = 0.0002
    -numguesses = 1 + 1 = 2

-while abs(0.0002^2-4) >= 0.01 and 0.0002 <= 4
    -true
    -ans = 0.0001 + 0.0001 = 0.0002
    -numguesses = 2 + 1 = 3

'''

#-------------------------------------------------------

'''
ALGORITHM when epsilion was 1

-initialising variables
-x=4
-epsilon=1
-ans=0

-while abs(0^2-4) >= 1 and 0 <= 4
    -true
    -ans = 0 + 1^2 = 1
    -numguesses = 0 + 1 = 1

-while abs(1^2-4) >= 1 and 1 <= 4
    -true
    -ans = 1 + 1 = 2
    -numguesses = 1 + 1 = 2

-while abs(2^2-4) >= 2 and 2 <= 4
    -false
    
-numguesses = 2
-ans=2

if abs(2**2 - 4) >= 1:
    -false
else:
    -true
    -print(2, 'is close square root of',4)

'''