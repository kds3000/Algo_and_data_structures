"""Реализация поиска кратчайшего расстояния между вершинами взвешенного графа с помощью Алгоритма Дейкстры"""
from collections import deque

edges = ['h k 16', 'a h 16', 'h e 19', 'a b 8', 'e i 14', 'b f 18', 'i f 13',
         'f d 9', 'f j 6', 'i l 7', 'j l 13', 'j c 11', 'c g 6', 'j g 17'
         ]


def get_weighted_graph(edge_list):
    """
    Converts list of weighted edges to dict of adjacencies
    :param edge_list: ['a b 2', 'b c 4', 'b a 3']
    :return:          {'a': {'b': 3}, 'b': {'a': 3, 'c': 4}, 'c': {'b': 4}}
    """
    graph = dict()

    for edge in edge_list:
        v1, v2, weight = edge.split()
        weight = int(weight)
        if v1 not in graph:
            graph[v1] = dict()
        if v2 not in graph:
            graph[v2] = dict()
        graph[v1][v2] = weight
        graph[v2][v1] = weight

    return graph


def dijkstra(start, finish, graph, distances=dict(), queue=None):
    """
    Calculates costs of ways to all possible vertexes
    :param start:      start vertex
    :param finish:     finish vertex
    :param graph:      graph we working with (dict of adjacencies)
    :param distances:  dict of costs of ways to all possible vertexes
    :param queue:      support queue
    :return:           dict of costs of ways to all possible vertexes
    """
    if queue is None:
        queue = deque(start)
        distances[start] = 0

    # contain way cost to all neighbour vertexes
    start_vertex = graph[start]
    for neighbour in start_vertex:
        if neighbour not in distances or distances[neighbour] > distances[start] + start_vertex[neighbour]:
            distances[neighbour] = distances[start] + start_vertex[neighbour]
            queue.append(neighbour)

    while queue:
        start = queue.popleft()
        dijkstra(start, finish, graph, distances, queue)

    return distances


def restore_way(finish, graph, distances):
    """
    Restores shortest way from start to finish with edges costs
    :param finish:     finish vertex
    :param graph:      graph we working with (dict of adjacencies)
    :param distances:  dict of costs of ways to all possible vertexes
    :return:           shortest way from start to finish with edges costs. For example 'gc6 cj11 jf6 fb18 ba8 ah16'
    """
    way = ''
    distance = distances[finish]
    while distance > 0:
        for neighbour in graph[finish]:
            if distance == graph[finish][neighbour] + distances[neighbour]:
                way += '{}{}{} '.format(finish, neighbour, graph[finish][neighbour])
                distance -= graph[finish][neighbour]
                finish = neighbour
                break
    return way


if __name__ == "__main__":
    graph1 = get_weighted_graph(edges)
    d = dijkstra('h', 'g', graph1)
    w = restore_way('g', graph1, d)
    print(w)