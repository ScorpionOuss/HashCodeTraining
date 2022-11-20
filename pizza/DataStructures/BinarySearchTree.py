
from collections import deque
from random import randint


class Node:
    
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Tree:

    def __init__(self, val):
        self.root = Node(val)
    
    def add(self, val):
        """
        Add an element to the binary search tree
        """
        curr = self.root
        while (curr.val <= val and curr.right) or (curr.val > val and curr.left):
            if curr.val <= val:
                curr = curr.right
            else:
                curr = curr.left
        if curr.val <= val:
            curr.right = Node(val)
        else:
            curr.left = Node(val)
    
    def bfs(self):
        "Breath first traversal"
        queue = deque([self.root])

        while queue:
            curr = queue.pop()
            print(curr.val)
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)


list_nums = [randint(0, 20) for _ in range(10)]

print(list_nums)
testTree =  Tree(10)

for val in list_nums:
    testTree.add(val)

testTree.bfs()