class Mine:
	def __init__(self, index, element, x, y, quantity):
		self.x = x
		self.y = y
		self.index = index
		self.element = element
		self.quantity = quantity

	def __str__(self):
		out = "{} mine [{}] at {},{} with quant: {}".format(
			self.element, self.index, self.x, self.y, self.quantity
		)
		return out


class Factory:
	def __init__(self, index, element, x, y):
		self.x = x
		self.y = y
		self.index = index
		self.element = element

	def __str__(self):
		out = "{} factory [{}] at {},{} with quant: {}".format(
			self.element, self.index, self.x, self.y
		)
		return out
