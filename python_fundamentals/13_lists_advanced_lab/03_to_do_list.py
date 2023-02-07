# https://judge.softuni.org/Contests/Practice/Index/1730#2

def add_note(seq, importance, note):
    seq.pop(importance)  # replace element if exists
    seq.insert(importance, note)
    return seq


todo_notes = [0] * 10  # priority from 1 to 10, means list with 10 elements!
command = input()
while command not in "End":
    tokens = command.split("-")
    priority = int(tokens[0]) - 1  # change range from [1-10] to [0-9] -> index ranges
    message = tokens[1]
    add_note(seq=todo_notes, importance=priority, note=message)
    command = input()

print([note for note in todo_notes if note])  # if note exists(note is not 0) print note
