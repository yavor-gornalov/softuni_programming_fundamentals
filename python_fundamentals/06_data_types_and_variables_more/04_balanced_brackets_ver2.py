# https://judge.softuni.org/Contests/Practice/Index/1723#3

number_of_lines = int(input())
demanded_bracket, next_bracket = "(", ")"
for _ in range(number_of_lines):
    line = input()
    if line not in [demanded_bracket, next_bracket]:
        continue
    if not line == demanded_bracket:
        print("UNBALANCED")
        break
    demanded_bracket, next_bracket = next_bracket, demanded_bracket
else:
    print("BALANCED")
