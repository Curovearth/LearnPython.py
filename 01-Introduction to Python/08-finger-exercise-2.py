numXs = int(input("how many times should I print the Letter X ?"))
toPrint = ''
iter_left = numXs
while(iter_left!=0):
    toPrint = toPrint + 'X'
    iter_left = iter_left - 1
print(toPrint)