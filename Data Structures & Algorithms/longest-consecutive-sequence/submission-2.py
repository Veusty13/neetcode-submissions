class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0
        set_nums: set = set(nums)
        max_counter: int = 1
        for num in set_nums:
            counter: int = 1
            before: int = num - 1
            if before not in set_nums:
                after: int = num + 1
                while True:
                    if after in set_nums:
                        counter += 1
                        max_counter = max(counter, max_counter)
                        after += 1
                    else: 
                        break
        return max_counter 
