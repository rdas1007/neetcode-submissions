class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        water = 0
        r = len(height) - 1
        maxl, maxr = 0, 0
        while l <= r:
            if maxl <= maxr:
                water += max(0, maxl - height[l])
                maxl = max(maxl, height[l])
                l += 1
            else:
                water += max(0, maxr - height[r])
                maxr = max(maxr, height[r])
                r -= 1
        return water
