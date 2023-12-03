import re
input = open('input.txt', 'r')
lines = input.readlines()
# remove \n if exists
lines = [line.strip() for line in lines]

# is there a symbol around the caracter?
symbols = ['*', '@', '+', '-', '=', '&', '/', '#', '%', '$']

def isSymbolAround(lineIndex, pos) :
    line = lines[lineIndex]
    previous_line = lines[lineIndex-1] if lineIndex > 0 else None
    next_line = lines[lineIndex+1] if lineIndex < len(lines)-1 else None

    if pos > 0 and pos < len(line)-1 :
        i = -1
        j = 2
    if pos == 0 :
        i = 0
        j = 2
    if pos == len(line)-1 :
        i = -2
        j = 0

    symbol_in_previous_line, symbol_in_next_line = False, False
    if previous_line :
        symbol_in_previous_line = any(symbol in previous_line[pos+i:pos+j] for symbol in symbols) if previous_line else False
    if next_line :
        symbol_in_next_line = any(symbol in next_line[pos+i:pos+j] for symbol in symbols) if next_line else False
    symbol_next_to = any(symbol in line[pos+i:pos+j] for symbol in symbols) 

    return symbol_in_next_line or symbol_in_previous_line or symbol_next_to
    
def posOfDigits(line):
    return [i for i in range(len(line)) if line[i].isdigit()]

def lign_to_numbers(line, posOfDigits):
    numbers = []
    for i in range(len(posOfDigits)):
        if i == 0 :
            numbers.append(line[posOfDigits[i]])
        elif posOfDigits[i] == posOfDigits[i-1]+1 :
            numbers[-1] += line[posOfDigits[i]]
        else :
            numbers.append(line[posOfDigits[i]])
    return numbers

def associate_numbers_and_digit_indexes(line):
    numbers_and_digit_indexes = {}
    numbers = lign_to_numbers(line, posOfDigits(line))
    digit_positions = posOfDigits(line)
    for number in numbers :
        numbers_and_digit_indexes[number] = {'lineIndex' : lines.index(line), 'positions' : []}
        for i in range(len(number)) :
            numbers_and_digit_indexes[number]['positions'].append(digit_positions.pop(0))
    return numbers_and_digit_indexes

valid_numbers_sum = 0
for line in lines :
    validated_lign = line
    # print('---- line number', lines.index(line), '----')
    # print(line)
    numbers = associate_numbers_and_digit_indexes(line)
    # print(numbers)
    for number in numbers :
        # verify if there is a symbol around the number
        for pos in numbers[number]['positions'] :
            # print(pos)
            if isSymbolAround(numbers[number]['lineIndex'], pos) :
                # print('symbol around', number)
                # print('adding',number)
                valid_numbers_sum += int(number)
                validated_lign = validated_lign.replace(number, '\033[92m'+number+'\033[0m')
                break
        else :
            # print('no symbol around', number)
            pass

    print(validated_lign)

print(valid_numbers_sum)