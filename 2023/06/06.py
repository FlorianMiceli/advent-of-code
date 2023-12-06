input = open('input.txt', 'r')
lines = input.readlines()

times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()

DEBUG = False

def getDistance(timeButtonHeld, timeToTravel):
    millimetersPerSecond = timeButtonHeld 
    return millimetersPerSecond * timeToTravel

def getNumberOfRecordDistance(timeToTravel, recordDistance):
    nbr_of_record_distance = 0
    for i in range(timeToTravel+1):
        time_to_travel_left = timeToTravel-i
        distance_travelled = getDistance(i, time_to_travel_left)
        # print it in green if it is a record distance
        if distance_travelled > recordDistance:
            print('\033[92m' + str(distance_travelled) + '\033[0m') if DEBUG else None
            nbr_of_record_distance += 1
        else:
            print(distance_travelled) if DEBUG else None
    return nbr_of_record_distance

def getWaysToWinMultiplied(times, distances):
    ways_to_win_multiplied = 1
    for i in range(len(times)):
        print('Time: ' + times[i] + ' Distance: ' + distances[i]) if DEBUG else None
        nbr_of_record_distance = getNumberOfRecordDistance(int(times[i]), int(distances[i]))
        ways_to_win_multiplied *= nbr_of_record_distance
    return ways_to_win_multiplied

ways_to_win_multiplied = getWaysToWinMultiplied(times, distances)
print(f'Part 1 : {ways_to_win_multiplied}')

### Part 2 ###

# concatenate all the times and distances
times_concat = [''.join(times)]
distances_concat = [''.join(distances)]

ways_to_win_multiplied = getWaysToWinMultiplied(times_concat, distances_concat)
print(f'Part 2 : {ways_to_win_multiplied}')