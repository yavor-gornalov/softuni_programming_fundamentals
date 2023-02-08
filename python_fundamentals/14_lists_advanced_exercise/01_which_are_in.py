# https://judge.softuni.org/Contests/Compete/Index/1731#0

first_string = input().split(", ")
second_string = input().split(", ")

new_list = [substring for substring in first_string for word in second_string if substring in word]
print(sorted(set(new_list), key=new_list.index))
