from readData import Request
from readData import Endpoints, Requests, Sizes, X


def is_valid(solution: dict):
    """
    Checks if videos fit in the caches 
    """
    for videos in solution.values():
        s = sum(Sizes[video] for video in videos)
        if s > X:
            return False
    return True


def get_lowest_latency(request: Request, solution: dict):
    """

    """
    endpoint = Endpoints[request.idEndpoint]
    latencies = []
    for connection in endpoint.cacheConnections:
        if request.idVideo in solution.get(connection.id, []):
            latencies.append(connection.latency)
        else:
            latencies.append(float("+inf"))

    return min(endpoint.latencyDC, min(latencies)) if len(latencies) != 0 else endpoint.latencyDC


def evaluate(solution):
    assert is_valid(solution), "Solution invalid"
    total_latency = 0
    total_requests = 0
    for request in Requests:
        l = get_lowest_latency(request, solution)
        total_latency += request.numReq * (Endpoints[request.idEndpoint].latencyDC - l)
        total_requests += request.numReqi

    return round(total_latency * 1000 / total_requests)
