#!/usr/bin/env python3

from common_library import Rides, distance, R, C, F, N, B, T
from common_library import evaluate

Rides.sort(key=lambda ride1: ride1.s)

schedule = [[] for _ in range(F)]
time_stamp = [0 for _ in range(F)]
car_position = [(0, 0) for _ in range(F)]
i = 0

for ride in Rides:
    schedule[i % F].append(ride)
    time_stamp[i % F] = max(ride.distance_to_start(car_position[i % F][0], car_position[i % F][1]),
                            ride.s) + ride.distance
    car_position[i % F] = (ride.x, ride.y)
    i += 1
    if i % F == 0:
        schedule = [x for _, _, x in sorted(zip(time_stamp, [i for i in range(F)], schedule))]
        # schedule.sort(key=lambda car: car[-1].s + car[-1].distance) both give the same result that is less than the upper bound

print(evaluate(schedule))
