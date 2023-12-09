lines = open('day6/part2/data.txt').read().split('\n')
time = int(lines[0].split(':')[1])
distance = int(lines[1].split(':')[1])

PRODUCT = 1
COUNT = 0

for ms in range(time+1):
    dist_traveled = ms * (time - ms)
    if dist_traveled > distance:
        COUNT += 1
PRODUCT *= COUNT

print(PRODUCT)


