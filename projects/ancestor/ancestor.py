
def earliest_ancestor(ancestors, starting_node):
    
    ancestors = reverse_graph(ancestors)
    print(ancestors)
    graph = {}
    for edge in ancestors:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

    print(graph)

    if starting_node not in graph:
        return -1

    q = []
    q.append([starting_node])

    paths = []

    # path = [[starting_node]]
    while len(q)> 0:
        path = q.pop()
        node = path[-1]

        if node in graph:

            for i in graph[node]:
                new_path = list(path)
                new_path.append(i)
                q.append(new_path)
        else:
            paths.append(path)
    
    print(paths)

    longer_path = {}
    for path in paths:
        if len(path) not in longer_path:
            longer_path[len(path)] = path
        elif path[-1] < longer_path[len(path)][-1]:
            longer_path[len(path)] = path
    
    print(longer_path)

    return longer_path[max(longer_path)][-1]



def reverse_graph(ancestors):
    reverse = []
    for i in ancestors:
        reverse.append((i[1],i[0]))
    return reverse