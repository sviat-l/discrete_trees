
from math import inf
import networkx as nx

# matrix O(E^2)
def pryma_alg1(graph):
    graph = [[x if x!=0 else inf for x in edges] for edges in graph]
    num_vertixes = len(graph)
    result = []
    # initialyze
    used = [False] * num_vertixes
    used[0] = 1
    for _ in range(num_vertixes-1):
        minimal = inf
        for i in range(num_vertixes):
            if used[i]:
                for j in range(num_vertixes):
                    if not (used[j] or i==j) and minimal < graph[i][j]:
                        current_pair = (i,j)
                        minimal = graph[i][j]
        used[current_pair[1]] = True
        result.append(current_pair)
    return result

# list edge O(E^2)
def pryma_alg2(graph:nx.Graph):
    number_of_vertixes = graph.number_of_nodes()
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))
    # initialyze
    used = [True] + [False] * (number_of_vertixes - 1)
    for _ in range(number_of_vertixes):
        minimal = inf
        for i,j, w in graph:
            if used[i]^used[j]:
                if  minimal < w:
                    x,y = (i,j)
                    minimal = graph[i][j]
            used[i], used[j] = True, True
        tree.add_weighted_edges_from(x , y,  weight=w)
    return tree


# min heap O(E*log(V)) dict with dict
import heapq
def prims3(graph:nx.Graph):
    number_of_vertixes = graph.number_of_nodes()
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))
    nx.to_dict_of_dicts(graph)
    used = [True] + [False]*(number_of_vertixes-1)
    edges = [(dct['weight'], 0, node) for node, dct in graph[0].items()]
    heapq.heapify(edges)
    while edges:
        weight, prev, cur = heapq.heappop(edges)
        if not used[cur]:
            used[cur] = True
            tree.add_edge(prev, cur, weight=weight)
            for foll, dct in graph[cur].items():
                if not used[foll]:
                    heapq.heappush(edges, (dct['weight'], cur, foll))
    return tree

# min heap O(E*log(V)) matrix
def prims4(graph:nx.Graph):
    number_of_vertixes = graph.number_of_nodes()
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))
    used = [True] + [False]*(number_of_vertixes-1)
    edges = [(weight, 0, node)  for node, weight in enumerate(graph[0]) if graph[0][node]]
    heapq.heapify(edges)
    while edges:
        weight, i, j = heapq.heappop(edges)
        if not used[j]:
            used[j] = True
            tree.add_weighted_edges_from(i,j)
            for k, weight in enumerate(graph[j]):
                if not used[k]:
                    heapq.heappush(edges, (weight, j, k))
    return tree


def prim_5(graph: nx.Graph):
    number_of_vertixes = graph.number_of_nodes()
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))
    edges = [edge[::-1] for edge in graph.edges(0,data='weight')]
    used = [True] + [False]*(number_of_vertixes-1)
    heapq.heapify(edges)
    while edges:
        weight, new_node, prev_node = heapq.heappop(edges)
        if not used[new_node]:
            used[new_node] = True
            tree.add_edge(prev_node, new_node, weight=weight)
            for _,nxt,weigt  in graph.edges(new_node, data='weight'):
                if not used[nxt]:
                    heapq.heappush( edges, (weigt, nxt, new_node))
    return tree
