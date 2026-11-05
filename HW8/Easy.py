##Chat Prompts:
#how do you take a networkx graph as an input in python? I just did this one to make sure I wasn't 
# supposed to be importing some premade graph

import networkx as nx

G = nx.Graph()
G.add_nodes_from(range(1,13))
G.add_edges_from([
    (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
    (2, 3), (2, 4), (2, 5), (2, 8), (2, 9),
    (3, 4), (3, 5), (3, 6), (3, 10),
    (4, 5), (4, 6), (4, 7), (4, 11),
    (5, 6), (5, 8), (5, 12),
    (6, 7), (6, 9),
    (7, 8),
    (8, 9),
    (9, 10)
    ])

print(f"There are {G.number_of_nodes()} nodes in this graph")
