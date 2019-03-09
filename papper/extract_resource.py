import xlrd
import time

start_time = time.time()

datafile = 'matrix_resource1.dat'
excelfile = 'sample1.xlsx'

workbook = xlrd.open_workbook(excelfile)
test_case = workbook.sheet_by_index(0)
relation = workbook.sheet_by_index(1)

resource = []

for i in range(1, test_case.nrows):
	repeat_flag = 0
	for j in range(1, i):
		diff_flag = 0
		for n in range(1, test_case.ncols):
			if(test_case.cell_value(j, n) != test_case.cell_value(i, n)):
				diff_flag = 1
				break
		if(diff_flag == 0):
			#print(int(test_case.cell_value(i, 0)), ' = ', int(test_case.cell_value(j, 0)))
			repeat_flag = 1
			break

	if repeat_flag == 0:
		resource.append(int(test_case.cell_value(i, 0)))

#print(resource)

resource_son = []
for i in range(len(resource)):
	resource_son.append([resource[i]])

for i in range(1, test_case.nrows):
	for j in range(1, i):
		diff_flag = 0
		for n in range(1, test_case.ncols):
			if(test_case.cell_value(j, n) != test_case.cell_value(i, n)):
				diff_flag = 1
				break
		if(diff_flag == 0):
			#print(test_case.cell_value(i, 0), ' = ', test_case.cell_value(j, 0))
			for n in range(len(resource_son)):
				if(test_case.cell_value(j, 0) == resource_son[n][0]):
					resource_son[n].append(int(test_case.cell_value(i, 0)))
			break

for i in range(len(resource_son)):
	print('Resource', i, ': ', end = '')
	print(resource_son[i], ' ', end = '')
#print(len(resource_son))

print()
fp = open(datafile, 'w')

for i in range(1, test_case.nrows):
	pass_flag = 0
	for t in range(len(resource_son)):
		if(test_case.cell_value(i, 0) in resource_son[t] and test_case.cell_value(i, 0) != resource_son[t][0]):
			pass_flag = 1
			break
	if(pass_flag == 1):
		continue
	for j in range(1, test_case.nrows):
		pass_flag = 0
		for t in range(len(resource_son)):
			if(test_case.cell_value(j, 0) in resource_son[t] and test_case.cell_value(j, 0) != resource_son[t][0]):
				pass_flag = 1
				break
		if(pass_flag == 1):
			continue
		elem = 0
		if(i == j):
			fp.write(str(int(elem)))
			fp.write(' ')
		else:
			for n in range(1, test_case.ncols):
				for s in range(1, relation.nrows):
					if(relation.cell_value(s, 0) == test_case.cell_value(0, n) and relation.cell_value(s, 1) == test_case.cell_value(i, n) and relation.cell_value(s, 2) == test_case.cell_value(j, n)):
						elem += relation.cell_value(s, 3)
			fp.write(str(int(elem)))
			fp.write(' ')
	fp.write("\n")

fp.close()

print('Time cost of extracting resource matrix from Excel: ')
print(time.time() - start_time, ' s')

fp = open(datafile, 'r')

temp = fp.readlines()
matrix = []
for x in temp:
	x = list(map(int, x.split()))
	matrix.append(x)

pre_min_cost = 0
for i in range(len(matrix) - 1):
	pre_min_cost += matrix[i][i + 1]

print()
print('Test cost after deleting cases in same resources: ')
print(pre_min_cost)

fp.close()