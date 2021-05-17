class tile():
	def __init__(self,value):
		self.value = value
		self.selected = False

	def getValue(self):
		return self.value

	def setValue(self,value):
		self.value = value

	def setSelected(self,value):
		self.selected = value

	def isSelected(self):
		return self.selected