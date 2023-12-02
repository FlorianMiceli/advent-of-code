input = open('input.txt', 'r')
lines = input.readlines()

games = {}
for line in lines :
    line = line[:-1] if line[-1] == '\n' else line # remove \n
    subsets = []
    subsets_str = line.split(':')[1].split(';')
    game_id = line.split(':')[0].replace('Game ', '')
    for subset_str in subsets_str :
        subset_dict = {}
        subset_items = subset_str.split(', ')
        for s in subset_items :
            s = s.split()
            subset_dict[s[1]] = int(s[0])
        subsets.append(subset_dict)
    games[game_id] = subsets

max_cubes_per_subset = { 'red' : 12, 'green' : 13, 'blue' : 14 }

def isGameValid(game, max_cubes_per_subset) :
    for subset in game :
        for color, count in subset.items() :
            if count > max_cubes_per_subset[color] :
                return False
    return True
    
ID_sum = 0
for game in games:
    if isGameValid(games[game], max_cubes_per_subset) :
        ID_sum += int(game)

print(f'ID sum: {ID_sum}')

### Part 2 ###

# get the minimum number of cubes for each color in all subsets
def getMinCubes(game) :
    min_cubes = {}
    for color in max_cubes_per_subset :
        min_cubes[color] = 0
    for subset in game :
        for color, count in subset.items() :
            if min_cubes[color] < count :
                min_cubes[color] = count
    return min_cubes

# multiply the minimum number of cubes of each color in a game
def powerCubes(min_cubes) :
    power = 1
    for color, count in min_cubes.items() :
        power *= count
    return power

sum_powers = sum(powerCubes(getMinCubes(games[game])) for game in games)

print(f'Sum of powers: {sum_powers}')