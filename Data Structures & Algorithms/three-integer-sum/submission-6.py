class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        all_combi = []
        n = len(nums)
        hashset = set()
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                qty = nums[l] + nums[r] + nums[i]
                if qty == 0 :
                    combi = [nums[i],nums[l],nums[r]]
                    if tuple(combi) in hashset: 
                        pass
                    else:
                        all_combi.append(combi)
                    hashset.add(tuple(combi))
                    l += 1
                    r -= 1
                elif qty > 0 :
                    r -= 1
                else:
                    l += 1
        return all_combi
