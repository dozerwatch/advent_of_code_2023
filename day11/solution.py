# Not my solution. This is a very elegant one though. I like very much. Thank you. Learned something!

lines = open("day11/data.txt").read().splitlines()
universe = [list(line) for line in lines]
empty_rows = [i for i, row in enumerate(universe) if all(char == '.' for char in row)]
empty_cols = [i for i, col in enumerate(zip(*universe)) if all(char == '.' for char in col)]
galaxies = [(row, col) for row, line in enumerate(universe) for col, char in enumerate(line) if char == '#']

p1 = 0
p2 = 0
for i, (galaxy_row, galaxy_col) in enumerate(galaxies):
    for (other_galaxy_row, other_galaxy_col) in galaxies[:i]:
        for row in range(min(other_galaxy_row, galaxy_row), max(other_galaxy_row, galaxy_row)):
            p1 += 2 if row in empty_rows else 1
            p2 += 1000000 if row in empty_rows else 1

        for col in range(min(other_galaxy_col, galaxy_col), max(other_galaxy_col, galaxy_col)):
            p1 += 2 if col in empty_cols else 1
            p2 += 1000000 if col in empty_cols else 1

print("Part 1: ", p1)
print("Part 2: ", p2)
