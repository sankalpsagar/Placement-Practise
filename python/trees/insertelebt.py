class node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

	def inorder(self, temp):
		if not temp:
			return

		self.inorder(temp.left)
		print(temp.val, end=" ")
		self.inorder(temp.right)

	def insert(self, data, temp):
		queue = []
		queue.append(temp)

		while (len(queue)):
			t = queue.pop(0)
			if not t.left:
				t.left = node(data)
				break
			else:
				queue.append(t.left)

			if not t.right:
				t.right = node(data)
				break
			else:
				queue.append(t.right)

if __name__ == '__main__': 
	root = node(10)  
	root.left = node(11)  
	root.left.left = node(7)  
	root.right = node(9)  
	root.right.left = node(15)  
	root.right.right = node(8)  

	print("Inorder traversal before insertion:", end = " ") 
	root.inorder(root)  

	key = 12
	root.insert(key, root)  

	print()  
	print("Inorder traversal after insertion:", end = " ") 
	root.inorder(root) 
	print()
  

