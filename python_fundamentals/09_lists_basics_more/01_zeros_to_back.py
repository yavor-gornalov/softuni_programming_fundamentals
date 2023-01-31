# https://judge.softuni.org/Contests/Practice/Index/1726#0

nums = list(map(int, input().split(", ")))

zero_counter = 0
while 0 in nums:
    nums.remove(0)
    zero_counter += 1

for _ in range(zero_counter):
    nums.append(0)

print(nums)
