""" Here I will write a program to solve the general version of Kirkman's Schoolgirl Problem
https://en.wikipedia.org/wiki/Kirkman%27s_schoolgirl_problem """

import numpy as np
from itertools import permutations, combinations
import string
import time
import math
import datetime


class KirkmanSolver:
    def __init__(self, num_girls=6, group_size=2, use_full_names=False):
        self.start_time = time.time()
        self.num_girls = num_girls
        self.group_size = group_size
        self.names = {
            'A': 'Abigail',
            'B': 'Belle',
            'C': 'Crystal',
            'D': 'Delilah',
            'E': 'Emma',
            'F': 'Felicia',
            'G': 'Gabrielle',
            'H': 'Harmony',
            'I': 'Iris',
            'J': 'Jasmine',
            'K': 'Kayleigh',
            'L': 'Liliana',
            'M': 'Megan',
            'N': 'Nadia',
            'O': 'Olivia',
            'P': 'Priscilla',
            'Q': 'Quinn',
            'R': 'Renee',
            'S': 'Samantha',
            'T': 'Tiffany',
            'U': 'Uma',
            'V': 'Victoria',
            'W': 'Wendy',
            'X': 'Xenia',
            'Y': 'Yasmine',
            'Z': 'Zoe'}
        self.girls = list(string.ascii_uppercase[:num_girls])
        if use_full_names:
            self.girls = [self.names[girl] for girl in self.girls]
        self.possible = (self.num_girls - 1) // (self.group_size - 1) == (
            self.num_girls - 1) / (self.group_size - 1)
        self.num_days = (self.num_girls - 1) // (self.group_size - 1)
        self.pairs = list(combinations(self.girls, 2))
        self.groups = list(combinations(self.girls, self.group_size))
        self.days = [day for day in combinations(self.groups, self.num_girls // self.group_size) if set(
            girl for group in day for girl in group) == set(self.girls)]
        self.num_poss_sol = self.nCr(len(self.days), self.num_days)
        self.solutions = []
        self.end_time = 0
        self.total_time = 0


    @staticmethod
    def nCr(n, r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)

    def print_hello_world(self):
        self.hello_world = 'hello world!'
        print(self.hello_world)

    @staticmethod
    def print_all_things(object):
        print('*' * 100)
        for i, x in enumerate(object, 1):
            print(f'{i}: {x}')
        print('*' * 100)

    def solve(self):
        for i, solution in enumerate(combinations(self.days, self.num_days)):
            if i%(10**6) == 0 and i > 1:
                print(f'Checking solution #{i:,}')
                times_elapsed = time.time() - self.start_time
                time_remaining = (times_elapsed) * (1 - (i / self.num_poss_sol)) ** (-1)
                print(f'At this rate, it will take {datetime.timedelta(seconds = time_remaining)} more seconds to complete this program')
                print()
            
            all_groups = list(group for day in solution for group in day)
            pair_counts = {}
            for pair in self.pairs:
                count = 0
                for group in all_groups:
                    if pair in list(combinations(group, 2)):
                        count += 1
                pair_counts[pair] = count
            if np.all([count == 1 for count in pair_counts.values()]):
                self.solutions.append(solution)

        if not self.solutions:
            print(f'There happen to be no solutions for {self.num_girls} girls and group size {self.group_size}.')
        else:
            print(f'Here are the solutions for {self.num_girls} girls and group size {self.group_size}.')
            print()
            for i, solution in enumerate(self.solutions, 1):
                print(f'Solution #{i}')
                for j, day in enumerate(solution, 1):
                    print(f'Day #{j}')
                    print(day)
                print()

        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        print(f'time elapsed: {self.total_time:.4}s')

    def solve2(self):
        """ This time try solving it using pair counts in each day.
        Maybe partition by pair counts."""
        pass


if __name__ == '__main__':
    solve = KirkmanSolver(num_girls=9, group_size=3)
    solve.solve()
