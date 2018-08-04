
#distance between A(x1, y1) and B(x2, y2)
def distance(x1, y1, x2, y2):
	return (abs(x2-x1)+abs(y2-y1))

def dist_obj(fst, snd):
	return distance(fst.x, fst.y, snd.x, snd.y)

#return the closest mine to the agent
def closestMine(agent, mineList, dict_):
	returnLocation = None
	minimum = 1000000
	for mine in mineList:
		if mine.element in agent.carrying_elements or mine.quantity == 0 or mine == agent.location_obj:
			continue
		dist = distance(agent.x, agent.y, mine.x, mine.y) + dict_[mine][0][1]
		if ( dist < minimum):
			returnLocation = mine
			minimum = dist
	return (minimum, returnLocation)

def closestFactory(agent, factList):
	returnLocation = None
	minimum = 1000000
	for fact in factList:
		dist = distance(agent.x, agent.y, fact.x, fact.y)
		if ( dist < minimum):
			returnLocation = fact
			minimum = dist
	return (minimum, returnLocation)

# Get total distance travelled by all drones up till now
def current_total_distance(drones):
	total = 0
	for d in drones:
		total += d.distance_travelled
	return total

# Get the total available capacity of all available drones
def free_capacity(drones):
	cap = 0
	for d in drones:
		if d.is_available():
			cap += d.capacity

def create_closest_dicts(mines, factories, dict_mines_factories):
	closest_factories = {}
	# closest_mines = {}
	for mine in mines:

		closest_factories[mine] = [ 
			( factory, dist_obj(mine, factory) ) 
				for factory in dict_mines_factories[mine.element]["factories"]
		]
		closest_factories[mine].sort(key = lambda x: x[1])
	return closest_factories

def get_all_mines_of_type(dict_mines_factories, type):
	return dict_mines_factories[type]["mines"]

def get_all_factories_of_type(dict_mines_factories, type):
	return dict_mines_factories[type]["factories"]

def check_if_mines_and_drones_empty(mines, drones):
	bools = {mine.quantity == 0 for mine in mines} | {drone.carrying_quantity == 0 for drone in drones}
	return False in bools
