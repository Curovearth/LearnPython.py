# Write a Python program to create a class and display the namespace of the said class

class Object:
    def __init__(self,name):
        self.n = name
    def get_math(self,sin):
        self.s = sin



for name in Object.__dict__:
    print(name)