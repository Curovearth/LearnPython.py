# Solution to Project Euler problem 2
# Copyright (c) Swarup Tripathy. All rights reserved.

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

first = 1
second = 2
sum = 0
list=[first,second]
while sum < 4000000:
    sum = first + second
    list.append(sum)
    first = second
    second = sum

even_list_sum=0
for i in range(len(list)):
    if list[i]%2==0:
        even_list_sum = list[i] + even_list_sum
    else:
        None

print(even_list_sum)
    
            