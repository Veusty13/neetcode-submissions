class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        index_start = 0
        index_end = n - 1
        while True:
            index_middle = index_start + ((index_end - index_start + 1)//2)
            ll = nums[index_start]
            lr = nums[index_middle - 1]
            rl = nums[index_middle]
            rr = nums[index_end]
            if ll <= lr:
                min_l = ll
            else:
                min_l = lr
            if rl <= rr:
                min_r = rl
            else:
                min_r = rr
            if min_l < min_r:
                index_end = index_middle - 1
            elif min_l > min_r:
                index_start = index_middle
            else:
                return min_l
            
            
            
            
            