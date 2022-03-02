grid =[
	[1,3,6,3,7,8],
	[4,7,2,3,4,1],
	[9,3,6,7,0,2],
	[7,8,7,2,3,8],
]
final_list = []
sum2=0
for i in range(len(grid)):
	#############################################
	############# Right and left ################
	#############################################
	list=[]
	for j in range(len(grid[i])):
		# print(grid[i][j], end=" ")
		try:
			sum=0
			
			for k in range(j,j+4):
				sum = sum + grid[i][k]
			list.append(sum)
			
		except IndexError:
			pass
	final_list.append(max(list))
	#############################################
	############### UP and DOWN #################
	#############################################
	sum2 = sum2 + grid[i][t]
print(sum2)
# print(final_list)