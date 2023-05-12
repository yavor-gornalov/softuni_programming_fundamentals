# https://judge.softuni.org/Contests/Compete/Index/1719#7

number_of_coffees = 0
is_extra_sleep_needed = False
while True:
    line = input()
    if line == "END":
        break

    if number_of_coffees >= 5:
        is_extra_sleep_needed = True
        break

    current_coffees = 0
    if line.lower() in ["coding", "cat", "dog", "movie"]:
        current_coffees = 1 if line.islower() else 2
    number_of_coffees += current_coffees


print("You need extra sleep") if is_extra_sleep_needed else print(number_of_coffees)
