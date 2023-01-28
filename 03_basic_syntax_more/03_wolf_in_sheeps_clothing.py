# https://judge.softuni.org/Contests/Practice/Index/1720#2

animals = input().split(', ')

wolf_index = animals.index("wolf")

if "wolf" == animals[-1]:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(animals) - 1 - wolf_index}! You are about to be eaten by a wolf!")
