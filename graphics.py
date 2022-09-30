# import to 2048.py

import pygame
from constants import *

def start_graphics():
	pygame.init()
	screen = pygame.display.set_mode(RES)
	pygame.display.set_caption('2048')

	screen.fill(BG_COLOR)
	new_game_button(screen)

	icon = pygame.image.load('assets/2048_logo.png')
	pygame.display.set_icon(icon)
	
	return screen


def cell_description(matrix):
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

	return color_grid, font_color_grid, font_size


def place_blocks(screen, matrix):
	
	color_grid, font_color_grid, font_size = cell_description(matrix)

	font = pygame.font.Font(FONT, font_size)

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


def only_text(screen, center, color, font, string):
	text = font.render(string, True, color)
	display_text = text.get_rect()
	display_text.center = center
	screen.blit(text, display_text)


def text_with_box(screen, left, top, width, height, box_color, font, font_color, string):
	box = pygame.Rect(left, top, width, height)
	box_rect = pygame.draw.rect(screen, box_color, box, border_radius=2)

	box_text = font.render(string, True, font_color)
	display_text = box_text.get_rect()
	display_text.center = box_rect.center
	screen.blit(box_text, display_text)

	return box


def update_score(screen, score):
	font = pygame.font.Font(FONT, 64)

	scoreboard = text_with_box(screen, 8, 82, 304, 78, BOX_COLOR, font, TEXT_COLOR, str(score))

	text = font.render("Score", True, (119,110,101))
	display_text = text.get_rect()
	display_text.midbottom = scoreboard.midtop
	screen.blit(text, display_text)


def new_game_button(screen):
	font = pygame.font.Font(FONT, 56)
	
	text_with_box(screen, 328, 82, 304, 78, BOX_COLOR, font, TEXT_COLOR, "New Game")


def lose_screen(screen):
	font = pygame.font.Font(FONT, 56)
	#Alpha color
	s = pygame.Surface((640,640))
	s.set_alpha(128)
	s.fill(BG_COLOR)
	screen.blit(s, (0,160))

	# Game Over Text
	only_text(screen, (320, 420), TEXT_COLOR, font, "Game Over")

	# Try again? Button
	font = pygame.font.Font(FONT, 36)
	text_with_box(screen, 204, 480, 232, 52, BOX_COLOR, font, TEXT_COLOR, "Try Again?")

def win_screen(screen):
	font = pygame.font.Font(FONT, 56)
	# Alpha color
	s = pygame.Surface((640,640))
	s.set_alpha(128)
	s.fill(BG_COLOR)
	screen.blit(s, (0,160))

	# You Win! Text
	only_text(screen, (320, 420), TEXT_COLOR, font, "You Win!")

	# Continue? Button
	font = pygame.font.Font(FONT, 36)
	text_with_box(screen, 204, 480, 232, 52, BOX_COLOR, font, TEXT_COLOR, "Continue?")