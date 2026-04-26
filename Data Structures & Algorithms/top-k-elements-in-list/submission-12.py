import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        if n == 0:
            return []
        if len(set(nums)) == 1:
            return [nums[0]]
        number_freq_map: Dict[int, int] = {}
        for i in range(n):
            if nums[i] in number_freq_map:
                number_freq_map[nums[i]] += 1
            else:
                number_freq_map[nums[i]] = 1
        heap: List = []
        for item in number_freq_map.items():
            freq_value: tuple[int, int] = (item[1], item[0])
            heapq.heappush(heap, freq_value)
            if len(heap) > k:
                _ = heapq.heappop(heap)
        return [value for (freq, value) in heap]