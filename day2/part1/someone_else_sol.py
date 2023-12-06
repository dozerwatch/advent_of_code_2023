POSSIBLE_CUBE_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

RESULT = 0

def is_game_possible(line: str) -> bool:
    subgames = line.split(":")[1].split(";")
    for subgame in subgames:
        for num_cubes in subgame.split(','):
            num, color = num_cubes.split()
            if int(num) > POSSIBLE_CUBE_COUNT[color]:
                return False
    return True

with open('./day2/data.txt', 'r') as f:
    lines = f.read()
for index, line in enumerate(lines.split("\n")):
    if is_game_possible(line):
        print(f"Game {index + 1} is possible")
        RESULT += (index + 1)

print(RESULT)