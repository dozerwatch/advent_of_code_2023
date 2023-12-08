# First one is way too slow, not feasible.

with open('data.txt', 'r') as f:
    lines = f.read().split('\n\n')
    
    seeds = lines[0].split(':')[1].split()
    seeds = [int(x) for x in seeds]

    for line in lines[1:]:
        maps = line.split('\n')[1:]
        for i in range(len(seeds)):
            for map in maps:
                map = map.split()
                map = [int(x) for x in map]
                dst, src, r = map[0], map[1], map[2]
                if src <= seeds[i] < src+r:
                    seeds[i] = seeds[i] + (dst - src)
                    break
    
    print(min(seeds))
                    
