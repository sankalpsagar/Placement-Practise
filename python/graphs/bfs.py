from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, s, d):
		self.graph[s].append(d)

	def bfs(self, s, visited):
		queue = []
		queue.append(s)
		visited[s] = True
		# print(visited)

		while len(queue):
			s = queue.pop(0)
			print(s, end = "")

			for i in self.graph[s]:
				if visited[i] == False:
					visited[i] = True
					queue.append(i)

			print()

if __name__ == '__main__':
	g = Graph(4) 
	g.addEdge(0, 1) 
	g.addEdge(0, 2) 
	g.addEdge(1, 2) 
	g.addEdge(2, 0) 
	g.addEdge(2, 3) 
	g.addEdge(3, 3) 

	visited = [False]*4

	print("Following is Breadth First Traversal (starting from vertex 2)") 
	g.bfs(2, visited) 

