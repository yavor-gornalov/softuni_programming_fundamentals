# https://judge.softuni.org/Contests/Practice/Index/1730#3

string = list(map(str, input().split(" ")))
word = input()

palindromes = list(filter(lambda el: el == el[::-1], string))
print(palindromes)
print(f"Found palindrome {palindromes.count(word)} times")
