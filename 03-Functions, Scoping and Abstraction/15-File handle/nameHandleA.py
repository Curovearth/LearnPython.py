from collections import namedtuple


nameHandle = open('AppendedData','w')
nameHandle.write('David\n')
nameHandle.write('John\n')
nameHandle.close()

nameHandle = open('AppendedData','a')
nameHandle.write('Curovearth\n')
nameHandle.write('Swarup\n')
nameHandle.close()

nameHandle = open('AppendedData','r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()