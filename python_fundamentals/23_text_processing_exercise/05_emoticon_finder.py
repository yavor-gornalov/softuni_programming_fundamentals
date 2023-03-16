# https://judge.softuni.org/Contests/Compete/Index/1740#4
"""
most important test!
input:
    here are some tri::cky emoj::is
output:
    ::, :c, ::, :i
"""

text = list(input())

while text:
    emoticon = ""
    symbol = text.pop(0)
    if symbol == ":" and len(text):
        addon = text.pop(0)
        emoticon = symbol + addon
        if addon == ":":
            text.insert(0, addon)
        if emoticon:
            print(emoticon)
