class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<r:
            m = l + (r-l)//2
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        print(l)
        if target >= nums[l] and target <= nums[-1]:
            l2, r2 = l, len(nums) - 1
        else:
            l2, r2 = 0, l - 1
        while l2 <= r2:
            m2 = l2 + (r2 - l2)//2
            if nums[m2] == target:
                return m2
            elif nums[m2] > target:
                r2 = m2 - 1
            else:
                l2 = m2 + 1
        return -1
            
