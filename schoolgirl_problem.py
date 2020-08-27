""" Here I will write a program to solve the general version of Kirkman's Schoolgirl Problem
https://en.wikipedia.org/wiki/Kirkman%27s_schoolgirl_problem """

import numpy as np
from itertools import permutations, combinations
import string
import time
import math
import datetime


class KirkmanSolver:
    def __init__(self, num_girls = 6, group_size = 2, use_full_names = False):
        self.num_girls = num_girls
        self.group_size = group_size
        self.girls = list(string.ascii_uppercase[:num_girls])
        self.possible = (n - 1) // (g - 1) == (n - 1) / (g - 1)
        self.num_days = (n - 1) // (g - 1)
        self.pairs = list(combinations(girls, 2))

    @staticmethod
    def nCr(n,r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)

    def generate_groups(self):
        pass

    def generate_days(self):
        pass

    def print_hello_world(self):
        self.hello_world = 'hello world!'
        print(self.hello_world)



if __name__ == '__main__':
    print(KirkmanSolver().pairs)