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

            for line in lines[1:]:
                line = line.strip().split(' ')
                _type = line[1]
                del line[1]
                if _type.isupper():
                    self.mines.append( Mine(_type, *(int(x) for x in line )))
                else:
                    self.factories.append( Factory(_type, *(int(x) for x in line )))

