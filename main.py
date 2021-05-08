from ClassParkingLot import ParkingLot

if __name__ == '__main__':
    while True:
        parking_lot = None
        try:
            test = int(input("If you want to start test parking press 0 if no 1: "))
            if test != 0:
                name = input("Enter name parking lot: ")
                Moto = int(input("Enter count place for Motorcycle: "))
                Auto = int(input("Enter count place for Auto: "))
                Bus = int(input("Enter count place for Bus: "))
                print()
                parking_lot = ParkingLot(name, Moto, Auto, Bus)
            elif test == 0:
                parking_lot = ParkingLot("Moscow", 1, 1, 1)
            break
        except ValueError:
            print("You entered incorrect data, try again\n")

    # parking_lot = ParkingLot(name, Moto, Auto, Bus)

    while True:
        action = 0
        while True:
            try:
                action = int(input("Enter the number of the item you want to execute: \n"
                                   "1. Display free parking spaces\n"
                                   "2. Display the parking scheme\n"
                                   "3. Display what vehicles are in the parking lot\n"
                                   "4. Add vehicles to the parking lot\n"
                                   "5. Remove vehicles from the parking lot\n"
                                   "If want stop program enter \"0\"\n")
                             )
                if action < 0 or action > 5:
                    raise Exception("You have selected an item not from the presented, try again\n")
                break
            except ValueError:
                print("!!! Your choice is wrong, please try again \n")
            except Exception as e:
                print(e)

        if action != 0:

            choice_transport = None
            if action == 4 or action == 5:
                transport = ["Moto", "Auto", "Bus"]
                while True:
                    try:
                        choice_transport = int(input("Select the vehicle you want to add / remove\n"
                                                     "1 - Motorcycle, 2 - Auto, 3 - Bus\n")) - 1
                        if choice_transport < 0 or choice_transport > 2:
                            raise Exception("You have selected an item not from the presented, try again\n")
                        choice_transport = transport[choice_transport]
                        break
                    except ValueError:
                        print("Wrong choice, try again")
                    except Exception as e:
                        print(e)

            if action == 1:
                parking_lot.show_free_place(),
            elif action == 2:
                parking_lot.show_schema(),
            elif action == 3:
                parking_lot.show_occupied_place(),
            elif action == 4:
                parking_lot.add_transport(choice_transport),
            elif action == 5:
                parking_lot.del_transport(choice_transport)

            input("Press Enter to continue...\n")

        else:
            break
