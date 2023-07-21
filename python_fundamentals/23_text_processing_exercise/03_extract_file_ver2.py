# https://judge.softuni.org/Contests/Compete/Index/1740#1

path = input()

file_with_extension = path.split("\\")[-1]
filename, extension = file_with_extension.split(".")

print(f"File name: {filename}\nFile extension: {extension}")
