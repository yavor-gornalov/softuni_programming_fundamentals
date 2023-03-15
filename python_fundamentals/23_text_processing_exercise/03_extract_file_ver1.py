# https://judge.softuni.org/Contests/Compete/Index/1740#2

path_args = input().split("\\")[-1]

file_args = path_args.split(".")
filetype = file_args.pop()
filename = ".".join(file_args)

print(f"File name: {filename}\n"
      f"File extension: {filetype}")
