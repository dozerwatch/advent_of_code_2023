import math as m, re
length = 140

board = list(open('day3/part1/data.txt'))

# Find the location of symbols
chars = {(r, c): [] for r in range(length) for c in range(length) 
                        if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row): 
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(lst) for lst in chars.values()))
print(sum(m.prod(p) for p in chars.values() if len(p)==2))
