#!/usr/bin/env python3

from common_library import Rides, distance, R, C, F, N, B, T
from common_library import evaluate

Rides.sort(key=lambda x: x.a * x.b)  # this only improves the algorithm


def choose_ride(car_position, total_distance):
    remaining_rides = list(filter(
        lambda ride: ride not in USED_RIDES, Rides))
    if not remaining_rides:
        return None
    return min(remaining_rides,
               key=lambda ride: (max(ride.s - total_distance + ride.distance_to_start(car_position[0],
                                                                                      car_position[1])-500, 0),
                                 -ride.distance / (
                                         ride.distance_to_start(car_position[0], car_position[1]) + ride.distance))) #todo can improve to take both into account at the same time


schedule = []
USED_RIDES = set()
for carNumber in range(F):
    print(carNumber)
    car_position = (0, 0)
    travel_distance = 0
    rides = []
    distance_between = 0
    while True:  # TODO there is some bugs the filter is too harsh
        next_ride = choose_ride(car_position, travel_distance)
        if not next_ride:
            break
        travel_distance += next_ride.distance_to_start(car_position[0], car_position[1])
        travel_distance += max(0, next_ride.s - travel_distance) + next_ride.distance
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
