# import logic functions
import logic
import graphics
from constants import *

import pygame
import sys
import time

if __name__ == '__main__':
	
# calls start_game to initialize game, set to mat to create the beginning matrix
	mat = logic.start_game()
	
	screen = graphics.start_graphics()
	
	score = 0
	won = False
	game_status = 'GAME NOT OVER'


while True:

	graphics.place_blocks(screen, mat)
	graphics.update_score(screen, score)
	if game_status == 'LOST':
		graphics.lose_screen(screen)
	elif game_status == 'WON':
		graphics.win_screen(screen)
	graphics.new_game_button(screen)
	pygame.display.update()

	mouse = pygame.mouse.get_pos()

	score_incr = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# Checks Mouse Clicks
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (328 <= mouse[0] <= 632 and 82 <= mouse[1] <= 160) or (game_status == 'LOST' and (204 <= mouse[0] <= 436 and 480 <= mouse[1] <= 532)):
				screen.fill(BG_COLOR)
				mat = logic.start_game()
				score = 0
				won = False
				game_status = 'GAME NOT OVER'

			if game_status == 'WON' and (204 <= mouse[0] <= 436 and 480 <= mouse[1] <= 532):
				screen.fill(BG_COLOR)
				game_status = 'GAME NOT OVER'
				won = True
		
		# Keyboard Input
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('w'):
				mat, flag, score_incr = logic.move_up(mat)

				# get the current state and print it
				status = logic.get_current_state(mat, won)

				# if game not over then continue
				if(status == 'GAME NOT OVER' and flag):
					logic.add_new_2(mat)
				else:
					game_status = status
					break

			if event.key == pygame.K_RIGHT or event.key == ord('a'):
				mat, flag, score_incr = logic.move_left(mat)
				status = logic.get_current_state(mat, won)
				if status == 'GAME NOT OVER' and flag:
					logic.add_new_2(mat)
				else:
					game_status = status
					break

			if event.key == pygame.K_UP or event.key == ord('s'):
				mat, flag, score_incr = logic.move_down(mat)
				status = logic.get_current_state(mat, won)
				if status == 'GAME NOT OVER' and flag:
					logic.add_new_2(mat)
				else:
					game_status = status
					break

			if event.key == pygame.K_UP or event.key == ord('d'):
				mat, flag, score_incr = logic.move_right(mat)
				status = logic.get_current_state(mat, won)
				if status == 'GAME NOT OVER' and flag:
					logic.add_new_2(mat)
				else:
					game_status = status
					break
				
	score += score_incr
	pygame.time.wait(10)
