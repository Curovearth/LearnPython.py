'''
Tried by Swarup Tripathy

Aim
- sorting by first name
- sorting by last name

Imspiration
- Selection sort algorithm
'''

# For finding the number of the alphabet
def alphNum(letter):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in alphabets:
        if letter == i:
            return alphabets.index(i)+1

# Sorting the list according the to the first name
def sortFirst(list):
    i=0
    while i != len(list):
        for j in range(i, len(list)):
            # print(j)
            let1 = list[i].split()[0][0]
            idx1 = alphNum(let1)

            let2 = list[j].split()[0][0]
            idx2 = alphNum(let2)
            if idx1 > idx2:
                list[i], list[j] = list[j], list[i]
        i += 1
    return list

# Sorting the list according to the last name
def sortLast(list):
    i=0
    while i != len(list):
        for j in range(i, len(list)):
            # print(j)
            let1 = list[i].split()[1][0]
            idx1 = alphNum(let1)

            let2 = list[j].split()[1][0]
            idx2 = alphNum(let2)
            if idx1 > idx2:
                list[i], list[j] = list[j], list[i]
        i += 1
    return list

names_list = ['Swarup Tripathy','Atul Thiyagarajan','Rajashree Pati','Yatharth Agarwal']
names_list2 = ['Tom Brady','Eric Grimson','Gisele Bundchan']

print('\nSorted (Acc to First Name): ',sortFirst(names_list))
print('Sorted (Acc to Last Name): ',sortLast(names_list))
print('\n')
print('Sorted (Acc to First Name)',sortFirst(names_list2 ))
print('Sorted (Acc to Last Name)',sortLast(names_list2))
