# To find all the prime numbers within the input number

def listPrime(n):
    result = []     # we'll be feeding the divisible values here(repeated values will be present)
    prime = []      # we'll be feeding the primes here
    for i in range(2,n+1):      # first for loop to go individually to all the elements
        for j in range(2,n+1):  # second for loop to list all the numbers before i so as to identify primes later.
            if i%j==0:          
                result.append(i)    # here the output would be something like [2,3,4,4,5,and so on] since we say that when an integer is divisible return i
            else:
                0

    length = len(result)    # we find the length of list -> result
    
    for i in range(length):
        a = result[i]       # we assign 'a' first to the element
        count = 0           # count represents the total number of times a is present in the list
        for j in range(length):     # second for loop to identify rest of the elements again to check if the same integer is present or not
            if a == result[j]:      # when we find an element = a we increase the value of count by 1
                count += 1
            else:
                continue
        if count==1:        # since prime numbers would only have count = 1 since no other number would be divisible 
            prime.append(a)
    return prime

def testCode():     # defining a test code since it's a good practice.
    for i in range(25):
        print(listPrime(i))

# testCode()