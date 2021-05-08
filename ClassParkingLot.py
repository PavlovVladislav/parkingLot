class ParkingLot:
    typePlace = ["Moto place", "Smart place", "Large place"]

    def __init__(self, name, motorcycle_place, smart_place, large_place):
        self.name = name
        self.arr_place = [motorcycle_place, smart_place, large_place]
        self.typePlace = {
            "Moto place": self.arr_place[0],
            "Smart place": self.arr_place[1],
            "Large place": self.arr_place[2]
        }
        self.transport = {
            "Moto": 0,
            "Auto": 0,
            "Bus": 0
        }

    def show_free_place(self):
        for key in self.typePlace:
            print(str(key) + " has " + str(self.typePlace[key]) + " free.")
        print()

    def draw_schema(self):
        i = 0
        for key in self.typePlace:
            print(str(key) + " : " + "1 " * (self.arr_place[i] - self.typePlace[key]) + "0 " * self.typePlace[key])
            i += 1
        print()

    def show_info(self):
        print("Moto on parking lot: " + str(self.transport["Moto"]))
        print("Auto on parking lot: " + str(self.transport["Auto"]))
        print("Bus on parking lot: " + str(self.transport["Bus"]), end='\n\n')

    def add_transport(self, type_transport):
        if type_transport == "Moto":
            for key in self.typePlace:
                if self.typePlace[key] != 0:
                    self.typePlace[key] = self.typePlace[key] - 1
                    self.transport["Moto"] += 1
                    print("Added 1 Moto", end='\n\n')
                    break
                else:
                    print("Don/'t have place for Moto", end='\n\n')

        elif type_transport == "Auto":
            if self.typePlace["Smart place"] != 0:
                self.typePlace["Smart place"] = self.typePlace["Smart place"] - 1
                self.transport["Auto"] += 1
            elif self.typePlace["Large place"] != 0:
                self.typePlace["Large place"] = self.typePlace["Large place"] - 1
                self.transport["Auto"] += 1
            else:
                print("Don/'t have place for Auto", end='\n\n')

        elif type_transport == "Bus":
            if self.typePlace["Large place"] // 5 != 0:
                self.typePlace["Large place"] = self.typePlace["Large place"] - 5
                self.transport["Bus"] += 1
            else:
                print("Don\'t have place for Bus", end='\n\n')

