#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations

from readData import Sizes, X, C, V
from evaluate import evaluate


def allocate(list_videos):
    available_size = [X for _ in range(C)]
    solution = defaultdict(list)
    for id, video in enumerate(list_videos):
        resp_cache = id % C
        if available_size[resp_cache] > Sizes[video]:
            solution[resp_cache].append(video)
            available_size[resp_cache] -= Sizes[video]
    return solution


def bruteForce():
    best_score = float("+inf")
    best_solution = None
    for l in permutations([i for i in range(V)]):
        solution = allocate(list(l))
        score = evaluate(solution)
        if score > best_score:
            best_solution = solution
    return best_score, best_solution


score, solution = bruteForce()
print(score)
print(solution)