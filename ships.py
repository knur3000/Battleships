import random

class Ship:
	def __init__(self, owner):
		self.coordinates = None
		self.orientation = None
		self.tries = 0

	def generateShip(self, size):
		isHorizontal = random.choice([True, False])
		self.orientation = isHorizontal

		if self.orientation:
			startPoint = [random.randint(1, 10), random.randint(1, 10-size)]
			self.coordinates = [ [startPoint[0], startPoint[1]+i] for i in range(size) ]
		else:
			startPoint = [random.randint(1, 10-size), random.randint(1, 10)]

			self.coordinates = [ [startPoint[0]+i, startPoint[1]] for i in range(size) ]
