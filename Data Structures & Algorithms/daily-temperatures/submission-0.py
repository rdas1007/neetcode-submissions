class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, a in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((i, a))
                continue
            
                # stack.append((i,a))
            # if stack[-1][1] < a:
            while stack[-1][1] < a:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
                if len(stack) == 0:
                    break
            stack.append((i,a))
        return res 
