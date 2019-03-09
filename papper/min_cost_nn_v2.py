def line_process(temp_path, temp_path_count, index_i):
	path[index_i] = []
	path_count[index_i] = 0
	path[index_i].extend(temp_path)
	path_count[index_i] += temp_path_count
	global startline
	global min_cost
	global min_cost_path

	if(len(path[index_i]) == len(matrix)):
		if(path_count[index_i] < min_cost):
			min_cost = path_count[index_i]
			min_cost_path = path[index_i]
		#print("path",end=" ")
		#print(path[index_i])
		#print("cost",end=" ")
		#print(path_count[index_i])
		
		return

	min_val = 100000
	for j,val in enumerate(matrix[index_i]):
		if(val <= min_val and j not in path[index_i] and j != index_i):
			min_val = val
	for j,val in enumerate(matrix[index_i]):
		if(val == min_val and j not in path[index_i] and j != index_i):
			min_index[index_i].append(j)
	
	while(min_index[index_i] != []):
		#print("before pop",end=" ")
		#print(min_index[index_i])

		temp = min_index[index_i].pop()
		#print("after pop",end=" ")
		#print(min_index[index_i])
		#print("temp",end=" ")
		#print(temp)
		temp_list = []
		temp_list.extend(path[index_i])
		temp_list.append(temp)
		
		#print("path",end=" ")
		#print(path[index_i])
		#print("temp_list",end=" ")
		#print(temp_list)

		temp_path_count = 0
		temp_path_count += path_count[index_i]
		temp_path_count += min_val
		line_process(temp_list, temp_path_count, temp)		

import time

start_time = time.time()

#get matrix from .dat file
fp = open('test.dat', 'r')
temp = fp.readlines()
matrix = []
for x in temp:
	x = list(map(int, x.split()))
	matrix.append(x)
fp.close()
#print (matrix)
#print (len(matrix))

min_cost_path = 0
min_cost = 100000

for startline in range(len(matrix)):
	path = []
	for val in range(len(matrix)):
		path.append([])
	min_index = []
	for val in range(len(matrix)):
		min_index.append([])
	path_count = []
	for val in range(len(matrix)):
		path_count.append(0)

	#print()
	#print("start",end=" ")
	#print(startline)
	path.append([startline])
	line_process([startline],path_count[startline], startline)

print("min cost path:", end=" ")
print(min_cost_path)
print("min cost:", end=" ")
print(min_cost)

print("execute time: ", time.time() - start_time)