# https://judge.softuni.org/Contests/Practice/Index/1732#0

population_wealth = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

average_wealth = sum(population_wealth) / len(population_wealth)

if minimum_wealth <= average_wealth:
    for index, el in enumerate(population_wealth):
        while population_wealth[index] < minimum_wealth:  # index is poor
            richest_index = population_wealth.index(max(population_wealth))
            difference = minimum_wealth - population_wealth[index]
            population_wealth[index] = minimum_wealth
            population_wealth[richest_index] -= difference
    print(population_wealth)
else:
    print("No equal distribution possible")

# Better code for me but Judge doesn't think so
# population_wealth = [int(x) for x in input().split(", ")]
# minimum_wealth = int(input())
#
# average_wealth = sum(population_wealth) / len(population_wealth)
#
# if minimum_wealth <= average_wealth:
#     for index, el in enumerate(population_wealth):
#         while population_wealth[index] < minimum_wealth:  # index is poor
#             richest_index = population_wealth.index(max(population_wealth))
#             population_wealth[index] += 1
#             population_wealth[richest_index] -= 1
#     print(population_wealth)
# else:
#     print("No equal distribution possible")
