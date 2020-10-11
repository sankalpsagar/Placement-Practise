class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.val = val

def inorder(root):
	# go to leftmost node while pushing to stack, when no left is available pop and print it and then go to right node and continue
	stack = []
	current = root

	while True:
		if current is not None:
			stack.append(current)
			current = current.left

		elif len(stack):
			current = stack.pop()
			print(current.val, end = " ")
			current = current.right

		else:
			break

	print()

def preorder(root):
	# print root go left most, print and then go right most and print
	
	if root is None:
		return

	stack = []
	current = root
	stack.append(current)

	while len(stack):
		current = stack.pop()
		print(current.val, end = " ")

		if current.right is not None:
			stack.append(current.right)

		if current.left is not None:
			stack.append(current.left)

	print()

def postorder(root):
	if root is None:
		return

	s1 = []
	s2 = []
	current = root
	s1.append(current)

	while s1:
		current = s1.pop()
		s2.append(current)
		if current.left:
			s1.append(current.left)
		if current.right:
			s1.append(current.right)

	while s2:
		current = s2.pop()
		print(current.val, end = " ")

	print()

def levelorder(root):
	# basically bfs for trees
	if root is None:
		return

	queue = []
	queue.append(root)

	while queue:
		s = queue.pop(0)
		print(s.val, end = " ")

		if s.left:
			queue.append(s.left)

		if s.right:
			queue.append(s.right)

	print()

# driver
# tree:
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 

print("Preorder: ")
preorder(root)
print("Inorder: ")
inorder(root)
print("Postorder: ")
postorder(root)
print("Levelorder: ")
levelorder(root)