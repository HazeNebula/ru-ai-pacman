shopNames = ['Aldi', 'Albert Heijn']
shopPrices = [{ 'apples': 1.00, 'oranges': 1.50, 'pears': 1.75 }, { 'kiwis': 6.00, 'apples': 4.50, 'peaches': 8.75 }]

for index in range( len( shopNames ) ):
	print( 'Welcome to ' + shopNames[index] + ' fruit shop' )
	apples = shopPrices[index]['apples']
	print( apples )
	print( 'Apples cost %.2f at %s.' % (apples, shopNames[index]) )