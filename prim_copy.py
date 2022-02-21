"""
Module to draw the minimum cost spanning tree of the graph set by the networkx Graph using
In this module is one function prim_mst which returns the minimum spanning tree of the graph
"""

import heapq
import networkx as nx


def prim_mst(graph: nx.Graph):
    """
    Find and return graph (the tree) with tha minimum spanning tree of the graph
    By using of the prim's algoritm
    :graph - networkx Graph object
    Return: tree with minimum edge costs of the set graph
    """
    number_of_vertixes = graph.number_of_nodes()
    # create an emthy networkx graph to store results
    tree = nx.Graph()
#     print(graph.edges(0,data='weig
    tree.add_nodes_from(range(number_of_vertixes))
    # change the graph into format of dictionary with dictioanary
    # ex.: {'A': {'B: {'weight': 1}, 'C': {'weight': 5}...}, 'B'...}
    edges = [edge[::-1] for edge in graph.edges(0,data='weight')]
    # initiate list with bool value that show wheather the node was used
    # set the value for
    used = [True] + [False]*(number_of_vertixes-1)
    # create edge_list with edges that has at least one used node
    # make it into binary tree
    heapq.heapify(edges)
    # do while there are still edges with one
    while edges:
        weight, new_node, prev_node = heapq.heappop(edges)
        # cheack wheather node on the other side of edge was used
        # (if current edge is valid)
        if not used[new_node]:
            # change value in used list ot the new_node
            used[new_node] = True
            # add the edge to the ansver graph
            tree.add_edge(prev_node, new_node, weight=weight)
            # iterate on edges that are incident to the new node
            # a heaped date with potentialy valid edges
            for _,nxt,weigt  in graph.edges(new_node, data='weight'):
                # add edges that has one used node and one not used (at the present time)
                # to the heap dataset with potentialy valid edges
                if not used[nxt]:
                    heapq.heappush( edges, (weigt, nxt, new_node))
    return tree
