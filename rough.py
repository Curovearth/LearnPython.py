# # grid =[
# # 	[1,3,6,3,7,8],
# # 	[4,7,2,3,4,1],
# # 	[9,3,6,7,0,2],
# # 	[7,8,7,2,3,8],
# # 	[1,2,3,4,5,6],
# # ]



# right_left_list = []
# up_down_list = []
# # sum3=0
# for i in range(len(grid)):
# 	#############################################
# 	############# Right and left ################
# 	#############################################
# 	# list=[]
# 	# for j in range(len(grid[i])):
# 	# 	# print(grid[i][j], end=" ")
# 	# 	try:
# 	# 		sum=0
			
# 	# 		for k in range(j,j+4):
# 	# 			sum = sum + grid[i][k]
# 	# 		list.append(sum)
			
# 	# 	except IndexError:
# 	# 		pass
# 	# right_left_list.append(max(list))
# 	#############################################
# 	############### UP and DOWN #################
# 	#############################################
# 	# sum2=0
# 	# for t in range(len(grid[0])):
# 	# 	try:
			
# 	# 		sum2 = sum2 + grid[t][i]
# 	# 	except IndexError:
# 	# 		pass
# 	# up_down_list.append(sum2)
	
# # print(up_down_list)
# # print(right_left_list)
# # print(up_down_list+right_left_list)
# 	None

# for m in range(len(grid[0])//2):
# 	#############################################
# 	############### Diagonal ####################
# 	#############################################
# 	sum3=0
# 	for i in range(len(grid)):
# 		try:
# 			sum3 = sum3 + grid[i][i+m]
# 			print(sum3, end=" ")
# 		except IndexError:
# 			pass
# 	print('\n')


# -----------------------------------------------------------------------

grid=[
	[1,2,3,4],
	[5,6,7,8],
	[9,1,1,1],
	[4,6,3,4],
]

list_right_left = []
list_up_down = []
list_diagonal = []

# --------- RIGHT LEFT -------------------------------------
def right_left(grid):
	for i in range(len(grid)):
		try:
			for j in range(len(grid[i])):
				sum_right_left=0
				for k in range(j,j+2):
					# print(sum_right_left,'+',grid[i][k])
					sum_right_left = sum_right_left + grid[i][k]
				list_right_left.append(sum_right_left)
		except IndexError:
			continue

# --------- UP DOWN ----------------------------------------
def up_down(grid):
	for i in range(len(grid)):
		try:
			for a in range(len(grid)):
				sum_up_down=0
				for b in range(a,a+2):
					# print(sum_up_down,'+',grid[k][i])
					sum_up_down = sum_up_down + grid[b][i]
				list_up_down.append(sum_up_down)
		except IndexError:
			continue

# --------- DIAGONAL --------------------------------------
def diagonal(grid):
	for i in range(len(grid)-1):	# checks for all the list rows
		sum = 1
		for j in range(len(grid[i])-1):
			sum = 1
			for k in range(2):
				# print(sum,'*',grid[i+k][j+k])
				sum = sum * grid[i+k][j+k]
				
			# print(sum)

# right_left(grid)
# up_down(grid)
diagonal(grid)


'''
grid[0][0] + grid[1][1]
grid[0][1] + grid[1][2]
grid[0][2] + grid[1][3]
'''



# if __name__ == '__main__':
# 	print(list_right_left)
# 	print(list_up_down)
# 	print(list_up_down)