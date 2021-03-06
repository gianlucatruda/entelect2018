from input import input
from tools import *
from output import output


def main():
    _input = input("map_2.input")

    closest_factories = create_closest_dicts(
        _input.mines, _input.factories, _input.dict_mines_factories
    )
    all_drones = _input.haulers + _input.excavators + _input.miners

    closest_factories = create_closest_dicts(
        _input.mines, _input.factories, _input.dict_mines_factories
    )
    all_drones = _input.miners + _input.excavators + _input.haulers
    not_done = True
    while not_done:
        # print ("STARTING")
        print("Remaining resources: ", sum(m.quantity for m in _input.mines), end="\r")

        for drone in all_drones:
            # closest mine for now
            if len(drone.carrying_elements) == drone.capacity:
                # move to closest factory and update quanity
                closest_facts = []
                for elem in drone.carrying_elements:
                    closest_facts.append(
                        closestFactory(
                            drone,
                            get_all_factories_of_type(
                                _input.dict_mines_factories, elem.upper()
                            ),
                        )
                    )

                closest_facts.sort(key=lambda x: x[0])

                # print ("Moving hauler for element ", drone.element)
                drone.move_to(closest_facts[0][1], False)

            else:
                # move to, update dist and index travelled
                # print ("Drone is ", drone.x, drone.y, " at ", drone.location_obj)
                close_mine = closestMine(drone, _input.mines, closest_factories)
                closest_facts = []
                if len(drone.carrying_elements) == 0:
                    if close_mine[1] == None:
                        # print ("closest mine is null")
                        continue
                    drone.move_to(close_mine[1])
                    continue

                for elem in drone.carrying_elements:
                    closest_facts.append(
                        closestFactory(
                            drone,
                            get_all_factories_of_type(
                                _input.dict_mines_factories, elem.upper()
                            ),
                        )
                    )

                closest_facts.sort(key=lambda x: x[0])
                if close_mine[1] == None:
                    # print ("closest mine is null")
                    drone.move_to(closest_facts[0][1], False)
                    continue
                to_move = (
                    closest_facts[0][1]
                    if closest_facts[0][0] < close_mine[0]
                    else close_mine[1]
                )
                if (
                    closest_facts[0][0]
                    < close_mine[0] - closest_factories[close_mine[1]][0][1]
                ):
                    to_move = closest_facts[0][1]
                else:
                    to_move = close_mine[1]
                drone.move_to(to_move, True)

        not_done = check_if_mines_and_drones_empty(_input.mines, all_drones)

    output("out5.txt", all_drones)
    import stats

    stats.show_stats(all_drones, _input.mines, _input.factories, _input.budget)


if __name__ == "__main__":
    main()
