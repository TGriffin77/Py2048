# import logic functions
import logic
import graphics

import pygame
import sys

if __name__ == '__main__':
	
# calls start_game to initialize game, set to mat to create the beginning matrix
	mat = logic.start_game()
	
	screen = graphics.start_graphics()
	
	score = 0

while True:
	
	graphics.place_blocks(screen, mat)
	graphics.update_score(screen, score)

	pygame.display.update()

	#print the matrix before each move
	score_incr = 0
	# take user input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('w'):
				mat, flag, score_incr = logic.move_up(mat)

				# get the current state and print it
				status = logic.get_current_state(mat)
				print(status)

				# if game not over then continue
				if(status == 'GAME NOT OVER' and flag):
					logic.add_new_2(mat)
				else:
					break

			if event.key == pygame.K_RIGHT or event.key == ord('a'):
				mat, flag, score_incr = logic.move_left(mat)
				status = logic.get_current_state(mat)
				print(status)
				if(status == 'GAME NOT OVER' and flag):
					logic.add_new_2(mat)
				else:
					break

			if event.key == pygame.K_UP or event.key == ord('s'):
				mat, flag, score_incr = logic.move_down(mat)
				status = logic.get_current_state(mat)
				print(status)
				if(status == 'GAME NOT OVER' and flag):
					logic.add_new_2(mat)
				else:
					break

			if event.key == pygame.K_UP or event.key == ord('d'):
				mat, flag, score_incr = logic.move_right(mat)
				status = logic.get_current_state(mat)
				print(status)
				if(status == 'GAME NOT OVER' and flag):
					logic.add_new_2(mat)
				else:
					break
	score += score_incr
