#!/usr/bin/env python3
import sys


class Streaming:
    """
    Streaming class encompassing all the data
    """

    def __init__(self, v, e, r, c, x, sizes, endpoints, requests):
        self.V = v
        self.E = e
        self.R = r
        self.C = c
        self.X = x
        self.Sizes = sizes
        self.Endpoints = endpoints
        self.Requests = requests


class Endpoint:
    """
    Endpoint Description
    """

    def __init__(self, ld, k):
        self.latencyDC = ld
        self.num_caches = k
        self.cacheConnections = []

    def add_connection(self, connCache):
        """
        Adding a connections to a cache
        """
        self.cacheConnections.append(connCache)


class CacheConnection:
    """
    Connection description: Cache - Endpoint
    """

    def __init__(self, id, latency):
        self.id = id
        self.latency = latency


class Request:
    """
    Request description class
    """

    def __init__(self, rv, re, rn):
        self.idVideo = rv
        self.idEndpoint = re
        self.numReq = rn


# First line, parameters
V, E, R, C, X = map(int, input().split())

# Videos size
Sizes = list(map(int, input().split()))

Endpoints = []
# Endpoint Description
for _ in range(E):
    ld, k = map(int, input().split())
    endpoint = Endpoint(ld, k)
    for _ in range(k):
        c, lc = map(int, input().split())
        endpoint.add_connection(CacheConnection(c, lc))
    Endpoints.append(endpoint)

Requests = []
# Request Description
for _ in range(R):
    rv, re, rn = map(int, input().split())
    request = Request(rv, re, rn)
    Requests.append(request)


streaming_data = Streaming(V, E, R, C, X, Sizes, Endpoint, Requests)
