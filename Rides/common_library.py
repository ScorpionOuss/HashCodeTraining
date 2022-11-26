#!/usr/bin/env python

def evaluate(allocations: list[list[Ride]]):
    total_score = 0
    for rides in allocations:
        car_score = 0
        car_pos = (0, 0)
        timestamp = 0
        for ride in rides:
            timestamp += abs(car_pos[0] - ride.a) + abs(car_pos[1] - ride.b)
            on_time = timestamp == ride.s
            timestamp += abs(ride.a - ride.x) + abs(ride.b - ride.y)
            if timestamp < T:
                car_score += 1 + int(on_time) * B
            else:
                break
        total_score += car_score
    return car_score
        
