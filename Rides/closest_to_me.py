#!/usr/bin/env python3

from common_library import Rides, distance, R, C, F, N, B, T
from common_library import evaluate

Rides.sort(key=lambda x: x.a * x.b)  # this only improves the algorithm


def choose_ride(car_position):
    return min(filter(lambda ride: ride not in USED_RIDES, Rides),
               key=lambda ride: ride.distance_to_start(car_position[0], car_position[1]))


schedule = []
USED_RIDES = set()
for carNumber in range(F):
    print(carNumber)
    car_position = (0, 0)
    travel_distance = 0
    rides = []
    distance_between = 0
    while True:
        next_ride = choose_ride(car_position)
        if not next_ride:
            break
        travel_distance += next_ride.distance + next_ride.distance_to_start(car_position[0], car_position[1])
        if travel_distance >= T:
            break
        distance_between += next_ride.distance + next_ride.distance_to_start(car_position[0], car_position[1])
        rides.append(next_ride)
        USED_RIDES.add(next_ride)
        car_position = (next_ride.x, next_ride.y)
    schedule.append(rides)
    print(travel_distance)
    print(distance_between)

print(evaluate(schedule))
