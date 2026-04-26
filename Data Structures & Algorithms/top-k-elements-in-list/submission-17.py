class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        heap = []
        counter = 0
        for item in freq.items():
            heapq.heappush(heap, (item[1], item[0]))
            counter += 1
            if counter > k:
                _ = heapq.heappop(heap)
        return [t[1] for t in heap]