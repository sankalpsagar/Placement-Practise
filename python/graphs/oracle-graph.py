# given nodes edges
# given paths arrays
# find if path possible, if no print last node it got stuck on
from collections import defaultdict
graph = defaultdict(list)

def bfs(v, graph, s, d):
	print("Source: ", s)
	print("Destination: ", d)
	visited = [False] * v
	q = []
	q.append(s)

	while(q):
		s = q.pop(0)
		# print(s)
		visited[s] = True

		for j in graph[s]:
			if visited[j] == False:
				q.append(j) 

	if visited[d] == False:
		return -1
	return 1

def addEdge(graph, u, v):
	graph[u].append(v)
	graph[v].append(u)

Nodes = [0, 1, 2, 3, 4, 5]
v = len(Nodes)
paths = [[0,1], [1,2], [2,3], [4,1]]
path = [0, 1, 2, 3]
path2 = [1, 2, 4, 5]

for i in paths:
	addEdge(graph, i[0], i[1])
	print("Added edge: ", graph)

for i in range(len(path)-1):
	res = bfs(v, graph, path[i], path[i+1])
	if res == -1:
		print("Traversal stopped at: ", path[i])
	if i == len(path)-2 and res == 1:
		print("Yes")

for i in range(len(path2)-1):
	res = bfs(v, graph, path2[i], path2[i+1])
	if res == -1:
		print("Traversal stopped at: ", path2[i])
	if i == len(path2)-2 and res == 1:
		print("Yes")