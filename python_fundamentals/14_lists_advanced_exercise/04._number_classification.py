# https://judge.softuni.org/Contests/Compete/Index/1731#3

num_list = list(map(int, input().split(", ")))

positive_nums = list(map(str, filter(lambda num: num >= 0, num_list)))
negative_nums = list(map(str, filter(lambda num: num < 0, num_list)))
even_nums = list(map(str, filter(lambda num: not num % 2, num_list)))
odd_nums = list(map(str, filter(lambda num: num % 2, num_list)))

print(f"Positive: {', '.join(positive_nums)}\n"
      f"Negative: {', '.join(negative_nums)}\n"
      f"Even: {', '.join(even_nums)}\n"
      f"Odd: {', '.join(odd_nums)}")
