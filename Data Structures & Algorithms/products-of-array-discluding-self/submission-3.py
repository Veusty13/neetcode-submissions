class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq_map = {}
        prod = 1
        for i in range(n):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1
            if nums[i] == 0:
                index_zero = i
            else:
                prod *= nums[i]
        if 0 not in freq_map:
            output = [int(prod/num) for num in nums]
        else:
            if freq_map[0] >= 2:
                output = [0]*n
            if freq_map[0] == 1:
                output = [0]*n
                output[index_zero] = prod
        return output