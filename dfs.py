graph1 = {
   '0' : ['1','2','3','4'],
    '1' : ['0','5'],
    '2' : ['0','5'],
    '3' : ['0','6'],
    '4' : ['0','6',],
    '5' : ['1','2','7'],
    '6' : ['3','4','7'],
    '7' : ['5','6'],
 
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'0', [])
print(visited)