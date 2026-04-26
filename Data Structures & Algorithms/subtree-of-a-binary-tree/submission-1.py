# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(cur, cur_subroot):
            if not cur and not cur_subroot:
                return 1
            if (not cur and cur_subroot) or (cur and not cur_subroot) or (cur.val != cur_subroot.val):
                return 0

            output = dfs(cur.left, cur_subroot.left) * dfs(cur.right, cur_subroot.right)
            return output
        to_do = [root]
        while to_do:
            new_to_do = []
            for cur in to_do:
                if cur.val != subRoot.val:
                    if cur.left:
                        new_to_do.append(cur.left)
                    if cur.right:
                        new_to_do.append(cur.right)
                else :
                    cur_subroot = subRoot
                    if dfs(cur, cur_subroot):
                        return True
                    if cur.left:
                        new_to_do.append(cur.left)
                    if cur.right:
                        new_to_do.append(cur.right)
            to_do = new_to_do
        return False