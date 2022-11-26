#!/usr/bin/env python3

R = 0  # number of rows of the grid
C = 0  # number of columns of the grid
F = 0  # number of vehicles in the fleet
N = 0  # number of rides
B = 0  # per-ride bonus for starting the ride on time
T = 0  # number of steps in the simulation
Rides = []  # list of rides


class Ride:
    def __init__(self, a, b, x, y, s, f):
        self.a = a  # the row of the start intersection
        self.b = b  # the column of the start intersection
        self.x = x  # the row of the finish intersection
        self.y = y  # the column of the finish intersection
        self.s = s  # the earliest start
        self.f = f  # the latest finish
        self.distance = abs(x - a) + abs(y - b)
        self.latest_start = f - self.distance

    def distance_to_start(self, x, y):
        """ returns the distance of the start from x,y (can be car coordinates)"""
        return abs(self.a - x) + abs(self.b - y)


def read_input():
    global R
    global C
    global F
    global N
    global B
    global T
    global Rides
    line1 = [int(i) for i in input().split()]
    R = line1[0]
    C = line1[1]
    F = line1[2]
    N = line1[3]
    B = line1[4]
    T = line1[5]
    for _ in range(N):
        line = [int(i) for i in input().split()]
        Rides.append(Ride(line[0], line[1], line[2], line[3], line[4], line[5]))


def evaluate(allocations: list[list[Ride]]):
    total_score = 0
    for rides in allocations:
        car_score = 0
        car_pos = (0, 0)
        timestamp = 0
        for ride in rides:
            timestamp += ride.distance_to_start(*car_pos)
            on_time = timestamp == ride.s
            timestamp += timestamp - ride.s
            timestamp += ride.distance
            car_pos = (ride.x, ride.y)
            if timestamp < T:
                car_score += 1 + int(on_time) * B
            else:
                break
        total_score += car_score
    return total_score
        

read_input()
