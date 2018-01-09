# bfs, dfs

# use adjacency list to represent graph
graph = {"A": ["B", "C", "H"],
         "B": ["A", "D", "E"],
         "C": ["A", "F", "G"],
         "D": ["B", "E"],
         "E": ["A", "B", "D"],
         "F": ["C"],
         "G": ["C"],
         "H": ["A", "E"]}


# use queue and stack

def bfs_queue(graph, start):
    explored = set()
    queue = [start]
    res = []
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.add(node)
            res.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return res
print(bfs_queue(graph, "A"), "BFS with queue")


def dfs_stack(graph, start):
    explored = set()
    stack = [start]
    res = []
    while stack:
        node = stack.pop(-1)
        if node not in explored:
            explored.add(node)
            res.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                stack.append(neighbour)
    return res
print(dfs_stack(graph, "A"), "DFS with stack")


# recursively dfs
def dfs_recursive(graph, node, explored, res):
    explored.add(node)
    res.append(node)
    for neighbour in graph[node]:
        if neighbour not in explored:
            dfs_recursive(graph, neighbour, explored, res)
    return res
print(dfs_recursive(graph, "A", set(), []), "DFS with recursive method")


# find the shortest path

def bfs_shortest_path(graph, start, end):
    explored = set()
    queue = [[start]]
    res = []
    if start == end:
        return ["start is same as end point"]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    res.append(new_path)
            explored.add(node)
    return res
print(bfs_shortest_path(graph, "A", "D"), "BFS find path with queue")


def dfs_shortest_path(graph, start, end):
    explored = set()
    stack = [[start]]
    res = []
    if start == end:
        return "it's already in the end"
    while stack:
        path = stack.pop(-1)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                if neighbour == end:
                    res.append(new_path)
                explored.add(node)
    return res
print(dfs_shortest_path(graph, "A", "D"), "DFS find path with stack")


# DFS find path with recursive method
def dfs_shortest_recursive(graph, start, end, path, res, explored):
    if path == []:
        path = [start]
    if start == end:
        res.append(path)
        return
    explored.add(start)
    for neighbour in graph[start]:
        if neighbour not in explored:
            explored.add(neighbour)
            dfs_shortest_recursive(graph, neighbour, end, path+[neighbour],res, explored)
            explored.remove(neighbour)
res = []
dfs_shortest_recursive(graph, "A", "D", [], res, set())
print(res, "DFS find path with recursive method")

















