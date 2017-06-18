'''
Given an array of tickets(start, destination)
[('SF', 'NY'), ('SJ', 'Chicago'), ('Chicago', 'LA'), ('NY', 'SJ')]
Find the order of which the tickets were used by this person

result:
SF -> NY -> SJ -> Chicago -> LA


Hint: ask me but try to look into the pattern. As you ask me more hints, it will lower your chance!

Square
'''
# create_graph builds a graph, string as a key and list of strings as a value.
def create_graph(tickets: list):
    graph = dict()
    
    for ticket in tickets:
        src,dst = ticket
        if src in graph:
            graph[src].append(dst)
        else:
            graph[src] = [dst]
    return graph

# get_start will get a starting node. Starting node must not exist in destinations. 
def get_start(graph: dict, tickets: list):
    cands = set()
    for ticket in tickets:
        dst = ticket[1]
        cands.add(dst)
    
    for ticket in tickets:
        src = ticket[0]
        if src not in cands:
            return src
    return None

def get_end(graph: dict, tickets: list):
    cands = set()
    for ticket in tickets:
        src = ticket[0]
        cands.add(src)
    
    for ticket in tickets:
        dst = ticket[1]
        if dst not in cands:
            return dst
    return None

def dfs(graph: dict, start: str, end: str, path: str, visited: set):
    # base case
    if start == end:
        return path + end
    
    if start not in visited:
        visited.add(start)
        for edge in graph[start]:
            if edge not in visited:
                temp = path+start+'->'
                path = dfs(graph, edge, end, temp, visited)
                if path:
                  return path
        visited.remove(start)
    return ''
                


def Solution(tickets: list):
    graph = create_graph(tickets)
    start = get_start(graph, tickets)
    end = get_end(graph, tickets)
    if not(start) or not(end):
        return print('Graph is incorrect')
    print(start,end,graph)
    return dfs(graph, start, end, '', set())


tickets = [('SF', 'NY'), ('SJ', 'Chicago'), ('Chicago', 'LA'), ('NY', 'SJ')]
print(Solution(tickets))