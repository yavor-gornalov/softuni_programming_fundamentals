# https://judge.softuni.org/Contests/Practice/Index/2474#2

integers = [int(x) for x in input().split()]

avg_value = sum(integers) / len(integers)


top_elements = [x for x in integers if x > avg_value]
filtered_elements = sorted(top_elements, reverse=True)[:5]

if filtered_elements:
    print(" ".join([str(x) for x in filtered_elements]))
else:
    print("No")
