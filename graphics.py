# import to 2048.py

import pygame

def start_graphics():
	pygame.init()
	screen = pygame.display.set_mode((640,800))
	pygame.display.set_caption('2048')

	screen.fill((187,173,160))
	

	return screen

def place_blocks(screen, matrix):
	
	font_size = 74

	color_grid = []
	for i in range(4):
		color_grid.append([0]*4)

	font_color_grid = []
	for i in range(4):
		font_color_grid.append([(249,246,242)]*4)


	for i in range(4):
		for j in range(4):
			match matrix[i][j]:
				case 0:
					color_grid[i][j] = (203,192,177)
				case 2:
					color_grid[i][j] = (238,228,217)
					font_color_grid[i][j] = (119,110,101)
				case 4:
					color_grid[i][j] = (237,224,200)
					font_color_grid[i][j] = (119,110,101)
				case 8:
					color_grid[i][j] = (242,177,121)
				case 16:
					color_grid[i][j] = (245,149,99)
				case 32:
					color_grid[i][j] = (246,124,95)
				case 64:
					color_grid[i][j] = (246,94,59)
				case 128:
					color_grid[i][j] = (237,207,114)
				case 256:
					color_grid[i][j] = (237,204,97)
				case 512:
					color_grid[i][j] = (237,200,80)
				case 1024:
					color_grid[i][j] = (237,197,63)
					font_size = 58
				case 2048:
					color_grid[i][j] = (237,194,46)
					font_size = 58
				case _:
					color_grid[i][j] = (60,58,50)
					font_size = 58

	font = pygame.font.Font("assets/ClearSans-Bold.ttf", font_size)

	# place the block and text
	block_top = 168
	WIDTH = 144
	HEIGHT = 144
	for row in range(4):
		block_left = 8
		for col in range(4):
			cell = pygame.Rect(block_left, block_top, WIDTH, HEIGHT)
			pygame.draw.rect(screen, color_grid[row][col], cell, border_radius=2)
			block_left += 160
			if matrix[row][col] != 0:
				text = font.render(str(matrix[row][col]), True, font_color_grid[row][col])
				display_text = text.get_rect()
				display_text.center = cell.center
				screen.blit(text, display_text)
		block_top += 160

def update_score(screen, score):
	font = pygame.font.Font("assets/ClearSans-Bold.ttf", 64)

	scorebox = pygame.Rect(8, 82, 304, 78)
	scoreboard = pygame.draw.rect(screen, (143,122,102), scorebox, border_radius=2)

	score_text = font.render(str(score), True, (249,246,242))
	display_score = score_text.get_rect()
	display_score.center = scoreboard.center
	screen.blit(score_text, display_score)

	text = font.render("Score", True, (119,110,101))
	display_text = text.get_rect()
	display_text.midbottom = scoreboard.midtop
	screen.blit(text, display_text)

	