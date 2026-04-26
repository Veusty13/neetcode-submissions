class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = {}
        unique_solutions = set()
        solutions = []
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        for i in range(n-1):
            freq[nums[i]] -= 1
            for j in range(i+1, n):
                freq[nums[j]] -= 1
                qty = -1 *(nums[i] + nums[j])
                if qty in freq and freq[qty] > 0:
                    sorted_solution = tuple(sorted([nums[i], nums[j], qty]))
                    if not sorted_solution in unique_solutions:
                        solutions.append([nums[i], nums[j], qty])
                    unique_solutions.add(sorted_solution)  
                freq[nums[j]] += 1
            freq[nums[i]] += 1
        return solutions

