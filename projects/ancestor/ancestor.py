from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    #setting up/buildling the graph 
    g = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        #add vertices and edges 
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)

    #BFS
    q = Queue()
    q.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    #while the queue is not empty 
    while q.size() > 0:
        #dequeue the current path
        path = q.dequeue()
        current_node = path[-1]

        #will return smaller value if there are equal values 
        if len(path) >= longest_path_length:
            if current_node < earliest_ancestor:
                longest_path_length = len(path)
                earliest_ancestor = current_node
        
        #keep track of the longest path
        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = g.vertices[current_node]
        for ancestor in neighbors:
            # copy the path
            path_copy = list(path)
            #append the ancestor
            path_copy.append(ancestor)
            q.enqueue(path_copy)

    return earliest_ancestor