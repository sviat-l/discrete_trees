import create_graph
from networkx.algorithms import tree
import kruskal_draft
import prims_drafts
import time
import networkx as nx
import prim_copy


graph = create_graph.gnp_random_connected_graph(10, 0.01)



print(prim_copy.prim_mst(graph).edges.data('weight'))
print(sum(edge[2] for edge in prim_copy.prim_mst(graph).edges.data('weight')))
# def pr(graph:nx.Graph):
#     print(graph.edges(0,data='weight'))
# pr(graph)
# print(graph)
# print(nx.to_dict_of_dicts(graph))

# print(prim.prims3(graph).edges.data('weight'))
# st = time.time()
# print(sum(edge[2] for edge in prims_drafts.prims3(graph).edges.data('weight')))
# print(time.time() -st)

# print(dict(st_G.edges))
# print(sorted(graph.edges.data('weight'), key=lambda edge: edge[2]))

# print(kruskal.kruskal1(st_G).edges.data('weight'))
# print(kruskal.kruskal2(st_G).edges.data('weight'))
# print(kruskal.kruskal3(st_G).edges.data('weight'))

# st = time.time()
# print(sum(edge[2] for edge in kruskal_draft.kruskal1(graph).edges.data('weight')))
# print(time.time() -st)

# st = time.time()
# print(sum(edge[2] for edge in kruskal.kruskal2(graph).edges.data('weight')))
# print(time.time() -st)

# times = 0
# for _ in range(200):
#     graph = create_graph.gnp_random_connected_graph(100, 0.01)
#     st = time.time()
#     x = sum(edge[2] for edge in kruskal_draft.kruskal3(graph).edges.data('weight'))
#     times += time.time() - st
# # print(time.time() -st)
# print(times)


mstk = tree.minimum_spanning_tree(graph, algorithm="kruskal")
# print(mstk.edges.data('weight'))
print(sum(edge[2] for edge in mstk.edges.data('weight')))



