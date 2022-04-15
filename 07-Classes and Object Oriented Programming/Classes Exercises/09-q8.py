# Write a Python program to create two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not

class Student:
    pass

class Marks:
    pass

s = Student()
m = Marks()
j = Student()

print('isinstance-------------------')
print(isinstance(s,Student))
print(isinstance(m,Marks))
print(isinstance(j,Marks))

print('\nissubclass-----------------')
print(issubclass(Student,object))
print(issubclass(Marks,object))