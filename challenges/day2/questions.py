with open('input.txt') as inp:
    inputs = inp.read().split('\n')

def answer1(input):
    return sum([
        int(e.split(' ')[-1])
        for e in input if e.split(' ')[0] == 'forward'
    ])*sum([
        int(e.split(' ')[-1]) if e.split(' ')[0] == 'down'
        else -int(e.split(' ')[-1])
        for e in input if e.split(' ')[0] in ['up', 'down']
    ])

def answer2(input):
    output = {'aim': 0,'horizontal': 0,'depth': 0}
    for line in input:
        direction, value = line.split(' ')
        if direction == 'forward':
            output['horizontal'] += int(value)
            output['depth'] += output['aim'] * int(value)
        elif direction == 'down':
            output['aim'] += int(value)
        elif direction == 'up':
            output['aim'] -= int(value)
    return output['horizontal'] * output['depth']
