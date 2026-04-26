class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n: int = len(heights)
        if n <= 1:
            return 0
        else:
            l = 0
            r = n-1
            max_area: int = 0
            while l < r:
                min_height: int = min(heights[l], heights[r])
                width: int = r - l
                area: int = min_height * width
                max_area = max(max_area, area)
                if min_height == heights[l]:
                    l += 1
                elif min_height == heights[r]:
                    r -= 1
        return max_area