import tools

class Drone:
	def __init__(self, kind):
		self.x = 0
		self.y = 0
		self.kind = kind.lower()
		self.capacity = 0
		self.carrying_element = "none"
		self.carrying_quantity = 0
		self.distance_travelled = 0

		if self.kind == "miner":
			self.capacity = 1
		elif self.kind == "excavator":
			self.capacity = 3
		elif self.kind == "hauler":
			self.capacity = 5
		else:
			print("Unrecognised drone kind:", self.kind)

	def move_to(self, location, verbose=True):
		X = location.x
		Y = location.y
		dist = tools.distance(self.x, self.y, X, Y)
		self.distance_travelled += dist
		self.x = X
		self.y = Y
		if verbose:
			print("Moved {} drone {} blocks to ({},{})".format(self.kind, dist, self.x, self.y))


	def __str__(self):
		out = "Drone of kind {} at ({},{}) carrying {} pieces of {} ".format(
			self.kind, self.x, self.y, self.carrying_element, self.carrying_quantity
		)
		return out
