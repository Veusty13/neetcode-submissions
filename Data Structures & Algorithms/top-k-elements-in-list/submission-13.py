class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []
        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1 
            else:
                hashmap[nums[i]] = 1
        for item in hashmap.items():
            heapq.heappush(heap, (item[1], item[0]))
            if len(heap) >= k + 1:
                _ = heapq.heappop(heap)
        return [v for (k,v) in heap]