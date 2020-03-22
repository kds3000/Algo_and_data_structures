"""Реализация поиска в глубину в неориентированном графе, реализация алгоритмов поиска компонент сильной
связности (Косарайю) и топологической сортировки (Тарьяна) в ориентированном графе
"""
EDGES = ['h k', 'a h', 'h e', 'a b', 'e i', 'b f', 'i f', 'f d', 'f j', 'i l', 'j l', 'j c', 'c g', 'j g']


def get_graph(edge_list):
    """
    Converts list to dict of adjacencies of graph
    :param edge_list: ['a b', 'b c', 'b d']
    :return:          {'a': {'b'},
                      'b': {'c', 'a', 'd'},
                      'c': {'b'}, 'd': {'b'}
                      }
    """
    graph = dict()
    for edge in edge_list:
        v1, v2 = edge.split()
        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()
        graph[v1].add(v2)
        graph[v2].add(v1)
    return graph


def get_orgraph(edge_list):
    """
    Converts list to dict of adjacencies of oriented graph
    :param edge_list: ['a b', 'b c', 'b d']
    :return:          {'a': {'b'},
                       'b': {'c', 'd'},
                       'c': set(),
                       'd': set()
                       }
    """
    graph = dict()
    for edge in edge_list:
        v1, v2 = edge.split()
        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()
        graph[v1].add(v2)

    return graph


def invert_orgraph(graph):
    """
    Reverse directions in oriented graph
    :param graph: {'a': {'b'},
                   'b': {'c', 'd'},
                   'c': set(),
                   'd': set()
                   }
    :return:      {'b': {'a'},
                   'a': set(),
                   'c': {'b'},
                   'd': {'b'}
                   }
    """
    inverted = dict()
    for key in graph:
        for value in graph[key]:
            if value not in inverted:
                inverted[value] = set()
            inverted[value].add(key)
        if key not in inverted:
            inverted[key] = set()
    return inverted


def dfs(vertex, graph, used=set(), stack=[]):
    """
    DFS algorithm. It bypasses through all vertexes in certain graph. Stores vertexes to a stack.
    :param vertex: start vertex for dfs
    :param graph: dict of adjacencies
    :param used: set of already 'visited' vertexes
    :param stack: support stack that stores visited vertexes
    """
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used, stack)
    stack.append(vertex)


def kosaraju(edge_list):
    """
    Kosaraju algorithm. It searches for strongly_connected_components in oriented graph
    :param edge_list: ['a b', 'b c', 'b d', 'c a']
    :return:          [['b', 'c', 'a'], ['d']]
    """
    # visited vertexes
    used = set()
    stack = []
    graph = get_orgraph(edge_list)
    for vertex in graph:
        if vertex not in used:
            dfs(vertex, graph, used, stack)

    graph = invert_orgraph(graph)
    # strongly_connected_components
    scc = []
    used = set()
    # index of current strongly connected component
    i = 0
    while stack:
        if stack[-1] not in used:
            vertex = stack.pop()
            # appending empty list, because dfs function working only with list
            scc.append([])
            dfs(vertex, graph, used, scc[i])
            i += 1
        else:
            stack.pop()
    return scc


def partial_topological_sort(vertex, graph, used, stack):
    """
    Returns list in inverted topological order. DFS start from start vertex. Function works with graph`s part.
    :param vertex: start vertex
    :param graph:  graph we are working with
    :param used:   set of visited vertexes
    :param stack:  list that stores vertexes in inverted topological order
    :raises: AssertionError: if through DFS function visits already used vertex.
        It means there is a cycle in the graph
    """
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour in stack:
            pass
        elif neighbour not in used:
            partial_topological_sort(neighbour, graph, used, stack)
        else:
            raise AssertionError('There is a cycle in the graph')
    stack.append(vertex)


def full_topological_sort(edge_list):
    """
    Returns list in inverted topological order. Function works with full graph.
    :param edge_list: ['a b', 'b c', 'b d']
    :return:          list that stores vertexes in inverted topological order, ['c', 'd', 'b', 'a'] for example
    """
    used = set()
    stack = []
    graph = get_orgraph(edge_list)
    for vertex in graph:
        if vertex not in used:
            partial_topological_sort(vertex, graph, used, stack)
    return stack


if __name__ == '__main__':
    pass



