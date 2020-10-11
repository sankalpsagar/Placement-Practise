from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = [[0 for x in range(V)] for y in range(V)]

	def addEdge(self, s, d):
		self.graph[s-1][d-1] = 1

	def printEdges(self):
		print()
		print("Printing Edges: ")
		for i in range(self.V):
			for j in range(self.V):
				if (self.graph[i][j] == 1):
					print("Edge: {}->{}".format(i+1, j+1))

if __name__ == '__main__':
 	v = int(input("Enter number of nodes: "))
 	g = Graph(v)
 	n = int(input("Enter number of edges: ")) 
 	for i in range(n):
 		print("Enter i, j: ")
 		i, j = map(int, input().split())
 		g.addEdge(i, j)
 		print("Inserted {}->{}".format(i, j))
 	g.printEdges()