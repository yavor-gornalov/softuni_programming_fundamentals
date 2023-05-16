# https://judge.softuni.org/Contests/Compete/Index/1722#8

class Snowball:
    def __init__(self, weight, time, quality):
        self.weight = weight
        self.time = time
        self.quality = quality

    def get_snowball_value(self):
        return (self.weight // self.time) ** self.quality if self.time != 0 else 0


snowballs_count = int(input())
best_snowball = Snowball(0, 0, 0)
for _ in range(snowballs_count):
    current_weight, current_time, current_quality = [int(input()) for _ in range(3)]
    current_snowball = Snowball(current_weight, current_time, current_quality)
    if current_snowball.get_snowball_value() > best_snowball.get_snowball_value():
        best_snowball = current_snowball

print(f"{best_snowball.weight} : {best_snowball.time} = {best_snowball.get_snowball_value()} ({best_snowball.quality})")
