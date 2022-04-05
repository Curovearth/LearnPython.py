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
    def get_salary(self):
        return self.salary
    
e = Employee('swarup','tripathy',1000)
print(e.email)