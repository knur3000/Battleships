class Board:
	def __init__(self):
		self.hiddenBoard = self.createBoard()
		self.userBoard = self.createBoard()

	def __str__(self):
		printable = []
		for line in self.userBoard:
			printable.append(" ".join(line))
		return "\n".join(printable)

	def createBoard(self):
		board = [["@" for y in range(12)] for x in range(12)]

		for index, line in enumerate(board):
			insertChar = ["*"] * 10

			if index not in [0, 11]:
				line[0] = str(index)
				line[1:-1] = insertChar
			else:
				line[1:11] = [str(i) for i in range(1,11)]

		return board

	def updateBoard(self, coordinates, user):
		"""Pobiera dane z klasy Ship. Przygotowane na dwóch graczy."""
		if user:
			for i in coordinates:
				self.hiddenBoard[i[0]][i[1]] = "X"
		else:
			for i in coordinates:
				self.hiddenBoard[i[0]][i[1]] = "Y"

		return None

	def checkAgainstBoard(self, coordinates, isHorizontal):
		neighbours = []

		if isHorizontal:
			start = coordinates[0]
			end = coordinates[-1]
			neighboursUp = [neighbours.append([self.hiddenBoard[point[0] + 1][point[1]], self.hiddenBoard[point[0] - 1][point[1]]])
							for point in coordinates]
			neighboursLeft = neighbours.append([self.hiddenBoard[start[0]][start[1] - 1], self.hiddenBoard[start[0] - 1][start[1] - 1],
				 			self.hiddenBoard[start[0] + 1][start[1] - 1]])
			neighboursRight = neighbours.append([self.hiddenBoard[end[0]][end[1] + 1], self.hiddenBoard[end[0] - 1][end[1] + 1],
				 			self.hiddenBoard[end[0] + 1][end[1] + 1]])

		else:
			start = coordinates[0]
			end = coordinates[-1]
			neighboursUp = [neighbours.append([self.hiddenBoard[point[0]][point[1] + 1], self.hiddenBoard[point[0]][point[1] - 1]])
							for point in coordinates]
			neighboursLeft = neighbours.append([self.hiddenBoard[start[0] - 1][start[1]], self.hiddenBoard[start[0] - 1][start[1] - 1],
				 			self.hiddenBoard[start[0] - 1][start[1] + 1]])
			neighboursRight = neighbours.append([self.hiddenBoard[end[0] + 1][end[1]], self.hiddenBoard[end[0] + 1][end[1] - 1],
				 			self.hiddenBoard[end[0] + 1][end[1] + 1]])

		result = [item[i] for item in neighbours for i in range(len(item))]

		return any(x in result for x in ["Y", "X"])