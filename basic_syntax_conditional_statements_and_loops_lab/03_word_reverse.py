# https://judge.softuni.org/Contests/Practice/Index/1718#2

def word_reverse(word):
    return word[::-1]


# main
text = input()
result = word_reverse(text)
print(result)
