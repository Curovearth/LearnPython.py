def isPalindrome(string):
    # defined the function to check if the string is palindrome or not
    length=len(string)
    ans=''
    for i in range(length):
        ans = ans + string[abs(i-(length-1))]
    if ans==string:
        print(string,'is palindrome',ans)
    else:
        print(string,'is not palindrome',ans)

string = str(input('give a string please: '))
isPalindrome(string)