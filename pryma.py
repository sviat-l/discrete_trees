
from math import inf
graph = [[]]

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
def pryma_alg2(graph):
    num_vertixes = len(graph)
    result = []
    # initialyze
    used = [False] * num_vertixes
    used[0] = 1
    for _ in range(num_vertixes):
        minimal = inf
        for i,j, weight in graph:
            if used[i]^used[j]:
                if  minimal < weight:
                    current_pair = (i,j)
                    minimal = graph[i][j]
            used[i], used[j] = True, True
        result.append(current_pair)
    return result


# min heap O(E*log(V))
import heapq
def prims3(graph):
    results = []
    number_of_vertixes = len(graph)
    used = [False]*number_of_vertixes
    used [0] = True
    edges = [(weight, 0, node)
        for node, weight in graph[0].items()]
    heapq.heapify(edges)
    wei = 0
    while edges:
        weight, i, j = heapq.heappop(edges)
        if not used[j]:
            used[j] = True
            wei += weight
            results.append((i,j,weight))
            for x, weight in graph[j].items():
                if not used[x]:
                    heapq.heappush(edges, (weight, j, x))

    return results, wei


def prims4(graph):
    results = []
    number_of_vertixes = len(graph)
    used = [False]*number_of_vertixes
    used [0] = True
    edges = [(weight, 0, node)  for node, weight in enumerate(graph[0]) if graph[0][node]]
    heapq.heapify(edges)
    wei = 0
    while edges:
        weight, i, j = heapq.heappop(edges)
        if not used[j]:
            used[j] = True
            wei += weight
            results.append((i,j,weight))
            for k, weight in enumerate(graph[j]):
                if not used[k]:
                    heapq.heappush(edges, (weight, j, k))
    return results, wei


G = {1: {2: 2, 3: 3},
    2: {1: 2, 3: 1, 4: 1, 5: 4},
    3: {1: 3, 2: 1, 6: 5},
    4: {2: 1, 5: 1},
    5: {2: 4, 4: 1, 6: 1},
    6: {3: 5, 5: 1, 0: 1},
    0: {6: 1},}
print(prims3(G))