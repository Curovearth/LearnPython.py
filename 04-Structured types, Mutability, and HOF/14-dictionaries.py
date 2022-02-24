# Dictionary being as set of key/value pairs. Literals of type dict are enclosed in curly braces
# and each element is written as a key followed by a colon followed by a value.

monthNumbers = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,
                1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May'}

print('The third month is ' + monthNumbers[3])      # identifying the key 3 that is asssigned to march
dist = monthNumbers['Apr'] - monthNumbers['Jan']    # Searching for the values assigned to 'apr' and 'jan'
print('Apr and Jan are',dist,'months apart')