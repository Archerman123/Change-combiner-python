
class coin():
	def __init__(self,value,color, image = "", scale = 100):
		self.value = value
		self.color = color
		self.image = image
		self.scale = scale

	def getVal(self):
		return self.value

	def getCol(self):
		return self.color

	def getImg(self):
		return self.image

	def getScale(self):
		return self.scale