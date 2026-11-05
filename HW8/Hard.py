#Chat Prompts
# 2. Write a Python function that takes a NetworkX graph as input and returns the number of nodes 
#  in the graph that have a degree greater than 5
#  Please explain to me what it means by "degree greater than 5"
#Then I had it give me an example of what making a large graph looks like so I could see what the 
#  syntax would be

import networkx as nx

counter = 0

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

for node in G.nodes:
    if  G.degree[node] > 5:
        counter += 1

print(f"There are {counter} nodes with a degree greater than five")