def scope_test():
    spam = "test spam"
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam   # here spam = 'local spam' doesn't work
        spam = "nonlocal spam"

    def do_global():
        global spam     # here global allows you to modify the varibale outside of the current scope
        spam = "global spam"
    
    do_local()
    print("After local assignment:",spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global
    print("After global assignment:",spam)

scope_test()
# print("In global scope:",)