def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg+' ')
        try:
            return valType(val)
        except ValueError:
            print(val,errorMsg)

readVal(int, 'enter an integer:','is not an integer')