G = {'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''}

def kahn(G):
    inDegree = {}
    for node in G:
        inDegree[node] = 0
    for node in G:
        for neighbor in G[node]:
            inDegree[neighbor] += 1

    res = []
    temp = []
    for node in inDegree:
        if inDegree[node] == 0:
            temp.append(node)

    while temp:
        node = temp.pop()
        res.append(node)
        for neighbor in G[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                temp.append(neighbor)
        # del G[node]
    return res


print(kahn(G))
