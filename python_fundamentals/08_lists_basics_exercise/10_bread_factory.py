# https://judge.softuni.org/Contests/Compete/Index/1725#9

# initial values
energy_limit, coins_limit = 100, 100

working_day_events = input().split("|")

current_energy, current_coins = energy_limit, coins_limit
is_handle_failed = False

for event in working_day_events:
    command, number = event.split("-")
    number = int(number)

    if command == "rest":
        if current_energy + number <= energy_limit:
            gained_energy = number
            current_energy += gained_energy
        else:
            gained_energy = energy_limit - current_energy
            current_energy = energy_limit
        print(f"You gained {gained_energy} energy.\n"
              f"Current energy: {current_energy}.")

    elif command == "order":
        earned_coins = number
        if current_energy < 30:
            current_energy += 50
            print("You had to rest!")
            continue
        current_energy -= 30
        current_coins += earned_coins
        print(f"You earned {earned_coins} coins.")
    else:
        ingredient, price = command, number
        if price > current_coins:
            print(f"Closed! Cannot afford {ingredient}.")
            break
        current_coins -= price
        print(f"You bought {ingredient}.")
else:
    print(f"Day completed!\n"
          f"Coins: {current_coins}\n"
          f"Energy: {current_energy}")
