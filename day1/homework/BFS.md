```py
# BFS or Breadth First Search 
# it is level order tree traversal for binary trees. http://www.geeksforgeeks.org/?p=2686
# Mostly it is used in Graph (Graph is a data structure similar to hash table. Google it.
# BFS uses queue(). As opposed to stack(), queue() is First In First Out. 

# Let's say you have a graph...
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['E'],
         'E': ['F', 'C', 'B'],
         'F': ['C']}
# Time complexity: O(V + E), v is a number of vertexes or nodes and E is a number of adj. nodes.
def BFS(graph, start, end):
    queue = [start]
    visited = set()
    while queue:
        el = queue.pop(0) # dequeue or pop first element
        if el not in visited:
            visited.add(el)
            queue.append(el)
            for adj in graph[el]:
                if adj not in visited:
                    queue.append(el)

# Later on, we will explore Dijkstra algorithm 
#(http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/)
```

