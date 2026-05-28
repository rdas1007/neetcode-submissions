class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_dict = defaultdict(int)
        maxVal = 0
        for i in nums:
            val_dict[i] += 1
            maxVal = max(maxVal, val_dict[i])
        bucket = [[] for _ in range(len(nums)+1)]
        # print(val_dict)
        for key, val in val_dict.items():
            bucket[val].append(key)
        print(bucket)
        print(maxVal)
        result_list = []
        while len(result_list)<k and maxVal>0:
            result_list.extend(bucket[maxVal])
            maxVal -= 1
            # if len(result_list) >= k:
        return result_list[:k]

