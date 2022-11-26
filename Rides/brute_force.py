#!/usr/bin/env python3
from common_library import Rides, R, C, F, N, B, T
from common_library import evaluate
from copy import deepcopy

# R = 0  # number of rows of the grid
# C = 0  # number of columns of the grid
# F = 0  # number of vehicles in the fleet
# N = 0  # number of rides
# B = 0  # per-ride bonus for starting the ride on time
# T = 0  # number of steps in the simulation
# Rides = []  # list of rides


def find_optimum():
    """
    Return the optimal solution using the brute force approach
    """
    current_solution = None
    current_score = 0

    fleets_list = [[]for _ in range(F)]
    def recursive_enumeration(r):
        if r == N:
            test_score = evaluate(fleets_list)
            # May need a copy
            if test_score > current_score:
                current_solution = deepcopy(fleets_list)
        for i in range(F):
            fleets_list[i].append(Rides[r])
            # A first evaluation Here
            # What would be the suitabke data structure.
            
            # if not validate(fleets_list):
            #     pass

            # N = 10
            # F1 = 3 (1)
            # F2 = 4 (2)
            # F3 = 4 (2)

            recursive_enumeration(r+1)
            fleets_list[i].pop()
    
    recursive_enumeration(0)
    return current_solution