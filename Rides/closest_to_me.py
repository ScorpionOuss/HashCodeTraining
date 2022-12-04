#!/usr/bin/env python3

from common_library import Rides, distance, R, C, F, N, B, T
from common_library import evaluate
Rides.sort(key=lambda x: x.a*x.b) # this only improves the algorithm
def choose_next(actual_ride, discovered,from0):
    min_ride = actual_ride
    min_dist = float("inf")
    min_distmult = float("inf")
    for ride in Rides:
        if ride not in discovered:
            d = distance(actual_ride, ride)
            if from0:
                return ride     
            # return  ride, d
            if d+1000 // ride.distance < min_distmult:
                min_ride = ride
                min_dist = d
                min_distmult= d+1000 //ride.distance
    return min_ride, min_dist


scheduel = [[] for _ in range(F)]
actual_ride = Rides[0]
discovered = {actual_ride}
total_distance = actual_ride.distance_to_start(0, 0)
while len(discovered) < N:
    print(total_distance)
    next_ride, distance_to_ride = choose_next(actual_ride, discovered)
    discovered.add(next_ride)
    total_distance += distance_to_ride + next_ride.distance
    carNumber = total_distance // T
    if carNumber >= F:
        break
    print(carNumber)
    scheduel[carNumber].append(next_ride)

print(evaluate(scheduel))
