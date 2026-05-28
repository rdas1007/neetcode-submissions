class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        final = [1]*len(nums)
        for i in range(len(nums)):
            final[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            final[i] *= post
            post *= nums[i]
        return final