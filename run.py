from game import placeShips, getInput
from board import Board
import os

board = Board()
placeShips(board)

print("Super rozrywka! Gra w statki!")
input("Wylosowano plansze, no to gramy! Nacisnij cośtam...")

points = 0

while points < 21:
	os.system('CLS')
	print("")
	print(board)
	print("")
	print("Podaj koordynaty dla X:")
	x = getInput()
	print("Podaj koordynaty Y:")
	y = getInput()

	if board.userBoard[x][y] in ["\033[1;34m~\033[1;m", "\033[1;31m#\033[1;m"]:
		print("")
		print("No to już było... Obecna plansza:\n")

	else:
		if board.hiddenBoard[x][y] in ["X", "Y"]:
			board.userBoard[x][y] = "\033[1;31m#\033[1;m"
		else:
			board.userBoard[x][y] = "\033[1;34m~\033[1;m"
		print("")
		print("Tak jest:\n")

	print(board)

	foundPoints = sum([x.count("\033[1;31m#\033[1;m") for x in board.userBoard])
	points = foundPoints
	print("")
	input("Pozostało do zatopienia: {x} / Naciśnij coś tam...".format(x=22-foundPoints))

else:
	print("Wspaniale, gra ukończona!")


