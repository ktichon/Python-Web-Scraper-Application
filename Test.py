class Inventory():
    HATS = 100

    def __init__(self, scarves, mittens):
        self.scarves = scarves
        self.mittens = mittens


warehouse1 = Inventory(200, 300)
warehouse2 = Inventory(888, 999)

warehouse1.mittens = warehouse1.mittens * 2
warehouse2.scarves = warehouse2.scarves * 2
Inventory.HATS = 111
Inventory.scarves = 0

print("New:", warehouse1.HATS, warehouse2.HATS)