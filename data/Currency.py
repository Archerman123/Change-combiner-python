import Coin
from Colors import *
class currency():
	def __init__(self,name):
		self.currencyName = name
		self.wallet = []
		self.bills = []

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

CANADIEN_CUR = currency("Canadien")
CANADIEN_CUR.addCoin(1,BRONZE)
CANADIEN_CUR.addCoin(5,SILVER)
CANADIEN_CUR.addCoin(10,DARK_GRAY)
CANADIEN_CUR.addCoin(25,GOLD)
#CANADIEN_CUR.addCoin(100,GOLD)
#CANADIEN_CUR.addCoin(200,GOLD)
CANADIEN_CUR.addBill(100)
CANADIEN_CUR.addBill(200)
CANADIEN_CUR.addBill(500)