# import logic functions
import logic

if __name__ == '__main__':
	
# calls start_game to initialize game, set to mat to create the beginning matrix
	mat = logic.start_game()

while(True):
	#print the matrix before each move
	for row in mat:
		print(row)

	# take user input
	x = input("Press the command : ")

	# Move up
	if(x == 'W' or x == 'w'):

		# call the move_up function
		mat, flag = logic.move_up(mat)

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		# if game not over then continue
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# Move down
	elif(x == 'S' or x == 's'):
		mat, flag = logic.move_down(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# Move left
	elif(x == 'A' or x == 'a'):
		mat, flag = logic.move_left(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# Move right
	elif(x == 'D' or x == 'd'):
		mat, flag = logic.move_right(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")
