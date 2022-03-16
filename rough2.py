file = open('ksjffljsk','r')
listLines = file.readlines()
totalSum = sum(int(i) for i in listLines)
print(totalSum)
print(str(totalSum)[:10])
print(len(str(totalSum)[:10]))

