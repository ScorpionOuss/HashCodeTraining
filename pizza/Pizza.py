from collections import defaultdict, deque
import heapq
from copy import copy, deepcopy

class Graph:

    def __init__(self, edges=None):
        """
        Constructor
        We can initialize the graph with the given edges
        """
        self.edges = defaultdict(set)
        for origin, destination in edges:
            self.edges[origin].add(destination)
            self.edges[destination].add(origin)

    def maxClique(self):
        """
        Returns the size of the max Clique
        """

        maxClique = set()
        currClique = set()
        
        def recursiveElimination(currVertices):
            nonlocal maxClique
            print(currClique)
            while currVertices:
                minElement = currVertices.pop()
                # Add
                currClique.add(minElement)

                # Max

                maxClique = max(maxClique, copy(currClique), key=len)
                
                recursiveElimination(currVertices.intersection(self.edges[minElement]))
                
                #Remove
                currClique.remove(minElement)
            
        currSet = set(self.edges.keys())

        recursiveElimination(currSet)
        
        return maxClique


    def add(self, vertex):
        """
        Adding a vertex to the graph
        0(1)
        """
        self.edges[vertex[0]].add(vertex[1])

edges = [(1, 2), (2, 3), (3, 4), (2, 4)]
exampleGraph = Graph(edges)
print(exampleGraph.edges)

print(exampleGraph.maxClique())