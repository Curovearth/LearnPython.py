def readInt():
    while True:
        val = input('enter an integer: ')
        try:
            return int(val)
        except ValueError:
            print(val,'is not an integer')

readInt()

'''
The following program executes a while loop 
where the val takes an input 
if the return int(val) returns an int value then the try block returns the integer
if the val input given is a non integer value the except block returns a 'not an integer' statement.
'''