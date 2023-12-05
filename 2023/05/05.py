input = open('input.txt', 'r')
lines = input.readlines()

seeds = lines[0].split(':')[1].split()

# remove seeds line and the empty line after it
lines.pop(0)
lines.pop(0)

# add an empty line at the end of the file
lines.append('\n')

# example : 'seed-to-soil map:' => (seed, soil)
def headerToPair(header):
    header = header.split(':')[0][:-4].split('-')
    return (header[0], header[2])

# examples : 
# 50 98 2 => {98: 50, 99: 51}
# 52 50 3 => {50: 52, 51: 53, 52: 54}
def lineToItemAssociationsDict(line):
    line = line.split()
    source_start = int(line[1])
    dest_start = int(line[0])
    count = int(line[2])
    return {source_start + i: dest_start + i for i in range(count)}

def isLineHeader(line):
    # remove \n
    line = line[:-1]
    return line[-1] == ':'

def isLineEmpty(line):
    return line == '\n'

def combineAssociationsDicts(dict1, dict2):
    return {**dict1, **dict2}


associations = {}
current_associations = {}
header_pair = None
print(seeds)
print('------------------')
for line in lines:
    print(line)

    # if line empty, add the current associations to the associations dict and reset the current associations
    if isLineEmpty(line):
        associations[header_pair] = current_associations
        current_associations = {}
        continue

    # if line is header, update header_pair
    if isLineHeader(line):
        header_pair = headerToPair(line)
        print(header_pair)
        continue

    # if line is an association, get the association dict and combine it with the current associations (if any)
    if not isLineHeader(line):
        line_associations = lineToItemAssociationsDict(line)
        current_associations = combineAssociationsDicts(current_associations, line_associations)
        continue

def getLocationFromSeed(seed):
    current_pair = ('seed', 'soil')
    current_associations = associations[current_pair]
    current_item_destination = current_associations[int(seed)] if int(seed) in current_associations.keys() else int(seed)
    while current_pair[1] != 'location':
        # find in assiciations the pair that has current_pair[1] as a source
        current_pair = list(filter(lambda pair: pair[0] == current_pair[1], associations.keys()))[0]
        current_associations = associations[current_pair]
        # we find the destination of the current item in the current associations, if it's not there, we go to the next pair
        if current_item_destination not in current_associations.keys():
            continue
        current_item_destination = current_associations[int(current_item_destination)]
    return current_item_destination
    
locations = []
for seed in seeds:
    location = getLocationFromSeed(seed)
    locations.append(location)
    print(location)

print(min(locations))