#!/usr/bin/env python3
from common_library import Rides, F,evaluate
schedule = [[Rides[int(i)] for i in input().split()[1:]] for _ in range(F)]
print(evaluate(schedule))
