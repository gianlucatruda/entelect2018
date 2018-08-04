class Mine:
	def __init__(self, element, index, x, y, quantity):
		self.x = x
		self.y = y
		self.index = index
		self.element = element
		self.quantity = quantity
		self.nearest_factories = []

	def __str__(self):
		out = "{} mine [{}] at {},{} with quant: {}".format(
			self.element, self.index, self.x, self.y, self.quantity
		)
		return out


class Factory:
	def __init__(self, element, index, x, y):
		self.x = x
		self.y = y
		self.index = index
		self.element = element
		self.nearest_mines = []

	def __str__(self):
		out = "{} factory [{}] at {},{}".format(
			self.element, self.index, self.x, self.y
		)
		return out
