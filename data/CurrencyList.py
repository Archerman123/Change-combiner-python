import Currency
from Colors import *

CUR_LIST = []

CAN_CUR = Currency.currency("Canadien Basic",'¢','$')
CAN_CUR.addCoin(1,BRONZE)
CAN_CUR.addCoin(5,SILVER)
CAN_CUR.addCoin(10,DARK_GRAY)
CAN_CUR.addCoin(25,GOLD)
CAN_CUR.addBill(100)

CAN_CUR_TRUE = Currency.currency("True Canadien",'¢','$')
#CAN_CUR_TRUE.addCoin(1,BRONZE)
CAN_CUR_TRUE.addCoin(5,SILVER)
CAN_CUR_TRUE.addCoin(10,DARK_GRAY)
CAN_CUR_TRUE.addCoin(25,GOLD)
CAN_CUR_TRUE.addCoin(100,BLUE)
CAN_CUR_TRUE.addCoin(200,PURPLE)
CAN_CUR_TRUE.addBill(500)
CAN_CUR_TRUE.addBill(1000)
CAN_CUR_TRUE.addBill(2000)

BRIT_CUR = Currency.currency("British sterling basic",'p','£')
BRIT_CUR.addCoin(1,BRONZE)
BRIT_CUR.addCoin(2,DARK_BROWN)
BRIT_CUR.addCoin(5,SILVER)
BRIT_CUR.addCoin(10,DARK_GRAY)
BRIT_CUR.addCoin(20,GOLD)
BRIT_CUR.addCoin(50,BLUE)
BRIT_CUR.addBill(100)

BRIT_CUR_TRUE = Currency.currency("True British sterling",'p','£')
BRIT_CUR_TRUE.addCoin(1,BRONZE)
BRIT_CUR_TRUE.addCoin(2,DARK_BROWN)
BRIT_CUR_TRUE.addCoin(5,SILVER)
BRIT_CUR_TRUE.addCoin(10,DARK_GRAY)
BRIT_CUR_TRUE.addCoin(20,GOLD)
BRIT_CUR_TRUE.addCoin(50,BLUE)
BRIT_CUR_TRUE.addCoin(100,PURPLE)
BRIT_CUR_TRUE.addCoin(200,GREEN)
BRIT_CUR_TRUE.addBill(500)
BRIT_CUR_TRUE.addBill(2000)

AUST_CUR = Currency.currency("Australian dollar basic",'c','$')
AUST_CUR.addCoin(5,SILVER)
AUST_CUR.addCoin(10,DARK_GRAY)
AUST_CUR.addCoin(20,GOLD)
AUST_CUR.addCoin(50,BLUE)
AUST_CUR.addBill(100)

CUR_LIST.append(CAN_CUR)
CUR_LIST.append(CAN_CUR_TRUE)
CUR_LIST.append(BRIT_CUR)
CUR_LIST.append(BRIT_CUR_TRUE)
CUR_LIST.append(AUST_CUR)