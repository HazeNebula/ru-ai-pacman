# Exercise made by Jasper van den Bogart (4781686) and Niels van Nistelrooij (4713648)
"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart( orderList, fruitShops ):
	"""
		orderList: List of (fruit, numPound) tuples
		fruitShops: List of FruitShops
	"""
	prices = [fruitShop.getPriceOfOrder( orderList ) for fruitShop in fruitShops]

	minIndex = 0
	minPrice = fruitShops[0].getPriceOfOrder( orderList )
	for index in range( len( fruitShops ) ):
		orderPrice = fruitShops[index].getPriceOfOrder( orderList )
		if ( orderPrice != None and minPrice != None and orderPrice < minPrice):
			minIndex = index
	minPrice = orderPrice

	return fruitShops[minIndex]

fruits1 = { 'apples': 2.0, 'oranges': 1.0 }
fruits2 = { 'apples': 1.0, 'oranges': 5.0 }
shop1 = shop.FruitShop( 'shop1', fruits1 )
shop2 = shop.FruitShop( 'shop2', fruits2 )
shops = [shop1, shop2]
orders1 = [('apples', 1.0), ('oranges', 3.0)]
orders2 = [('apples', 3.0)]
print( "For order", orders1, "the best shop is", shopSmart( orders1, shops ).getName() )
print( "For order", orders2, "the best shop is", shopSmart( orders2, shops ).getName() )
