class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return n
        graph = {i:[] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        nodes = [i for i in range(n)]
        path = set()
        def dfs(i, path):
            if i in path:
                pass
            else:
                path.add(i)
                for j in graph[i]:
                    dfs(j, path)
        counter = 0
        while nodes:
            counter += 1
            path = set()
            dfs(nodes[0], path)
            for node in path:
                nodes.remove(node)
        return counter
            
            