# https://judge.softuni.org/Contests/Compete/Index/1722#8

n = int(input())
max_snowball_value, max_snowball_weight, max_snowball_time, max_snowball_quality = 0, 0, 0, 0
for _ in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight // snowball_time) ** snowball_quality
    if snowball_value > max_snowball_value:
        max_snowball_value, max_snowball_weight, max_snowball_time, max_snowball_quality \
            = snowball_value, snowball_weight, snowball_time, snowball_quality
print(f"{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")
