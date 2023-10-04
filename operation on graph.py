class Graph:
    def __init__(self, n):
        self.vertices = [[] for _ in range(n+1)]
    
    def add_edge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)
    
    def print_adjacent_vertices(self, u):
        print(*self.vertices[u])
n = int(input())
k = int(input())

graph = Graph(n)

for _ in range(k):
    operation= list(map(int, input().split()))
    
    if operation[0] == 1:
        u,v=operation[1],operation[2]
        graph.add_edge(u, v)
    elif operation[1] == 2:
        u=operation[1]
        graph.print_adjacent_vertices(u)
