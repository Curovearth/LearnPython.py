# Write a Python program to import built-in array module and display the namespace of the said module

import math

for name in math.__dict__:
    print(name)