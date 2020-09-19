""" 
Solver Logic for Kirkman Schoolgirl Problem.
"""

import numpy as np
import pandas as pd
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
            self.num_girls - 1) / (self.group_size - 1) and (self.num_girls // self.group_size == self.num_girls / self.group_size)
        self.num_days = (self.num_girls -
                         1) // (self.group_size - 1) if self.possible else None
        self.pairs = list(combinations(self.girls, 2))  if self.possible else None
        self.groups = list(combinations(self.girls, self.group_size))  if self.possible else None
        self.days = [day for day in combinations(self.groups, self.num_girls // self.group_size) if set(
            girl for group in day for girl in group) == set(self.girls)]  if self.possible else None
        self.num_poss_sol = self.nCr(len(self.days), self.num_days) if self.possible else None
        self.solutions = []  if self.possible else None
        self.end_time = 0  if self.possible else None
        self.total_time = 0  if self.possible else None
        self.solution_df = pd.DataFrame(columns=[
            'num_girls',
            'group_size',
            'possible_to_solve',
            'num_days',
            'num_possible_solutions',
            'num_actual_solutions',
            'total_solve_time',
            'solution_num',
            'day_num',
            'group_num',
            'group',
            'named_group'
        ])

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
        print(f'possible? {self.possible}')
        if self.possible:

            for i, solution in enumerate(combinations(self.days, self.num_days)):
                # if i%(10**6) == 0 and i > 1:
                # print(f'Checking solution #{i:,}')
                # times_elapsed = time.time() - self.start_time
                # time_remaining = (times_elapsed) * (1 - (i / self.num_poss_sol)) ** (-1)
                # print(f'At this rate, it will take {datetime.timedelta(seconds = time_remaining)} more seconds to complete this program')
                # print()

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

            # if not self.solutions:
            #     print(f'There happen to be no solutions for {self.num_girls} girls and group size {self.group_size}.')
            # else:
            #     print(f'Here are the solutions for {self.num_girls} girls and group size {self.group_size}.')
            #     print()
            #     for i, solution in enumerate(self.solutions, 1):
            #         print(f'Solution #{i}')
            #         for j, day in enumerate(solution, 1):
            #             print(f'Day #{j}')
            #             print(day)
            #         print()

        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        print(f'time elapsed: {self.total_time:.4}s')
        print('DONE')

        if not self.possible:
            row_dict = {
                        'num_girls': self.num_girls,
                        'group_size': self.group_size,
                        'possible_to_solve': self.possible,
                        'num_days': 0,
                        'num_possible_solutions': 0,
                        'num_actual_solutions': 0,
                        'total_solve_time': np.NaN,
                        'solution_num': np.NaN,
                        'day_num': np.NaN,
                        'group_num': np.NaN,
                        'group': np.NaN,
                        'named_group': np.NaN
                    }

            self.solution_df = self.solution_df.append(
                row_dict, ignore_index=True)

        else:    
            for i, solution in enumerate(self.solutions, 1):
                for j, day in enumerate(solution, 1):
                    for k, group in enumerate(day, 1):
                        row_dict = {
                            'num_girls': self.num_girls,
                            'group_size': self.group_size,
                            'possible_to_solve': self.possible,
                            'num_days': self.num_days,
                            'num_possible_solutions': self.num_poss_sol,
                            'num_actual_solutions': len(self.solutions),
                            'total_solve_time': datetime.timedelta(seconds = self.total_time),
                            'solution_num': i,
                            'day_num': j,
                            'group_num': k,
                            'group': group,
                            'named_group': tuple([self.names[name] for name in group])
                        }

                        self.solution_df = self.solution_df.append(
                            row_dict, ignore_index=True)

    def write_solutions(self):
        try:
            old_solution_df = pd.read_csv('Kirkman_solutions.tsv', sep='\t')
            new_solution_df = pd.concat([old_solution_df, self.solution_df])
            new_solution_df.to_csv(
                'Kirkman_solutions.tsv', sep='\t', index=False)
        except:
            self.solution_df.to_csv(
                'Kirkman_solutions.tsv', sep='\t', index=False)

        solution_df = pd.read_csv('Kirkman_solutions.tsv', sep='\t')
        solution_df = solution_df.drop_duplicates(subset=[
                'num_girls',
                'group_size',
                'possible_to_solve',
                'num_days',
                'num_possible_solutions',
                'num_actual_solutions',
                'solution_num',
                'day_num',
                'group_num',
                'group',
                'named_group'
            ], keep='first', ignore_index = True)
        solution_df = solution_df.sort_values(by=[
                'num_girls',
                'group_size',
                'solution_num',
                'day_num',
                'group_num',
            ], ignore_index = True)
        solution_df.to_csv('Kirkman_solutions.tsv', sep='\t', index=False)

    def solve2(self):
        """ This time try solving it using pair counts in each day.
        Maybe partition by pair counts."""
        pass


def full_solve(num_girls, group_size):
    solver_object = KirkmanSolver(num_girls=num_girls, group_size=group_size)
    solver_object.solve()
    solver_object.write_solutions()
    return solver_object


if __name__ == '__main__':
    for n in range(2, 10):
        for g in range(2, n + 1):
            print(n, g)
            full_solve(n, g)