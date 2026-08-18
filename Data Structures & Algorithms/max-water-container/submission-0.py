class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            width = r-l
            length = min(heights[l],heights[r])
            area = length * width
            if area > best:
                best = area
            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
        return best