```py

# DFS is called Depth first search.
# It is implemented as typical Tree Traversal (pre-order, in-order, and post-order)
# Also, it is implemented as Graph Traversal (using Stack). 
def pre_order(root):
    if not root:
        return
    pre_order(root.left)
    print(root.val)
    pre_order(root.right)

def in_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if not root:
        return
    pre_order(root.left)
    pre_order(root.right)
    print(root.val)

# Let's say you have a graph...
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['E'],
         'E': ['F', 'C', 'B'],
         'F': ['C']}

# this is graph traversal.
def DFS(graph, start, end):
    stack = [start]
    path, visited = '', set()
    while stack:
        el = stack.pop()
        if el not in visited:
            if el == end:
                path += el
                return path
            path += el + '->'
            visited.add(el)
            for node in graph[el]:
                if node not in visited:
                    stack.append(node)
    return 'Destination is unreachable'

# modified version.
def DFS_modified(graph, src, dest, visited, path):

    # if src becomes dest, return path
    if src == dest:
        return path + dest
    
    if src not in visited:
        visited.add(src)
        for node in graph[src]:
            if node not in visited:
                sol = DFS_modified(graph, node, dest, visited, path + src + '->')
                if sol:
                    return sol
        visited.remove(src)
    return None

print(DFS(graph, 'A', 'F'))
ret = DFS_modified(graph, 'A', 'F', set(), '')
if ret:
    print(ret)
else:
    print('Path does not exist!')

# Output:
# A->C->D->K->E->B->F
# A->B->C->D->E->F

# Try to understand the difference between DFS and DFS_modified. Both serve different purposes.
# test it out in https://repl.it/languages/python3

```