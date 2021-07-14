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
pygame.display.set_caption("Coin combiner: Menu")
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
	CurrentGame = False
	while True:
		screen.fill((0, 0, 0))
		draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

		mx, my = pygame.mouse.get_pos()

		buttons = []
		yLevel = 100
		buttons.append([pygame.Rect(50, yLevel, 250, 25)])
		pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, yLevel, 300, 25))
		draw_text("New Game", font, (255, 255, 255), screen, 50,yLevel + 5)
		yLevel += 50

		if CurrentGame:
			buttons.append([pygame.Rect(50, yLevel, 250, 25)])
			pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, yLevel, 300, 25))
			draw_text("continue", font, (255, 255, 255), screen, 50,yLevel + 5)
			yLevel += 50

			if buttons[1][0].collidepoint((mx, my)):
				if click:
					CurrentGame.play()

		if buttons[0][0].collidepoint((mx, my)):
			if click:
				CurrentGame = Game.game((options))



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
		draw_text("Disable", font, (255, 255, 255), screen, 20,80)
		draw_text("Enable", font, (255, 255, 255), screen, 175,80)

		cur = options["Currency"]
		cur = CUR_LIST[int(cur)].getName()
		draw_text('Currency: ' + cur, font, (255, 255, 255), screen, 20, 120)
		btn3 = pygame.Rect(20, 150, 125, 20)
		if btn3.collidepoint((mx, my)):
			if click:
				curSel(-1, options)

		btn4 = pygame.Rect(175, 150, 125, 20)
		if btn4.collidepoint((mx, my)):
			if click:
				curSel(1, options)

		pygame.draw.rect(screen, (255, 0, 0), btn3)
		pygame.draw.rect(screen, (255, 0, 0), btn4)
		draw_text("<", font, (255, 255, 255), screen, 20,150)
		draw_text(">", font, (255, 255, 255), screen, 175,150)

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

def curSel(jump,options):
	if int(options["Currency"])+jump >= len(CUR_LIST):
		options["Currency"] = 0
	elif int(options["Currency"])+jump <= 0:
		options["Currency"] = len(CUR_LIST)-1
	else:
		options["Currency"] = int(options["Currency"])+jump

main_menu()
