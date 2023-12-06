SUM = 0

def get_power_of_minimum_set_of_cubes(game):
    '''
        Return the power of minimum set of cubes for each game.

        The minimum set of cubes is the fewest number of cubes of each color
        that could the game requires. There are only red, green, and blue cubes.

        The power of the minimum set is the their product.
    '''
    MINIMUM_SET = {'red': 0,
                   'green': 0,
                   'blue': 0}   # Fewest number of cubes for each color

    # Get the minimum set of cubes
    subgames = game.split(':')[1].split(';')
    for subgame in subgames:
        pairs = subgame.split(',')
        for pair in pairs:
            num, color = pair[1:].split(' ')
            if int(num) > MINIMUM_SET[color]:
                MINIMUM_SET[color] = int(num)

    # Get the power (product)
    power = 1
    for _, val in MINIMUM_SET.items():
        power *= val

    return power
            
with open('./day2/part2/data.txt', 'r') as f:
    games = f.read().splitlines()
    for game in games:
        power = get_power_of_minimum_set_of_cubes(game)
        SUM += power

print(SUM)