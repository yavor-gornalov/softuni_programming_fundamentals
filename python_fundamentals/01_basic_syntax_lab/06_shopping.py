# https://judge.softuni.org/Contests/Practice/Index/1718#5

budget = int(input())
command = input()

while not command == "End":
    product_price = int(command)
    if budget < product_price:
        print("You went in overdraft!")
        break
    budget -= product_price
    command = input()
else:
    print("You bought everything needed.")
