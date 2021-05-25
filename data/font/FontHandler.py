import pygame

pygame.font.init()

MENUFONT = pygame.font.Font("data/font/freesansbold.ttf", 20)
UIFONT = pygame.font.Font("data/font/freesansbold.ttf", 22)

def makeFont(size):
	return pygame.font.Font("data/font/freesansbold.ttf", int(size))