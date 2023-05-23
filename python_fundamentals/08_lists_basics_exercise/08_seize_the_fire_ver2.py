# https://judge.softuni.org/Contests/Compete/Index/1725#7

fire_types_ranges = {
    "High": range(81, 125 + 1),
    "Medium": range(51, 80 + 1),
    "Low": range(1, 50 + 1)
}

# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
fire_cells = [[cell.split(" = ")[0], int(cell.split(" = ")[1])] for cell in input().split("#")]
water = int(input())

putted_out_cells = []
total_effort, total_fire = 0, 0
while fire_cells:
    current_fire_type, current_value = fire_cells.pop(0)
    if current_value not in fire_types_ranges[current_fire_type]:
        continue
    if water < current_value:
        continue
    water -= current_value
    total_fire += current_value
    total_effort += 0.25 * current_value
    putted_out_cells.append(current_value)

print("Cells:")
[print(f" - {c}") for c in putted_out_cells]
print(f"Effort: {total_effort:.2f}\nTotal Fire: {total_fire}")
