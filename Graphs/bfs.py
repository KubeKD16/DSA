from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self,a):
        queue = []
        visited = [False] * (max(self.graph)+1)
        print("Visited list is {}".format(visited))
        
        queue.append(a)
        visited[a] = True

        while queue:
            element = queue.pop(0)
            print(element, end=" ")

            for i in self.graph[element]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.add_edge(0,1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)

g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(1)

# print(g)

