class ParkingLot:
    typePlace = ["Moto place", "Smart place", "Large place"]

    transport = {
        "Moto": 0,
        "Auto": 0,
        "Bus": 0
    }

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

    def show_free_place(self):
        for i in range(len(self.schema)):
            print(str(self.typePlace[i]) + " has " + str(self.schema[i].count(0)) + " free.")
        print()

    def show_schema(self):
        for i in range(len(self.schema)):
            print(self.typePlace[i], end=':')
            for j in range(len(self.schema[i])):
                print(self.schema[i][j], end=' ')
            print()
        print()

    def show_info(self):
        print("Moto on parking lot: " + str(self.transport["Moto"]))
        print("Auto on parking lot: " + str(self.transport["Auto"]))
        print("Bus on parking lot: " + str(self.transport["Bus"]))
