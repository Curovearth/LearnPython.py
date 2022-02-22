tech = ['MIT','Oxford']
ivys = ['Brown','Caltech']

univ1 = [tech,ivys]
univ2 = [['MIT','Oxford'],['Brown','Caltech']]

print('id of univ1',id(univ1))
print(univ1)
print(univ2)
print('id of univ2',id(univ2))

tech.append('RPI')
print(univ1)