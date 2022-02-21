import networkx as nx

# O(VE)
def kruskal1(graph:nx.Graph)->nx.Graph:
    def union(i,j, dct):
        i,j = sorted([i,j])
        class2 = node_classes[j]
        for x in dct[class2]:
            node_classes[x] = node_classes[i]
        dct[node_classes[i]] |= dct.pop(class2)
        return dct

    number_of_vertixes = graph.number_of_nodes()
    node_classes = list(range(number_of_vertixes))
    classes_nodes = {i:{i} for i in range(number_of_vertixes)}

    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))

    edged = sorted(graph.edges.data('weight'), key=lambda edge: edge[2])
    ind = 0
    while number_of_vertixes > 1:
        i, j, w = edged[ind]
        if node_classes[i] != node_classes[j]:
            number_of_vertixes -= 1
            tree.add_edge(i, j, weight=w)
            classes_nodes = union(i,j, classes_nodes)
        ind+=1
    return tree

def kruskal2(graph:nx.Graph)->nx.Graph:
    def find_class(node):
        while node!= node_classes[node]:
            node = node_classes[node]
        return node
        return node if node_classes[node] == node else find_class(node_classes[node])

    number_of_vertixes = graph.number_of_nodes()
    node_classes = list(range(number_of_vertixes))
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))

    edge_list = sorted(graph.edges.data('weight'), key=lambda edge: edge[2])
    ind = 0
    while number_of_vertixes > 1:
        i, j, w = edge_list[ind]
        i_class = find_class(i)
        j_class = find_class(j)
        if i_class != j_class:
            number_of_vertixes -= 1
            tree.add_edge(i, j, weight=w)
            if i < j:
                node_classes[i_class] = j_class
            else:
                node_classes[j_class] = i_class
        ind+=1
    return tree



def kruskal3(graph:nx.Graph)->nx.Graph:
    def find_class(node):
        while node!= classes[node]:
            node = classes[node]
        return node

    def union(i_class, j_class):
        if level[i_class] > level[j_class]:
            classes[j_class] = i_class
        else:
            classes[i_class] = j_class
            if level[i_class] == level[j_class]:
                level[j_class]+=1

    number_of_vertixes = graph.number_of_nodes()
    classes = {i:i for i in range(number_of_vertixes)}
    level = {i:0 for i in range(number_of_vertixes)}
    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))

    edges = sorted(graph.edges.data('weight'), key=lambda edge: edge[2])
    ind = 0
    # while number_of_vertixes > 1:
    #     i,j, w = edges[ind]
    #     ind += 1
    for cur_edge in edges:
        if number_of_vertixes == 1:
            break
        i, j, w = cur_edge
        i_class = find_class(i)
        j_class = find_class(j)
        if i_class != j_class:
            number_of_vertixes -= 1
            tree.add_edge(i, j, weight=w)
            union(i_class, j_class)
    return tree

def kruskal4(graph:nx.Graph)->nx.Graph:
    def union(i,j, dct, lst):
        i,j = sorted([i,j])
        class2 = lst[j]
        for x in dct[class2]:
            lst[x] = lst[i]
        dct[lst[i]] |= dct.pop(class2)
        return dct, lst

    number_of_vertixes = graph.number_of_nodes()
    node_classes = list(range(number_of_vertixes))
    classes_nodes = {i:{i} for i in range(number_of_vertixes)}

    tree = nx.Graph()
    tree.add_nodes_from(range(number_of_vertixes))

    edged = sorted(graph.edges.data('weight'), key=lambda edge: edge[2])
    ind = 0
    while number_of_vertixes > 1:
        i, j, w = edged[ind]
        if node_classes[i] != node_classes[j]:
            number_of_vertixes -= 1
            tree.add_edge(i, j, weight=w)
            classes_nodes, node_classes = union(i,j, classes_nodes, node_classes)
        ind+=1
    return tree
