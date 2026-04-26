class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r :
            middle = l + ((r - l) // 2)
            if nums[middle] < nums[r] :
                r = middle
            else:
                l = middle + 1
        return nums[l]

            

            
            
            
            