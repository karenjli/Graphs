from util import Stack, Queue

class Graph:
    def __init__(self):
        self.verticies={}
        
    def add_vertex(self,vertex):
        self.verticies[vertex]=set()

    def add_edge(self, v1,v2):
        if v1 in self.vertices and v2 in self.verticies:
            self.verticies[v1].add[v2]
            
    def get_neighbors(self, vertex_id):
        return self.verticies[vertex_id]        

    
def earliest_ancestor(ancestors, starting_node):
    # Create graph
    graph = Graph()
    # Create an empty stack
    stack =Stack()
    # Add the starting node to the stack
    stack.push(starting_node)
    # Create a set to keep track of visited nodes
    visited = set()
    # While the stack is not empty
    while stack.size() > 0:
        # Pop the first vertex
        v=stack.pop()
        if v not in visited:
            print(v)
            visited.add(v)
        for neighbor in graph.get_neighbors(v):
            s.push(neighbor)