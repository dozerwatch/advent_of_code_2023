with open('./day2/test.txt') as f:
    lines = f.read().splitlines()

    for line in lines[0:1]:
        d = dict(item.split() for item in line.split(':'))