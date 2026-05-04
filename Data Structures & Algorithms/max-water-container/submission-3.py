class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0
        while l < r :
            min_height = min(heights[l], heights[r])
            area = (r - l) * min_height
            max_area = max(area, max_area)
            if min_height == heights[l]:
                l += 1
            else :
                r -= 1
        return max_area
