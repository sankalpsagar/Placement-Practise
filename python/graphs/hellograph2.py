from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, s, d):
		self.graph[s-1].append(d-1)

	def printForEdge(self, s):
		print(self.graph)
		print("")
		print("Printing edges for {}.".format(s))
		print("Head", end = "")
		for items in self.graph[s-1]:
				print("->{}".format(int(items)+1), end="")
		print("\nDone.")

if __name__ == '__main__':
	v, e = map(int, input("Enter number of nodes and edges: ").split())
	g = Graph(v)
	for i in range(e):
		s, d = map(int, input("Enter node1 and node2: ").split())
		g.addEdge(s, d)
	s = int(input("Enter source node to print for: "))
	g.printForEdge(s)