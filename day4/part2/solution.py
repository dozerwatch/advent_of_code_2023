with open('day4/part2/data.txt', 'r') as f:
    cards = f.read().splitlines()
    s = len(cards)
    instances = {i:1 for i in range(len(cards))}

    for i, card in enumerate(cards):
        win_nums = card.split('|')[0].split(':')[1].split()
        my_nums = card.split('|')[1].split()

        for _ in range(instances[i]):
            c = 0
            for n in my_nums:
                if n in win_nums:
                    s += 1
                    c += 1
                    instances[i+c] += 1

    print(s)

