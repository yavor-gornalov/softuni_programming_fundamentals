# https://judge.softuni.org/Contests/Compete/Index/1725#4

def faro_shuffle(seq, shuttles):
    middle_idx = len(seq) // 2

    result = seq
    for i in range(shuttles):
        first_half, second_half = result[:middle_idx], result[middle_idx:]

        current_shuttle_result = []
        while first_half or second_half:
            current_shuttle_result.extend([first_half.pop(0), second_half.pop(0)])

        result = current_shuttle_result

    return result


cards = input().split(" ")
number_of_shuttles = int(input())
print(faro_shuffle(cards, number_of_shuttles))
