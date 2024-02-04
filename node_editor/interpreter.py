import logging
from collections import defaultdict
from node_editor.node import Node
from node_editor.nodes.begin_node import Begin_Node

# This class represents a directed graph using
# adjacency list representation
class NodeGraph:
 
    # Constructor
    def __init__(self, start_node):
        self.graph = defaultdict(list)
        self._start_node = start_node
 
     
    # Function to add an edge to graph
    def add_edge(self, node1: Node, node2: Node):
        assert node1
        assert node2

        self.graph[node1].append(node2)
        logging.debug(f"NodeGraph: Added edge {node1.title_text} <---> {node2.title_text}")
    
    def process_node(self, node):
        logging.debug(f"NodeGraph: Processing {node.title_text}")
        node.execute()

    # A function used by DFS
    def dfs_util(self, node : Node, visited):
        self.process_node(node)
        # Mark the current node as visited
        # and print it
        visited.add(node)
        print(node, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)
 
     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        if self._start_node:
            # Create a set to store visited vertices
            visited = set()
    
            # Call the recursive helper function
            # to print DFS traversal
            self.dfs_util(self._start_node, visited)
        else:
            logging.warning("NodeGraph: Begin node is none")
 