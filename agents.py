import tools
from locations import Mine, Factory

class Drone:
	def __init__(self, kind):
		self.x = 0
		self.y = 0
		self.location_obj = None
		self.kind = kind.lower()
		self.capacity = 0
		self.carrying_element = "none"
		self.carrying_quantity = 0
		self.distance_travelled = 0
		self.index_history = []

		if self.kind == "miner":
			self.capacity = 1
		elif self.kind == "excavator":
			self.capacity = 3
		elif self.kind == "hauler":
			self.capacity = 5
		else:
			print("Unrecognised drone kind:", self.kind)

	# Move the drone to a mine or factory
	def move_to(self, location, verbose=True):
		X = location.x
		Y = location.y
		self.location_obj = location
		dist = tools.distance(self.x, self.y, X, Y)
		self.distance_travelled += dist
		self.index_history.append(location.index)
		self.x = X
		self.y = Y

		if verbose:
			print("NOTE:Moved {} drone {} blocks to ({},{})".format(self.kind, dist, self.x, self.y))

		self.take_action(location, verbose)
		if verbose:
			print(str(self))


	def take_action(self, location, verbose=True):
		if type(location) == Mine:
			self.collect(location, verbose)
		elif type(location) == Factory:
			self.deposit(location, verbose)
		else:
			# couldn't identify location
			print("ERROR:{} drone at index {} couldn't identify the location type!".format(self.kind, location.index))

	def collect(self, location, verbose=True):
		loc_elem = location.element.lower()
		if self.carrying_quantity == 0:
			self.pick_up(location, verbose)
		else:
			# if you're already carrying the same element, can't pick up
			if self.carrying_element.lower() == loc_elem:
				print("ERROR: Drone already carrying that")
			else:
				if self.capacity - self.carrying_quantity > 0:
					self.pick_up(location, verbose)

	def pick_up(self, location, verbose=True):
		if location.quantity > 0:
			# pick up one
			location.mine()
			self.carrying_quantity += 1
		else:
			print("Mine already empty")
		self.carrying_element = location.element.lower()
		if verbose:
			print("NOTE:Drone picked up from mine --> ", str(location))

	def deposit(self, location, verbose=True):
		loc_elem = location.element.lower()
		if self.carrying_quantity == 0:
			print("ERROR:{} drone at '{}' has nothing to deposit!".format(self.kind,str(location)))
		else:
			if self.carrying_element.lower() == loc_elem:
				# Drop the stuff off
				self.carrying_element = "none"
				self.carrying_quantity = 0
				if verbose:
					print("NOTE:{} deposited materials at factory".format(str(self)))
			else:
				print("ERROR:Drone at factory [index = {}] carrying the wrong element: {} instead of {}".format(str(location.index),self.carrying_element.lower(), loc_elem))

	def is_available(self):
		if self.carrying_element in ["none", "null", "None", "", " ", None] and self.carrying_quantity == 0:
			return True
		return False

	def __str__(self):
		out = "NOTE:Drone of kind {} at ({},{}) carrying {} pieces of {} ".format(
			self.kind, self.x, self.y, self.carrying_quantity, self.carrying_element
		)
		return out
