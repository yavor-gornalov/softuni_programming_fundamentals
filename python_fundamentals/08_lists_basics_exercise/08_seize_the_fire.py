# https://judge.softuni.org/Contests/Compete/Index/1725#7

cells = input().split('#')
water = int(input())

effort, total_fire = 0, 0
put_out = []
for cell in cells:
    fire_type, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    if fire_type == "High" and cell_value in range(81, 126) or \
            fire_type == "Medium" and cell_value in range(51, 81) or \
            fire_type == "Low" and cell_value in range(1, 51):

        if cell_value <= water:
            water -= cell_value
            effort += cell_value / 4
            total_fire += cell_value
            put_out.append(str(cell_value))
    continue

print("Cells:")
for i in range(len(put_out)):
    print(f" - {put_out[i]}")
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")
