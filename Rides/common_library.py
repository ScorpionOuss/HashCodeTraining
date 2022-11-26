#!/usr/bin/env python
R=0
C=0
F=0
N=0
B=0
T=0
Rides=[]


class ride:
    def __init__(self, a, b, x, y, s, f):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.distance = abs(x-a)+abs(y-b)
        self.latest_start= f-self.distance

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
        Rides.append(ride(line[0],line[1],line[2],line[3],line[4],line[5]))

