# https://judge.softuni.org/Contests/Compete/Index/1740#9

tickets = [x.strip() for x in input().split(", ")]
winning_symbols = "@#$^"
for ticket in tickets:
    is_winning = False
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    for symbol in winning_symbols:
        if len(ticket) != 20:
            continue
        if symbol * len(ticket) == ticket:
            print(f"ticket \"{ticket}\" - {len(ticket) // 2}{symbol} Jackpot!")
            is_winning = True
            break
        for count in range(len(ticket) // 2, len(ticket) // 4, -1):
            fst_half, snd_half = ticket[:len(ticket) // 2], ticket[len(ticket) // 2:]
            if symbol * count in fst_half and symbol * count in snd_half:
                print(f"ticket \"{ticket}\" - {count}{symbol}")
                is_winning = True
                break
        if is_winning:
            break
    if not is_winning:
        print(f"ticket \"{ticket}\" - no match")
