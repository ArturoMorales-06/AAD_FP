import networkx as nx 
import matplotlib.pyplot as plt 
import bfs, sys

def color_graph(G, set, color1, color2):
    try:
        node_list = G.nodes()
        color_map = []
        for node in node_list:
            if(set.count(node) == 0):
                color_map.append(color2)
            else:
                color_map.append(color1)
        return color_map
    except:
        sys.exit("Invalid Input - CG") 

def khop_neighborhood(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k+1)
        neighborhood_list = []
        odd_layers = []
        for i in range(len(bfs_result)):
            neighborhood_list += bfs_result[i]
            if(i % 2 == 1):
                odd_layers += bfs_result[i]
        khop_neighborhood_graph = nx.subgraph(G, neighborhood_list)
        color_map = color_graph(khop_neighborhood_graph, odd_layers, 'yellow', 'green')
        nx.draw(khop_neighborhood_graph, node_color = color_map, with_labels=True)
        plt.show()
    except:
        sys.exit("Invalid Input - KHopN")

def k_length_path(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k)
        current_node = bfs_result[k-1][0]
        k_path = nx.null_graph()
        k_path.add_node(current_node)
        for i in range(k-2, -1, -1):
            current_neighbors = list(nx.neighbors(G, current_node))
            for node in bfs_result[i]:
                if(current_neighbors.count(node) == 1):
                    k_path.add_node(node, name=node)
                    k_path.add_edge(current_node, node)
                    current_node = node 
                    break
                else:
                    continue
        nx.draw(k_path, with_labels=True)
        plt.show()
    except:
        sys.exit("Invalid Input - KLP")

def k_independent_set(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k)
        bfs_length = len(bfs_result)
        adjacent_nodes = []
        independent_set = []
        adj_flag = False
        for i in range(0,k):
            if(i % 2 == 0):
                for node in bfs_result[i]:
                    current_neighbors = list(nx.neighbors(G, node))
                    for ind_node in independent_set:
                        if(current_neighbors.count(ind_node) != 0):
                            adjacent_nodes.append(node)
                            adj_flag = True
                            break
                        else:
                            continue
                    if(adj_flag == False):
                        independent_set.append(node)
                    if(len(independent_set) >= k):
                        break
                    adj_flag = False
                if(len(independent_set) >= k):
                    break
            else:
                for adj_node in bfs_result[i]:
                    adjacent_nodes.append(adj_node)

            if(len(independent_set) >= k):
                break
        subgraph_nodes = independent_set + adjacent_nodes
        k_ind_set_graph = nx.subgraph(G, subgraph_nodes)
        color_map = color_graph(k_ind_set_graph, independent_set, 'red', 'blue')
        nx.draw(k_ind_set_graph, node_color = color_map, with_labels = True)
        plt.show()
    except:
        sys.exit("Invalid Input - KIS")

# Read or Create a graph and write it to a file  
# tet = nx.tetrahedral_graph()
# nx.write_adjlist(tet, "tet.txt")

# Read a graph from a file
G = nx.read_adjlist("road-road-ad-list.txt")
# G = nx.read_adjlist("converted_twitter.txt")
# G = nx.read_adjlist("tet.txt")
nx.freeze(G)

# TRY

# PATH
# k_length_path(G, '1', 6)

# NEIGHBORHOOD
# khop_neighborhood(G, '1', 3)

# INDEPENDENT SET
# k_independent_set(G, '1', 5)

# BFS
# print(bfs.bfs(G, '1', 2))