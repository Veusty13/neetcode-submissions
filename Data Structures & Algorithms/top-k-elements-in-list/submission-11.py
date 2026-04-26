class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        output: List[int] = []
        if n == 0: 
            return output
        if len(set(nums)) == 1:
            return [nums[0]]
        value_freq_map: Dict[int, int] = {}
        freq_value_map: Dict[int, List[int]] = {}
        for i in range(n):
            if nums[i] in value_freq_map.keys():
                value_freq_map[nums[i]] += 1
            else:
                value_freq_map[nums[i]] = 1
        for value, freq in value_freq_map.items():
            if freq in freq_value_map.keys():
                freq_value_map[freq].append(value)
            else:
                freq_value_map[freq] = [value]
        for freq in range(n, 0, -1):
            if freq in freq_value_map.keys():
                output += freq_value_map[freq]
                len_output: int = len(output)
                if len_output >= k:
                    output = output[:k]
        return output
            