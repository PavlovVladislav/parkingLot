from ClassParkingLot import ParkingLot

if __name__ == '__main__':
    parkingLot = ParkingLot('Moscow', 3, 5, 15)
    parkingLot.draw_schema()
    parkingLot.show_free_place()
    parkingLot.show_info()
    parkingLot.add_transport("Moto")
    parkingLot.draw_schema()
    for i in range(4):
        parkingLot.add_transport("Bus")
    parkingLot.draw_schema()