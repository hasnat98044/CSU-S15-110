graph = {
	'0' : ['1','2','3','4'],
	'1' : ['0','5'],
	'2' : ['0','5'],
	'3' : ['0','6'],
	'4' : ['0','6'],
	'5' : ['1','2','7'],
	'6' : ['3','4','7'],
	'7' : ['5','6'],
}

def bfs_connected_component(graph, start):
	explored = []
	queue = [start]
	levels = {}
	levels[start] = 0
	visited= [start]

	while  queue:
		node = queue.pop(0)
		explored.append(node)
		neighbours =  graph[node]
		for neighbour in neighbours:
			if neighbour not in visited:
			   queue.append(neighbour)
			   visited.append(neighbour)
			   levels[neighbour] = levels [node]+1
	print (levels)
	return explored
ans = bfs_connected_component(graph,'0')
print(ans)

