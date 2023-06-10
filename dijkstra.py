"""shortest path algorithm
atuthor: Harry Gao
"""
import re
from graph import Graph
from heapq import *
import networkx as nx
import matplotlib.pyplot as plt

GRAPH = Graph()
    
class Dijkstra():
    def __init__(self, graph) -> None:
        # storage graph
        self.graph = graph
        # vertex_num: the number of graph's vertexs
        self.vertex_num = len(graph)
    
    def check_connectivity(self):
        """hypothesis: this is a connectivity graph
        """
        pass
    
    def search_path(self, start, end):
        """search the path from start_node to end_node and return the weights
        """
        [weight, path] = self._search_all_paths(start)[end]
        final_path = start
        for p in path[1:]:
            final_path = final_path+"->"+p[1]
        return final_path, weight
    
    def _search_all_paths(self, start):
        """search all paths from start_node to the other nodes and get weigths
        """
        # candidates(storage the min next_node): [(next_node_weight=0, exist_node=0, next_node=0)]
        candidates = []
        # paths(path from start to end): {end_node: [weight, [(edge), (edge), ... ] ], ...}
        paths = {}
        # initialize start vertex
        init_path = {start: [0, [(),]], }
        paths.update(init_path)
        # iterate over the nodes of graph
        search_times = 1
        while search_times < self.vertex_num:
            candidates = []
            next_node = []
            for exist_node in list(paths.keys()):
                # edges wihich is not in the set
                edges = []
                for edge in self.graph[exist_node]:   # edge: (7, 'A', 'B')
                    if (edge[2] in list(paths.keys())):
                        continue
                    edges += [edge] # edges: [(7, 'A', 'B'), (8, 'B', 'C')]
                # min_edge adjacent to exist_node
                if(edges != []):
                    heapify(edges)
                    min_edge = edges[0]
                    next_node = min_edge[2]
                    next_node_weight = paths[exist_node][0] + min_edge[0]
                    candidates += [(next_node_weight, exist_node, next_node)]

            # choose the minist weight vertex and add it to exist_vertexts
            heapify(candidates)
            candidate = candidates[0]
            paths.update({candidate[2]: [candidate[0], paths[candidate[1]][1] + [(candidate[1], candidate[2])]]})
            search_times += 1
        # paths: {end_node: [end_node_weight, [path:(edge),]], }
        return paths
    
    def draw_origin_graph(self):
        # draw vetex
        G = nx.Graph()
        G.add_nodes_from([i for i in list(self.graph.keys())])
        # draw edge
        for vertex_adj in self.graph.values():
            for edge in vertex_adj:
                G.add_edge(edge[1], edge[2])
        # draw graph
        plt.figure(figsize=(6,4))
        pos=nx.circular_layout(G)
        nx.draw(G,pos=pos, with_labels=True)
        plt.savefig("origin graph",dpi=1000,bbox_inches = 'tight')
        
    def draw_dj_graph(self, path):
        # draw vetex
        G = nx.DiGraph()
        G.add_nodes_from([i for i in list(self.graph.keys())])
        # draw edge
        path = list(''.join(re.findall(r'[A-Za-z]', path)))
        edges = [(path[node_idx], path[node_idx+1]) for node_idx in range(len(path)-1)]
        G.add_edges_from(edges)
        # draw graph
        plt.figure(figsize=(6,4))
        pos=nx.circular_layout(G)
        nx.draw(G,pos=pos, with_labels=True)
        plt.savefig("dj graph",dpi=1000,bbox_inches = 'tight')
        

graph1 = Dijkstra(GRAPH.graph)

print("You change the structure of Graph by modifying the graph.py.")
print("Please input your start/end node.")
while 1:
    start_node = input("start node:")
    end_node = input("end node:")
    draw_config = input("draw the graph(YES/NO):")
    path, weight = graph1.search_path(start=start_node, end=end_node)
    print(f"Path:{path}")
    print(f"Weight:{weight}")
    if draw_config.title() in ["YES", "Y"]:
        graph1.draw_origin_graph()
        graph1.draw_dj_graph(path)
