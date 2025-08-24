class Tree(): 
    def __init__(self) -> None:
        self.root = None
        self.vertex_cnt = 0
        self.daepth = 0
    
    def addnode(self, node, parents): 
        if self.root == None: 
            self.root = node
        else: 
            parent = self.root
            while 
    
    def preorder_find(self, find_data): 
        stack = []
        cur = self.root
        if cur.data == find_data: 
            return cur
        while True: 
            stack.append(cur)
            cur = cur.left
            if cur.data == find_data

class Node(): 
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def preorder_find

N = int(input())