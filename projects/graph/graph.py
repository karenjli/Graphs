"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # push the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited node
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Pop, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        node = starting_vertex
        # Check if the node is visited

        # If not...
        if node not in visited:

            # Marked as visited
            visited.add(node)
            # Print
            print(node)
            # Call DFT_Recursive on each child
            for child in self.vertices[node]:
                if child not in visited:
                    self.dft_recursive(child, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            vertex = path[-1]
            # CHECK IF IT'S THE TARGET
            if vertex not in visited:
                if vertex == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                visited.add(vertex)
            # Check if it's been visited
            for next_vert in self.get_neighbors(vertex):
                # If it has not been visited...
                new_path = list(path)
                # Mark it as visited
                new_path.append(next_vert)
                # Then add a PATH TO all neighbors to the back of the queue
                # Make a copy of the path before adding
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        #     """
        #     Return a list containing a path from
        #     starting_vertex to destination_vertex in
        #     depth-first order.
        #     """
        # Create an empty stack
        s = Stack()
        # Add a PATH to the starting vertex_id to the stak
        s.push([starting_vertex])
        # Create an empty set to store visited node
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first Path
            path = s.pop()
            # Grab the last vertex of the path
            vertex = path[-1]
            # Check if the vertex is in visited
            if vertex not in visited:

                if vertex == destination_vertex:
                    return path
                visited.add(vertex)

                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited = None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initialize visited if it's not yet initialized
        if visited is None:
            visited = set()
        # Initialized path if it's not yet initialized
        if path is None:
            path=[]
        # Check if starting vertex has been visited
        if starting_vertex not in visited:
        # If not...
            visited.add(starting_vertex)
            path_copy=path.copy()
            path_copy.append(starting_vertex)
            # If starting vertex is destination vertex
            if starting_vertex==target_value:
                # return path
                return path_copy
            # Mark it as visited
            # Call DFS on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                path_copy=path.copy()
                self.dfs_recursive(neighbor, target_value, visited, path)
                if path_copy is not None:
                    return path_copy
                
        # s = Stack()
        # visited = set()
        # path = []
        # visited.add(starting_vertex)
        # path = path+[starting_vertex]
        # if starting_vertex == target_value:
        #     return path
        # for child in self.vertices[starting_vertex]:
        #     if child not in visited:
        #         new_path = self.dfs_recursive(child, path, visited)
        #     if new_path:
        #         return new_path
        # return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("-----")
    graph.dft_recursive(1)
    print("-----")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("------")
    print(graph.dfs_recursive(1, 6))
