# Exercise made by Jasper van den Bogart (4781686) and Niels van Nistelrooij (4713648)

fruitPrices = { 'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
	'limes': 0.75, 'strawberries': 1.00
}

def buyLotsOfFruit( orderList ):
	"""
		orderList: List of (fruit, numPounds) tuples

	Returns cost of order
	"""

	sum = 0.0
	for fruit, pounds in orderList:
		if fruit in fruitPrices:
			sum = sum + pounds * fruitPrices[fruit]
		else:
			return None

	return sum

orderList = [('apples', 2), ('pears', 3), ('limes', 4)]
print( 'Cost of', orderList, 'is', buyLotsOfFruit( orderList ) )
