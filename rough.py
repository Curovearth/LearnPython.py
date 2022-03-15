'''
Pseudo Code

- using itertools to iterate starting from 1
- we need to find the total divisors

'''

import itertools, math

def num_divisors(n):
  toEnd = int(math.sqrt(n))
  result = sum(2 for i in range(1,toEnd+1) if n%i==0)
  print(result)
  return result

triangleNumber = 0
for i in itertools.count(1):
  triangleNumber += i
  if num_divisors(triangleNumber) >= 500:
    print(triangleNumber)
    break
  else:
    continue
