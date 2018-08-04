from locations import Mine, Factory
from agents import Drone
import tools

def show_stats(drones, mines, factories, budget):

	print("\nSTATS--------------------")
	unmined = sum(m.quantity for m in mines)
	print("{} mines with {} unmined resources".format(len(mines),unmined))
	delivered = sum(f.quantity for f in factories)
	print("{} factories with {} total resources".format(len(factories),delivered))
	carrying = sum(d.carrying_quantity for d in drones)
	print("{} drones carrying {} materials".format(len(drones), carrying))
	dist = tools.current_total_distance(drones)
	print("Total drone distance: {}".format(dist))
	print("Amount under budget: R{}".format(budget - dist))


