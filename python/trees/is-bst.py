# check if tree is bst
import sys

class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.val = val

def is_bst(root, min_value = -(sys.maxsize - 1), max_value = sys.maxsize):
	if root == None:
		return True

	if root.val < min_value or root.val > max_value:
		return False

	return is_bst(root.left, min_value, root.val-1) and is_bst(root.right, root.val+1, max_value)

root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (is_bst(root)): 
    print("Is BST")
else: 
    print("Not a BST")

root = Node(4) 
root.left = Node(5) 
root.right = Node(2) 
root.left.left = Node(1) 
root.left.right = Node(3) 

if (is_bst(root)): 
    print("Is BST")
else: 
    print("Not a BST")