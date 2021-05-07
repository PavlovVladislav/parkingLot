class parkingLot:
    typePlace = ["Moto place", "Smart place", "Large place"]

    def __init__(self, name, motorcycle_place, smart_place, large_place):
        self.name = name
        self.motorcycle_place = motorcycle_place
        self.smart_place = smart_place
        self.large_place = large_place
        self.schema = [
            [0] * self.motorcycle_place,
            [0] * self.smart_place,
            [0] * self.large_place
        ]

    def show_free_place(self, place):
        print(str(self.typePlace[place]) + " has " + str(self.schema[place].count(0)) + " free place")
        return

    def show_schema(self):
        for i in range(len(self.schema)):
            print(self.typePlace[i], end=':')
            for j in range(len(self.schema[i])):
                print(self.schema[i][j], end=' ')
            print()
        print()
