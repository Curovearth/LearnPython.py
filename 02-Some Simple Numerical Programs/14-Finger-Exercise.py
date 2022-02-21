# Add some code to the implementation of Newton Raphson that keeps track of the number of iterations used to find the root. Use that code as part of a program that compares the efficiency of NR method and 
# bisection search.

# -------NR method Initiation-----
number = 19
total_guesses = 0
# ------Common to both methods----
epsilon = 0.01
numb_guess = number/2
#-------Bi section search initiation-----
val_high = max(0,number)
val_low = 0
ans = (val_high+val_low)/2.0

while abs((numb_guess**2)-number)>=epsilon:
    numb_guess = numb_guess-(((numb_guess**2)-number)/(2*numb_guess))
    total_guesses += 1
print("NR METHOD")
print("Total Guess:",total_guesses,"and",numb_guess,"is a close square root of",number)

total_guesses = 0;
while abs(ans**2-number)>=epsilon:
    total_guesses += 1;
    if ans**2 < number:
        val_low=ans
    else:
        val_high=ans
    ans=(val_high+val_low)/2
    
print("BI-SECTION ALGORITHM")
print("Total Guess:",total_guesses,"and",ans,"is a close square root of",number)


