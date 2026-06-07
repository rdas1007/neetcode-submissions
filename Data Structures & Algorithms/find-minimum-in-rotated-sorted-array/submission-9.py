class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        if len(nums) == 1:
            return nums[0]
        while l<r:
            pivot = l + (r-l)//2
            if nums[r] > nums[pivot]:
                r = pivot
            # elif nums[r] > nums[pivot]:
                
            else:
                l = pivot + 1
                
        return nums[l]