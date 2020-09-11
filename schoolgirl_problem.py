""" Here I will write a program to solve the general version of Kirkman's Schoolgirl Problem
https://en.wikipedia.org/wiki/Kirkman%27s_schoolgirl_problem """

from schoolgirl_solver.solver import full_solve

for n in range(2, 16):
    for g in range(2, n + 1):
        print(n, g)
        full_solve(n, g)