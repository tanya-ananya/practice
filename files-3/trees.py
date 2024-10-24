class BinaryTree:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = [None]*capacity
        self.size = 0
    def insert(self, value): #similar to list method append()
        if self.size < self.capacity:
            self.nodes[self.size] = value
            self.size += 1
            return True
        else:
            return False
    def print_tree(self):
        for i in range(self.size):
            print(self.nodes[i])

    #driver code
tree1 = BinaryTree(10)
tree1.insert('a')
tree1.insert('b')
tree1.insert('c')
tree1.insert('d')
tree1.insert('e')
tree1.insert('f')
tree1.insert('g')
tree1.insert('h')
tree1.print_tree()


class binary:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

grandchild1 = binary(4, None, None)
grandchild2 = binary(5, None, None)
child1 = binary(2, grandchild1, grandchild2)
child2 = binary(3, None, None)
parent = binary(1, child1, child2)

def traversePreOrder(node):
    print(node.value)
    if node.left != None:
        traversePreOrder(node.left)
    if node.right != None:
        traversePreOrder(node.right)