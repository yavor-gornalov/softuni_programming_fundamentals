# https://judge.softuni.org/Contests/Compete/Index/1740#9
import re


def is_ticket_valid(ticket): return len(ticket) == 20


def get_combinations_length_and_symbol(ticket):
    winning_symbols = '@#$^'

    max_combination = 0
    max_symbol = ""
    for symbol in winning_symbols:
        pattern = f"\\{symbol}+"
        regex = re.compile(pattern)
        first = regex.search(ticket[:10])
        second = regex.search(ticket[10:])
        if first and second:
            max_combination = max(0, min(len(first.group()), len(second.group())))
            max_symbol = symbol

    return max_combination, max_symbol


def check_ticket(ticket):
    if not is_ticket_valid(ticket):
        return "invalid ticket"

    combination_length, symbol = get_combinations_length_and_symbol(ticket)

    if combination_length < 6:
        return f'ticket "{ticket}" - no match'

    if combination_length < 10:
        return f'ticket "{ticket}" - {combination_length}{symbol}'

    return f'ticket "{ticket}" - {combination_length}{symbol} Jackpot!'


tickets = [t.strip() for t in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))
