def bfs_iterative(graph, start):
	queue =  [start] 
	visited = []

	while queue:
		vertex = queue.pop(0)
		if vertex in visited:
			continue
		visited.append(vertex)
		for neighbor in graph[vertex]:
			queue.append(neighbor)

	return visited

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(bfs_iterative(adjacency_matrix, 1))

#python3 bfs_non_recursive.py
