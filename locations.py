class Mine:
    def __init__(self, element, index, x, y, quantity):
        self.x = x
        self.y = y
        self.index = index
        self.element = element
        self.quantity = quantity
        self.nearest_factories = []

    def mine(self):
        if self.quantity < 1:
            print("You'r taking away too much at this mine -> ", str(self))
            self.quantity = 0
        else:
            self.quantity -= 1
            # if self.quantity == 0:
            # 	print("NOTE:Mine empty -> ", str(self))

    def __str__(self):
        out = "{} mine [index = {}] at ({},{}) with quant: {}".format(
            self.element, self.index, self.x, self.y, self.quantity
        )
        return out


class Factory:
    def __init__(self, element, index, x, y):
        self.x = x
        self.y = y
        self.index = index
        self.element = element
        self.nearest_mines = []
        self.quantity = 0

    def deposit(self):
        self.quantity += 1

    def __str__(self):
        out = "{} factory [index = {}] at {},{}".format(
            self.element, self.index, self.x, self.y
        )
        return out
