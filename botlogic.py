import keyboard
import logic
import random

def input_next_move(matrix):
	score_dict = {
		"up" : [0]*3,
		"left" : [0]*3,
		"down" : [0]*3,
		"right" : [0]*3,
	}
	for move in score_dict:
		new_matrix = []
		for i in range(4):
			new_matrix.append([0]*4)
		for i in range(4):
			for j in range(4):
				new_matrix[i][j] = matrix[i][j]
		
		score_dict[move] = simulate_move(new_matrix, matrix, move)
	
	# Find largest Value, if all equal, find the best amount combined, or find best next_move
	max = [0,0,0]
	best_move = ''
	for i in range(3):
		for move in score_dict:
			if score_dict[move][i] > max[i]:
				best_move = move
				max[i] = score_dict[move][i]
		if max[i] != 0:
			break
	
	match best_move:
		case "up":
			keyboard.press_and_release('w')
		case "left":
			keyboard.press_and_release('a')
		case "down":
			keyboard.press_and_release('s')
		case "right":
			keyboard.press_and_release('d')
		case _:
			key = random.choice(['w','a','s','d'])
			keyboard.press_and_release(key)

# function to simulate the next move for each input
def simulate_move(matrix_test, matrix_orig, move):
	score_incr = 0
	
	match move:
		case "up":
			matrix_test, temp, score_incr = logic.move_up(matrix_test)
		case "left":
			matrix_test, temp, score_incr = logic.move_left(matrix_test)
		case "down":
			matrix_test, temp, score_incr = logic.move_down(matrix_test)
		case "right":
			matrix_test, temp, score_incr = logic.move_right(matrix_test)
	
	orig_total_cells = 0
	for row in matrix_orig:
		for cell in row:
			if cell != 0:
				orig_total_cells+=1

	test_total_cells = 0
	for row in matrix_test:
		for cell in row:
			if cell != 0:
				test_total_cells+=1

	net_total_cells = orig_total_cells - test_total_cells
	
	next_move = 0
	if score_incr and net_total_cells == 0:
		# Any adjacent cells can be combined
		for i in range(3):
			for j in range(3):
				if matrix_test[i][j] == matrix_test[i + 1][j] or matrix_test[i][j] == matrix_test[i][j + 1]:
					next_move+=1

		for j in range(3):
			if matrix_test[3][j] == matrix_test[3][j + 1]:
				next_move+=1

		for i in range(3):
			if matrix_test[i][3] == matrix_test[i + 1][3]:
				next_move+=1

	return [score_incr, net_total_cells, next_move] 
	#return [score_incr, next_move, net_total_cells] 
	#return [next_move, net_total_cells, score_incr] 
	#return [next_move, score_incr, net_total_cells] 
	#return [net_total_cells, next_move, score_incr] 
	#return [net_total_cells, score_incr, next_move] 
	
