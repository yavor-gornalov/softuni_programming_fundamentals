# https://judge.softuni.org/Contests/Practice/Index/1732#0

population_wealth = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

if minimum_wealth <= sum(population_wealth) / len(population_wealth):
    while any(x < minimum_wealth for x in population_wealth):
        wealthiest_idx = population_wealth.index(max(population_wealth))
        poorest_idx = population_wealth.index(min(population_wealth))
        population_wealth[wealthiest_idx] -= minimum_wealth - population_wealth[poorest_idx]
        population_wealth[poorest_idx] = minimum_wealth
    print(population_wealth)
else:
    print("No equal distribution possible")
