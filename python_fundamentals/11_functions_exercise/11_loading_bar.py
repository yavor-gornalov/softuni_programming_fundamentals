# https://judge.softuni.org/Contests/Compete/Index/1728#10

def loading_bar(percent: int):
    percent_count = percent // 10
    dots_count = (100 - percent) // 10
    if percent < 100:
        print(f"{percent}% [{'%' * percent_count}{'.' * dots_count}]\n"
              f"Still loading...")
    else:
        print(f"{percent}% Complete!\n"
              f"[{'%' * percent_count}{'.' * dots_count}]")


n = int(input())
loading_bar(n)
