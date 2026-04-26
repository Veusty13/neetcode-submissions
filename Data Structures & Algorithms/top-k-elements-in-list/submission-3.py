class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        mapper_count: Dict[str, int] = {}
        for i in range(n):
            value: str = str(nums[i])
            if value in mapper_count :
                mapper_count[value] += 1
            else :
                mapper_count[value] = 1
        ordered_unique_counts: List[int] = sorted(mapper_count.values())
        biggest_counts: List[int] = ordered_unique_counts[(-1*k):]
        output_values: List[str] = [
            int(value) for value,count in mapper_count.items() if count in biggest_counts
        ]
        return output_values


            