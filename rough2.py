from math import sqrt

def num_divisors(n):
	end = int(sqrt(n))
	print('end=',end)
	# result = sum(2 for i in range(1, end + 1) if n % i == 0)
	for i in range(1,end+1):
		print(n,'%',i)
		if n%i==0:
			print(2)
	# if end**2 == n:
	# 	result -= 1
	# return 'num is ',n,result
	# return result

# for i in range(1,10):
#     print(num_divisors(i))

print(num_divisors(8))