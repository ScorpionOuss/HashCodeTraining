#!/usr/bin/env python3

from common_library import Rides, R, C, F, N, B, T

distance = 0
for ride in Rides:
    distance += ride.distance
print(distance/N  )
