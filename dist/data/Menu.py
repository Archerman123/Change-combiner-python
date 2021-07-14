#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
# taken from https://www.youtube.com/watch?v=0RryiSjpJn0&ab_channel=DaFluffyPotato
import pygame
import sys
import Game
from CurrencyList import *
from FontHandler import *
import JsonReader
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = MENUFONT
optionFile = JsonReader.reader("data/Options.json")

def changeOptions(toChange, newVal,options):
		options[toChange] = newVal
		optionFile.writeData(options)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
	options = optionFile.getData()
	click = False
	while True:
		screen.fill((0, 0, 0))
		draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

		mx, my = pygame.mouse.get_pos()

		buttons = []
		yLevel = 100
		for cur in CUR_LIST:
			buttons.append([pygame.Rect(50, yLevel, 250, 25),cur])
			pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, yLevel, 300, 25))
			draw_text(cur.getName(), font, (255, 255, 255), screen, 50,yLevel + 5)
			yLevel += 50

		for butts in buttons:
			if butts[0].collidepoint((mx, my)):
				if click:
					Game.game(options)

		button_options = pygame.Rect(50, yLevel, 300, 25)
		if button_options.collidepoint((mx, my)):
			if click:
				optionMenu(options)
		pygame.draw.rect(screen, (255, 0, 0), button_options)
		draw_text("Options", font, (255, 255, 255), screen, 50,yLevel + 5)
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		mainClock.tick(60)

def optionMenu(options):
	running = True
	click = False
	while running:

		screen.fill((0, 0, 0))

		mx, my = pygame.mouse.get_pos()

		draw_text('options', font, (255, 255, 255), screen, 20, 20)
		draw_text('Text on coins: ' + options["Text Overlay"], font, (255, 255, 255), screen, 20, 50)

		btn1 = pygame.Rect(20, 80, 125, 20)
		if btn1.collidepoint((mx, my)):
			if click:
				changeOptions("Text Overlay","False",options)

		btn2 = pygame.Rect(175, 80, 125, 20)
		if btn2.collidepoint((mx, my)):
			if click:
				changeOptions("Text Overlay","True",options)

		pygame.draw.rect(screen, (255, 0, 0), btn1)
		pygame.draw.rect(screen, (255, 0, 0), btn2)
		draw_text("Make False", font, (255, 255, 255), screen, 20,80)
		draw_text("Make True", font, (255, 255, 255), screen, 175,80)

		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		mainClock.tick(60)



main_menu()
