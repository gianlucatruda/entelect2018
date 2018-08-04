from input import input
from tools import create_closest_dicts

def main():
    i = input('map_1.input')
    
    print (create_closest_dicts(i.mines, i.factories, i.dict_mines_factories))
    


if __name__ == "__main__":
    main()