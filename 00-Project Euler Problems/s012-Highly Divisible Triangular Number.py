'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

################# PSEUDO CODE ##################################

'''
WHAT ALL WE KNOW?
Triangle numbers are nothing but sum of the natural numbers up till the mentioned number
1st = 1+0 = 1
2nd = 1+2 = 3
3rd = 1+2+3 = 6
4th = 1+2+3+4 = 10
.
.
.
sum of natural numbers = [n*(n+1)]/2

WRITING THE CODE!
- while loop(since we don't know the number)
- feeding the numbers to [n*(n+1)]/2 to cal the sum
- to cal the divisors for the sum and store it in a list
- cal the length of list 
- one which exceeds or has 500 divisors should be the first one
'''
i=100000
while(i<100001):
    divisors_list = []
    # print('val of i=',i)
    sum = int((i*(i+1))/2)
    # print('sum is', sum)
    for j in range(1,sum+1):
        if sum%j == 0:
            divisors_list.append(j)
        else:
            continue
    # print('list is',divisors_list)
    length = len(divisors_list)
    print('len is',length)
    if length >= 500:
        break
    i = i+1

print(sum)