class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def LCA(root, n1, n2):
	if root == None:
		return False

	if (root.data > n1 and root.data > n2):
		return LCA(root.left, n1, n2)

	if (root.data < n1 and root.data < n2):
		return LCA(root.right, n1, n2)

	return root.data

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
print("LCA(10, 14): ", LCA(root, 10, 14))
print("LCA(10, 22): ", LCA(root, 10, 22))
print("LCA(10, 25): ", LCA(root, 10, 25))