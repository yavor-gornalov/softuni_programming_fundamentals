# https://judge.softuni.org/Contests/Practice/Index/1724#3

n = int(input())
filter_word = input()
string_list = []
filtered_list = []
for _ in range(n):
    string = input()
    string_list.append(string)
    if filter_word in string:
        filtered_list.append(string)

print(string_list)
print(filtered_list)
