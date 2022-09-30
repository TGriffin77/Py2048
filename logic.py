# import to 2048.py

import random

# function to initialize game
def start_game():

	# Declares an empty 4x4 matrix
	mat = []
	for i in range(4):
		mat.append([0]*4)

	# calls the add_new to randomly place a 2 on the board
	add_new(mat)
	# calls the add_new2 to randomly place either a 2 or 4 on the board
	add_new_2(mat)
	return mat


# functon to add a new 2 in a random cell
def add_new(mat):
	r = random.randrange(0,4)
	c = random.randrange(0,4)
	
	mat[r][c] = 2

# function to add a new 2 or 4 in a random cell
def add_new_2(mat):

	# finds how many empty cells there are left
	val = 16
	for i in mat:
		for j in i:
			if j != 0:
				val -= 1

	# will only run if there are still empty cells
	if val != 0:
		# chooses a random index for new cell. Also chooses either 2 or 4 for the new cell's value
		r = random.randrange(0, 4)
		c = random.randrange(0, 4)
		number = random.choice([2,4])

		# While loop will break when it finds an empty cell
		while mat[r][c] != 0:
			# generators a random index
			r = random.randrange(0, 4)
			c = random.randrange(0, 4)

		# Will place the random value of "2 or 4" in the index
		mat[r][c] = number

# function to get current state of game
def get_current_state(mat, won):

	# if any cell value equals 2048, WIN
	if not won:
		for i in range(4):
			for j in range(4):
				if mat[i][j]== 2048:
					return 'WON'

	# If there is still an empty cell, GAME NOT OVER
	for i in range(4):
		for j in range(4):
			if mat[i][j]== 0:
				return 'GAME NOT OVER'

	# Any adjacent cells can be combined, GAME NOT OVER
	for i in range(3):
		for j in range(3):
			if mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]:
				return 'GAME NOT OVER'

	for j in range(3):
		if mat[3][j]== mat[3][j + 1]:
			return 'GAME NOT OVER'

	for i in range(3):
		if mat[i][3]== mat[i + 1][3]:
			return 'GAME NOT OVER'

	# Else, LOSE
	return 'LOST'

# Moves everything to max left position
def compress(mat):

	# Determines if change during turn
	changed = False

	# empty new matrix
	new_mat = []
	for i in range(4):
		new_mat.append([0] * 4)
		
	# shifts all values into the left-most extreme
	for i in range(4):
		pos = 0
		for j in range(4):
			if mat[i][j] != 0:
				
				# if cell is not empty, place into the next unoccupied cell in that row
				new_mat[i][pos] = mat[i][j]
				
				# Changes to True, if the value is not in same cell as before
				if j != pos:
					changed = True
				pos += 1

	# return new matrix and change-state
	return new_mat, changed

# Merge Like numbers
def merge(mat):
	
	changed = False

	score_incr = 0
	
	for i in range(4):
		for j in range(3):

			# if cell has same value as next cell and not zero
			if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:

				# double current cell, make next cell empty
				mat[i][j] = mat[i][j] * 2
				mat[i][j + 1] = 0
				score_incr +=mat[i][j]

				# check if a change happened
				changed = True

	return mat, changed, score_incr

# reverse the matrix
def reverse(mat):
	new_mat =[]
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[i][3 - j])
	return new_mat

# transpose the matrix
def transpose(mat):
	new_mat = []
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[j][i])
	return new_mat

# moves cell left
def move_left(grid):

	new_grid, changed1 = compress(grid)

	new_grid, changed2, score_incr = merge(new_grid)
	
	changed = changed1 or changed2

	new_grid, temp = compress(new_grid)

	return new_grid, changed, score_incr

# moves cells right
def move_right(grid):

	new_grid = reverse(grid)

	new_grid, changed, score_incr = move_left(new_grid)

	new_grid = reverse(new_grid)
	return new_grid, changed, score_incr

# moves cells up
def move_up(grid):

	new_grid = transpose(grid)

	new_grid, changed, score_incr = move_left(new_grid)

	new_grid = transpose(new_grid)
	return new_grid, changed, score_incr

# moves cells down
def move_down(grid):

	new_grid = transpose(grid)

	new_grid, changed, score_incr = move_right(new_grid)

	new_grid = transpose(new_grid)
	return new_grid, changed, score_incr