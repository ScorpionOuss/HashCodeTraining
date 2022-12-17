from readData import Endpoints, Requests


def get_lowest_latency(request, solution):
    endpoint = Endpoints[request.idEndpoint]
    latencies = []
    for connection in endpoint.cacheConnections:
        if request.video in solution.get(connection.id, []):
            latencies.append(connection.latency)
        else:
            latencies.append(float("+inf"))
    return min(endpoint.latencyDC, latencies)

def evaluate(solution):
    total_latency = 0
    for id, request in enumerate(Requests):
        l = get_lowest_latency(id, solution)
        total_latency += request.numReq * (l - Endpoints[request.idEndpoint].latencyDC)
    return round(total_latency * 1000 / len(Requests))
