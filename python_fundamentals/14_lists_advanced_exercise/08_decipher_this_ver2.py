# https://judge.softuni.org/Contests/Compete/Index/1731#7

message = input()

deciphered_message = []
for word in message.split():
    first_letter = ""
    deciphered_word = []
    for letter in word:
        if letter.isnumeric():
            first_letter += letter
            continue
        deciphered_word.append(letter)

    deciphered_word[0], deciphered_word[-1] = deciphered_word[-1], deciphered_word[0]
    deciphered_word = chr(int(first_letter)) + "".join(deciphered_word)

    deciphered_message.append(deciphered_word)

print(*deciphered_message, sep=" ")
