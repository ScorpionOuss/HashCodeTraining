from readData import Request
from readData import Endpoints, Requests, Sizes, X


def is_valid(solution: dict):
    for videos in solution.values():
        s = sum(Sizes[video] for video in videos)
        if s > X:
            return False
    return True


def get_lowest_latency(request: Request, solution: dict):
    endpoint = Endpoints[request.idEndpoint]
    latencies = []
    for connection in endpoint.cacheConnections:
        if request.idVideo in solution.get(connection.id, []):
            latencies.append(connection.latency)
        else:
            latencies.append(float("+inf"))
    return min(endpoint.latencyDC, latencies)


def evaluate(solution):
    assert is_valid(solution), "Solution invalid"
    total_latency = 0
    for id, request in enumerate(Requests):
        l = get_lowest_latency(id, solution)
        total_latency += request.numReq * (l - Endpoints[request.idEndpoint].latencyDC)
    return round(total_latency * 1000 / len(Requests))