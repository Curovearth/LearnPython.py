#  Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and 
# the value of the __module__ attribute of the Student class

class Student():
    def __init__(self,name,classroom):
        self.name = name
        self.room = classroom
    
    def get_name(self):
        return self.name
    def get_classroom(self):
        return self.room


if __name__=="__main__":
    print(type(Student))
    user = Student('swarup','Q502')
    print(user.get_name())
    for i in Student.__dict__:
        print(i)