# Exercise made by Jasper van den Bogart (4781686) and Niels van Nistelrooij (4713648)

def quickSort( list ):
	if len( list ) <= 1:
		return list
	else:
		p = list[0]
		return quickSort( [e for e in list[1:] if e <= p] ) + [p] + quickSort( [e for e in list[1:] if e > p] )

print( quickSort( [2, 3, 1, 2, 5] ) )
