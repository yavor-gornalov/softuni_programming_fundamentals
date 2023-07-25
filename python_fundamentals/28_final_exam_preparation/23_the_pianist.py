# https://judge.softuni.org/Contests/Practice/Index/2525#2

def add_piece(piece, composer, key):
    if piece in pieces:
        print(f"{piece} is already in the collection!")
    else:
        print(f"{piece} by {composer} in {key} added to the collection!")
        pieces[piece] = [composer, key]


def remove_piece(piece):
    if piece not in pieces:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        del pieces[piece]
        print(f"Successfully removed {piece}!")


def change_piece_key(piece, new_key):
    if piece not in pieces:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        pieces[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")


commands = {
    "Add": add_piece,
    "Remove": remove_piece,
    "ChangeKey": change_piece_key
}

pieces = {}
pieces_count = int(input())
for _ in range(pieces_count):
    line = input()
    piece, composer, key = line.split("|")
    pieces[piece] = [composer, key]

while True:
    line = input()
    if line == "Stop":
        break
    command, *args = line.split("|")
    commands[command](*args)

for piece, (composer, key) in pieces.items():
    print(f"{piece} -> Composer: {composer}, Key: {key}")
