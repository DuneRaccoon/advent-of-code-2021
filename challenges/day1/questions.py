with open('input.txt') as inp:
    inputs = [int(e) for e in inp.read().split('\n')]

def answer1(input):
    return len([e for i, e in enumerate(input) if i and e > input[i-1]])


def answer2(input):
    return answer1([sum(e) for e in [input[i:i+3] for i in range(len(input))][:-2]])
