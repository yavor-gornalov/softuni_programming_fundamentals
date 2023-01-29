# https://judge.softuni.org/Contests/Compete/Index/1719#8

gryffindor_count = 0
slytherin_count = 0
ravenclaw_count = 0
hufflepuff_count = 0

name = input()
while not name == "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()

else:
    print("Welcome to Hogwarts.")
