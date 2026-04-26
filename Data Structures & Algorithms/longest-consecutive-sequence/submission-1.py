class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        n: int = len(nums)
        max_counter: int = 0
        for i in range(n):
            current_value: int = nums[i]
            counter:int = 0
            while True:
                plus_one: int = current_value + 1
                if plus_one in nums:
                    current_value = plus_one
                    counter += 1
                else: 
                    break
            current_value = nums[i]
            while True:
                minus_one: int = current_value - 1
                if minus_one in nums:
                    current_value = minus_one
                    counter += 1
                else: 
                    break
            max_counter = max(max_counter, counter)
        return max_counter + 1

