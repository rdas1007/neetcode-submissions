class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicta = {}
        for i in range(len(nums)):
            try:
                if dicta[nums[i]] == 1:
                    return True
            except:
                dicta[nums[i]] = 1 
            # if nums[i] in nums[i+1:]:
                # return True
        return False