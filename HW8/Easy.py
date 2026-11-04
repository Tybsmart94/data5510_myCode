##Chat Prompts:
#how do you take a networkx graph as an input in python? I just did this one to make sure I wasn't 
# supposed to be importing some premade graph

import networkx as nx

G = nx.Graph()
G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])
G.add_edges_from([(1, 2), (1, 3)])

print(G.number_of_nodes())
