SUM, plays= 0, []
lines = open('day7/part2/data.txt').read().splitlines()
for line in lines:
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', 'A0CDE'))
    replacement_hands = [hand.replace('0', r) for r in hand]
    counts = [[h.count(x) for h in replacement_hands for x in h][x:x+5] for x in range(0,25,5)]
    sorted_hands = [sorted(h, reverse=True) for h in counts]
    type = max(sorted_hands)
    plays.append((type, hand, int(bid)))
for rank, (type, hand, bid) in enumerate(sorted(plays), 1):
    SUM += rank * bid
print(SUM)



