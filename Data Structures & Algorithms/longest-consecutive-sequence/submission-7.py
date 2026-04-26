class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if not nums:
            return 0
        hashset = set(nums)
        visited = set()
        max_counter = 1
        counter = 1
        for num in nums:
            if num not in visited :
                cur = num
                while cur + 1 in hashset:
                    visited.add(cur)
                    counter += 1
                    cur = cur + 1
                cur = num
                while cur - 1 in hashset:
                    visited.add(cur)
                    counter += 1
                    cur = cur - 1
                max_counter = max(max_counter, counter)
                counter = 1
        return max_counter
            