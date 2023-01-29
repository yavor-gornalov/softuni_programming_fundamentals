# https://judge.softuni.org/Contests/Practice/Index/1724#2

n = int(input())

positives, negatives = [], []
for _ in range(n):
    number = int(input())
    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)

print(f"{positives}\n"
      f"{negatives}\n"
      f"Count of positives: {len(positives)}\n"
      f"Sum of negatives: {sum(negatives)}")
