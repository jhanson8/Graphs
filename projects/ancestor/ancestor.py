from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)

    #BFS
    q = Queue()
    q.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if len(path) >= longest_path_length:
            if current_node < earliest_ancestor:
                longest_path_length = len(path)
                earliest_ancestor = current_node

        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = g.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            q.enqueue(path_copy)

    return earliest_ancestor