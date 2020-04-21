from ships import Ship

def placeShips(board):

	def singlePlayer(name, size):
		newShip = Ship(name)
		newShip.generateShip(size)

		while board.checkAgainstBoard(newShip.coordinates, newShip.orientation):
			newShip.generateShip(size)
		else:
			board.updateBoard(newShip.coordinates, False) #False = pierwszy użytkownik, zostawiam na multiplayer :)

	singlePlayer("Radek", 5)
	singlePlayer("Radek", 4)
	singlePlayer("Radek", 4)
	singlePlayer("Radek", 3)
	singlePlayer("Radek", 3)
	singlePlayer("Radek", 2)

	return None

def getInput():
	correct = False

	while not correct:
		try:
			number = input("=>Od 1 do 10:")
			if int(number) in range(1,11):
				correct = True
			else:
				print("Podaj liczbę od 1 do 10:")
				continue

		except ValueError:
			print("NIE CWANIAKUJ! Podaj liczbę!")
			continue

	return int(number)