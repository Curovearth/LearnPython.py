import datetime

class Person(object):

    def __init__(self,name):
        # Creating a person
        self.name = name
        try:
            lastBlank = name.rindex(' ')        # finds the last occurrence of the specified value.
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        # gets the name of the person
        return self.name
    
    def getLastName(self):
        # gets the lastname of the person
        return self.lastName

    def setBirthday(self,birthdate):
        # sets the birthday of the person
        self.birthday = birthdate

    def getAge(self):
        # gets the age of the person in days
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        '''
        Returns True if self precedes other in alphabetical order, and False otherwise. Comparison is based on the 
        last names, bt if these are the same full names are compared.
        '''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name


class MITperson(Person):
    nextIdNum = 0

    def __init__(self,name):
        Person.__init__(self,name)      # to initialise the inherited instance variable self.name
        self.idNum = MITperson.nextIdNum
        MITperson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum < other.idNum

    def isStudent(self):
        return isinstance(self,Student) #isinstance() function returns True if the specified object is of the specified type, otherwise False

class Student(MITperson):
    pass

class UG(Student):
    def __init__(self,name, classYear):
        MITperson.__init__(self,name)
        self.classYear = classYear

    def getClass(self):
        return self.year

class Grad(Student):
    pass    # has no attributes other than those inherited from its superclass


p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver',1984)
print(p5,'is a graduate student is',type(p5)==Grad)
print(p5,'is an undergraduate student is',type(p5)==UG)