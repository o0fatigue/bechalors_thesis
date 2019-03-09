import xlrd
import time

start_time = time.time()

datafile = 'matrix_test1.dat'
excelfile = 'sample1.xlsx'

workbook = xlrd.open_workbook(excelfile)
test_case = workbook.sheet_by_index(0)
relation = workbook.sheet_by_index(1)

fp = open(datafile, 'w')

for i in range(1, test_case.nrows):
	for j in range(1, test_case.nrows):
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

print('Time cost of extracting test matrix from Excel: ')
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
print('Test cost before minimizing: ')
print(pre_min_cost)

fp.close()