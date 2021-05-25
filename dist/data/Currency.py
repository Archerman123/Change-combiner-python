import Coin

class currency():
	def __init__(self,name,changeType,noteType = ''):
		self.currencyName = name
		self.wallet = []
		self.bills = []
		self.changeType = changeType
		self.noteType = noteType

	def getName(self):
		return self.currencyName

	def getNType(self):
		return self.noteType

	def getType(self):
		return self.changeType

	def addCoin(self,value,color):
		self.wallet.append(Coin.coin(value,color))

	def addBill(self,value):
		self.bills.append(value)

	def size(self):
		return len(self.wallet)

	def getCoinByValue(self,value):
		for coin in self.wallet:
			if coin.getVal() == value:
				return coin
		return False

	def getCoinById(self,id):
		if id <= len(self.wallet):
			return self.wallet[id - 1]

	def getIdByValue(self,value):
		for coin in self.wallet:
			if coin.getVal() == value:
				return self.wallet.index(coin) + 1
		for bills in self.bills:
			if bills == value:
				return "Bill!"
		return False
