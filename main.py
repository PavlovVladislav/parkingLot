from ClassParkingLot import ParkingLot

if __name__ == '__main__':
    parkingLot = ParkingLot('Moscow', 3, 5, 15)
    parkingLot.show_schema()
    parkingLot.show_free_place()
    parkingLot.show_info()
    parkingLot.add_transport("Auto")
    parkingLot.show_schema()
    parkingLot.add_transport("Moto")
    parkingLot.show_schema()