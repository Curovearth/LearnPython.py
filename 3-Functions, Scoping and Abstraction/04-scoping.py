from tkinter import Y


def f(x):
    y=1
    x=x+y
    print('x=',x)
    return x

x=3
y=2
z=f(x)
print('z=',z)   #4
print('x=',x)   #3
print('y=',y)   #2