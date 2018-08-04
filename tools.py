
#distance between A(x1, y1) and B(x2, y2)
def distance(x1, y1, x2, y2):
	return (abs(x2-x1)+abs(y2-y1))

#return the closest mine to the agent
def closestMine(agent, mineList):
	returnLocation = None
	minimum = 1000000;
	for mine in mineList:
		if (distance(agent.x, agent.y, mine.x, mine.y) < minimum):
			returnLocation = mine
			minimum = distance(agent.x, agent.y, mine.x, mine.y)
	return returnLocation

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
