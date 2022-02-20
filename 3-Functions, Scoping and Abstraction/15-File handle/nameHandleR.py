from unicodedata import name


nameHandle = open('babies','r') # reading the content from an existing file
for i in nameHandle:
    print(i)    # prints all the content present in file
nameHandle.close()  # closing the nameHandle