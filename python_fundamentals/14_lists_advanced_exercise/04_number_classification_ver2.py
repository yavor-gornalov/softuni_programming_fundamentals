# https://judge.softuni.org/Contests/Compete/Index/1731#3

nums = [int(x) for x in input().split(", ")]

positive_nums = [str(x) for x in nums if x >= 0]
negative_nums = [str(x) for x in nums if x < 0]
even_nums = [str(x) for x in nums if x % 2 == 0]
odd_nums = [str(x) for x in nums if x % 2 != 0]

print(f"Positive: {', '.join(positive_nums)}\n"
      f"Negative: {', '.join(negative_nums)}\n"
      f"Even: {', '.join(even_nums)}\n"
      f"Odd: {', '.join(odd_nums)}")
