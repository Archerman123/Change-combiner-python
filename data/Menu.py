#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
# taken from https://www.youtube.com/watch?v=0RryiSjpJn0&ab_channel=DaFluffyPotato
from pygame.locals import *
import pygame
import sys
import Game
from CurrencyList import *
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
	while True:
		screen.fill((0, 0, 0))
		draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

		mx, my = pygame.mouse.get_pos()

		button_1 = pygame.Rect(50, 100, 200, 50)
		button_2 = pygame.Rect(50, 200, 200, 50)
		button_3 = pygame.Rect(50, 300, 200, 50)
		button_4 = pygame.Rect(50, 400, 200, 50)
		if button_1.collidepoint((mx, my)):
			if click:
				game(CAN_CUR)
		if button_2.collidepoint((mx, my)):
			if click:
				game(CAN_CUR_TRUE)
		if button_3.collidepoint((mx, my)):
			if click:
				game(BRIT_CUR)
		if button_4.collidepoint((mx, my)):
			if click:
				options()
		pygame.draw.rect(screen, (255, 0, 0), button_1)
		pygame.draw.rect(screen, (255, 0, 0), button_2)
		pygame.draw.rect(screen, (255, 0, 0), button_3)
		pygame.draw.rect(screen, (255, 0, 0), button_4)

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		mainClock.tick(60)


def game(currency):
	running = True
	while running:
		screen.fill((0, 0, 0))

		Game.game(currency)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		pygame.display.update()
		mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
