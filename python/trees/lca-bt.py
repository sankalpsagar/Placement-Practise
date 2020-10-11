class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.val = val

def LCAUtil(root, key, path):
	if root == None:
		return False

	path.append(root.val)

	if root.val == key:
		print("Path for {}: ".format(key), path)
		return True

	if (root.right != None and LCAUtil(root.right, key, path)) or (root.left != None and LCAUtil(root.left, key, path)):
		return True

	path.pop()
	return False

def LCA (root, n1, n2):
	path1 = []
	path2 = []

	if (not LCAUtil(root, n1, path1)) or (not LCAUtil(root, n2, path2)):
		return -1

	i = 0
	while i < len(path1) and i < len(path2):
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
print("LCA(4,5) = ", LCA(root, 4, 5))
print("LCA(3,4) = ", LCA(root, 3, 4))