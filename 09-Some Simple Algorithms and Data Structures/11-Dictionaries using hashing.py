class intDict(object):
    '''
    A dictionary with integer keys
    '''

    def __init__(self,numBuckets):
        '''
        Create an empty dictionary
        '''
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self,key,dictVal):
        '''
        Assumes key an int, adds an entry
        '''
        hashBucket = self.buckets[key%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key,dictVal)
                return 
        hashBucket.append((key,dictVal))

    def getValue(self,key):
        '''
        Assumes key an int
        Returns value associated with key
        '''
        hashBuckets = self.buckets[key%self.numBuckets]
        for e in hashBuckets:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'

import random

'''
The following code first constructs an intDict with 17 buckets and 20 entries. The values of the entries are the integers 0 to 19.
The keys are chosen at rondom using random.choice from integers in the range 0 to 10**5-1
The code then prints the individual hash buckets by interating over D.buckets
'''

D = intDict(17)
for i in range(20):
    # choose a random int in the range 0 to 10**5-1
    key = random.choice(range(10**5))
    D.addEntry(key,i)
print('The value of intDict is:')
print(D)

print('\n','the buckets are:')
for hashBucket in D.buckets:
    print(' ',hashBucket)