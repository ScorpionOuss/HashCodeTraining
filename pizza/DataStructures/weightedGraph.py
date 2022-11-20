from collections import defaultdict
import heapq

class Graph:

    def __init__(self, edges=None):
        self.edges = defaultdict(set)
        self.vertices = set()
        for origin, destination, cost in edges:
            self.edges[origin].add((destination, cost))
            self.vertices.update((origin, destination))
    
    def addEdge(self, edge):
        """
        Adding an edge to the graph
        """
        self.edges[edge[0]].add((edge[1], edge[2]))
        self.vertices.update((edge[0], edge[1]))
    
    def removeEdge(self, edge):
        if self.search(edge):
            self.edges[edge[0]].remove((edge[1], edge[2]))
            return 1
        return 0
    
    def search(self, edge):
        return (edge[1], edge[2]) in self.edges[edge[0]]
    

    def dijkstra(self, origin, destination):
        """
        Returns the cost of the shortest path following Dijkstar Algorithm
        The constraint is that there is no negative weights
        """
        nextNodes = [(0, origin)]
        heapq.heapify(nextNodes)
        visited = set()

        while nextNodes:
            currCost, curr = heapq.heappop(nextNodes)
            if curr == destination:
                return currCost
            if curr in visited:
                continue
            visited.add(curr)
            for node, weight in self.edges[curr]:
                if node not in visited:
                    heapq.heappush(nextNodes, (weight + currCost, node))
        return  -1

    def bellmanFord(self, origin, destination):
        """
        Find the cost associated to the shortest path
        from the origin to the destination
        """
        # We can initialize map with values: 0 for the origin and +inf for the other and do the propagation V times
        costs = {x:float('inf') for x in self.vertices}
        costs[origin] = 0

        for _ in range(len(self.vertices)):
            # print(costs)
            for origin in self.edges:
                for dest, cost in self.edges[origin]:
                    costs[dest] = min(costs[dest], cost + costs[origin])
                    # print("origin: ", origin, " costOrigin: ", costs[origin], " destination: ", destination, " costTransition: ", cost, " decided for destination : ", costs[destination])
        return costs[destination]


edges = [(1, 2, 1), (1, 3, 3), (2, 4, 2), (4, 6, 2), (3, 5, 3), (5, 7, 2), (3, 7, 2), (7, 8, 1)]
exampleGraph = Graph(edges)
print(exampleGraph.edges)
exampleGraph.addEdge((6, 7, 3))
print(exampleGraph.edges)
print("Dijkstra: ", exampleGraph.dijkstra(1, 5))
print(exampleGraph.vertices)
print("BellmanFord: ", exampleGraph.bellmanFord(1, 5))
