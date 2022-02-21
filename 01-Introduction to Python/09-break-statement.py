#checking the divisibility 
#when not aware about the number directly use while loop

x=1
while(x!=0):
    if x%11==0 and x%12==0:
        break
    else:
        x=x+1;

print(x,'is divisible by 11 and 12')