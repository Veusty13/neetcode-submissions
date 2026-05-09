"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = {}
        def dfs(node):
            if node.val not in clone:
                clone[node.val] = []
                for nei in node.neighbors:
                    clone[node.val].append(nei.val)
                    dfs(nei)
        dfs(node)
        cloned_nodes = {k:Node(val=k) for k in clone}
        for k in clone:
            for nei_val in clone[k]:
                cloned_nodes[k].neighbors.append(cloned_nodes[nei_val])
        return cloned_nodes[1]
            
