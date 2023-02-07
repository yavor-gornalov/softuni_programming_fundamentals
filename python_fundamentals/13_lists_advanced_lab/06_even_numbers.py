# https://judge.softuni.org/Contests/Practice/Index/1730#5

# get all nums from input string
nums = list(map(int, input().split(", ")))
# for n in range of list indexes check if nums[n] is even and add it to even_indexes
even_indexes = list(map(lambda n: n if not nums[n] % 2 else None, range(len(nums))))
# filter None elements from list with even indexes
even_indexes_filtered = list(filter(lambda index_el: index_el is not None, even_indexes))

print(even_indexes_filtered)
