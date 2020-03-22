"""Реализация поиска в ширину.
Решение задачи по восстановлению кратчайшей траектории шахматного коня.
"""
from collections import deque
from DFS import get_graph

EDGES = ['h k', 'a h', 'h e', 'a b', 'e i', 'b f', 'i f', 'f d', 'f j', 'i l', 'j l', 'j c', 'c g', 'j g']


def get_checkmate_deck():
    """
    Generate 2d checkmate_deck (list of lists)
    :return: [['8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h'],
              ...
              ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h']]
    """
    rows = '87654321'
    columns = 'abcdefgh'
    deck = [[''] * 8 for _ in range(8)]
    for row in range(8):
        for column in range(8):
            deck[row][column] = rows[row] + columns[column]
    return deck


def add_horse_available_fields(graph, deck, start_row, start_column, checked_fields):
    """
    Constructs a graph using checkmate horse moving concept. Recursively adds available for horse moving fields.
    :param graph: graph we work with (dict of adjacencies)
    :param deck: checkmate deck abstraction (list of lists with field names)
    :param start_row: index of row of start field
    :param start_column: index of column of start field
    :param checked_fields: set of already checked fields
    """
    def get_new_position(row_delta, column_delta):
        """
        Nested function that adds deltas to current position. Returns new position (position after one horse step).
        :param row_delta: row position change
        :param column_delta: column position change
        :return: tuple of (new_row_index, new_column_index)
        """
        new_row = start_row - row_delta
        new_column = start_column + column_delta
        return new_row, new_column

    start = deck[start_row][start_column]
    if start in checked_fields:
        return
    checked_fields.add(start)

    # Horse can move only in relative positions from list_of_deltas
    list_of_deltas = [(1, -2), (2, -1), (2, 1), (1, 2),
                      (-1, 2), (-2, -1), (-2, 1), (-1, -2)
                      ]

    for i in range(len(list_of_deltas)):
        delta_row = list_of_deltas[i][0]
        delta_column = list_of_deltas[i][1]
        tmp_row, tmp_column = get_new_position(delta_row, delta_column)

        # new position can not be beyond checkmate deck boundaries
        if 0 <= tmp_row <= 7 and 0 <= tmp_column <= 7:
            finish = deck[tmp_row][tmp_column]
            graph[start].add(finish)
            # repeats until all available fields checked
            add_horse_available_fields(graph, deck, tmp_row, tmp_column, checked_fields)


def get_checkmate_horse_graph(start_field):
    """
    Creates empty graph and fills it using add_horse_available_fields function
    :param start_field: start horse position to construct graph for. Example ['4b']
    :return:            full graph with all available horse moves
    """
    start_field_indexes = convert_field_name_to_indexes(start_field)
    row, column = start_field_indexes[0], start_field_indexes[1]
    deck = get_checkmate_deck()
    graph = dict()
    checked_fields = set()

    for row in range(len(deck)):
        for column in range(len(deck[row])):
            field = deck[row][column]
            graph[field] = set()

    add_horse_available_fields(graph, deck, row, column, checked_fields)

    return graph


def bfs(vertex, graph, distances, shortest_ways, queue=deque()):
    """
    breadth-first search recursive algorithm
    :param vertex: start vertex
    :param graph: graph we are working with
    :param distances: dict of minimal distances (in steps) from start vertex to each vertex
    :param shortest_ways: dict of shortest trajectories from start vertex to each vertex
    :param queue: support queue
    """
    if vertex not in distances:
        distances[vertex] = 0
        shortest_ways[vertex] = vertex
    for neighbour in graph[vertex]:
        if neighbour not in distances:
            queue.append(neighbour)
            distances[neighbour] = distances[vertex] + 1
            shortest_ways[neighbour] = shortest_ways[vertex] + ' ' + vertex + neighbour
    while len(queue) > 0:
        vertex = queue.popleft()
        bfs(vertex, graph, distances, shortest_ways, queue)


def find_shortest_ways_using_bfs(start_field):
    """
    Calculates shortest trajectories and minimum distances (in steps) from start field to each field
    :return: dict of shortest trajectories from start field to each field
    """
    # will contain for each field number of minimum required steps from start field to finish field
    distances = dict()
    # will contain shortest trajectories from start field to each field
    shortest_ways = dict()
    graph = get_checkmate_horse_graph(start_field)
    bfs(start_field, graph, distances, shortest_ways)
    return shortest_ways


def convert_field_name_to_indexes(field_name):
    """
    Converts string field name to a tuple of two integer indexes
    :param field_name: '4d'
    :return:           (4, 3)
    """
    rows = '87654321'
    columns = 'abcdefgh'
    row_index = column_index = None

    row_name = field_name[0]
    for i in range(8):
        if rows[i] == row_name:
            row_index = i

    column_name = field_name[1]
    for i in range(8):
        if columns[i] == column_name:
            column_index = i

    return row_index, column_index


if __name__ == '__main__':
    result = find_shortest_ways_using_bfs('4d')
    print(result['7f'])
