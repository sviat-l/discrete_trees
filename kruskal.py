"""
Module to draw the minimum cost spanning tree of the graph set by the networkx Graph using kruskal algorythm
In this module is one function kruskal_mst which returns the minimum spanning tree of the graph
"""
import networkx as nx


def kruskal_mst(graph: nx.Graph) -> nx.Graph:
    def find_class(node):
        """
        return class of the node
        """
        # find class of the node while index
        while node != classes[node]:
            # change node to its 'parent' node
            node = classes[node]
        return node

    def union(i_class: int, j_class: int) -> None:
        """
        unite two classes of the nodes
        """
        # check which level of tree is more
        # add tree of the lower level to the tree of the higher
        if level[i_class] > level[j_class]:
            classes[j_class] = i_class
        else:
            classes[i_class] = j_class
            # if two tree levels are equel change one of the levele
            if level[i_class] == level[j_class]:
                level[j_class] += 1

    number_of_vertixes = graph.number_of_nodes()
    # initialize starting classes (each node in the other set/class)
    classes = {i: i for i in range(number_of_vertixes)}
    # initialize starting level of each class(tree) equal to 0
    level = {i: 0 for i in range(number_of_vertixes)}
    # create ansver graph, add nodes
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))
    # sort edges by its
    edges = sorted(graph.edges.data('weight'), key=lambda edge: edge[2])
    # iterate for edges
    for cur_edge in edges:
        # stop if we already created a tree
        if number_of_vertixes == 1:
            break
        # get new edge min cost frome the list of sorted edges
        i, j, weigt = cur_edge
        # find classes for each point and compare them
        i_class, j_class = find_class(i), find_class(j)
        # if nodes are not in the sama set/class
        if i_class != j_class:
            number_of_vertixes -= 1
            # add edge to the ansver graph
            tree.add_edge(i, j, weight=weigt)
            # unite two classes
            union(i_class, j_class)
    return tree
