# Contains a class that can be used to keep track of the grades of a collection of students. Instances of class grades
# are implemented using a list and a dictionary. The list keeps track of the students in the class. The dictionary maps a student's
# identification number to a list of grades.

class Grades(object):
    nextId = 0

    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
        

    def getIdNum(self):
        self.idNum = nextId
        nextId += 1
        return self.idNum
        

    def addStudents(self,student):
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        

        self.grades[student.getIdNum()]=[]
        self.isSorted = False   # the instance variable isSorted is used to keep track of whether or not the list of students has been sorted since the last time a student was added to it.
    
    def addGrade(self,student,grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self,student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
        
    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

p = Grades()
l = ['boy1','boy2','boy3']
for i in l:
    p.addStudents(i)

print(p.getGrades('boy1'))