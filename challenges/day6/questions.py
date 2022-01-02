with open('example.txt') as inp:
    all_fish = [int(e) for e in inp.read().split(',')]

class memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not str(args) in self.memo:
            self.memo[str(args)] = self.f(*args)
        return self.memo[str(args)]

def reproduce(all_fish: list):
    return_fish = []
    for fish in all_fish:
        if fish == 0:
            return_fish.append(6)
            return_fish.append(8)
        else:
            return_fish.append(fish - 1)
    return return_fish

@memoize
def lantern_fish(all_fish: str, num_days: int):
    
    if not num_days:
        return all_fish

    return lantern_fish(reproduce(all_fish), num_days-1)
