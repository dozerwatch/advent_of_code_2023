with open('part2/data.txt', 'r') as f:
    lines = f.read().split('\n\n')
    
    seeds = lines[0].split(':')[1].split()
    seeds = [int(x) for x in seeds]
    s = []
    for i in range(16, len(seeds)-2, 2):
        for x in range(seeds[i]+284900000, seeds[i]+seeds[i+1]-253500000, 1):
            s.append(x)
    seeds = s

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
