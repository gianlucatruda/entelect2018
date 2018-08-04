from input import input
from tools import create_closest_dicts, closestMine, get_all_mines_of_type, check_if_mines_and_drones_empty, current_total_distance
from output import output

def main():
    _input = input('../input/map_1.input')
    
    closest_factories = create_closest_dicts(_input.mines, _input.factories, _input.dict_mines_factories)
    all_drones =  _input.haulers + _input.excavators + _input.miners 
    not_done = True
    while not_done:
        print ("STARTING")

        for drone in all_drones:
            # closest mine for now
            if drone.carrying_quantity == drone.capacity:
                # move to closest factory and update quanity
                closest_fact = closest_factories[drone.location_obj][0][0]
                # print ("Moving hauler for element ", drone.element)
                drone.move_to(closest_fact, True)

            else:
                # move to, update dist and index travelled    
                print ("Drone is ", drone.x, drone.y, " at ", drone.location_obj)
                if drone.carrying_quantity > 0:
                    print ("Carrying quanity not 0, going to another mine")
                    
                    close_mine = closestMine(drone, get_all_mines_of_type(_input.dict_mines_factories, drone.location_obj.element))
                    if close_mine == None:
                        closest_fact = closest_factories[drone.location_obj][0][0]
                        drone.move_to(closest_fact, True)
                        continue
                else:
                    close_mine = closestMine(drone, _input.mines)

                if close_mine == None:
                    print ("closest mine is null")
                    continue
                drone.move_to(close_mine, True)
        not_done = check_if_mines_and_drones_empty(_input.mines, all_drones)

    for mine in _input.mines:
        if mine.quantity != 0:
            print ("mine ", mine, " still has stuff ")

    for drone in all_drones:
        if drone.carrying_quantity != 0:
            print ("drone", drone, "still has stuff")
    print ("dist", current_total_distance(all_drones))
    output('out.out', all_drones)



if __name__ == "__main__":
    main()