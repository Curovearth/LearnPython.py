# import time

def isPalindrome(s):
    # start = time.time()
    def toChars(s):
        s = s.lower()       # converting all the characters of string in lowercase
        letters = ''        # initialising an empty string
        
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    # isPal will use recursion to do the real work
    # recursive part of the implementation is reached only on string of length two or more
    def isPal(s):
        if len(s) <=1:
            return True
        else:
            # the code first checks whether the first and last characters are same, and if they are goes on to check whether the string minus those two characters is palindrome
            return s[0] == s[-1] and isPal(s[1:-1])
    # end = time.time()
    # print(end-start)
    return isPal(toChars(s))


string = str(input('give a string please: '))

print(isPalindrome(string))


