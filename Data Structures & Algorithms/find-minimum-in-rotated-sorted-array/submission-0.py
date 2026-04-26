class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        while True:
            index_middle = len(nums)//2
            ll = nums[0]
            lr = nums[index_middle - 1]
            rl = nums[index_middle]
            rr = nums[-1]
            if ll <= lr:
                min_l = ll
            else:
                min_l = lr
            if rl <= rr:
                min_r = rl
            else:
                min_r = rr
            if min_l < min_r:
                nums = nums[:index_middle]
            elif min_l > min_r:
                nums = nums[index_middle:]
            else:
                return min_l
            
            
            
            
            