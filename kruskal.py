import random
from unittest import result
import networkx as nx
import matplotlib.pyplot as plt

from itertools import combinations, groupby


# O(VE)
def kruskal1(graph):
    def union(i,j, dct, lst):
        class2 = lst[j]
        for x in dct[class2]:
            lst[x] = lst[i]
        dct[lst[i]] |= dct.pop(class2)
        return dct, lst

    graph = sorted(graph, key=lambda edge: edge[2])
    number_of_vertixes = 0
    node_classes = [i for i in range(number_of_vertixes)]
    classes_nodes = {i:{i} for i in range(number_of_vertixes)}
    ind = 0
    tree = []
    while number_of_vertixes > 1:
        i, j, w = graph[ind]
        if node_classes[i] != node_classes[j]:
            number_of_vertixes -= 1
            tree.append((i,j,w))
            if i > j:
                classes_nodes, node_classes = union(i,j, classes_nodes, node_classes)
            else:
                classes_nodes, node_classes = union(j,i, classes_nodes, node_classes)
        ind+=1
    return tree

def kruskal1_0(graph):
    def find_class(node):
        return node if node_classes[node] == node else find_class(node_classes[node])
    graph = sorted(graph, key=lambda edge: edge[2])
    number_of_vertixes = 0
    node_classes = [i for i in range(number_of_vertixes)]
    ind = 0
    tree = []
    while number_of_vertixes > 1:
        i, j, _ = graph[ind]
        i_class = find_class(i)
        j_class = find_class(j)
        if i_class != j_class:
            number_of_vertixes -= 1
            tree.append(graph[ind])
            if i > j:
                node_classes[i] = j_class
            else:
                node_classes[j] = i_class
        ind+=1
    return tree



def kruskal2(graph):
    num_nodes = graph.number_of_nodes()
    classes = {i:i for i in range(num_nodes)}
    level = {i:0 for i in range(num_nodes)}
    result = []

    def find_class(node):
        return node if classes[node] == node else find_class(classes[node])

    def union(i_class, j_class):
        if level[i_class] > level[j_class]:
            classes[j_class] = i_class
        else:
            classes[i_class] = j_class
            if level[i_class] == level[j_class]:
                level[j_class]+=1

    edges = sorted(graph.weighted_edges(), key= lambda edge:edge[2])
    ind = 0
    while num_nodes > 1:
        i,j, _ = edges[ind]
        i_class = find_class(i)
        j_class = find_class(j)
        if i_class != j_class:
            num_nodes -= 1
            result.append(edges[ind])
            union(i_class, j_class)
        ind += 1
