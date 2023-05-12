# https://judge.softuni.org/Contests/Compete/Index/1719#8

houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

student = input()
while student != "Welcome!":
    if student == "Voldemort":
        print("You must not speak of that name!")
        break

    name_length = len(student)
    if name_length < 5:
        house_idx = 0
    elif name_length == 5:
        house_idx = 1
    elif name_length == 6:
        house_idx = 2
    else:
        house_idx = 3

    print(f"{student} goes to {houses[house_idx]}.")
    student = input()

else:
    print("Welcome to Hogwarts.")
