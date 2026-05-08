# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, counter):
            if not node:
                return 0
            counter += 1
            if not node.left and not node.right:
                return counter
            elif node.left and node.right :
                return max(dfs(node.left, counter), dfs(node.right, counter))
            elif node.left:
                return dfs(node.left, counter)
            else:
                return dfs(node.right, counter)
        counter = 0
        return dfs(root, counter)