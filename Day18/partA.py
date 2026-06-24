class Graph:
    def __init__(self):
        # Initialize an empty dictionary to hold the adjacency list
        self.adj_list = {}

    def add_vertex(self, v):
        # Add a vertex only if it doesn't already exist
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        # Ensure both vertices exist in the graph first
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Add undirected edges (both ways)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def display(self):
        print("--- Adjacency List ---")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {', '.join(neighbors)}")
        print("----------------------")