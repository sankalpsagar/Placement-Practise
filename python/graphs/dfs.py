from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, s, d):
		self.graph[s].append(d)

	def dfs(self, s, visited):
		stack = []
		stack.append(s)

		visited[s] == True
		while len(stack):
			s = stack.pop()
			if visited[s]:
				continue

			visited[s] = True
			print(s, end =" ")

			for i in self.graph[s]:
				if visited[i] == False:
					stack.append(i)

if __name__ == '__main__':
	g = Graph(4) 
	g.addEdge(0, 1) 
	g.addEdge(0, 2) 
	g.addEdge(1, 2) 
	g.addEdge(2, 0) 
	g.addEdge(2, 3) 
	g.addEdge(3, 3)

	visited = [False]*4 
  
	print("Following is DFS from (starting from vertex 2)") 
	g.dfs(2, visited) 
	print()
