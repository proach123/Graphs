"""
Simple graph implementation
"""
# import os

# os.chdir('~/Desktop/python/week-5/Graphs/projects/graph')

from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
            

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
                return print(f'{v1} not in graph')
                


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return print(f'{vertex_id} not in graph')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        last = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            new = queue.dequeue()
            if new not in last:
                print(new)
                last.add(new)
                for i in self.vertices:
                    queue.enqueue(i)
                    

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        last = set()
        while stack.size() > 0:
            new = stack.pop()
            if new not in last:
                print(new)
                last.add(new)
                for i in self.vertices:
                    stack.push(i)

    def dft_recursive(self, starting_vertex, last = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            current = stack.pop()
            if current not in last:
                print(f'recursive number: {current}')
                last.add(current)
                for i in self.vertices[current]:
                    self.dft_recursive(i, last)





#   # Initial run
#         if visited is None:
#             visited = set()
#         # Can't think of how to do this without setting visited as a parameter
#         # If vertex not visited yet, add to set and print
#         if vertex not in visited:
#             visited.add(vertex)
#             print(vertex)
#             # Recursivly do the same for neighbors of vertex (DEPTH first, so it moves down the tree)
#             for i in self.get_neighbors(vertex):
#                 self.dft_recursive(i, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        last = set()
        
        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]
            if v not in last:
                if v == destination_vertex:
                    return path
                last.add(v)
                for i in self.vertices:
                    path_copy = path.copy()
                    path_copy.append(i)
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        
        last = set()
        
        while stack.size() > 0: 
            path = stack.pop()
            v = path[-1]
            
            if v not in last:
                if v == destination_vertex:
                    return path      
                last.add(v)
              
                for i in self.vertices[v]:
                  
                    path_copy = path.copy()             
                    path_copy.append(i)                
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, last = set()):

        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # stack = Stack()
        # stack.push([starting_vertex])
        # while stack.size() > 0:
        #     current_path = stack.pop()
        #     v = current_path[-1]
        #     if v not in last:
        #         if v == destination_vertex:
        #             return current_path
        #         last.add(v)
        #         for i in self.vertices[current_path]:
        #             self.dfs_recursive(i,last)
        pass



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
    graph.dft_recursive(1)

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
    print(graph.dfs_recursive(1, 6))
