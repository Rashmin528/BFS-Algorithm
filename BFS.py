graph = {'A': ['B','C'],
         'B': ['D','E','A'],
         'C': ['F','G','A'],
         'D': ['B'],
         'E': ['B','H'],
         'F': ['C'],
         'G': ['C'],
         'H': ['E']}

def bfs(graph, start):
    visited = []
    queue = [start]
 
    while queue:
        node = queue.pop(0)
        if node not in visited:
	    visited.extend(node)
            neighbours = graph[node]
 
            for neighbour in neighbours:
                queue.extend(neighbour)
    return visited
 
print(bfs(graph,'A'))
