# https://judge.softuni.org/Contests/Compete/Index/1731#7

message = input().split()

decrypted_message = []
for word in message:
    word = list(word)
    first_letter = [n for n in word if n.isnumeric()]
    word = [ch for ch in word if ch not in first_letter]
    word[0], word[-1] = word[-1], word[0]
    first_letter = chr(int("".join(first_letter)))
    word.insert(0, first_letter)
    word = "".join(word)

    decrypted_message.append(word)

print(" ".join(decrypted_message))
