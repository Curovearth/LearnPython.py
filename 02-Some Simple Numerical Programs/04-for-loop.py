x=4
for i in range(4):
    print(i)
    x=5

# even if you specify the new value of x, it doesn't affect the number of iterations. The arguments to the range function in the line
# with for are evaluated just before the first iteration of the loop and reevaluated for subsequent iterations 