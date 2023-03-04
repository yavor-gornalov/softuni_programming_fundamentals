# https://judge.softuni.org/Contests/Practice/Index/1733#1

class Party:
    def __init__(self):
        self.people = []


new_party = Party()
while True:
    command = input()
    if command == "End":
        break
    new_party.people.append(command)

print(f"Going: {', '.join(new_party.people)}\nTotal: {len(new_party.people)}")
