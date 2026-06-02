class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        maxVal = 0
        while l<r:
            vol = (r - l) * min(heights[l], heights[r])
            maxVal = max(maxVal, vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxVal
