#write a program that asks the user to input 10 integers and then prints the largest odd number that was entered. 
#if no odd number was entered, it should print a message to that effect


a = int(input("int1 = "))
b = int(input("int2 = "))
c = int(input("int3 = "))
d = int(input("int4 = "))
e = int(input("int5 = "))
f = int(input("int6 = "))
g = int(input("int7 = "))
h = int(input("int8 = "))
i = int(input("int9 = "))
j = int(input("int10 = "))

list = [a,b,c,d,e,f,g,h,i,j]
odd = []
i = len(list)
count=0
while(i!=0):
    if(list[i-1]%2!=0):
        odd.append(list[i-1])
    else:
        count = count + 1
    i-=1

largest = odd[1]
flag=0
i=len(odd)
while(i!=0):
    if(odd[i-1]>largest):
        largest = odd[i-1]
    else:
        flag = flag+1
    i-=1

print("largest odd number is",largest)