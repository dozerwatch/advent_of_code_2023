PIPES = '|-LJ7F'                                                    # Pipes

map = open('day10/test.txt').read().splitlines()                    # Puzzle input
pipe_loc = {(r, c):map[r][c] for r in range(len(map)) 
                for c in range(len(map)) if map[r][c] in PIPES}     # Location of all pipes

# Check if a surrounding pipe is valid around start
def is_pipes_around_start_valid(pos, pipe):
    '''
    pos: 
        (r, c) a tuple containing the row and column of the position
    pipe:
        (r, c) a tuple containing the row and column of the start
    
    Return True if a surrounding pipe is valid around a position, else False
    '''

    # |
    if pipe_loc[pipe] == '|':
        if pos[1] == pipe[1]:   # Same column
          return pos[0] == pipe[0]+1 or pos[0] == pipe[0]-1
        return False
    # -
    elif pipe_loc[pipe] == '-':
        if pos[0] == pipe[0]:   # Same row
            return pos[1] == pipe[1]+1 or pos[1] == pipe[1]-1
        return False
    # 7
    elif pipe_loc[pipe] == '7':
        if pipe[0] == pos[0]:   # Same row
            return pos[1] == pipe[1]-1
        elif pipe[1] == pos[1]: # Same column
            return pos[0] == pipe[0]+1
        return False
    # L
    elif pipe_loc[pipe] == 'L':
        if pipe[0] == pos[0]:   # Same row
            return pos[1] == pipe[1]+1
        elif pipe[1] == pos[1]: # Same column
            return pos[0] == pipe[0]-1
        return False
    # J
    elif pipe_loc[pipe] == 'J':
        if pipe[0] == pos[0]:   # Same row
            return pos[1] == pipe[1]-1
        elif pipe[1] == pos[1]: # Same column
            return pos[0] == pipe[0]-1
        return False
    # F
    else:
        if pipe[0] == pos[0]:   # Same row
            return pos[1] == pipe[1]+1
        elif pipe[1] == pos[1]: # Same column
            return pos[0] == pipe[0]+1
        return False
    
def is_pipe_valid(pos, pipe):
    '''
    pos: 
        (r, c) a tuple containing the row and column of the position
    pipe:
        (r, c) a tuple containing the row and column of the pipe
    
    Return True if a surrounding pipe is valid around a position, else False
    '''

    # |
    if pipe_loc[pos] == '|':
        if pos[1] == pipe[1]:
            if pipe[0] == pos[0]-1:     # Located above
                return pipe_loc[pipe] == '|' or pipe_loc[pipe] == '7' or pipe_loc[pipe] == 'F'
            else:                       # Located below
                return pipe_loc[pipe] == '|' or pipe_loc[pipe] == 'L' or pipe_loc[pipe] == 'J'
        return False
    # -
    if pipe_loc[pos] == '-':
        if pos[0] == pipe[0]:
            if pipe[1] == pos[1]-1:     # Located left
                return pipe_loc[pipe] == '-' or pipe_loc[pipe] == 'L' or pipe_loc[pipe] == 'F'
            else:                       # Located right
                return pipe_loc[pipe] == '-' or pipe_loc[pipe] == '7' or pipe_loc[pipe] == 'J'
        return False
    # 7
    if pipe_loc[pos] == '7':
        if pipe[1] == pos[1]-1 and pipe[0] == pos[0]:       # Located left
            return pipe_loc[pipe] == '-' or pipe_loc[pipe] == 'L' or pipe_loc[pipe] == 'F'
        if pipe[1] == pos[1] and pipe[0] == pos[0]+1:       # Located below
            return pipe_loc[pipe] == '|' or pipe_loc[pipe] == 'L' or pipe_loc[pipe] == 'J'
        return False
    # L
    if pipe_loc[pos] == 'L':
        if pipe[1] == pos[1]+1 and pipe[0] == pos[0]:       # Located right
            return pipe_loc[pipe] == '-' or pipe_loc[pipe] == '7' or pipe_loc[pipe] == 'J'
        if pipe[1] == pos[1] and pipe[0] == pos[0]-1:       # Located above
            return pipe_loc[pipe] == '|' or pipe_loc[pipe] == '7' or pipe_loc[pipe] == 'F'
        return False
    # J
    if pipe_loc[pos] == 'J':
        if pipe[1] == pos[1]-1 and pipe[0] == pos[0]:       # Located left
            return pipe_loc[pipe] == '-' or pipe_loc[pipe] == 'L' or pipe_loc[pipe] == 'F'
        if pipe[1] == pos[1] and pipe[0] == pos[0]-1:       # Located above
            return pipe_loc[pipe] == '|' or pipe_loc[pipe] == '7' or pipe_loc[pipe] == 'F'
        return False
    # F
    if pipe_loc[pos] == 'F':
        if pipe[1] == pos[1]+1 and pipe[0] == pos[0]:       # Located right
            return pipe_loc[pipe] == '-' or pipe_loc[pipe] == '7' or pipe_loc[pipe] == 'J'
        if pipe[1] == pos[1] and pipe[0] == pos[0]+1:       # Located below
            return pipe_loc[pipe] == '|' or pipe_loc[pipe] == 'L' or pipe_loc[pipe] == 'J'
        return False
    
    return False
    
def find_pipes(pos, valid_pipes):
    '''
    pos: 
        (r, c) a tuple containing the row and column of the position

    valid_pipes:
        a list containing all the pipes that were already accounted for in the main loop

    Return a set of valids pipes around given position not already in main loop.
    '''
    row, col = pos
    box_around_pos = {(r, c) for r in (row-1, row, row+1) for c in (col-1, col, col+1)}
    pipes_around_pos = box_around_pos & pipe_loc.keys()
    valids = set()
    for pipe in pipes_around_pos:
        if pipe not in valid_pipes:
            valids.add(pipe)
    return valids

# Find the starting point
start = ()
for i in range(len(map)):
    if 'S' in map[i]:
        start = (i, map[i].index('S'))

valid_pipes = []    # List for main loop pipes 
new_pipes = []

# Find the two valid pipes around start
if not new_pipes:   
    pipes_around_start = find_pipes(start, valid_pipes)
    for pipe in pipes_around_start:
        if is_pipes_around_start_valid(start, pipe):
            new_pipes.append(pipe)

# Find main loop pipes
while(True):
    valid_pipes.extend(new_pipes)
    old_pipes = new_pipes
    new_pipes = []
    for pipe in old_pipes:
        pipes_around = find_pipes(pipe, valid_pipes)
        for pipe_around in pipes_around:
            if is_pipe_valid(pipe, pipe_around):
                new_pipes.append(pipe_around)
    if all([True if x in valid_pipes else False for x in new_pipes]):
        break

print("Part 1: ", int(len(valid_pipes)/2))

# -------- Part 2 -------- #










