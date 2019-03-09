import time

start_time = time.time()
#get matrix from .dat file
fp = open("matrix_test1.dat")
temp = fp.readlines()
matrix = []
for x in temp:
	x = list(map(int, x.split()))
	matrix.append(x)
fp.close()
#print (matrix)
#print (len(matrix))

all_edge = []
all_edge_index = []
count_vertex = []
path = []
cost = 0
group = []

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if(i == j):
			continue
		else:
			all_edge.append(matrix[i][j])
			all_edge_index.append([i, j])
	count_vertex.append(0)		
#print(all_edge)
#print(all_edge_index)

#print(count_vertex)
for i in range(len(all_edge)):
	for j in range(len(all_edge) - i - 1):
		if(all_edge[j] < all_edge[j + 1]):
			temp = all_edge[j]
			index_temp = all_edge_index[j]
			all_edge[j] = all_edge[j + 1]
			all_edge_index[j] = all_edge_index[j + 1]
			all_edge[j + 1] = temp
			all_edge_index[j + 1] = index_temp

#print(all_edge)
#print(all_edge_index)

while(len(path) != len(matrix) - 1):
	
	start_group = -1
	end_group = -1
	min_temp = all_edge.pop()
	min_index_temp = all_edge_index.pop()
	#print(all_edge)
	if(count_vertex[min_index_temp[0]] == 2 or count_vertex[min_index_temp[1]] == 2):
		continue
	for i in range(len(group)):
		if(min_index_temp[0] in group[i]):
			start_group = i
		if(min_index_temp[1] in group[i]):
			end_group = i
	if(start_group == end_group and start_group != -1):
		continue
	path.append(min_index_temp)
	cost += min_temp
	count_vertex[min_index_temp[0]] += 1
	count_vertex[min_index_temp[1]] += 1
	if(start_group == -1 and end_group == -1):
		group.append([min_index_temp[0],min_index_temp[1]])
	elif(start_group == -1 and end_group != -1):
		group[end_group].append(min_index_temp[0])
	elif(start_group != -1 and end_group == -1):
		group[start_group].append(min_index_temp[1])
	elif(start_group != -1 and end_group != -1):
		group[start_group] = group[start_group] + group[end_group]
		del group[end_group]

sequence = []

for i in range(len(count_vertex)):
	if(count_vertex[i] == 1):
		sequence.append(i)
		break
while(len(sequence) <= len(path)):
	for i in range(len(path)):
		for j in range(len(path[i])):
			if(path[i][j] == sequence[-1]):
				sequence.append(path[i][1 - j])
				path[i] = [-1, -1]

#print("path: ", end = "")
#print(path)
print("cost: ", end = "")
print(cost)
#print("count vertex: ", end = "")
#print(count_vertex)
#print("group: ", end = "")
#print(group)
print("path: ", sequence)
print("execute time: ", time.time() - start_time)