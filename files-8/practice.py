class Node:
   def __init__(self, key):
       self.left = None
       self.right = None
       self.val = key
class BST:
   def __init__(self):
       self.root = None
   def insert(self, key):
       new_node = Node(key)
      
       if self.root is None:
           self.root = new_node
           return
      
       current = self.root
       parent = None


       while current is not None:
           parent = current
           if key < current.val:
               current = current.left
           else:
               current = current.right


       if key < parent.val:
           parent.left = new_node
       else:
           parent.right = new_node
   def inorder(self, node):
       if node:
           self.inorder(node.left)
           print(node.val, end=" ")
           self.inorder(node.right)
if __name__ == "__main__":
   bst = BST()


   elements = [50, 30, 20, 40, 70, 60, 80]
   for elem in elements:
       bst.insert(elem)
  
   print("in-order traversal")
   bst.inorder(bst.root)
   print()


