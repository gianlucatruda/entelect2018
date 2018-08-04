from locations import Mine, Factory
from agents import Drone
class input:

    def __init__(self, file_name):

        with open(file_name) as infile:
            lines = infile.readlines()

            params = (int(x) for x in lines[0].split(' '))

            self.map_size = next(params), next(params)
            self.miners = [Drone("miner") for x in range(next(params))] 
            self.excavators = [Drone("excavator") for x in range(next(params))] 
            self.haulers = [Drone("hauler") for x in range(next(params))] 
            self.n_mines = next(params)            
            self.mines = []            
            self.n_factories = next(params)
            self.factories = []
            self.budget = next(params)
            
            self.dict_mines_factories = {}

            for line in lines[1:]:
                line = line.strip().split(' ')
                _type = line[1]
                del line[1]
                if _type.isupper():
                    mine = Mine(_type, *(int(x) for x in line ))
                    self.mines.append(mine)

                    if not self.dict_mines_factories.get(_type):
                        self.dict_mines_factories[_type] = {"mines": [], "factories": []}
                    self.dict_mines_factories[_type]["mines"].append(mine)


                else:
                    factory = Factory(_type, *(int(x) for x in line ))
                    self.factories.append( factory)
                        
                    self.dict_mines_factories[_type.upper()]["factories"].append(factory)

    def print_dict(self):
        for i,v in self.dict_mines_factories.items():
            print ("RESOURCE " + i)
            for typ, lst in v.items():
                print ( typ, end =": [")
                for res in lst:
                    print (res, end="; ")
                print("]")