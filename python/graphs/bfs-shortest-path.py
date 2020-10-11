from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, s, d):
		# undirected graph, so add edge both ways
		self.graph[s].append(d)
		self.graph[d].append(s)

	def bfslength(self, s):
		queue = []
		visited = [False]*self.V
		level = [0]*self.V
		paths = {}
		paths[s] = [s]
		# print(paths)

		queue.append(s)
		while(len(queue)):
			src = queue.pop(0)
			visited[src] = True

			for i in self.graph[src]:
				if visited[i] == False:
					paths[i] = paths[src] + [i]
					# print(paths)
					visited[i] = True
					level[i] = 1 + level[src]
					queue.append(i)

		# check if all nodes reached
		for i in range(self.V):
			if i not in paths:
				paths[i] = [-1]

		return level, paths

if __name__ == '__main__':
	g = Graph(8)
	g.addEdge(0,3)
	g.addEdge(1,2)
	g.addEdge(3,4)
	g.addEdge(3,7)
	g.addEdge(4,5)
	g.addEdge(4,6)
	g.addEdge(4,7)
	g.addEdge(5,6)
	g.addEdge(6,7)
	dist, paths = g.bfslength(0)
	for i in range(g.V):
		print("Distance from {} for {}: {}".format(0, i, dist[i]))
		print("Path: {}".format(paths[i]))