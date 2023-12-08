with open('test.txt', 'r') as f:
    lines = f.read().split('\n\n')
    
    seeds = lines[0].split(':')[1].split()
    seeds = [int(x) for x in seeds]

    for line in lines[1:]:
        maps = line.split('\n')[1:]
        m = {}
        for map in maps:
            map = map.split()
            map = [int(x) for x in map]
            for i in range(map[2]):
                m[map[1]+i] = map[0] + i
        
        for i in range(len(seeds)):
            if seeds[i] in m:
                seeds[i] = m[seeds[i]]

        print(seeds)
