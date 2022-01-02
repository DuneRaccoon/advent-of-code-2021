from typing import List
from collections import defaultdict


class Board(object):

    def __init__(self, positions: list):
        self.positions = positions
        self.number_to_position = {
            k: (x, y) for x in range(len(self.positions))
            for y, k in enumerate(self.positions[x])
        }
        self.called = []
        self.bingo = False

    def __repr__(self):
        return '\n'.join([' '.join(l) for l in self.positions])

    def call_draw(self, number: str):
        has_number = self.number_to_position.get(number)
        if has_number:
            self.called.append(has_number)
            x, y = has_number
            self.positions[x][y] = f"{number}*"

    def is_bingo(self):
        horizontal = defaultdict(list)
        vertical = defaultdict(list)
        for call in self.called:
            horizontal[call[0]].append(call[1])
            vertical[call[1]].append(call[0])
        self.bingo = any(sorted(list(val)) == list(range(5)) for val in horizontal.values())\
            or any(sorted(list(val)) == list(range(5)) for val in vertical.values())
        return self.bingo

    def final_score(self, winning_number: str):
        unmarked = [
            int(val) for line in self.positions for val in line
            if val not in [
                self.positions[marked[0]][marked[1]] for marked in self.called
            ]
        ]
        return sum(unmarked) * int(winning_number)


with open('input.txt') as file:
    input = file.read().split('\n\n')
    draws = input[0].split(',')
    boards = [Board([[_ for _ in e.split(' ') if _]
                    for e in b.split('\n')]) for b in input[1:]]


def get_first_win(draws: list, boards: List[Board]):
    for draw in draws:
        for board in boards:
            board.call_draw(draw)
            if not board.bingo:
                if board.is_bingo():
                    # print(f'BINGO!\n\n{board}')
                    return board.final_score(draw)


def get_last_win(draws: list, boards: List[Board]):
    wins = []
    for draw in draws:
        for board in boards:
            if board in [w[0] for w in wins]:
                continue
            board.call_draw(draw)
            if not board.bingo:
                if board.is_bingo():
                    # print(f'BINGO!\n\n{board}')
                    wins.append((board, board.final_score(draw)))
    return wins[-1]
