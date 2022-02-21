import random
import networkx as nx
import matplotlib.pyplot as plt

from itertools import combinations, groupby

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False) -> list[tuple[int, int]]:
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi
    graph, but enforcing that the resulting graph is conneted
    """

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))

    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)

    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,10)

    if draw:
        plt.figure(figsize=(10,6))
        nx.draw(G, node_color='lightblue',
            with_labels=True,
            node_size=500)

    return G

G = gnp_random_connected_graph(10,0.5,False)
print(G.edges)
print(G.number_of_nodes())
print(list(G.adj[0]))
# S = nx.to_numpy_matrix(G)
# S[0][0] = 1
# print(S)