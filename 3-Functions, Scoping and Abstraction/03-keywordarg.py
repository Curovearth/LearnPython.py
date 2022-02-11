# here the function printName assumes firstName and lastName to be strings and that reverse is boolean

def printName(firstName,lastName,reverse):
    if reverse:
        print(lastName + ', '+ firstName)
    else:
        print(firstName,lastName)

printName('Olga','Puchmajerova',False)
printName('Olga','Puchmajerova',reverse=False)
printName('Olga',lastName='Puchmajerova',reverse=False)
printName(lastName='Puchmajerova',firstName='Olga',reverse=False)
# printName('Olga',lastName='Puchmajerova',False) ###Positional argument cannot appear after keyword arguments