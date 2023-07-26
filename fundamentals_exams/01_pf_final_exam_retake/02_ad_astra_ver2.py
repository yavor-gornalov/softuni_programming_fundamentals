# https://judge.softuni.org/Contests/Practice/Index/2525#1
import re

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"

line = input()
items = re.findall(pattern, line)

products = []
total_calories = 0
for sep, item, best_before, calories in items:
    products.append(f"Item: {item}, Best before: {best_before}, Nutrition: {calories}")
    total_calories += int(calories)

print(f"You have food to last you for: {total_calories // 2000} days!")
print(*products, sep="\n")
