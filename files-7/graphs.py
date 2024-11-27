class Graph:
    def __init__(self, n):
        self.nodes = n
        # create the 2-D matrix
        self.adj = matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u][v] = 1
    def print_adj_matrix(self):
        for row in self.adj:
            print(row)

graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2,1)
graph.add_edge(2,3)
graph.print_adj_matrix()

class Graph:
    def __init__(self):
        # create a dictionary
        self.adj_list = {}
    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]
    def print_adj_list(self):
        for key in self.adj_list:
            print('Node: ', key, ' Neighbors: ', self.adj_list[key])

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2,1)
graph.add_edge(2,3)
graph.print_adj_list()

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")  # Raise an exception if b is zero
    return a / b