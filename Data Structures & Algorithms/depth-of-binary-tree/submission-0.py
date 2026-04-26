# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur = root
        def dfs(cur):
            if not cur.right and not cur.left:
                return 0
            if not cur.right and cur.left:
                return 1 + dfs(cur.left)
            if not cur.left and cur.right:
                return 1 + dfs(cur.right)
            if cur.left and cur.right:
                return max(1 + dfs(cur.left), 1 + dfs(cur.right))
        if cur:
            nb_elements = dfs(cur)
            return 1 + nb_elements
        else:
            return 0
            
        