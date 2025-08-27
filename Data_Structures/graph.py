from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(self.vertices)]
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)
        
    def addVertex(self):
        self.graph.append([])
        self.vertices += 1
        
    def dfs(self, start):
        visited = [False for i in range(self.vertices)] 
        self.__dfs_helper(visited, start)
        
    def __dfs_helper(self, visited, u):
        print(u)
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.__dfs_helper(visited, v)
                
    def bfs(self, start):
        visited = [False for i in range(self.vertices)]
        level = 0
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            size = len(q)
            while size:
                item = q.popleft()
                print(f"level: {level}: ", item)
                for v in self.graph[item]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        
                size -= 1
            level += 1
            
                    
    def getComponentCount(self):
        visited = [False for i in range(self.vertices)]
        count = 0
        for i in range(self.vertices):
            if not visited[i]:
                self.__dfs_helper(visited, i)
                count += 1
                
        return count
    
    def getShortestPath(self, src, dst):
        visited = [False for i in range(self.vertices)]
        q = deque()
        q.append(src)
        visited[src] = True
        level = 0
        while q:
            size = len(q)
            while size:
                item =  q.popleft()
                if dst == item:
                    return level
                for v in self.graph[item]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True
                size -= 1
            level += 1
            
        return -1
                            
    def getNumberOfNodesAtAGivenLevel(self, level):
        visited = [False] * self.vertices
        q = deque()
        q.append(0)
        visited[0] = True
        count = 0
        while q:
            size = len(q)
            while size:
                item = q.popleft()
                if level == 0:
                    count += 1
                for v in self.graph[item]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                size -= 1
            level -= 1
                        
        return count
    
    def getNumberOfPathsFromSrcToDst(self, src, dst):
        visited = [False for i in range(self.vertices)] 
        return self.helper_number_of_paths(visited, src, dst)
        
    def helper_number_of_paths(self, visited, src, dst):
        if dst == src:
            return 1
        visited[src] = True
        path_count = 0
        for v in self.graph[src]:
            if not visited[v]:
                path_count += self.helper_number_of_paths(visited, v, dst)
        visited[src] = False
        
        return path_count
        
    def dfs(self, start):
        visited = [False for i in range(self.vertices)] 
        self.__dfs_helper(visited, start)
        
    def __dfs_helper1(self, visited, u):
        print(u)
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.__dfs_helper(visited, v)
            visited[v] = False
    
    def transpose(self):
        new_graph = Graph(self.vertices)
        for i in range(self.vertices):
            for item in self.graph[i]:
                new_graph.addEdge(item, i)
        return new_graph
    
    def hasCycleUndirected(self):
        def dfs(u, parent):
            visited[u] = True
            for v in self.graph[u]:
                if v != parent and visited[v]:
                    return True
                if v != parent: 
                    if dfs(v, u): return  True
            return False

        visited = [False] * self.vertices
        for i in range(self.vertices): 
            if not visited[i]:  
                if dfs(i, -1):
                    return True
        return False
    
    def hasCycleDirected(self):
        def dfs(u):
            visited[u] = onStack[u]  = True
            print(u)
            for v in self.graph[u]:
                if onStack[v]:
                    return True
                if not visited[v]:
                    if dfs(v): return True
            onStack[u] = False
            return False
        
        visited = [False for i in range(self.vertices)]
        onStack = [False for i in range(self.vertices)]
        for i in range(self.vertices): 
            if not visited[i]:  
                if dfs(i):
                    return True
        return False
    
    def make_edges(self):
        edges = []
        for i in range(self.vertices):
            for j in range(len(self.graph[i])):
                edges.append((i, self.graph[i][j]))
        return edges
    
    def kahns_algorithm(self):
        edges = self.make_edges()
        inDegree = [0] * self.vertices
        graph = Graph(self.vertices)
        for edge in edges:
            graph.graph[edge[0]].append(edge[1])
            inDegree[edge[1]] += 1
        res = []
        q = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            item = q.popleft()
            res.append(item)
            for v in self.graph[item]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
                    
        return res
    
    def kosaraju_algorithm(self):
        def dfs_helper(graph, visited, u, stack, fill = True):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs_helper(graph, visited, v, stack, fill)
            if fill:
                stack.append(u)
            
        stack = list()
        visited = [False] * self.vertices
        for i in range(self.vertices):
            if not visited[i]:
                dfs_helper(self.graph, visited, i, stack)
            
        print(stack)
        
        new_graph = self.transpose()
        visited = [False] * self.vertices
        count = 0
        while stack:
            item = stack.pop()
            if not visited[item]:
                dfs_helper(new_graph.graph, visited, item, [], False)
                count += 1
            
        return count
    
    def tarjan_algorithm(self):
        def dfs(u):
            nonlocal id, scc_count
            stack.append(u)
            visited[u] = True
            ids[u] = id
            ll[u] = id
            id += 1
            
            for v in self.graph[u]:
                if ids[v] == -1:
                    dfs(v)
                    ll[u] = min(ll[u], ll[v])
                elif visited[v]:
                    ll[u] = min(ll[v], ll[u])
            if ids[u] == ll[u]:
                while True:
                    node = stack.pop()
                    visited[node] = False
                    if node == u:
                        break
                scc_count += 1
                    
            
        visited = [False] * self.vertices
        stack = []
        id = 0
        ids = [-1] * self.vertices
        ll = [-1] * self.vertices
        scc_count = 0
        
        for i in range(self.vertices):
            if ids[i] == -1:
                dfs(i)
            
        return scc_count

    def __str__(self):
        return f"{self.graph}"
        
        


g = Graph(6)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,5)
g.addEdge(4,5)

print(g.getNumberOfPathsFromSrcToDst(0, 5))

