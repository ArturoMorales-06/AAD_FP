import networkx as nx 
import matplotlib.pyplot as plt 
import bfs, sys

def khop_neighborhood(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k)
        neighborhood_list = []
        for i in range(len(bfs_result)):
            neighborhood_list += bfs_result[i]
        khop_neighborhood_graph = nx.subgraph(G, neighborhood_list)
        nx.draw(khop_neighborhood_graph)
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
        nx.draw(k_path)
        plt.show()
    except:
        sys.exit("Invalid Input - KLP")

def k_independent_set(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k)
        bfs_length = len(bfs_result)
        u_neighbors = list(nx.neighbors(G, u))
        subgraph_nodes = []
        independent_set = []
        subgraph_nodes.append(u)
        for i in range(1, bfs_length - 1):
            for node in bfs_result[i]:
                for neighbor in list(nx.neighbors(G, node)):
                    if(u_neighbors.count(neighbor) == 0 and neighbor != u and independent_set.count(neighbor) == 0 and subgraph_nodes.count(neighbor) == 0):
                        independent_set.append(neighbor)
                        if(subgraph_nodes.count(node) == 0):
                            subgraph_nodes.append(node)
                    if(len(independent_set) >= k-1):
                        break
                    else:
                        continue
                if(len(independent_set) >= k-1):
                    break
            if(len(independent_set) >= k-1):
                break
        subgraph_nodes = subgraph_nodes + independent_set
        k_ind_set_graph = nx.subgraph(G, subgraph_nodes)
        nx.draw(k_ind_set_graph)
        plt.show()

    except:
        sys.exit("Invalid Input - KIS")

# def k_independent_set(G, u, k):
#     try:
#         G_nodes = G.nodes()
#         u_neighbors = list(nx.neighbors(G, u))
#         subgraph_nodes = []
#         for i in range(k):
#             for node in G_nodes:
#                 if(u_neighbors.count(node) == 0):
#                     subgraph_nodes.append(node)
#                     break
#                 else:
#                     continue
#         k_ind_set_graph = nx.subgraph(G, subgraph_nodes)
#         nx.draw(k_ind_set_graph)
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

k_independent_set(tet, '1', 5)

# k_length_path(tet, '1', 4)

# khop_neighborhood(tet, '1', 3)

# bf = bfs.bfs(tet, '1', 2)
# print(bf)

# print(tet.nodes())

# nx.draw(tet)
# plt.show()