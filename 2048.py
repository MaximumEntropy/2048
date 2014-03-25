import random
MATRIX = [[244,21,47,9],[222,10,42,43],[32,24,160,41],[640,128,1226,2048]]
INITIAL_MATRIX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
TEST_MATRIX = [[0,0,0,0],[0,2,0,4],[0,0,0,2],[0,0,0,4]]
def spawn_new_item(matrix):
	free_list = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				free_list.append([i,j])
	if len(free_list) == 0:
		return matrix
	random_location = random.randrange(len(free_list))
	row_column = free_list[random_location]
	random_row = row_column[0]
	random_column = row_column[1]
	matrix[random_row][random_column] = 2
	return matrix
def initialize_matrix(matrix):
	random_row_1 = random.randrange(4)
	random_column_1 = random.randrange(4)
	matrix[random_row_1][random_column_1] = 2
	while True:
		random_row_2 = random.randrange(4)
		random_column_2 = random.randrange(4)
		if random_column_2!= random_column_1 or random_row_1!=random_row_2:
			matrix[random_row_2][random_column_2] = 2
			break
	return matrix
def transpose_matrix(matrix):
	mat_dim = len(matrix)
	transposed_matrix = []
	for i in range(mat_dim):
		column = [row[i] for row in matrix]
		transposed_matrix.append(column)
	return transposed_matrix
def get_column(matrix,i):
	column = [row[i] for row in matrix]
	return column
def print_line():
	print('-   -   -   -   -   -   -   -   -')
def display_matrix(matrix):
	print_line()
	for row in matrix:
		rowstring = '|   '
		for item in row:
			rowstring += str(item)
			rowstring += '   |   '
		print rowstring
		print_line()
def push_left_row(row):
	for i in range(len(row)):
		index = i - 1
		if row[i] == 0:
			continue
		while index >= 0:
			if row[index] == 0:
				row[index] = row[index+1]
				row[index+1] = 0
			else:
				break
			index = index-1
	return row
def check_merge(row):
	for i in range(len(row)-1):
		if row[i] == row[i+1]:
			row[i] = 2*row[i]
			row[i+1] = 0
			row = push_left_row(row)
	return row
def push_left(row,index):
	print 'In Push Function :'
	print row,index
	i = index
	item = row[index]
	if item == 0:
		return row,9999
	while i > 0:
		if row[i-1] > 0:
			return row,i
		else:
			row[i-1] = row[i]
			row[i] = 0
		i = i - 1
		#print row
		#print '-------'
	return row,i
def check_merge_left(row,index):
	if index == 0:
		return row,False
	else:
		if row[index] == row[index-1]:
			row[index-1] = row[index]*2
			row[index] = 0
			return row,True
		else:
			return row,False
def two_merge_check_left(row):
	for i in range(len(row)-1,-1,-1):
		if i == 0:
			return row
		if row[i] > 0 and row[i-1] == 0 and (i-1)!=0:
			row[i-1] = row[i]
			row[i] = 0
	return row
def aftercheck(row):
	for i in range(len(row)-1):
		if row[i] == 0 and row[i+1] > 0:
			row[i] = row[i+1]
			row[i+1] = 0
	return row
def move_left_row(row):
	prev_merge = False
	for i in range(len(row)-1,-1,-1):
		row,index = push_left(row,i)
		print 'Push : '
		print row,index
		if index == 9999:
			continue
		if prev_merge == False:
				row,check = check_merge_left(row,index)
				prev_merge = check
				print 'Merge :'
				print row,check
		else:
			prev_merge = False
	row = two_merge_check_left(row)
	row = aftercheck(row)
	return row
#def move_left(matrix):
	temp_matrix = []
	for row in matrix:
		prev_merge = False
		for i in range(len(row)-1,-1,-1):
			row,index = push_left(row,i)
			if index == 9999:
				continue
			if prev_merge == False:
				row,check = check_merge_left(row,index)
				prev_merge = check
			else:
				prev_merge = False
		row = two_merge_check_left(row)
		row = aftercheck(row)
		temp_matrix.append(row)
	return temp_matrix
#def move_right(matrix):
	temp_matrix = []
	for row in matrix:
		prev_merge = False
		row.reverse()
		for i in range(len(row)-1,-1,-1):
			row,index = push_left(row,i)
			if index == 9999:
				continue
			if prev_merge == False:
				row,check = check_merge_left(row,index)
				prev_merge = check
			else:
				prev_merge = False
		row = two_merge_check_left(row)
		row = aftercheck(row)
		row.reverse()
		temp_matrix.append(row)
	return temp_matrix
#def move_up(matrix):
	temp_matrix = []
	for j in range(len(matrix)):
		column = get_column(matrix,j)
		prev_merge = False
		for i in range(len(column)-1,-1,-1):
			column,index = push_left(column,i)
			if index == 9999:
				continue
			if prev_merge == False:
				column,check = check_merge_left(column,index)
				prev_merge = check
			else:
				prev_merge = False
		column = two_merge_check_left(column)
		column = aftercheck(column)
		temp_matrix.append(column)
	temp_matrix = transpose_matrix(temp_matrix)
	return temp_matrix
#def move_down(matrix):
	temp_matrix = []
	for j in range(len(matrix)):
		column = get_column(matrix,j)
		prev_merge = False
		column.reverse()
		for i in range(len(column)-1,-1,-1):
			column,index = push_left(column,i)
			if index == 9999:
				continue
			if prev_merge == False:
				column,check = check_merge_left(column,index)
				prev_merge = check
			else:
				prev_merge = False
		column = two_merge_check_left(column)
		column = aftercheck(column)
		column.reverse()
		temp_matrix.append(column)
	temp_matrix = transpose_matrix(temp_matrix)
	return temp_matrix
def move_left(matrix):
	temp_matrix = []
	for row in matrix:
		row = push_left_row(row)
		row = check_merge(row)
		temp_matrix.append(row)
	return temp_matrix
def move_right(matrix):
	temp_matrix = []
	for row in matrix:
		row.reverse()
		row = push_left_row(row)
		row = check_merge(row)
		row.reverse()
		temp_matrix.append(row)
	return temp_matrix
def move_up(matrix):
	temp_matrix = []
	for i in range(len(matrix)):
		column = get_column(matrix,i)
		column = push_left_row(column)
		column = check_merge(column)
		temp_matrix.append(column)
	temp_matrix = transpose_matrix(temp_matrix)
	return temp_matrix
def move_down(matrix):
	temp_matrix = []
	for i in range(len(matrix)):
		column = get_column(matrix,i)
		column.reverse()
		column = push_left_row(column)
		column = check_merge(column)
		column.reverse()
		temp_matrix.append(column)
	temp_matrix = transpose_matrix(temp_matrix)
	return temp_matrix
def accept_input():
	print 'A : Left  D: Right  W: Up and S: Down'
	user_input = raw_input('Your move...')
	return user_input
def check_for_win_condition(matrix):
	checkflag = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 2048:
				checkflag = 1
	if checkflag == 1:
		return True
	else:
		return False
def check_for_lose_condition(matrix):
	check_left = 0
	check_right = 0
	check_up = 0
	check_down = 0
	left_matrix = move_left(matrix)
	if left_matrix == matrix:
		check_left = 1
	right_matrix = move_right(matrix)
	if right_matrix == matrix:
		check_right = 1
	up_matrix = move_up(matrix)
	if up_matrix == matrix:
		check_up = 1
	down_matrix = move_down(matrix)
	if down_matrix == matrix:
		check_down = 1
	if check_down == 1 and check_up == 1 and check_left == 1 and check_right == 1:
		return True
	else:
		return False
def mainloop():
	matrix = initialize_matrix(INITIAL_MATRIX)
	display_matrix(matrix)
	while True:
		user_input = accept_input()
		if user_input == 'A' or user_input == 'a':
			matrix = move_left(matrix)
		elif user_input == 'D' or user_input == 'd':
			matrix = move_right(matrix)
		elif user_input == 'W' or user_input == 'w':
			matrix = move_up(matrix)
		elif user_input == 'S' or user_input == 's':
			matrix = move_down(matrix)
		else:
			print 'Invalid Selection'
		matrix = spawn_new_item(matrix)
		display_matrix(matrix)
		#result = check_for_win_condition(matrix)
		#if result == True:
	#		print 'YOU WIN! :)'
	#	result = check_for_lose_condition(matrix)
	#	if result == True:
	#		print 'YOU LOSE! :('
#row = push_left_row([0,4,0,4])
#print check_merge(row)
#display_matrix(TEST_MATRIX)
#matrix = move_down(TEST_MATRIX)
#display_matrix(matrix)
mainloop()
#display_matrix(TEST_MATRIX)
#matrix = move_left(TEST_MATRIX)
#display_matrix(matrix)
#matrix = spawn_new_item(matrix)
#display_matrix(matrix)
#display_matrix(MATRIX)
#matrix = move_right(MATRIX)
#display_matrix(matrix)
#display_matrix(MATRIX)
#matrix = move_up(MATRIX)
#display_matrix(matrix)
#matrix = move_right(MATRIX)
#display_matrix(matrix)
#print move_left_row([0,4,2,2])