# Module used to compute a path of length "k" that has
# node "u" as one of its endpoints
import networkx as nx 
import sys
import bfs  

def k_len_path(G, u, k):
    try:
        bfs.bfs(G, u, k)
    except:
        sys.exit("Invalid Input - KLP")
