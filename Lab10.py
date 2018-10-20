# Class:	        	CSE 1321L
# Section:		12         
# Term:		Fall  
# Instructor:	Kevin Markley 
# Name:		Dexter Onyewuchi   
# Lab:	10

#Rectangle

class Rectangle:
	def __init__(self, height = 1 , width = 1):
		self.height = height
		self.width = width
	def getArea(self):
		area = self.height * self.width
		return area
	def getPerimeter(self):
		perimeter = 2*(self.height + self.width)
		return perimeter
	def getHeight(self):
		return self.height
	def getWidth(self):
		return self.width
	def main(self):
		print(f'Height:\t\t{self.getHeight()}')
		print(f'Width:\t\t{self.getWidth()}')
		print(f'Area:\t\t{self.getArea()}')
		print(f'Perimeter:\t{self.getPerimeter()}\n')

x = Rectangle()
y = Rectangle(height = 5, width = 6)
x.main()
y.main()

# Stock

class Stock:
	def __init__(self, stock, symbol, pcp, cp):
		self.stock = stock
		self.symbol = symbol
		self.previousClosingPrice = pcp
		self.currentPrice = cp
	def getName(self):
		return self.stock
	def getSymbol(self):
		return self.symbol
	def setClosingPrice(self):
		return self.previousClosingPrice
	def setCurrentPrice(self):
		return self.currentPrice
	def getChangePercent(self):
		return f'{round(((self.currentPrice/self.previousClosingPrice) - 1)*100)}%'
	def toString(self):
		print(f'\t{self.stock} stock closing price is ${self.setCurrentPrice()}\n')
	def main(self):
		print(f'{self.getName()} stock:')
		print(f'\tSymbol:\t\t{self.getSymbol()}')
		print(f'\tClosing price:\t{self.setClosingPrice()}')
		print(f'\tCurrent price:\t{self.setCurrentPrice()}')
		print(f'\tChange percent:\t{self.getChangePercent()}')
		self.toString()

google = Stock('Google', 'GOG', 134.67, 131.98)
microsoft = Stock('Microsoft', 'MSF', 156.52, 161.22)
google.main()
microsoft.main()