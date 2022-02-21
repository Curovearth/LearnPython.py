# Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise
# HINT: you might want to use the built-in str operation in.

def isIn(x,y):
    if x in y or y in x:
        return True
    else:
        return False

print(isIn('swarup','war'))