class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if not nums:
            return 0
        hashset = set(nums)
        max_counter = 0
        counter = 0
        for num in nums:
            cur = num
            while cur in hashset:
                counter += 1
                cur = cur + 1
            max_counter = max(max_counter, counter)
            counter = 0
        return max_counter
            