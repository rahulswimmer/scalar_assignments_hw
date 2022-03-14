class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None

if __name__ == '__main__':
    btree = BTree(25)