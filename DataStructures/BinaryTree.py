from collections import deque

class Node:

    def __init__(self, val):
        """
        Constructor
        """
        self.val = val
        self.right = None
        self.left = None
    
    def inOrderDFS(self):
        """
        Recursive dfs
        """
        print(self.val)
        if self.left:
            self.left.inOrderDFS()
        if self.right:
            self.right.inOrderDFS()
        

    def preOrderDFS(self):
        """
        PreOrder DFS
        """
        if self.left:
            self.left.preOrderDFS()
        print(self.val)
        if self.right:
            self.right.preOrderDFS()
        

    def postOrderDFS(self):
        """
        PostOrder DFSs
        """
        if self.left:
            self.left.postOrderDFS()
        if self.right:
            self.right.postOrderDFS()
        print(self.val)


class Tree:

    def __init__(self, root):
        self.root = root
        # self.num_node = 1 


    def insertInRow(self, val):
        """
        Inserting the value at the first vacant place
        in a breadth first traversal
        """
        queue = deque([self.root])
        while queue:
            curr = queue.pop()
            if not curr.left:
                curr.left = Node(val)
                return
            if not curr.right:
                curr.right = Node(val)
                return 
            queue.appendleft(curr.left)
            queue.appendleft(curr.right)
        raise Exception

    def bfs(self):
        """
        Breadth first serach traversal
        """
        print("Starting BFS:")
        queue = deque([self.root])
        while queue:
            curr = queue.pop()
            print(curr.val)
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)
        print("End")
    

    def dfs(self):
        """
        Iterative version of the in-order DFS algorithm
        [In order to have it in the tree class in stead of 
        have a recursive impelementation in the Node class]
        """
        print("Starting DFS:")
        stack = [self.root]

        while stack:
            curr = stack.pop()
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        print("End")

    def PreItDFS(self):
        """
        Iterative PreOrder DFS
        """
        print("Iterative PreOrder: ")
        stack = []
        curr = self.root
        while curr or stack:
            if not curr:
                curr = stack.pop()
                print(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left


    def postIterativeDFS(self):
        """
        Post order DFS iterative algorithm
        """
        print("Post Iterative DFS")
        stack = []
        curr = self.root

        while curr or stack:
            if not curr:
                curr, finished = stack.pop()
                if finished:
                    print(curr.val)
                    curr = None
                else:
                    stack.append((curr, True))
                    curr = curr.right
            else:
                stack.append((curr, False))
                curr = curr.left
        


    def inOrderDFS(self):
        self.root.inOrderDFS()

    def postOrderDFS(self):
        self.root.postOrderDFS()
    
    def preOrderDFS(self):
        self.root.preOrderDFS()


tree1 = Tree(Node(0))

for i in range(1, 10):
    tree1.insertInRow(i)

tree1.bfs()
tree1.dfs()
print("IN order DFS:")
tree1.inOrderDFS()
print("Post Order DFS:")
tree1.postOrderDFS()
print("Pre Order DFS:")
tree1.preOrderDFS()

tree1.PreItDFS()
tree1.postIterativeDFS()
# Then start inserting

# The question is How to construct a tree from a list?
# Question about tree construction: I will do it later


# The other increment is to do all the dfs iteratively