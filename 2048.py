def print_line():
	print('-	-	-	-	-	-	-	- 	-')
def display_matrix():
	matrix = []
	for i in range(4):
		matrix.append([0,0,0,0])
	print_line()
	for row in matrix:
		rowstring = '|\t'
		for item in row:
			rowstring += str(item)
			rowstring += '\t|\t'
		print rowstring
		print_line()

display_matrix()