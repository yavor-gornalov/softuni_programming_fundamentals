# https://judge.softuni.org/Contests/Practice/Index/2031#0

food, hay, cover, guinea_pig_weight = [1000 * float(input()) for _ in range(4)]

for current_day in range(1, 31):
    food -= 300
    if current_day % 2 == 0:
        hay -= 0.05 * food
    if current_day % 3 == 0:
        cover -= guinea_pig_weight / 3

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(
        f"Everything is fine! Puppy is happy! "
        f"Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
