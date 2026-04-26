class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n: int = len(nums)
        res: List[List[int]] = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            l:int = i + 1
            r:int = n - 1
            while l < r :
                calc: int = nums[i] + nums[l] + nums[r]
                if calc == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1 
                    r -= 1
                    while (nums[l] == nums[l-1]) and l < r :
                        l += 1   
                elif calc > 0:
                    r -= 1
                else:
                    l += 1
        return res
                
            
        