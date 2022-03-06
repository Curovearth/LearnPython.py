grid =[
	[1,3,6,3,7,8],
	[4,7,2,3,4,1],
	[9,3,6,7,0,2],
	[7,8,7,2,3,8],
	[1,2,3,4,5,6],
]
right_left_list = []
up_down_list = []
# sum3=0
for i in range(len(grid)):
	#############################################
	############# Right and left ################
	#############################################
	# list=[]
	# for j in range(len(grid[i])):
	# 	# print(grid[i][j], end=" ")
	# 	try:
	# 		sum=0
			
	# 		for k in range(j,j+4):
	# 			sum = sum + grid[i][k]
	# 		list.append(sum)
			
	# 	except IndexError:
	# 		pass
	# right_left_list.append(max(list))
	#############################################
	############### UP and DOWN #################
	#############################################
	# sum2=0
	# for t in range(len(grid[0])):
	# 	try:
			
	# 		sum2 = sum2 + grid[t][i]
	# 	except IndexError:
	# 		pass
	# up_down_list.append(sum2)
	
# print(up_down_list)
# print(right_left_list)
# print(up_down_list+right_left_list)
	None

for m in range(len(grid[0])//2):
	#############################################
	############### Diagonal ####################
	#############################################
	sum3=0
	for i in range(len(grid)):
		try:
			sum3 = sum3 + grid[i][i+m]
			print(sum3, end=" ")
		except IndexError:
			pass
	print('\n')


