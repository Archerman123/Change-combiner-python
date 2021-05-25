import pygame

pygame.font.init()

MENUFONT = pygame.font.Font("freesansbold.ttf", 20)
UIFONT = pygame.font.Font("freesansbold.ttf", 22)

def makeFont(size):
	return pygame.font.Font("freesansbold.ttf", int(size))