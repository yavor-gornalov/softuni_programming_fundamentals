# https://judge.softuni.org/Contests/Practice/Index/1739#1

words = input().split()
final_string = ""
for word in words:
    final_string += word * len(word)
print(final_string)
