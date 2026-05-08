# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, p,ancestors):
            ancestors.append(node)
            if p.val < node.val:
                return dfs(node.left, p, ancestors)
            if p.val > node.val:
                return dfs(node.right, p, ancestors)
            if p.val == node.val:
                return ancestors
        ancestors_p = dfs(root, p, []) 
        ancestors_q = dfs(root, q, [])
        common_ancestors = []
        for ancestor_p, ancestor_q in zip(ancestors_p, ancestors_q):
            if ancestor_p == ancestor_q :
                common_ancestors.append(ancestor_p)
            else:
                break
        return common_ancestors[-1]


        
            

