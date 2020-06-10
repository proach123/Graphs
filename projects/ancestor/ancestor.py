class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('oops')


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    q = Queue()

    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        g.add_edge(i[1], i[0])
   
    q.enqueue([starting_node])
    max_path = 1
    earliest_ancestor = -1  
    while q.size() > 0:
        path = q.dequeue()
        vert = path[-1]
        if (len(path) >= max_path and vert < earliest_ancestor or len(path) > max_path):
            earliest_ancestor = vert
            max_path = len(path)
        for i in g.vertices[vert]:
            path_copy = list(path)
            path_copy.append(i)
            q.enqueue(path_copy)
    return earliest_ancestor



if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 1))