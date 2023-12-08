file = '/Users/hongtan/Desktop/advent_of_code_2023/day4/data.txt'
sum = 0
with open(file, 'r') as f:
    cards = f.read().splitlines()
    for card in cards:
        win_nums = card.split('|')[0].split(':')[1].split()
        my_nums = card.split('|')[1].split()

        c = -1

        for n in my_nums:
            if n in win_nums:
                c += 1

        if c != -1:
            sum += 2**c

print(sum)