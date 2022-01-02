from collections import defaultdict

with open('input.txt') as inp:
    input = inp.read().split('\n')

def answer1(input):
    gamma = ''.join([max(line, 
        key=lambda x: line.count(x)) for line in [
        [line[_] for line in input]
        for _ in range(len(input[0]))
    ]])
    epsilon = ''.join([min(line, 
        key=lambda x: line.count(x)) for line in [
        [line[_] for line in input]
        for _ in range(len(input[0]))
    ]])
    return int(gamma, 2)*int(epsilon, 2)

ratings = {'oxygen': max, 'co2': min}

def get_rating(input: list, position: int = 0, rating: str = 'oxygen'):
    keep_no = '1' if rating == 'oxygen' else '0'
    if len(input) == 1:
        return input[0]
    commonalities = defaultdict(list)
    for line in input:
        commonalities[line[position]].append(line)
    if len(commonalities['0']) == len(commonalities['1']):
        input = commonalities[keep_no]
    else:
        input = ratings[rating](commonalities.items(), key=lambda x: len(x[1]))[1]
    return get_rating(input, position=position+1)
    
def answer2(input: list):
    oxygen = get_rating(input, rating='oxygen')
    co2 = get_rating(input, rating='co2')
    return int(oxygen, 2)*int(co2, 2)

    

