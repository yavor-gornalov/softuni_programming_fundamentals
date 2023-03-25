# https://judge.softuni.org/Contests/Practice/Index/2307#2

cars = {}
max_fuel = 75
min_milage = 10000
max_milage = 100000

n = int(input())
for _ in range(n):
    car, milage, fuel = input().split("|")
    cars[car] = {
        "milage": int(milage),
        "fuel": int(fuel)
    }

while True:
    command = input()
    if command == "Stop":
        break
    command_args = command.split(" : ")
    action = command_args[0]
    car = command_args[1]
    if action == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["milage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["milage"] >= max_milage:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        fuel = int(command_args[2])
        if cars[car]["fuel"] + fuel > max_fuel:
            fuel = max_fuel - cars[car]["fuel"]
        cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometers = int(command_args[2])
        if cars[car]["milage"] - kilometers >= min_milage:
            cars[car]["milage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]["milage"] = min_milage

for car, car_data in cars.items():
    print(f"{car} -> Mileage: {car_data['milage']} kms, Fuel in the tank: {car_data['fuel']} lt.")
