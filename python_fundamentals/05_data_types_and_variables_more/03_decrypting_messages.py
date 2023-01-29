# https://judge.softuni.org/Contests/Practice/Index/1723#2

encryption_number = int(input())
n = int(input())

decrypted_text = ""
for _ in range(n):
    ch = input()
    decrypted_text += chr(ord(ch) + encryption_number)

print(decrypted_text)
