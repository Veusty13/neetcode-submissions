class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            m = l + (r-l)//2
            lv = nums[l]
            mv = nums[m]
            rv = nums[r]
            if mv < rv:
                r = m
            else:
                l = m + 1
        return nums[l]