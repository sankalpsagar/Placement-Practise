class node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

	def print(self):
		print("\t{}".format(self.val))
		print("/\t\t\\")
		print("{}\t\t{}".format(self.left.val, self.right.val))
		print("Data: {}. Left: {}. Right: {}.".format(self.val, self.left.val, self.right.val))

if __name__ == '__main__':
	root = node(1)
	left = node(2)
	right = node(3)
	root.left = left
	root.right = right
	root.print()