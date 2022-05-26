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

p1 = MITperson('Barbara Beaver')
print(str(p1) + '\'s id number is '+str(p1.getIdNum())) # \ is an escape character used to indicate that the next character should be treated in a special way.
p2 = MITperson('Swarup tripathy')
print(str(p2) + '\'s id number is '+str(p2.getIdNum()))