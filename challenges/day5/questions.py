from collections import defaultdict

def overlap(input: str, diagonal: bool = False):
    with open(input) as inp:
        inputs = [
            [tuple([int(e) for e in coords.split(',')]) for coords in line] for line in
            [line.split(' -> ') for line in inp.read().split('\n')]
        ]
    crossover = defaultdict(int)
    for line in inputs:
        start, end = line
        x1, y1, x2, y2 = list(start) + list(end)
        if x1 == x2:
            for c in range(min(y1, y2), max(y1, y2)+1):
                crossover[(x1, c)] += 1
        elif y1 == y2:
            for c in range(min(x1, x2), max(x1, x2)+1):
                crossover[(c, y1)] += 1
        elif diagonal:
            x = list(range(min(x1, x2), max(x1, x2)+1))
            y = list(range(min(y1, y2), max(y1, y2)+1))
            if x1 > x2 and y1 < y2:
                zipped = list(zip(x[::-1],y))
            elif x1 < x2 and y1 > y2:
                zipped = list(zip(x, y[::-1]))
            else:
                zipped = list(zip(x, y))
            for coord in zipped:
                crossover[coord] += 1
    return len([c for c,v in crossover.items() if v >= 2])

example_1 = overlap('example.txt')
crossover_1 = overlap('input.txt')

example_2 = overlap('example.txt', diagonal=True)
crossover_2 = overlap('input.txt', diagonal=True)
