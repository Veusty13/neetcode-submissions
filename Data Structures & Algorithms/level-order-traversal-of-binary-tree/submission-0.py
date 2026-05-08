# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        nodes_current_level = [root]
        vals_all_levels = []
        while nodes_current_level:
            vals_current_level = [n.val for n in nodes_current_level]
            vals_all_levels.append(vals_current_level)
            nodes_next_level = []
            for node in nodes_current_level:
                if node.left:
                    nodes_next_level.append(node.left)
                if node.right:
                    nodes_next_level.append(node.right)
            nodes_current_level = nodes_next_level
        return vals_all_levels

        
