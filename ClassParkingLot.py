class ParkingLot:
    typePlace = ["Moto place", "Smart place", "Large place"]

    def __init__(self, name, motorcycle_place, smart_place, large_place):
        self.name = name
        self.arr_place = [motorcycle_place, smart_place, large_place]
        self.transport = {
            "Moto": 0,
            "Auto": 0,
            "Bus": 0
        }
        self.schema = [
            [0] * self.arr_place[0],
            [0] * self.arr_place[1],
            [0] * self.arr_place[2]
        ]

    def show_free_place(self):
        for i in range(len(self.schema)):
            try:
                print(self.typePlace[i] + " has " + str(self.schema[i].count(0)) + " free.")
            except:
                print(self.typePlace[i] + " has 0 free.")
        print()

    def show_schema(self):
        for i in range(len(self.schema)):
            print(self.typePlace[i], end=':')
            for j in range(len(self.schema[i])):
                print(self.schema[i][j], end=' ')
            print()
        print()

    def show_occupied_place(self):
        print("Moto on parking lot: " + str(self.transport["Moto"]))
        print("Auto on parking lot: " + str(self.transport["Auto"]))
        print("Bus on parking lot: " + str(self.transport["Bus"]), end='\n\n')

    def add_transport(self, type_transport):
        if type_transport == "Moto":
            add = 0
            for i in range(len(self.schema)):
                if self.schema[i].count(0) != 0:
                    self.schema[i][self.schema[i].index(0)] = "M"
                    self.transport["Moto"] += 1
                    print("Added 1 Moto", end='\n\n')
                    add += 1
                    break
            if add == 0:
                print("Don\'t have place for Moto", end='\n\n')

        elif type_transport == "Auto":
            add = 0
            for i in range(1, len(self.schema)):
                if self.schema[i].count(0) != 0:
                    self.schema[i][self.schema[i].index(0)] = "A"
                    self.transport["Auto"] += 1
                    print("Added 1 Auto", end='\n\n')
                    add += 1
                    break
            if add == 0:
                print("Don\'t have place for Auto", end='\n\n')

        elif type_transport == "Bus":
            if self.schema[2].count(0) // 5 != 0:
                start = self.schema[2].index(0)
                for i in range(5):
                    self.schema[2][start + i] = "B"
                self.transport["Bus"] += 1
                print("Added 1 Bus", end='\n\n')
            elif self.schema[2].count(0) == 0:
                print("Don\'t have place for Bus", end='\n\n')

    def del_transport(self, type_transport):
        if type_transport == "Moto":
            add = 0
            revers_schema = self.schema[::-1]
            for i in range(len(revers_schema)):
                if revers_schema[i].count('M') != 0:
                    revers_schema[i].reverse()
                    revers_schema[i][revers_schema[i].index('M')] = 0
                    revers_schema[i].reverse()
                    self.transport["Moto"] -= 1
                    add += 1
                    self.schema = revers_schema[::-1]
                    print("Removed 1 Moto", end='\n\n')
                    break
            if add == 0:
                print("All place for Moto are free", end='\n\n')

        elif type_transport == "Auto":
            add = 0
            revers_schema = self.schema[::-1]
            for i in range(len(revers_schema)-1):
                if revers_schema[i].count('A') != 0:
                    revers_schema[i].reverse()
                    revers_schema[i][revers_schema[i].index('A')] = 0
                    revers_schema[i].reverse()
                    self.transport["Auto"] -= 1
                    self.schema = revers_schema[::-1]
                    print("Removed 1 Auto", end='\n\n')
                    add += 1
                    break
            if add == 0:
                print("Don\'t have place for Auto", end='\n\n')

        elif type_transport == "Bus":
            if self.schema[2].count(0) // 5 != 0:
                self.schema[2].reverse()
                start = self.schema[2].index('B')
                for i in range(5):
                    self.schema[2][start + i] = 0
                self.schema[2].reverse()
                self.transport["Bus"] -= 1
                print("Removed 1 Bus", end='\n\n')
            else:
                print("All place for Bus are free", end='\n\n')
