import numpy as np

# the variable containing our puzzle to be solved
puzzle = [[0,0,0,2,6,0,7,0,1],
		  [6,8,0,0,7,0,0,9,0],
		  [1,9,0,0,0,4,5,0,0],
		  [8,2,0,1,0,0,0,4,0],
		  [0,0,4,6,0,2,9,0,0],
		  [0,5,0,0,0,3,0,2,8],
		  [0,0,9,3,0,0,0,7,4],
		  [0,4,0,0,5,0,0,3,6],
		  [7,0,3,0,1,8,0,0,0]]

# defines a function that checks if an entry is valid within its row, column and square
def possible(y,x,n):
	global puzzle

	# row and column validation
	for i in range(0,9):
		if puzzle[y][i] == n:
			return False
	for i in range(0,9):
		if puzzle[i][x] == n:
			return False	

	# square validation
	# the below two variables are essential for searching the square the entry would exist in
	x0 = (x//3)*3
	y0 = (y//3)*3

	for i in range(0,3):
		for j in range(0,3):
			if puzzle[y0+i][x0+j] == n:
				return False
	return True

# defines the recurive backtracking algorithm used to solve the sudoku puzzle
def solve():
	global puzzle

	for y in range(9):
		for x in range(9):
			if puzzle[y][x] == 0:
				for n in range(1,10):
					if possible(y,x,n):
						puzzle[y][x] = n
						solve()
						puzzle[y][x] = 0
				return
	print(np.matrix(puzzle))


#-------------------------------------------------------------------------------------------------------------------#
#	Test Area																										#
#-------------------------------------------------------------------------------------------------------------------#
solve()
