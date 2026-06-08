class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(len(s))
        # if s == "":
        #     return 0
        # if len(s) == 1:
        #     return 1
        l = 0
        # last_ind = 0
        max_l = 0
        dicta = {}
        for r in range(len(s)):
            # print(dicta)
            if s[r] in dicta:
                l = max(l, dicta[s[r]] + 1)
            max_l = max(max_l, r - l + 1)
            dicta[s[r]] = r   
        return max_l                