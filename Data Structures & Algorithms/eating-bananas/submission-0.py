class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r
        while l<=r:
            time = 0
            pivot = l + (r-l)//2
            for i in piles:
                time += math.ceil(i/pivot)
            if time <= h:
                minK = min(minK, pivot)
                r = pivot - 1
            else:
                l = pivot + 1
        return minK