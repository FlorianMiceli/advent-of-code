input = open('input.txt', 'r')
lines = input.readlines()

calibration_values_sum, first_digit, second_digit = 0, 0, 0
for line in lines :

    # from left
    for char in line :
        if char.isdigit() :
            first_digit = char
            break

    # from right
    for char in reversed(line):
        if char.isdigit():
            second_digit = char
            break
    calibration_values_sum += int(first_digit + second_digit)

print(calibration_values_sum)

### PART 2 ###

numbers = { "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def getNumberAt(line, pos) :
    for number in numbers.keys() :
        if pos + len(number) > len(line) :
            continue
        if line[pos:pos+len(number)] == number :
            return number
    return False
   
calibration_values_sum, first_digit, second_digit = 0, 0, 0
for line in lines :
    
    # from left 
    for i in range(len(line)) :
        char = line[i]
        if char.isdigit() :
            first_digit = char
            break
        if getNumberAt(line, i) :
            first_digit = str(numbers[getNumberAt(line, i)])
            break

    # from right
    for i in range(len(line)-1,0,-1) :
        char = line[i]
        if char.isdigit():
            second_digit = char
            break
        if getNumberAt(line, i) :
            second_digit = str(numbers[getNumberAt(line, i)])
            break

    calibration_values_sum += int(first_digit + second_digit)
        
print(calibration_values_sum)