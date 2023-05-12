# https://judge.softuni.org/Contests/Compete/Index/1719#11

class Decoration:
    def __init__(self, price, spirit, ):
        self.price = price
        self.spirit = spirit


ornament_set = Decoration(2, 5)
tree_skirt = Decoration(5, 3)
tree_garland = Decoration(3, 10)
tree_lights = Decoration(15, 17)

quantity_of_decorations = int(input())
days_to_christmas = int(input())

total_cost = 0
total_spirit = 0
for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set.price
        total_spirit += ornament_set.spirit
    if day % 3 == 0:
        total_cost += quantity_of_decorations * (tree_skirt.price + tree_garland.price)
        total_spirit += tree_skirt.spirit + tree_garland.spirit
    if day % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights.price
        total_spirit += tree_lights.spirit
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_cost += tree_skirt.price + tree_garland.price + tree_lights.price
        total_spirit -= 20
        if day == days_to_christmas:
            total_spirit -= 30

print(f"Total cost: {total_cost}\nTotal spirit: {total_spirit}")
