# Write a Python program to create an instance of a specified class and display the namespace of the said instance.

class Classroom:
    def __init__(self,room,teacher):
        self.room = room
        self.teacher = teacher

class Student(Classroom):
    def __init__(self, name, rollno,room,teacher):
        self.name = name
        self.rollno = rollno
        Classroom.__init__(self,room,teacher)

    def get_rollno(self,rollno):
        return self.rollno
student = Student('Swarup','0167','TT141','Ma\'am')
print(student.__dict__)

'''
Output is 
{'name': 'Swarup', 'rollno': '0167', 'room': 'TT141', 'teacher': "Ma'am"}
'''