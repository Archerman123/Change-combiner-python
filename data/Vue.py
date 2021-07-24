import sys
sys.path.append('pygame')
import pygame
from Colors import *
TILE_IMG_ONE = pygame.image.load("data/img/Tile1.png")

class vue():
	def __init__(self,screen,grid):
		self.screen = screen
		self.grid = grid
		self.margin = self.grid.getTileMargin()
		self.width = self.grid.getTileWidth()
		self.height = self.grid.getTileHeight()

	def printEmptySquare(self,column,row):
		color = WHITE
		pygame.draw.rect(self.screen,
                        color,
                        [(self.margin + self.width) * column + self.margin,
                        (self.margin + self.height) * row + self.margin,
                        self.width,
                        self.height])
		imgTile = TILE_IMG_ONE
		imgTile = pygame.transform.scale(imgTile, (self.width, self.height))
		self.screen.blit(imgTile,[(self.margin + self.width) * column + self.margin,
                    (self.margin + self.height) * row + self.margin,
                    self.width,
                    self.height])