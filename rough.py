string = 'swarup'
string = string.lower()
letters = ''
for c in string:
    if c in 'abcdefghijklmnopqrstuvwxyz':
        letters = letters + c
print(letters)
print(type(letters))

