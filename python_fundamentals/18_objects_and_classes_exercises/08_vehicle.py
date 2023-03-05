# https://judge.softuni.org/Contests/Compete/Index/1734#7

class Vehicle:
    def __init__(self, vehicle_type: str, model: str, price: float):
        self.type = vehicle_type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money < self.price:
            return "Sorry, not enough money"
        if self.owner:
            return "Car already sold"
        self.owner = owner
        change = money - self.price
        return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if not self.owner:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"
#
#
# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
