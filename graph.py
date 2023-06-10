"""Graph:
    A/B/C/D ...: represent the vertex node
    (8, 'C', 'B'): edge_weight, exist_node, next_node
"""
class Graph():
    def __init__(self) -> None:
        self.graph =  {'A': [(7, 'A', 'B'), (5, 'A', 'D')], 
         'C': [(8, 'C', 'B'), (5, 'C', 'E')], 
         'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')], 
         'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')], 
         'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')], 
         'G': [(9, 'G', 'E'), (11, 'G', 'F')], 
         'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]} 
