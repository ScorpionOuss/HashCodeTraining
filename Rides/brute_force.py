#!/usr/bin/env python3


 


def evaluate(solution):
    return 0

def find_optimum(fleets, rides, T, B):
    """
    Return the optimal solution using the brute force approach
    """
    current_solution = None

    fleets_list = [[]for _ in range(fleets)]
    def recursive_enumeration(r):
        if r == len(rides):
            test_score = evaluate(fleets_list)
            # May need a copy
            current_solution = max(current_solution, fleets_list, key = evaluate)
        for i in range(fleets):
            fleets_list[i].append(rides[r])
            recursive_enumeration(r+1)
            fleets_list[i].pop()

    return