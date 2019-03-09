import time

start_time = time.time()
#get matrix from .dat file
fp = open("test.dat")
temp = fp.readlines()
matrix = []
for x in temp:
	x = list(map(int, x.split()))
	matrix.append(x)
fp.close()
#print (matrix)
#print (len(matrix))

min_path_count = 100000 #initial min sum

#loop start line, since the starting line affects the result
for startline in range(len(matrix)):
	#path init
	path_count = 0
	path = [startline]
	index_i = startline
	i = matrix[index_i]
	
	#print("start line: ",startline)
	#print("cost: ", end = "")

	while(len(path) < len(matrix)):
		min_val = 100000 #initial min value of the line
		for j,val in enumerate(i):
			if(val < min_val and j not in path and j != index_i):
				min_val = val
				min_index = j
		#print(min_val, " ", end = "")
		path.append(min_index)
		path_count += min_val
		index_i = min_index
		i = matrix[min_index]

	#print()
	if(path_count < min_path_count):
		min_path_count = path_count
		min_path = path
		min_startline = startline

#output minimized result
#print("min start line: ",min_startline)
print("min cost: ", min_path_count)
print("min path: ", min_path)
print("execute time: ", time.time() - start_time)