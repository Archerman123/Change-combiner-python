import Tile
import Currency
from Colors import *
from Currency import *

class grid():
	def __init__(self):
		self.row = 10
		self.column = 10
		self.tWidth = 50
		self.tHeight = 50
		self.tMargin = 10
		self.grid = []
		self.regenGrid()

	def getRowLenght(self):
		return self.row

	def getColumnLenght(self):
		return self.column

	def regenGrid(self):
		for row in range(self.row):
			self.grid.append([])
			for column in range(self.column):
				self.grid[row].append(Tile.tile(0))

	def setTileValue(self,row,column,value):
		self.grid[row][column].setValue(value)

	def getGrid(self):
		return self.grid

	def	getTileValue(self,row,column):
		return self.grid[row][column].getValue()

	def getTileWidth(self):
		return self.tWidth

	def getTileHeight(self):
		return self.tHeight

	def getTileMargin(self):
		return self.tMargin

	def getSelectedValue(self):
		total = 0
		for row in range(self.row):
			for column in range(self.column):
				if self.grid[row][column].isSelected():
					total += CANADIEN_CUR.getCoinById(self.grid[row][column].getValue()).getVal()
		return total

	def combine(self,row,column):
		total = self.getSelectedValue()
		combined = False
		cashGain = 0
		result = CANADIEN_CUR.getIdByValue(total)
		#print(result)
		if result == "Bill!":
			combined = True
			cashGain = total
		if result:
			newID = result
			#print(newID)
		else:
			return False

		for rowL in range(self.row):
			for columnL in range(self.column):
				if self.grid[rowL][columnL].isSelected():
					self.grid[rowL][columnL].setValue(0)

		if not result == "Bill!":
			self.grid[row][column].setValue(newID)

		return cashGain

	def unselectAll(self):
		for row in range(self.row):
			for column in range(self.column):
				self.grid[row][column].setSelected(False)

	def isSelect(self,row,column):
		return self.grid[row][column].isSelected()

	def setSelect(self,row,column,value):
		self.grid[row][column].setSelected(value)