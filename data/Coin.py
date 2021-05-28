
class coin():
	def __init__(self,value,color, image = ""):
		self.value = value
		self.color = color
		self.image = image

	def getVal(self):
		return self.value

	def getCol(self):
		return self.color

	def getImg(self):
		return self.image