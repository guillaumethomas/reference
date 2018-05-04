'''
http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
'''


def dfs(graph, start):
    '''
    Depth-first search (DFS) is an algorithm for traversing or
    searching tree or graph data structures. One starts at the root
    (selecting some arbitrary node as the root in the case of a graph)
    and explores as far as possible along each branch before backtracking.
    '''

    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_paths(graph, start, goal):
    # use a generator
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs(graph, start):
    '''
    Breadth-first search (BFS) is an algorithm for traversing or
    searching tree or graph data structures. It starts at the
    tree root (or some arbitrary node of a graph,
    sometimes referred to as a 'search key'[1]) and
    explores the neighbor nodes first, before moving
    to the next level neighbors.
    '''
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == "__main__":

    'Adjacency list'
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    'vs Adjency Matrix'
    print(graph)
    print(dfs(graph, 'A'))
    print(list(dfs_paths(graph, 'A', 'F')))
    print(bfs(graph, 'A'))
    print(list(bfs_paths(graph, 'A', 'F')))
    print(shortest_path(graph, 'A', 'F'))
