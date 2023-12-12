from math import lcm

lines = open('day8/data.txt').read().splitlines()
steps, networks = lines[0], lines[2:]
net = {}
for network in networks:
    src, dst = network.split(' = ')
    net[src] = tuple([dst[1:4], dst[6:9]])

# loc = 'AAA'                                     # part 1
locs = [x for x in net.keys() if x[2] == 'A']   # part 2
count = 0
c = True
# while(c):
#     for step in steps:
#         if step == 'R':
#             for i in range(len(locs)):
#                 locs[i] = net[locs[i]][1]
#         else:
#             for i in range(len(locs)):
#                 locs[i] = net[locs[i]][0]

#         count += 1

#         for x in locs:
#             if x[2] == 'Z':
#                 print(x, count)
#     if not c:
#         break

print(lcm(12083, 16579, 17141, 18827, 19951, 22199))    # part 2