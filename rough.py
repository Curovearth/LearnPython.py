# undergraduate and graduate

import datetime

class Person():
    def __init__(self,name):
        self.name = name
        try:
            ind = name.rindex(' ')
            self.lastName = name[ind+1:]
            self.firstName = name[:ind]
        except:
            self.lastName = name
            self.firstName = name

    def getLastName(self):
        return self.lastName 
    def getFirstName(self):
        return self.firstName 
    
    def setBirthday(self, birthday):
        self.birthday = birthday
    
    def getAge(self):
        return (datetime.today() - self.birthday())

    def __str__(self):
        return self.name

class MITPerson(Person):
    nextId = 0

    def __init__(self,name):
        Person.__init__(self,name)
        self.idnumber = MITPerson.nextId
        MITPerson.nextId += 1
    
    def getIdNum(self):
        return self.idnumber
    
    def isStudent(self):
        return isinstance(self,Student)
    
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.classyear = classYear

    def getClass(self):
        return self.year

class Grad(Student):
    pass

p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver',1984)
print(p5,'is a graduate student is',type(p5)==Grad)
print(p5,'is an undergraduate student is',type(p5)==UG)