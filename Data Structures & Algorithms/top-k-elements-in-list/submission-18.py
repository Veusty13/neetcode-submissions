import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        output = []
        counter = 0
        for num, count in freq.items():
            heapq.heappush(output, (count, num))
            counter += 1
            if counter > k:
                heapq.heappop(output)
        return [x[1] for x in output]