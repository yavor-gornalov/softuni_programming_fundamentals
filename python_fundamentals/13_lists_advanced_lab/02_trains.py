# https://judge.softuni.org/Contests/Practice/Index/1730#1

def add(sequence, count): sequence[-1] += count


def insert(sequence, index, count): sequence[index] += count


def leave(sequence, index, count): sequence[index] -= count


train = [0] * int(input())

command = input()
while command not in "End":
    tokens = command.split()
    action = tokens[0]

    if action in "add":
        people = int(tokens[1])
        add(sequence=train, count=people)
    elif action in ["insert", "leave"]:
        wagon = int(tokens[1])
        people = int(tokens[2])
        if action in "insert":
            insert(sequence=train, index=wagon, count=people)
        elif action in "leave":
            leave(sequence=train, index=wagon, count=people)

    command = input()

print(train)
