class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums :
            return []
        target_leaves = []
        def dfs(i, leaf):
            if sum(leaf) == target:
                target_leaves.append(leaf)
            if i == len(nums):
                return
            if sum(leaf) < target:
                left_path = dfs(i, leaf + [nums[i]])
                right_path = dfs(i + 1, leaf)
        dfs(0, [])
        return target_leaves

                

            
