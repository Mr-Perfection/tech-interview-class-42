'''
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
'''
# create_graph takes edges in which each edge contains (src, dest, cost)
def create_graph(edges):
    graph = dict()

    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append((edge[1], edge[2]))
        else:
            graph[edge[0]] = [(edge[1], edge[2])]
    
    return graph

# dijkstra function uses BFS and priority queue to find the shortest path between start and end.
# I use pop() for my queue because my queue is sorted in reverse order.
# This could've instead implemented using pop(0) or dequeue() operation with queue sorted in order.
def dijkstra(graph, start, end):
    # initial start with (cost, node, path)
    # visited set() to mark visited nodes
    queue = [(0, start, '')]
    visited = set()

    while queue:
        cost, node, path = queue.pop() # destructured element
        if node not in visited:
            visited.add(node)
            if node == end:
                return cost, path+node
            else:
                path += node + '->'
            
            for adj in graph[node]:
                if adj[0] not in visited:
                    # add adj. node's cost to cost and pass in dest. node and path
                    # the reason why I am not adding path + dest. node is that
                    # if..else conditions above will handle the path 
                    queue.append((cost+adj[1], adj[0], path))
            queue.sorted(reverse=True)
    return 0, 'Path does not exist'

### TEST
# Given with edges between vertices, find the shortest path.
# Try out with different inputs inside edges.
edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]
graph = create_graph(edges)
print(dijkstra(graph, 'A','E'))
