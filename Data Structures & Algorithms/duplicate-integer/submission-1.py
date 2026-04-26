class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_nums : int = len(nums)
        for i in range(length_nums):
            for j in range(length_nums) :
                if i < j and nums[i] == nums[j]:
                    return True
        return False

        