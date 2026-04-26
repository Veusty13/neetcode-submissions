class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        hashset = set(nums)
        for num in nums:
            len = 1
            if num - 1 in hashset:
                len += 1
                while num - len in hashset:
                    len += 1
            max_len = max(max_len, len)
        return max_len