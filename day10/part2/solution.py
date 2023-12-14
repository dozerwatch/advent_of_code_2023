PIPES = '|-LJ7F'                                                    # Pipes

map = open('day10/part2/test.txt').read().splitlines()                    # Puzzle input
pipe_loc = {(r, c):map[r][c] for r in range(len(map))               # Location of all pipes
            for c in range(len(map)) if map[r][c] in PIPES}

