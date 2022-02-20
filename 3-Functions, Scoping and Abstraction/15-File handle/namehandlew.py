nameHandle = open('kids','w')   # creating a file named 'kids' and opening it in terms of writing to that file
for i in range(2):  # to feed in two strings
    name = str(input('enter name: ')) # taking input from the user to feed into the file
    nameHandle.write(name+'\n') # whatever the user has written is then written to that file
nameHandle.close()  # finally we make sure that we close the file