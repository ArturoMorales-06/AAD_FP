import networkx as nx 
import matplotlib.pyplot as plt 
import bfs, sys

def color_graph(G, set):
    try:
        node_list = G.nodes()
        color_map = []
        for node in node_list:
            if(set.count(node) == 0):
                color_map.append('blue')
            else:
                color_map.append('red')
        return color_map
    except:
        sys.exit("Invalid Input - CG") 

def khop_neighborhood(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k+1)
        neighborhood_list = []
        for i in range(len(bfs_result)):
            neighborhood_list += bfs_result[i]
        khop_neighborhood_graph = nx.subgraph(G, neighborhood_list)
        nx.draw(khop_neighborhood_graph, with_labels=True)
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
        color_map = color_graph(k_ind_set_graph, independent_set)
        nx.draw(k_ind_set_graph, node_color = color_map, with_labels = True)
        plt.show()
    except:
        sys.exit("Invalid Input - KIS")

            

# def k_independent_set(G, u, k):
#     try:
#         bfs_result = bfs.bfs(G, u, k)
#         bfs_length = len(bfs_result)
#         neighbors_len = len(bfs_result[1])
#         subgraph_nodes = [u]
#         color_map = ['red']
#         for node in bfs_result[1]:
#             subgraph_nodes.append(node)
#             color_map.append('blue')
#         for i in range(2, bfs_length - 1):
#             for node in bfs_result[i]:
#                 if(len(subgraph_nodes) - (neighbors_len + 1) >= k):
#                     break
#                 else:
#                     subgraph_nodes.append(node)
#                     color_map.append('red')
#             if(len(subgraph_nodes) - (neighbors_len + 1) >= k):
#                 break

#     except:

# def k_independent_set(G, u, k):
#     try:
#         bfs_result = bfs.bfs(G, u, k)
#         bfs_length = len(bfs_result)
#         u_neighbors = list(nx.neighbors(G, u))
#         subgraph_nodes = []
#         independent_set = []
#         subgraph_nodes.append(u)
#         for i in range(1, bfs_length - 1):
#             for node in bfs_result[i]:
#                 for neighbor in list(nx.neighbors(G, node)):
#                     if(u_neighbors.count(neighbor) == 0 and neighbor != u and independent_set.count(neighbor) == 0 and subgraph_nodes.count(neighbor) == 0):
#                         independent_set.append(neighbor)
#                         if(subgraph_nodes.count(node) == 0):
#                             subgraph_nodes.append(node)
#                     if(len(independent_set) >= k-1):
#                         break
#                     else:
#                         continue
#                 if(len(independent_set) >= k-1):
#                     break
#             if(len(independent_set) >= k-1):
#                 break
#         subgraph_nodes = subgraph_nodes + independent_set
#         k_ind_set_graph = nx.subgraph(G, subgraph_nodes)
#         nx.draw(k_ind_set_graph, with_labels=True)
#         plt.show()
#     except:
#         sys.exit("Invalid Input - KIS")


# Create a tetrahedral graph and write it to a file  
# tet = nx.tetrahedral_graph()
# nx.write_adjlist(tet, "tet.txt")

# Read a graph from a file
tet = nx.read_adjlist("road-road-ad-list.txt")
# tet = nx.read_adjlist("tet.txt")
nx.freeze(tet)

# Show the nodes and edges in the graph 
# print("Nodes: " + str(tet.nodes))
# print("Edges: " + str(tet.edges))

# DEBUG ZONE 

# k_independent_set(tet, '1', 15)

# k_length_path(tet, '1', 10)

# khop_neighborhood(tet, '1', 3)

# bf = bfs.bfs(tet, '1', 2)
# print(bf)

# print(tet.nodes())

# nx.draw(tet)
# plt.show()