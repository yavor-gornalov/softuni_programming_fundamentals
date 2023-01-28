# https://judge.softuni.org/Contests/Practice/Index/1720#3

input_string = input().lower()

pattern = ["Sand", "Water", "Fish", "Sun"]

# print(input_string.count(pattern[0]))

total_count = 0
for word in pattern:
    current_count = input_string.count(word.lower())
    total_count += current_count
print(total_count)
