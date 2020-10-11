class node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def inorder(temp):
	if not temp:
		return

	inorder(temp.left)
	print(temp.val, end=" ")
	inorder(temp.right)

def delete_deepest(root, d_node):
	queue = []
	queue.append(root)
	while(len(queue)):
		temp = queue.pop(0)
		if temp is d_node:
			temp = None
			return
		if temp.right:
			if temp.right is d_node:
				# print(temp.val)
				temp.right = None
				return
			else:
				queue.append(temp.right)

		if temp.left:
			if temp.left is d_node:
				# print(temp.val)
				temp.left = None
				return
			else:
				queue.append(temp.left)

def deletion(root, key):
	# print(key)
	if root == None:
		# print("none")
		return None
	if root.left == None and root.right == None:
		if root.val == key:
			# print("oops")
			return None
		else:
			return root

	key_node = None
	queue = []
	# print("queue")
	queue.append(root)

	while(len(queue)):
		temp = queue.pop(0)
		# print(temp.val)
		if temp.val == key:
			key_node = temp
		if temp.left:
			queue.append(temp.left)
			# print(queue)
		if temp.right:
			queue.append(temp.right)
			# print(queue)
	if key_node:
		x = temp.val
		# if it is d_node delete it
		# if it is some other node find
		# deepest node and delete it
		delete_deepest(root, temp)
		key_node.val = x

	return root


if __name__=='__main__': 
	root = node(10) 
	root.left = node(11) 
	root.left.left = node(7) 
	root.left.right = node(12) 
	root.right = node(9) 
	root.right.left = node(15) 
	root.right.right = node(8) 
	print("The tree before the deletion:") 
	inorder(root) 
	key = 11
	root = deletion(root, key) 
	print() 
	print("The tree after the deletion:") 
	inorder(root) 
	print()