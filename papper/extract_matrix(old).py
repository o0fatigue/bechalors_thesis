import xlrd
workbook = xlrd.open_workbook('./test_case.xlsx')
test_case = workbook.sheet_by_index(1)

#Extract test resources from test cases

resource = []

for i in range(1, test_case.nrows):
	repeat_flag = 0
	for j in range(1, i):
		#Add test resources conditions below
		if(test_case.cell_value(j, 1) == test_case.cell_value(i, 1) and test_case.cell_value(j, 2) == test_case.cell_value(i, 2)):
			print(test_case.cell_value(i, 0), ' = ', test_case.cell_value(j, 0))
			repeat_flag = 1
			break

	if repeat_flag == 0:
		resource.append(test_case.cell_value(i, 0))

print(resource)

resource_son = []
for i in range(len(resource)):
	resource_son.append([resource[i]])

for i in range(1, test_case.nrows):
	for j in range(1, i):
		#Add test resources conditions below
		if(test_case.cell_value(j, 1) == test_case.cell_value(i, 1) and test_case.cell_value(j, 2) == test_case.cell_value(i, 2)):
			print(test_case.cell_value(i, 0), ' = ', test_case.cell_value(j, 0))
			for n in range(len(resource_son)):
				if(test_case.cell_value(j, 0) == resource_son[n][0]):
					resource_son[n].append(test_case.cell_value(i, 0))
			break

print(resource_son)

#Export resource matrix from test resources

fp = open('resource_matrix.dat', 'w')
relation = workbook.sheet_by_index(0)

for i in range(len(resource)):
	for j in range(len(resource)):
		if(i == j):
			fp.write('0')
			fp.write(' ')
		else:
			
			fp.write(' ')
	fp.write("\n")

fp.close()




