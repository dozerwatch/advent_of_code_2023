# Restrictions for each color
r = 12
g = 13
b = 14
sum = 0

with open('./day2/test.txt') as f:
    lines = f.read().splitlines()

    games = {}      # Dictionary to store the games and their sets

    for line in lines:

        # Make games dictionary
        # For ease of eye
        colon = line.index(':')
        first_semicolon = line.index(';')
        second_semicolon = line.rfind(';')

        # Find the game_id, set 1, 2, and 3
        game_id = int(line[colon-2:colon])
        set_1 = line[colon+1: first_semicolon]
        if first_semicolon == second_semicolon:
            set_2 = line[first_semicolon+1: ]
            set_3 = ''
        else:
            set_2 = line[first_semicolon+1: second_semicolon]
            set_3 = line[second_semicolon+1:]
        
        games[game_id] = [set_1, set_2, set_3]

    for id, sets in games.items():
        valid = True

        for set in sets:
            blue = set.find('blue') - 2
            green = set.find('green') -2
            red = set.find('red') -2

            if blue != -3 and int(set[blue-1:blue+1]) > b:
                valid = False
                break
            if green != -3 and int(set[green-1:green+1]) > g:
                valid = False
                break
            if red != -3 and int(set[red-1:red+1]) > r:
                valid = False
                break
        
        if valid:   # Game is possible
            if id == 0:
                id = 100
            sum += id

print(sum)

