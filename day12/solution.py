lines = open('day12/test.txt').read().splitlines()
sizes = []
records = []
for line in lines:
    record, size = line.split(' ')
    records.append(record)
    sizes.append([int(x) for x in size.split(',')])

