"""OOP kontrolltöö."""


class House:
    """House class, parent to other rooms."""
    STATE_NEW = "New house"
    STATE_RENOVATED = "Renovated"
    STATE_USED = "Used house"
    STATE_GHOST = "Ghost house"

    def __init__(self, address: str, rooms: int, floors: int):
        """Initialize house class."""
        self.__rooms = rooms
        self.__floors = floors
        self.__address = address
        self.__state = House.STATE_NEW
        self.__price: int = 100000

    def get_rooms(self):
        """Return number of rooms."""
        return self.__rooms

    def get_floors(self):
        """Return number of floors."""
        return self.__floors

    def get_address(self):
        """Return house address."""
        return self.__address

    def get_price(self):
        """Return price.."""
        return self.__price

    def get_state(self):
        """Return state."""
        return self.__state

    def change_house_price(self, price, state):
        """Price the house: set price and state of house."""
        self.__price = price
        state_list = [House.STATE_NEW, House.STATE_RENOVATED, House.STATE_USED, House.STATE_GHOST]
        if state in state_list:
            self.__state = state

    def renovate(self, rooms):
        """Set new number of rooms and state of house."""
        self.__rooms = rooms
        self.__state = House.STATE_RENOVATED


class Small_house(House):
    """Small house class."""

    def __init__(self, address, rooms=4, floors=1):
        super().__init__(address, rooms, floors)


if __name__ == '__main__':
    house1 = House("Koht", 10, 2)
    house2 = Small_house("Koht2")

    print("House 1")
    print(house1.get_rooms())
    print(house1.get_floors())
    print(house1.get_address())
    print(house1.get_price())
    print(house1.get_state())

    house1.change_house_price(50000, "Used house")
    print(house1.get_price())
    print(house1.get_state())

    house1.renovate(5)
    print(house1.get_rooms())
    print(house2.get_state())

    print()
    print("House 2")
    print(house2.get_rooms())
    print(house2.get_floors())
    print(house2.get_address())
    print(house2.get_price())
    print(house2.get_state())

    house2.change_house_price(50000, "Used house")
    print(house2.get_price())
    print(house2.get_state())

    house1.renovate(2)
    print(house1.get_rooms())
    print(house2.get_state())

    houses = []
    rooms = 5
    for i in range(60):
        houses.append(House(f"Uus tn {i + 1}", 6, 2))
    for i in range(40):
        houses.append(Small_house(f"Väike tn {i + 1}"))

    for i in houses:
        print(f"{i.get_address()} Floors: {i.get_floors()}, Rooms: {i.get_rooms()}")
