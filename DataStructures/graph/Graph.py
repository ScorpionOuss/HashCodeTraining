from collections import defaultdict, deque
import heapq

class Graph:

    def __init__(self, edges=None):
        """
        Constructor
        We can initialize the graph with the given edges
        """
        self.edges = defaultdict(set)
        for origin, destination in edges:
            self.edges[origin].add(destination)
            # self.edges[destination].append(origin)
    

    def add(self, vertex):
        """
        Adding a vertex to the graph
        0(1)
        """
        self.edges[vertex[0]].add(vertex[1])
    
    def delete(self, vertex):
        """
        Deletes the vertex if it exists, in which case returns 1
        otherwise returns 0
        0(1)
        """
        if self.search(vertex):
            self.edges[vertex[0]].remove(vertex[1])
            return 
        return 0

    def search(self, vertex):
        """
        Search if the vertex exists in the graph
        """
        return vertex[1] in self.edges[vertex[0]]

    def recursiveDfs(self, node):
        """
        Recursive DFS traversal
        (From a given node?)
        """

        print("Recursive DFS")
        visited = set()

        def recursiveDFS(node):
            if node in visited:
                return
            print(node)
            for adjacent in self.edges[node]:
                if adjacent not in visited:
                    recursiveDFS(adjacent)
        
        recursiveDFS(node)


    def iterativeDfs(self, node):
        """
        Iterative DFS traversal
        """
        print("Iterative DFS")
        stack = [node]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            print(curr)
            for adjacent in self.edges[curr]:
                if adjacent not in visited:
                    stack.append(adjacent)

    def bfs(self, node):
        """
        Breadth first search traversal
        """
        print("BFS traversal")
        queue = deque([node])
        visited = set()
        while queue:
            curr = queue.pop()
            if curr in visited:
                continue
            visited.add(curr)
            print(curr)
            for adjacent in self.edges[curr]:
                if adjacent not in visited:
                    queue.appendleft(adjacent)


    def hasPath(self, origin, destination):
        """
        Returns True if there is a path from the origin to the destination
        """
        queue = [origin]
        visited = set()
        while queue:
            curr = queue.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for adjacent in self.edges[curr]:
                if adjacent == destination:
                    return True
                if adjacent not in visited:
                    queue.append(adjacent)
        return False



    def cyclicDependency(self):
        """
        Detects if there is any cyclic dependency in the graph
        """
        visited = set()
        backtrack = set()


        def dfs(node):
            if node in backtrack:
                return True
            if node in visited:
                return False
            backtrack.add(node)
            visited.add(node)
            for adjacent in self.edges[node]:
                if dfs(adjacent):
                    return True
            backtrack.remove(node)
            return False

        for node in self.edges:
            if node not in visited:
                if dfs(node):
                    return True
        return False


edges = [(1, 2), (2, 4), (4, 6), (1, 3), (3, 5), (3, 7), (5, 7)]
exampleGraph = Graph(edges)
print(exampleGraph.edges)
exampleGraph.add((7, 8))
print(exampleGraph.edges)
exampleGraph.delete((3, 7))
print(exampleGraph.edges)
print(exampleGraph.search((4, 6)))
exampleGraph.recursiveDfs(1)
exampleGraph.iterativeDfs(1)
exampleGraph.bfs(1)

print(exampleGraph.hasPath(1, 8))
print(exampleGraph.hasPath(2, 8))

print("Cyclic dependency?: ", exampleGraph.cyclicDependency())
exampleGraph.add((4, 1))
print("Cyclic dependency?: ", exampleGraph.cyclicDependency())