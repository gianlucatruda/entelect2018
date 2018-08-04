from locations import Mine, Factory

class input:

    def __init__(self, file_name):

        with open(file_name) as infile:
            lines = infile.readlines()

            params = (int(x) for x in lines[0].split(' '))

            self.map_size = next(params), next(params)
            self.miners = next(params)
            self.excavators = next(params)
            self.haulers = next(params)
            self.n_mines = next(params)            
            self.mines = []            
            self.n_factories = next(params)
            self.factories = []
            self.budget = next(params)
            
            self.dict_mines_facts = {}

            for line in lines[1:]:
                line = line.strip().split(' ')
                _type = line[1]
                del line[1]
                if _type.isupper():
                    mine = Mine(_type, *(int(x) for x in line ))
                    self.mines.append(mine)

                    if not self.dict_mines_facts.get(_type):
                        self.dict_mines_facts[_type] = {"mines": [], "factories": []}
                    self.dict_mines_facts[_type]["mines"].append(mine)


                else:
                    factory = Factory(_type, *(int(x) for x in line ))
                    self.factories.append( factory)
                        
                    self.dict_mines_facts[_type.upper()]["factories"].append(factory)

    def print_dict(self):
        for i,v in self.dict_mines_facts.items():
            print ("RESOURCE " + i)
            for typ, lst in v.items():
                print ( typ, end =": [")
                for res in lst:
                    print (res, end="; ")
                print("]")