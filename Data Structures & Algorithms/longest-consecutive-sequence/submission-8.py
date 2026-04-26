class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if not nums:
            return 0
        hashset = set(nums)
        max_counter = 1
        for num in hashset:
            counter = 1
            if num - 1 not in hashset:
                cur = num
                while cur + 1 in hashset:
                    counter += 1
                    cur = cur + 1
                max_counter = max(max_counter, counter)
                counter = 1
        return max_counter