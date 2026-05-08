# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def find_node_candidates(node, subRoot, candidates) -> List[TreeNode]:
            if node.val == subRoot.val :
                candidates.append(node)
            if node.left :
                find_node_candidates(node.left, subRoot, candidates)
            if node.right :
                find_node_candidates(node.right, subRoot, candidates)
            return candidates
        def equals_sub_tree(node, subRoot) -> bool:
            if (not node and not subRoot):
                return True
            if (not node and subRoot):
                return False
            if (node and not subRoot):
                return False
            if (node.val != subRoot.val):
                return False
            if (node.val == subRoot.val) and (not node.left and not subRoot.left) and (not node.right and not subRoot.right):
                return True
            return equals_sub_tree(node.left, subRoot.left) and equals_sub_tree(node.right, subRoot.right)
        candidates = find_node_candidates(root, subRoot,[])
        for node in candidates:
            if equals_sub_tree(node, subRoot):
                return True
        return False
