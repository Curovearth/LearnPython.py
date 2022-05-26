class Employee:
    def __init__(self,first,last,salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = first + '.' + last + '@gmail.com'
    
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    def get_salary(self):
        return self.salary
    
class Developer(Employee):
    pass

e = Developer('swarup','tripathy',1000)
e = Developer('John','Guttag',1000)
print(e.email)
print(e.get_first_name())
print(e.get_last_name())
print(e.get_full_name())
print(e.get_salary())