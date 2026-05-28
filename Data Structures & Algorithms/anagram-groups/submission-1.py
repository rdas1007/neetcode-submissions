class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_dict = defaultdict(list)
        for i in strs:
            key = sorted(i)
            an_dict[''.join(key)].append(i)
        return list(an_dict.values())