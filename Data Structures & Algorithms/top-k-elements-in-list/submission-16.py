class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        bucket = {}
        max_freq = 0
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            max_freq = max(max_freq, freq[nums[i]])
        for num in freq:
            if freq[num] in bucket:
                bucket[freq[num]].append(num)
            else:
                bucket[freq[num]] = [num]
        res = []
        for i in range(max_freq, 0, -1):
            if i in bucket:
                res += bucket[i]
                if len(res) == k:
                    return res
        return res