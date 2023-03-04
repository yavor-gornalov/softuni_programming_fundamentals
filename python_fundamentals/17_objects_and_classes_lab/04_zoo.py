# https://judge.softuni.org/Contests/Practice/Index/1733#3

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
num = int(input())

my_zoo = Zoo(zoo_name)
for _ in range(num):
    animal_species, animal_name = input().split()
    my_zoo.add_animal(animal_species, animal_name)

species_info = input()
print(my_zoo.get_info(species_info))
