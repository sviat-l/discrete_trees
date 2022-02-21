"""
MODULE TO RUN TESTS and compare two algoritms
Create graph that visualisize them
"""
import create_graph
import kruskal
import prim
import time
import matplotlib.pyplot as plt

number_of_iterations = 10
number_of_nodes = 1000
completeness = 1
step = 10

plt.xlabel('nodes')
plt.ylabel('time(s)')
plt.title(f'Prim(red)  ---   Kruskal(yellow)\n\
 Iterations made - {number_of_iterations}\
    Completeness - {completeness}    Step - {step}')
x_arguments, prim_times, kruskal_times = [], [], []


def find_time(cur_nodes_num, flag='kruskal'):
    # choose algorithm
    if flag == 'prim':
        mst_algo = prim.prim_mst
    else:
        mst_algo = kruskal.kruskal_mst
    sum_times = 0
    for _ in range(number_of_iterations):
        graph = create_graph.gnp_random_connected_graph(
            cur_nodes_num, completeness)
        # calculate time
        st = time.time()
        mst = mst_algo(graph)
        sum_times += time.time() - st
    return sum_times/number_of_iterations

# iterate on nun nodes from 0 to max number
for vertecies in range(step, number_of_nodes, step):
    x_arguments.append(vertecies)
    prim_times.append(find_time(vertecies, "prim"))
    kruskal_times.append(find_time(vertecies, "kruskal"))

plt.plot(x_arguments, prim_times, label="prim", color="red")
plt.plot(x_arguments, kruskal_times, label="kruskal", color="yellow")
plt.savefig("plot")
