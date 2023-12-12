SUM, plays = 0, []
lines = open('day7/test.txt').read().splitlines()
for line in lines:
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', 'ABCDE'))
    type = sorted([hand.count(card) for card in hand], reverse=True)
    plays.append((type, hand, int(bid)))
for rank, (type, hand, bid) in enumerate(sorted(plays), 1):
    SUM += rank * bid
print(SUM)



