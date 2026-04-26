# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        to_do = [cur]
        while any(to_do):
            new_to_do = []
            for cur in to_do:
                new_right, new_left = cur.left, cur.right
                cur.left = new_left
                cur.right = new_right
                if cur.left:
                    new_to_do += [cur.left]
                if cur.right:
                    new_to_do += [cur.right]
            to_do = new_to_do
        return root