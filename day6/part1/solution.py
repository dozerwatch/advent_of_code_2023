lines = open('day6/data.txt').read().split('\n')
time = [int(x) for x in lines[0].split(':')[1].split()]
distance = [int(x) for x in lines[1].split(':')[1].split()]

PRODUCT = 1

for i in range(len(time)):
    count = 0
    for ms in range(time[i]+1):
        dist_traveled = ms * (time[i] - ms)
        if dist_traveled > distance[i]:
            count += 1
    PRODUCT *= count

print(PRODUCT)


