'''
    My first attempt at this was an absolute fail! My code is messy and long and
    confusing. Overall, just really poor design. AND it gives the incorrect answer.
    So yeah, I looked online for a solution and came across one that is very elegent
    and I understand it. This is me using that knowledge and trying to implement it
    myself.
'''

# This is the only part that I copied and pasted.
POSSIBLE_CUBE_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

SUM = 0

def is_possible_game(line):
    '''
    Takes a line (game) and returns True is game is possible, otherwise False
    '''

    subgames = line.split(':')[1].split(';')
    for subgame in subgames:
        pairs = subgame.split(',')
        for pair in pairs:
            num, color = pair[1:].split(' ')
            if int(num) > POSSIBLE_CUBE_COUNT[color]:
                return False
    return True

with open('./day2/data.txt', 'r') as f:
    lines = f.read()
    for id, line in enumerate(lines.split('\n')):
        if is_possible_game(line):
            SUM += id+1

print(SUM)