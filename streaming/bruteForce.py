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
    return solution


def permute(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permute(remLst):
           l.append([m] + p)
    return l


def bruteForce():
    best_score = float("+inf")
    best_solution = None
    for l in permutations([i for i in range(V)]):
        solution = allocate(list(l))
        score = evaluate(solution)
        if score < best_score:
            best_solution = solution
    return best_solution