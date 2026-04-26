class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_nums = len(nums)
        for i in range(length_nums): 
            for j in range(length_nums): 
                if i < j and (nums[i] + nums[j] == target) :
                    return [i,j]
        return []