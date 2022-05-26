
def foo():
    x = 20
    def bar():
        global X
        x = 25

    print("Before calling bar:",x)
    print("calling bar")
    bar()
    print("After calling bar:",x)

foo()
# print("x in main:",x)

'''
x in main will print 25

- in the above program we declared a global variable inside the nested function bar()
- before and after calling bar(), the varibale x takes the value of local variable x = 20
- outside the foo() function x=25
'''