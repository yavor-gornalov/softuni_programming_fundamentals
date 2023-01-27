# https://judge.softuni.org/Contests/Compete/Index/1719#9

start_str = input()
final_str = input()
result = None
for i, ch in enumerate(start_str):
    if final_str[i] == start_str[i]:
        continue
    result = final_str[:i + 1] + start_str[i + 1:]
    print(result)
